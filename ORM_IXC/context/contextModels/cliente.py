from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.clienteModel import ClientModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule

class Cliente(IContext[ClientModel, ClientModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, ClientModel, manager)
    def Add(self, obj: ClientModel) -> Any:
        return self._MakePost(obj)
    def Update(self, obj: ClientModel) -> Any:
        return self._MakePut(obj)
    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para ServiceOrder")
    def SelectAll(self) -> List[ClientModel]:
        return cast(List[ClientModel], self._SearchAll())
    def SearchById(self, id: int):
        return super().SearchById(id)
    def SelectByFilter(self, search: Any) -> List[ClientModel]:
        return cast(List[ClientModel], self.getByFilter(search))
    def SelectByFilterAssync(self, search: SearchModule, page_size: int = 172) -> Iterator[ClientModel]:
        return cast(Iterator[ClientModel], super().cursorByFilter(search, page_size))
    def SelectAllAssync(self) -> Iterator[ClientModel]:
        return cast(Iterator[ClientModel], super()._SelectAllAssync())
