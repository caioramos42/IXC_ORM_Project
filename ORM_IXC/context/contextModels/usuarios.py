from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.usuariosModel import UsuariosModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule
import requests


class Usuarios(IContext[UsuariosModel, UsuariosModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, UsuariosModel, manager)

    def Add(self, obj: UsuariosModel) -> Any:
        return self._MakePost(obj)

    def Update(self, obj: UsuariosModel, search: SearchModule) -> list[requests.Response]:
        return self._MakeUpdate(obj, search)

    def Delete(self, search: SearchModule) -> List[requests.Response]:
        return super()._MakeDelete(search)

    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para Usuários")

    def SelectAll(self) -> List[UsuariosModel]:
        return cast(List[UsuariosModel], self._SearchAll())

    def SelectByFilter(self, search: Any) -> List[UsuariosModel]:
        return cast(List[UsuariosModel], self.getByFilter(search))

    def SelectByFilterAssync(
        self,
        search: SearchModule,
        page_size: int = 172
    ) -> Iterator[UsuariosModel]:
        return cast(Iterator[UsuariosModel], super().cursorByFilter(search, page_size))

    def SelectAllAssync(self) -> Iterator[UsuariosModel]:
        return cast(Iterator[UsuariosModel], super()._SelectAllAssync())
