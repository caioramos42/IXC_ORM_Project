from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models import loginModel

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