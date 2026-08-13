from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.patrimonioModel import PatrimonioModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule
import requests


class Patrimonio(IContext[PatrimonioModel, PatrimonioModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, PatrimonioModel, manager)

    def Add(self, obj: PatrimonioModel) -> Any:
        return self._MakePost(obj)

    def Update(self, obj: PatrimonioModel, search: SearchModule) -> list[requests.Response]:
        return self._MakeUpdate(obj, search)

    def Delete(self, search: SearchModule) -> List[requests.Response]:
        return super()._MakeDelete(search)

    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para Patrimônio")

    def SelectAll(self) -> List[PatrimonioModel]:
        return cast(List[PatrimonioModel], self._SearchAll())

    def SelectByFilter(self, search: Any) -> List[PatrimonioModel]:
        return cast(List[PatrimonioModel], self.getByFilter(search))

    def SelectByFilterAssync(
        self,
        search: SearchModule,
        page_size: int = 172
    ) -> Iterator[PatrimonioModel]:
        return cast(Iterator[PatrimonioModel], super().cursorByFilter(search, page_size))

    def SelectAllAssync(self) -> Iterator[PatrimonioModel]:
        return cast(Iterator[PatrimonioModel], super()._SelectAllAssync())
