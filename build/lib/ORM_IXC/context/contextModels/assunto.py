from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.assuntoModel import AssuntoModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule
import requests


class Assunto(IContext[AssuntoModel, AssuntoModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, AssuntoModel, manager)

    def Add(self, obj: AssuntoModel) -> Any:
        return self._MakePost(obj)

    def Update(self, obj: AssuntoModel, search: SearchModule) -> list[requests.Response]:
        return self._MakeUpdate(obj, search)

    def Delete(self, search: SearchModule) -> List[requests.Response]:
        return super()._MakeDelete(search)

    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para Assunto")

    def SelectAll(self) -> List[AssuntoModel]:
        return cast(List[AssuntoModel], self._SearchAll())

    def SelectByFilter(self, search: Any) -> List[AssuntoModel]:
        return cast(List[AssuntoModel], self.getByFilter(search))

    def SelectByFilterAssync(
        self,
        search: SearchModule,
        page_size: int = 172
    ) -> Iterator[AssuntoModel]:
        return cast(Iterator[AssuntoModel], super().cursorByFilter(search, page_size))

    def SelectAllAssync(self) -> Iterator[AssuntoModel]:
        return cast(Iterator[AssuntoModel], super()._SelectAllAssync())
