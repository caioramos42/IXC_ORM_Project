from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager

class Contabil(IContext, DefaultActions):
    def __init__(self, manager:Manager):
        self.table = "planejamento_analitico"
        self.manager = manager
    def Add(self, obj):
        pass
    def Update(obj):
        pass
    def DeleteById(id:int):
        pass