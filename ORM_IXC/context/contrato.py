from IXC_ORM_Project.interfaces.IContext import IContext
from IXC_ORM_Project.context.defaultActions.defaultActions import DefaultActions
from IXC_ORM_Project.context.request.manager import Manager

class Contrato(IContext, DefaultActions):
    def __init__(self, manager:Manager):
        self.table = "cliente_contrato"
        self.manager = manager
    def Add(self, obj):
        pass
    def Update(self, obj):
        pass
    def DeleteById(id:int):
        pass