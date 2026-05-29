import requests
from typing import Iterator, Any, cast
from dataclasses import fields as get_dataclass_fields, MISSING

from ORM_IXC.context.request.manager import Manager

from ORM_IXC.models.searchUtils.searchModel import SearchModule
from ORM_IXC.enums.operators import Operators
from ORM_IXC.enums.methods import Actions
from ORM_IXC.interfaces.IModel import IModel
from ORM_IXC.statemants.classBase import Field
from abc import ABC

class DefaultActions(ABC):
    def __init__(self, contextModel: type[IModel], manager: Manager):
        self.contextModel: type[IModel] = contextModel
        self.manager: Manager = manager

    def _get_context_model(self) -> IModel:
        return cast(IModel, object.__new__(self.contextModel))

    def _get_table(self) -> str:
        return self._get_context_model().table
        
    def SearchById(self, id: int) -> list[IModel]:
        search = SearchModule(
            searchField="id",
            query=str(id),
            oper=Operators.EQUALS,
            context_model=self._get_context_model(),
            sortName="id",
        )
        return self.manager.make_request(search, Actions.LIST)
    
    def _SearchAll(self) -> list[IModel]:
        search = SearchModule(
            searchField="id",
            query="0",
            oper=Operators.MORETHAN,
            context_model=self._get_context_model(),
            sortName="id",
        )
        return self.manager.make_request(search, Actions.LIST)

    def SelectAll(self) -> Any:
        return self._SearchAll()
    
    def getByFilter(self, search: SearchModule) -> list[IModel]:
        table = self._get_table()
        search.set_context_model(self._get_context_model())
        search.set_table(table)
        if len(search.grid_param) != 0:
            for param in search.grid_param:
                if not param.searchField.startswith(f"{table}."):
                    param.searchField = f"{table}.{param.searchField}"
        return self.manager.make_request(search, Actions.LIST)

    def cursorByFilter(self, search: SearchModule, page_size: int = 200) -> Iterator[IModel]:
        table = self._get_table()
        search.set_context_model(self._get_context_model())
        search.set_table(table)
        if len(search.grid_param) != 0:
            for param in search.grid_param:
                if not param.searchField.startswith(f"{table}."):
                    param.searchField = f"{table}.{param.searchField}"
        return self.manager.iter_list_request(search, page_size)
    
    def _MakePost(self, modelForSend: IModel) -> requests.Response:
        # `table` é preenchido pelo contexto antes do envio.
        return self.manager.make_request(modelForSend, Actions.INSERT)
    
    def _MakePut(self, modelForSend: IModel) -> requests.Response:
        # Para EDIT, o IXC espera o ID na URL; os models gerados guardam isso em id_autoincrement.
        model_id = getattr(modelForSend, "id", None)
        if model_id is None:
            model_id = getattr(modelForSend, "id_autoincrement", None)
        model_id = str(model_id) if model_id is not None else None

        if model_id in (None, '', '0'):
            raise ValueError("Para editar, o ID deve ser preenchido")

        return self.manager.make_request(modelForSend, Actions.EDIT)

    def _MakeDelete(self, search: SearchModule) -> list[requests.Response]:
        found_records = self.getByFilter(search)
        
        if not found_records:
            raise ValueError("Nenhum registro encontrado para os filtros especificados")
        print(len(found_records))
        responses: list[requests.Response] = []
        for record in found_records:
            response = self.manager.make_request(record, Actions.DELETE)
            responses.append(response)

        return responses

    def _MakeUpdate(self, modelForUpdate: IModel, search: SearchModule) -> list[requests.Response]:
        found_records = self.getByFilter(search)
        
        if not found_records:
            raise ValueError("Nenhum registro encontrado para os filtros especificados")
        
        # 2. Obter apenas os campos que foram efetivamente alterados no modelo
        update_values: dict[str, Any] = {}
        if hasattr(modelForUpdate, 'changed_fields'):
            changed_fields = modelForUpdate.changed_fields()
            print(changed_fields)
            if changed_fields:
                if hasattr(modelForUpdate, 'changed_values'):
                    update_values = modelForUpdate.changed_values()
                else:
                    try:
                        source_values = modelForUpdate.to_dict()
                    except Exception:
                        source_values = dict(vars(modelForUpdate))
                    update_values = {
                        k: v for k, v in source_values.items()
                        if k in changed_fields and k not in ("id", "id_autoincrement")
                    }

        if not update_values:
            if hasattr(modelForUpdate, 'changed_values'):
                update_values = modelForUpdate.changed_values()
            else:
                try:
                    update_values = {
                        k: v for k, v in modelForUpdate.to_dict().items()
                        if k not in ("id", "id_autoincrement")
                    }
                except Exception:
                    update_values = {
                        k: v for k, v in dict(vars(modelForUpdate)).items()
                        if k not in ("id", "id_autoincrement")
                    }

        if not update_values:
            raise ValueError("Nenhum campo foi alterado em relação ao modelo padrão")
        
        # 3. Para cada registro encontrado, aplicar apenas os campos alterados
        responses = []
        for record in found_records:
            # Determinar id do registro (id ou id_autoincrement) — extrai valor cru de Field quando necessário
            def _extract_raw(obj, name: str):
                # Prefer method provided by BaseModel
                if hasattr(obj, '_raw_value'):
                    try:
                        return obj._raw_value(name)
                    except Exception:
                        pass
                val = getattr(obj, name, None)
                if isinstance(val, Field):
                    return val._val
                return val

            record_id = _extract_raw(record, 'id') or _extract_raw(record, 'id_autoincrement')
            if record_id in (None, '', '0'):
                raise ValueError("Registro retornado não possui id para edição")

            # Atribuir apenas os campos alterados ao registro (para marcar changed_fields)
            for key, raw_value in update_values.items():
                if key in ("id", "id_autoincrement"):
                    continue
                if hasattr(record, key):
                    print(key + " " +str(raw_value))
                    setattr(record, key, raw_value)
            print(record.to_dict())
            # Enviar o próprio registro atualizado (o manager usa record.to_dict())
            response = self.manager.make_request(record, Actions.EDIT)
            responses.append(response)
        
        return responses

    # def update(self, model: IModel, search: SearchModule) -> list[requests.Response]:
    #     """UPDATE com pesquisa - wrapper público para _MakeUpdate"""
    #     return self._MakeUpdate(model, search)

    def _SelectAllAssync(self, page_size: int = 200):
            search = SearchModule(
                searchField="id",
                query="0",
                oper=Operators.MORETHAN,
                context_model=self._get_context_model(),
                sortName="id",
            )
            return self.manager.iter_list_request(search, page_size)
