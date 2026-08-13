from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.transmissorModel import TransmissorModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule
import requests


class Transmissor(IContext[TransmissorModel, TransmissorModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, TransmissorModel, manager)

    def Add(self, obj: TransmissorModel) -> Any:
        return self._MakePost(obj)

    def Update(self, obj: TransmissorModel, search: SearchModule) -> list[requests.Response]:
        return self._MakeUpdate(obj, search)

    def Delete(self, search: SearchModule) -> List[requests.Response]:
        return super()._MakeDelete(search)

    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para Transmissor")

    def SelectAll(self) -> List[TransmissorModel]:
        return cast(List[TransmissorModel], self._SearchAll())

    def SelectByFilter(self, search: Any) -> List[TransmissorModel]:
        return cast(List[TransmissorModel], self.getByFilter(search))

    def SelectByFilterAssync(
        self,
        search: SearchModule,
        page_size: int = 172
    ) -> Iterator[TransmissorModel]:
        return cast(Iterator[TransmissorModel], super().cursorByFilter(search, page_size))

    def SelectAllAssync(self) -> Iterator[TransmissorModel]:
        return cast(Iterator[TransmissorModel], super()._SelectAllAssync())
