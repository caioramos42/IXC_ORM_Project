from typing import Any
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.contasAReceber import ContasAReceberModel

class AReceber(IContext[ContasAReceberModel, ContasAReceberModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, ContasAReceberModel, manager)
    def Add(self, obj: ContasAReceberModel) -> ContasAReceberModel:
        return self._MakePost(obj)
    def Update(self, obj: ContasAReceberModel) -> Any:
        return self._MakePut(obj)
    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para ServiceOrder")
    def SelectAll(self) -> Any:
        return self._SearchAll()
    def MakeUpdate(self, modelForUpdate: IModel, search: SearchModule) -> list[requests.Response]:
        return self._MakeUpdate(modelForUpdate, search)
