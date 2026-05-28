from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.searchUtils.searchModel import SearchModule
from ORM_IXC.models.tableModels.serviceOrderModel import ServiceOrderModel

class ServiceOrder(IContext[ServiceOrderModel, ServiceOrderModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, ServiceOrderModel, manager)
    def Add(self, obj: ServiceOrderModel) -> Any:
        return self._MakePost(obj)
    def Update(self, obj: ServiceOrderModel) -> Any:
        return self._MakePut(obj)
    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para ServiceOrder")
    def SelectAll(self) -> List[ServiceOrderModel]:
        return cast(List[ServiceOrderModel], self._SearchAll())
    def SelectByFilter(self, search: SearchModule) -> List[ServiceOrderModel]:
        return cast(List[ServiceOrderModel], super().getByFilter(search))
    def SelectByFilterAssync(self, search: SearchModule, page_size: int = 172) -> Iterator[ServiceOrderModel]:
        return cast(Iterator[ServiceOrderModel], super().cursorByFilter(search, page_size))
    def SelectAllAssync(self) -> Iterator[ServiceOrderModel]:
        return cast(Iterator[ServiceOrderModel], super()._SelectAllAssync())
