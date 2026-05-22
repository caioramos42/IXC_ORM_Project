from typing import Any
import requests

from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.loginModel import LoginModel

class Login(IContext[LoginModel, LoginModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, LoginModel, manager)
    def Add(self, obj: LoginModel) -> requests.Response:
        return self._MakePost(obj)
    def Update(self, obj: LoginModel) -> Any:
        return self._MakePut(obj)
    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para ServiceOrder")
    def SelectAll(self) -> Any:
        return self._SearchAll()
