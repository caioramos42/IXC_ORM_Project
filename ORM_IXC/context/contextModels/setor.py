from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.setorModel import SetorModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule
import requests


class Setor(IContext[SetorModel, SetorModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, SetorModel, manager)

    def Add(self, obj: SetorModel) -> Any:
        return self._MakePost(obj)

    def Update(self, obj: SetorModel, search: SearchModule) -> list[requests.Response]:
        return self._MakeUpdate(obj, search)

    def Delete(self, search: SearchModule) -> List[requests.Response]:
        return super()._MakeDelete(search)

    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para Setor")

    def SelectAll(self) -> List[SetorModel]:
        return cast(List[SetorModel], self._SearchAll())

    def SelectByFilter(self, search: Any) -> List[SetorModel]:
        return cast(List[SetorModel], self.getByFilter(search))

    def SelectByFilterAssync(
        self,
        search: SearchModule,
        page_size: int = 172
    ) -> Iterator[SetorModel]:
        return cast(Iterator[SetorModel], super().cursorByFilter(search, page_size))

    def SelectAllAssync(self) -> Iterator[SetorModel]:
        return cast(Iterator[SetorModel], super()._SelectAllAssync())
