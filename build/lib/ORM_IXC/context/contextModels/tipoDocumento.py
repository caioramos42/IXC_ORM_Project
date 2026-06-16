from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.tipoDocumentoModel import TipoDocumentoModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule
import requests


class TipoDocumento(IContext[TipoDocumentoModel, TipoDocumentoModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, TipoDocumentoModel, manager)

    def Add(self, obj: TipoDocumentoModel) -> Any:
        return self._MakePost(obj)

    def Update(self, obj: TipoDocumentoModel, search: SearchModule) -> list[requests.Response]:
        return self._MakeUpdate(obj, search)

    def Delete(self, search: SearchModule) -> List[requests.Response]:
        return super()._MakeDelete(search)

    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para TipoDocumento")

    def SelectAll(self) -> List[TipoDocumentoModel]:
        return cast(List[TipoDocumentoModel], self._SearchAll())

    def SelectByFilter(self, search: Any) -> List[TipoDocumentoModel]:
        return cast(List[TipoDocumentoModel], self.getByFilter(search))

    def SelectByFilterAssync(
        self,
        search: SearchModule,
        page_size: int = 172
    ) -> Iterator[TipoDocumentoModel]:
        return cast(Iterator[TipoDocumentoModel], super().cursorByFilter(search, page_size))

    def SelectAllAssync(self) -> Iterator[TipoDocumentoModel]:
        return cast(Iterator[TipoDocumentoModel], super()._SelectAllAssync())
