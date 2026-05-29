from typing import Any, List, Iterator, cast

from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.contratoDoClienteModel import ContratoDoClienteModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule
import requests

class ContratoDoCliente(IContext[ContratoDoClienteModel, ContratoDoClienteModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, ContratoDoClienteModel, manager)
    def Add(self, obj: ContratoDoClienteModel) -> Any:
        return self._MakePost(obj)
    def Update(self, obj: ContratoDoClienteModel, search: SearchModule) -> list[requests.Response]:
        return self._MakeUpdate(obj, search)
    def Delete(self, search: SearchModule) -> List[requests.Response]:
        return super()._MakeDelete(search)
    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para ServiceOrder")
    def SelectAll(self) -> List[ContratoDoClienteModel]:
        return cast(List[ContratoDoClienteModel], self._SearchAll())
    def SelectByFilter(self, search: Any) -> List[ContratoDoClienteModel]:
        return cast(List[ContratoDoClienteModel], self.getByFilter(search))
    def SelectByFilterAssync(self, search: SearchModule, page_size: int = 172) -> Iterator[ContratoDoClienteModel]:
        return cast(Iterator[ContratoDoClienteModel], super().cursorByFilter(search, page_size))
    def SelectAllAssync(self) -> Iterator[ContratoDoClienteModel]:
        return cast(Iterator[ContratoDoClienteModel], super()._SelectAllAssync())