from typing import Any

from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.contratoDoClienteModel import ContratoDoClienteModel

class ContratoDoCliente(IContext[ContratoDoClienteModel, ContratoDoClienteModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, ContratoDoClienteModel, manager)
    def Add(self, obj: ContratoDoClienteModel) -> ContratoDoClienteModel:
        return self._MakePost(obj)
    def Update(self, obj: ContratoDoClienteModel) -> Any:
        return self._MakePut(obj)
    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para ServiceOrder")
    def SelectAll(self) -> Any:
        return self._SearchAll()
