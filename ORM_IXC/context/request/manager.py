import requests
import base64
from typing import Any, overload, Literal

from ORM_IXC.enums.methods import Actions
import urllib3
from ORM_IXC.interfaces.IModel import IModel

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
        total = int(data.get("total", 0))
        registros = data.get("registros", [])

        converted = []
        for registro in registros:
            if "id" in registro and "id_autoincrement" not in registro:
                registro["id_autoincrement"] = registro["id"]
            converted.append(request.dto_convert(registro))

        if total == 1:
            return converted[0]
        return converted

    @overload
    def make_request(self, request: IModel, method: Literal[Actions.DELETE, Actions.EDIT]) -> requests.Response: ...

    @overload
    def make_request(self, request: IModel, method: Literal[Actions.INSERT]) -> requests.Response: ...

    @overload
    def make_request(self, request: IModel, method: Literal[Actions.LIST]) -> IModel | list[IModel]: ...

    def make_request(self, request: IModel, method: Actions) -> requests.Response | IModel | list[IModel]:
        hostBefore = self.host
        self.insertTable(method, request.table)
        try:
            match method:
                case Actions.DELETE:
                    return requests.post(
                        "{}/{}".format(self.host, self._get_request_id(request)),
                        headers=self.header,
                        verify=False
                    )
                case Actions.EDIT:
                    return requests.put(
                        "{}/{}".format(self.host, self._get_request_id(request)),
                        json=request.to_dict(),
                        headers=self.header,
                        verify=False
                    )
                case _:
                    response = requests.post(
                        self.host,
                        json=request.to_dict(),
                        headers=self.header,
                        verify=False
                    )
                    if method == Actions.LIST:
                        return self._convert_list_response(response, request)
                    return response
        except Exception:
            raise
        finally:
            self.host = hostBefore
        
