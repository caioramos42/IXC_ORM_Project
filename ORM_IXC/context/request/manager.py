import requests
import base64
from typing import Any, Iterator, overload, Literal

from ORM_IXC.enums.methods import Actions
import urllib3
from ORM_IXC.interfaces.IModel import IModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule

from typing import Generic, Iterator, TypeVar

T = TypeVar("T")

class QueryCursor(Generic[T]):

    def __init__(self, generator: Iterator[T]):
        self._generator = generator

        self.total: int = 0
        self.page: int = 1
        self.page_size: int = 0

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._generator)

class Manager:
    
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    def __init__(self, host: str, token: str):
        self.host = "https://{}/webservice/v1/".format(host)
        self.token = token
        self.header = {
            'Authorization': 'Basic {}'.format(base64.b64encode(token.encode('utf-8')).decode('utf-8')),
            'Content-Type': 'application/json'
        }
    def insertTable(self, method: Actions, table: str) -> None:
        self.header['ixcsoft'] = method.value.data
        self.host += "{}".format(table)
        
    def _get_request_id(self, request: IModel) -> str:
        request_id = getattr(request, "id", None)
        if request_id is not None:
            return str(request_id)
        request_id = getattr(request, "id_autoincrement", None)
        if request_id is not None:
            return str(request_id)
        raise ValueError("Para editar ou deletar, o model precisa ter id ou id_autoincrement")

    def _convert_list_response(self, response: requests.Response, request: IModel) -> IModel | list[IModel]:
        if "<div" in response.text:
            raise(ValueError(f"Erro ao processar request: {response.text.split(">")[1].replace("</div","")}"))
        data: dict[str, Any] = response.json()
        registros = data.get("registros", [])

        converted = []
        for registro in registros:
            if "id" in registro and "id_autoincrement" not in registro:
                registro["id_autoincrement"] = registro["id"]
            converted.append(request.dto_convert(registro))

        return converted

    def _make_list_request(self, request: SearchModule) -> list[IModel]:
        converted: list[IModel] = []
        page = int(getattr(request, "page", 1))
        amount = int(getattr(request, "amount", 9999))
        paginate_all = amount == 9999

        while True:
            if hasattr(request, "setPage"):
                request.setPage(page)
            response = requests.post(
                self.host,
                json=request.to_dict(),
                headers=self.header,
                verify=False
            )
            if "<div" in response.text:
                raise(ValueError(f"Erro ao processar request: {response.text.split(">")[1].replace("</div","")}"))

            data: dict[str, Any] = response.json()
            total = int(data.get("total", 0))
            registros = data.get("registros", [])

            for registro in registros:
                if "id" in registro and "id_autoincrement" not in registro:
                    registro["id_autoincrement"] = registro["id"]
                converted.append(request.dto_convert(registro))

            if len(converted) >= total or len(registros) == 0:
                break

            if not paginate_all:
                break

            page += 1

        return converted
    def _iter_internal(self, request: SearchModule, page_size: int):
        hostBefore = self.host

        self.insertTable(Actions.LIST, request.table)

        try:

            page = int(getattr(request, "page", 1))

            requested_amount = int(
                getattr(request, "amount", 9999)
            )

            limit_total = (
                requested_amount
                if requested_amount != 9999
                else None
            )

            effective_page_size = (
                min(page_size, limit_total)
                if limit_total is not None
                else page_size
            )

            if hasattr(request, "setaAmount"):
                request.setaAmount(effective_page_size)

            yielded = 0

            while True:

                if hasattr(request, "setPage"):
                    request.setPage(page)

                response = requests.post(
                    self.host,
                    json=request.to_dict(),
                    headers=self.header,
                    verify=False
                )

                if "<div" in response.text:
                    raise ValueError(
                        f"Erro: {response.text}"
                    )

                data = response.json()

                registros = data.get("registros", [])

                if len(registros) == 0:
                    break

                total = int(data.get("total", 0))

                for registro in registros:

                    if (
                        "id" in registro
                        and "id_autoincrement" not in registro
                    ):
                        registro["id_autoincrement"] = registro["id"]

                    if (
                        limit_total is not None
                        and yielded >= limit_total
                    ):
                        break

                    yielded += 1

                    yield request.dto_convert(registro)

                if (
                    limit_total is not None
                    and yielded >= limit_total
                ):
                    break

                if page * effective_page_size >= total:
                    break

                page += 1

        finally:
            self.host = hostBefore
    def iter_list_request(
        self,
        request: SearchModule,
        page_size: int = 200
    ) -> QueryCursor[IModel]:

        cursor = QueryCursor(self._iter_internal(request, page_size))

        return cursor
    # def iter_list_request(self, request: SearchModule, page_size: int = 200) -> Iterator[IModel]:
    #     hostBefore = self.host
    #     self.insertTable(Actions.LIST, request.table)
    #     try:
    #         page = int(getattr(request, "page", 1))
    #         requested_amount = int(getattr(request, "amount", 9999))
    #         limit_total = requested_amount if requested_amount != 9999 else None
    #         effective_page_size = min(page_size, limit_total) if limit_total is not None else page_size

    #         if hasattr(request, "setaAmount"):
    #             request.setaAmount(effective_page_size)

    #         yielded = 0

    #         while True:
    #             if hasattr(request, "setPage"):
    #                 request.setPage(page)

    #             response = requests.post(
    #                 self.host,
    #                 json=request.to_dict(),
    #                 headers=self.header,
    #                 verify=False
    #             )

    #             if "<div" in response.text:
    #                 raise(ValueError(f"Erro ao processar request: {response.text.split(">")[1].replace("</div","")}"))

    #             data: dict[str, Any] = response.json()
    #             registros = data.get("registros", [])

    #             if len(registros) == 0:
    #                 break

    #             for registro in registros:
    #                 if "id" in registro and "id_autoincrement" not in registro:
    #                     registro["id_autoincrement"] = registro["id"]
    #                 if limit_total is not None and yielded >= limit_total:
    #                     break
    #                 yielded += 1
    #                 yield request.dto_convert(registro)

    #             if limit_total is not None and yielded >= limit_total:
    #                 break

    #             total = int(data.get("total", 0))
    #             if page * effective_page_size >= total:
    #                 break

    #             page += 1
    #     finally:
    #         self.host = hostBefore

    @overload
    def make_request(self, request: IModel, method: Literal[Actions.DELETE, Actions.EDIT]) -> requests.Response: ...

    @overload
    def make_request(self, request: IModel, method: Literal[Actions.INSERT]) -> requests.Response: ...

    @overload
    def make_request(self, request: IModel, method: Literal[Actions.LIST]) -> list[IModel]: ...

    def make_request(self, request: IModel, method: Actions) -> requests.Response | list[IModel]:
        hostBefore = self.host
        self.insertTable(method, request.table)
        try:
            match method:
                case Actions.DELETE:
                    print("passei aqui")
                    return requests.delete(
                        "{}/{}".format(self.host, self._get_request_id(request)),
                        headers=self.header,
                        verify=False
                    )
                case Actions.EDIT:
                    print("{}/{}".format(self.host, self._get_request_id(request)))
                    #print(request.to_dict())
                    reqs = request.to_dict()
                    reqs.pop("id", None)
                    print(reqs)
                    return requests.put(
                        "{}/{}".format(self.host, self._get_request_id(request)),
                        json=reqs,
                        headers=self.header,
                        verify=False
                    )
                case _:
                    if method == Actions.LIST:
                        if isinstance(request, SearchModule):
                            return self._make_list_request(request)
                        raise ValueError("Para listar, o request deve ser do tipo SearchModule")
                    response = requests.post(
                        self.host,
                        json=request.to_dict(),
                        headers=self.header,
                        verify=False
                    )
                    return response
        except Exception:
            raise
        finally:
            self.host = hostBefore

