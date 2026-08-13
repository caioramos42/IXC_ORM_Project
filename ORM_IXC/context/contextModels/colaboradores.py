from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.colaboradoresModel import ColaboradoresModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule
import requests


class Colaboradores(IContext[ColaboradoresModel, ColaboradoresModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, ColaboradoresModel, manager)

    def Add(self, obj: ColaboradoresModel) -> Any:
        return self._MakePost(obj)

    def Update(self, obj: ColaboradoresModel, search: SearchModule) -> list[requests.Response]:
        return self._MakeUpdate(obj, search)

    def Delete(self, search: SearchModule) -> List[requests.Response]:
        return super()._MakeDelete(search)

    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para Colaboradores")

    def SelectAll(self) -> List[ColaboradoresModel]:
        return cast(List[ColaboradoresModel], self._SearchAll())

    def SelectByFilter(self, search: Any) -> List[ColaboradoresModel]:
        return cast(List[ColaboradoresModel], self.getByFilter(search))

    def SelectByFilterAssync(
        self,
        search: SearchModule,
        page_size: int = 172
    ) -> Iterator[ColaboradoresModel]:
        return cast(Iterator[ColaboradoresModel], super().cursorByFilter(search, page_size))

    def SelectAllAssync(self) -> Iterator[ColaboradoresModel]:
        return cast(Iterator[ColaboradoresModel], super()._SelectAllAssync())
