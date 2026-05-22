from typing import Any
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.clienteModel import ClientModel

class Cliente(IContext[ClientModel, ClientModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, ClientModel, manager)
    def Add(self, obj: ClientModel) -> ClientModel:
        return self._MakePost(obj)
    def Update(self, obj: ClientModel) -> Any:
        return self._MakePut(obj)
    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para ServiceOrder")
    def SelectAll(self) -> Any:
        return self._SearchAll()
    def SearchById(self, id: int):
        return super().SearchById(id)
