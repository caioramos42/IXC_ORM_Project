from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.radacctModel import RadacctModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule
import requests


class Radacct(IContext[RadacctModel, RadacctModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, RadacctModel, manager)

    def Add(self, obj: RadacctModel) -> Any:
        return self._MakePost(obj)

    def Update(self, obj: RadacctModel, search: SearchModule) -> list[requests.Response]:
        return self._MakeUpdate(obj, search)

    def Delete(self, search: SearchModule) -> List[requests.Response]:
        return super()._MakeDelete(search)

    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para Radacct")

    def SelectAll(self) -> List[RadacctModel]:
        return cast(List[RadacctModel], self._SearchAll())

    def SelectByFilter(self, search: Any) -> List[RadacctModel]:
        return cast(List[RadacctModel], self.getByFilter(search))

    def SelectByFilterAssync(
        self,
        search: SearchModule,
        page_size: int = 172
    ) -> Iterator[RadacctModel]:
        return cast(Iterator[RadacctModel], super().cursorByFilter(search, page_size))

    def SelectAllAssync(self) -> Iterator[RadacctModel]:
        return cast(Iterator[RadacctModel], super()._SelectAllAssync())
