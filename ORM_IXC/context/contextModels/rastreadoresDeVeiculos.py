from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.rastreadoresDeVeiculosModel import RastreadoresDeVeIculosModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule
import requests


class RastreadoresDeVeIculos(IContext[RastreadoresDeVeIculosModel, RastreadoresDeVeIculosModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, RastreadoresDeVeIculosModel, manager)

    def Add(self, obj: RastreadoresDeVeIculosModel) -> Any:
        return self._MakePost(obj)

    def Update(self, obj: RastreadoresDeVeIculosModel, search: SearchModule) -> list[requests.Response]:
        return self._MakeUpdate(obj, search)

    def Delete(self, search: SearchModule) -> List[requests.Response]:
        return super()._MakeDelete(search)

    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para RastreadoresDeVeículos")

    def SelectAll(self) -> List[RastreadoresDeVeIculosModel]:
        return cast(List[RastreadoresDeVeIculosModel], self._SearchAll())

    def SelectByFilter(self, search: Any) -> List[RastreadoresDeVeIculosModel]:
        return cast(List[RastreadoresDeVeIculosModel], self.getByFilter(search))

    def SelectByFilterAssync(
        self,
        search: SearchModule,
        page_size: int = 172
    ) -> Iterator[RastreadoresDeVeIculosModel]:
        return cast(Iterator[RastreadoresDeVeIculosModel], super().cursorByFilter(search, page_size))

    def SelectAllAssync(self) -> Iterator[RastreadoresDeVeIculosModel]:
        return cast(Iterator[RastreadoresDeVeIculosModel], super()._SelectAllAssync())
