from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager

class Atendimento(IContext, DefaultActions):
    def __init__(self, manager:Manager):
        self.table = "su_ticket"
        self.manager = manager
    def Add(self, obj):
        return self._MakePost(obj)
    def Update(obj):
        pass
    def DeleteById(id:int):
        pass