from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.cidadeModel import CidadeModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule
import requests


class Cidade(IContext[CidadeModel, CidadeModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, CidadeModel, manager)

    def Add(self, obj: CidadeModel) -> Any:
        return self._MakePost(obj)

    def Update(self, obj: CidadeModel, search: SearchModule) -> list[requests.Response]:
        return self._MakeUpdate(obj, search)

    def Delete(self, search: SearchModule) -> List[requests.Response]:
        return super()._MakeDelete(search)

    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para Cidade")

    def SelectAll(self) -> List[CidadeModel]:
        return cast(List[CidadeModel], self._SearchAll())

    def SelectByFilter(self, search: Any) -> List[CidadeModel]:
        return cast(List[CidadeModel], self.getByFilter(search))

    def SelectByFilterAssync(
        self,
        search: SearchModule,
        page_size: int = 172
    ) -> Iterator[CidadeModel]:
        return cast(Iterator[CidadeModel], super().cursorByFilter(search, page_size))

    def SelectAllAssync(self) -> Iterator[CidadeModel]:
        return cast(Iterator[CidadeModel], super()._SelectAllAssync())
