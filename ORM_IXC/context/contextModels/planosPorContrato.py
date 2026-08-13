from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.planosPorContratoModel import PlanosPorContratoModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule
import requests


class PlanosPorContrato(IContext[PlanosPorContratoModel, PlanosPorContratoModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, PlanosPorContratoModel, manager)

    def Add(self, obj: PlanosPorContratoModel) -> Any:
        return self._MakePost(obj)

    def Update(self, obj: PlanosPorContratoModel, search: SearchModule) -> list[requests.Response]:
        return self._MakeUpdate(obj, search)

    def Delete(self, search: SearchModule) -> List[requests.Response]:
        return super()._MakeDelete(search)

    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para PlanosPorContrato")

    def SelectAll(self) -> List[PlanosPorContratoModel]:
        return cast(List[PlanosPorContratoModel], self._SearchAll())

    def SelectByFilter(self, search: Any) -> List[PlanosPorContratoModel]:
        return cast(List[PlanosPorContratoModel], self.getByFilter(search))

    def SelectByFilterAssync(
        self,
        search: SearchModule,
        page_size: int = 172
    ) -> Iterator[PlanosPorContratoModel]:
        return cast(Iterator[PlanosPorContratoModel], super().cursorByFilter(search, page_size))

    def SelectAllAssync(self) -> Iterator[PlanosPorContratoModel]:
        return cast(Iterator[PlanosPorContratoModel], super()._SelectAllAssync())
