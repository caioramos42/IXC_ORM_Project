from typing import Any

from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.serviceOrderModel import ServiceOrderModel

class ServiceOrder(IContext[ServiceOrderModel, ServiceOrderModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, ServiceOrderModel, manager)
    def Add(self, obj: ServiceOrderModel) -> ServiceOrderModel:
        return self._MakePost(obj)
    def Update(self, obj: ServiceOrderModel) -> Any:
        return self._MakePut(obj)
    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para ServiceOrder")
    def SelectAll(self) -> Any:
        return self._SearchAll()
