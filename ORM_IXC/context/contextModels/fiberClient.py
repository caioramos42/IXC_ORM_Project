from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.clienteFibraModel import ClienteFibraModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule

class ClienteFibra(IContext[ClienteFibraModel, ClienteFibraModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, ClienteFibraModel, manager)
    def Add(self, obj: ClienteFibraModel) -> Any:
        return self._MakePost(obj)
    def Update(self, obj: ClienteFibraModel) -> Any:
        return self._MakePut(obj)
    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para ServiceOrder")
    def SelectAll(self) -> List[ClienteFibraModel]:
        return cast(List[ClienteFibraModel], self._SearchAll())
    def SelectByFilter(self, search: Any) -> List[ClienteFibraModel]:
        return cast(List[ClienteFibraModel], self.getByFilter(search))
    def SelectByFilterAssync(self, search: SearchModule, page_size: int = 172) -> Iterator[ClienteFibraModel]:
        return cast(Iterator[ClienteFibraModel], super().cursorByFilter(search, page_size))
    def SelectAllAssync(self) -> Iterator[ClienteFibraModel]:
        return cast(Iterator[ClienteFibraModel], super()._SelectAllAssync())