from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.planoDeVendaModel import PlanoDeVendaModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule
import requests


class PlanoDeVenda(IContext[PlanoDeVendaModel, PlanoDeVendaModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, PlanoDeVendaModel, manager)

    def Add(self, obj: PlanoDeVendaModel) -> Any:
        return self._MakePost(obj)

    def Update(self, obj: PlanoDeVendaModel, search: SearchModule) -> list[requests.Response]:
        return self._MakeUpdate(obj, search)

    def Delete(self, search: SearchModule) -> List[requests.Response]:
        return super()._MakeDelete(search)

    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para PlanoDeVenda")

    def SelectAll(self) -> List[PlanoDeVendaModel]:
        return cast(List[PlanoDeVendaModel], self._SearchAll())

    def SelectByFilter(self, search: Any) -> List[PlanoDeVendaModel]:
        return cast(List[PlanoDeVendaModel], self.getByFilter(search))

    def SelectByFilterAssync(
        self,
        search: SearchModule,
        page_size: int = 172
    ) -> Iterator[PlanoDeVendaModel]:
        return cast(Iterator[PlanoDeVendaModel], super().cursorByFilter(search, page_size))

    def SelectAllAssync(self) -> Iterator[PlanoDeVendaModel]:
        return cast(Iterator[PlanoDeVendaModel], super()._SelectAllAssync())
