import requests

from ORM_IXC.context.request.manager import Manager

from ORM_IXC.models.searchUtils.searchModel import SearchModule
from ORM_IXC.enums.operators import Operators
from ORM_IXC.enums.methods import Actions
from ORM_IXC.interfaces.IModel import IModel
from abc import ABC

class DefaultActions(ABC):
    def __init__(self, contextModel: type[IModel], manager: Manager):
        self.contextModel: type[IModel] = contextModel
        self.manager: Manager = manager

    def _get_context_model(self) -> IModel:
        return self.contextModel.__new__(self.contextModel)

    def _get_table(self) -> str:
        return self._get_context_model().table
        
    def SearchById(self, id: int) -> IModel | list[IModel]:
        search = SearchModule(
            searchField="id",
            query=str(id),
            oper=Operators.EQUALS,
            context_model=self._get_context_model(),
            sortName="id",
        )
        return self.manager.make_request(search, Actions.LIST)
    
    def _SearchAll(self) -> IModel | list[IModel]:
        search = SearchModule(
            searchField="id",
            query="0",
            oper=Operators.MORETHAN,
            context_model=self._get_context_model(),
            sortName="id",
        )
        return self.manager.make_request(search, Actions.LIST)
    
    def getByFilter(self, search: SearchModule) -> IModel | list[IModel]:
        table = self._get_table()
        search.set_context_model(self._get_context_model())
        search.set_table(table)
        if len(search.grid_param) != 0:
            for param in search.grid_param:
                if not param.searchField.startswith(f"{table}."):
                    param.searchField = f"{table}.{param.searchField}"
        return self.manager.make_request(search, Actions.LIST)
    
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
        
    
    
