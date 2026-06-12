from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.searchUtils.searchModel import SearchModule
from ORM_IXC.models.tableModels.vendedorModel import VendedorModel
import requests

class Vendedor(IContext[VendedorModel, VendedorModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, VendedorModel, manager)
    def Add(self, obj: VendedorModel) -> Any:
        return self._MakePost(obj)
    def Update(self, obj: VendedorModel, search: SearchModule) -> list[requests.Response]:
        return self._MakeUpdate(obj, search)
    def Delete(self, search: SearchModule) -> List[requests.Response]:
        return super()._MakeDelete(search)
    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para Vendedor")
    def SelectAll(self) -> List[VendedorModel]:
        return cast(List[VendedorModel], self._SearchAll())
    def SelectByFilter(self, search: SearchModule) -> List[VendedorModel]:
        return cast(List[VendedorModel], super().getByFilter(search))
    def SelectByFilterAssync(self, search: SearchModule, page_size: int = 172) -> Iterator[VendedorModel]:
        return cast(Iterator[VendedorModel], super().cursorByFilter(search, page_size))
    def SelectAllAssync(self) -> Iterator[VendedorModel]:
        return cast(Iterator[VendedorModel], super()._SelectAllAssync())
