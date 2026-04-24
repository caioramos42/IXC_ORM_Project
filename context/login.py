from IXC_ORM_Project.interfaces.IContext import IContext
from IXC_ORM_Project.context.defaultActions.defaultActions import DefaultActions
from IXC_ORM_Project.context.request.manager import Manager
from IXC_ORM_Project.models import loginModel

class Login(IContext, DefaultActions):
    def __init__(self, manager:Manager):
        self.table = "radusuarios"
        self.manager = manager
    def Add(self, obj: loginModel):
        pass
    def Update(obj, id: int):
        pass
    def DeleteById(id:int):
        pass