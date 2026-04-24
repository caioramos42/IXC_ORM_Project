from IXC_ORM_Project.interfaces.IContext import IContext
from IXC_ORM_Project.context.defaultActions.defaultActions import DefaultActions
from IXC_ORM_Project.context.request.manager import Manager

class AReceber(IContext, DefaultActions):
    def __init__(self, manager:Manager):
        self.table = "fn_areceber"
        self.manager = manager
    def Add(self, obj):
        return self._MakePost(obj)
    def Update(self, obj):
        pass
    def DeleteById(id:int):
        pass