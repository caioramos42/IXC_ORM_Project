from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.veiculosModel import VeiculosModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule
import requests

class Veiculos(IContext[VeiculosModel, VeiculosModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, VeiculosModel, manager)

    def Add(self, obj: VeiculosModel) -> Any:
        return self._MakePost(obj)

    def Update(self, obj: VeiculosModel, search: SearchModule) -> list[requests.Response]:
        return self._MakeUpdate(obj, search)

    def Delete(self, search: SearchModule) -> List[requests.Response]:
        return super()._MakeDelete(search)

    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para Veículos")

    def SelectAll(self) -> List[VeiculosModel]:
        return cast(List[VeiculosModel], self._SearchAll())

    def SelectByFilter(self, search: Any) -> List[VeiculosModel]:
        return cast(List[VeiculosModel], self.getByFilter(search))

    def SelectByFilterAssync(
        self,
        search: SearchModule,
        page_size: int = 172
    ) -> Iterator[VeiculosModel]:
        return cast(Iterator[VeiculosModel], super().cursorByFilter(search, page_size))

    def SelectAllAssync(self) -> Iterator[VeiculosModel]:
        return cast(Iterator[VeiculosModel], super()._SelectAllAssync())
