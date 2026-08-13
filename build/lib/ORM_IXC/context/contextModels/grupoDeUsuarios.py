from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.grupoDeUsuariosModel import GrupoDeUsuariosModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule
import requests


class GrupoDeUsuarios(IContext[GrupoDeUsuariosModel, GrupoDeUsuariosModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, GrupoDeUsuariosModel, manager)

    def Add(self, obj: GrupoDeUsuariosModel) -> Any:
        return self._MakePost(obj)

    def Update(self, obj: GrupoDeUsuariosModel, search: SearchModule) -> list[requests.Response]:
        return self._MakeUpdate(obj, search)

    def Delete(self, search: SearchModule) -> List[requests.Response]:
        return super()._MakeDelete(search)

    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para GrupoDeUsuários")

    def SelectAll(self) -> List[GrupoDeUsuariosModel]:
        return cast(List[GrupoDeUsuariosModel], self._SearchAll())

    def SelectByFilter(self, search: Any) -> List[GrupoDeUsuariosModel]:
        return cast(List[GrupoDeUsuariosModel], self.getByFilter(search))

    def SelectByFilterAssync(
        self,
        search: SearchModule,
        page_size: int = 172
    ) -> Iterator[GrupoDeUsuariosModel]:
        return cast(Iterator[GrupoDeUsuariosModel], super().cursorByFilter(search, page_size))

    def SelectAllAssync(self) -> Iterator[GrupoDeUsuariosModel]:
        return cast(Iterator[GrupoDeUsuariosModel], super()._SelectAllAssync())
