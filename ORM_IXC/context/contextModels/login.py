from typing import Any, List, Iterator, cast
import requests
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.loginModel import LoginModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule

class Login(IContext[LoginModel, LoginModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, LoginModel, manager)
    def Add(self, obj: LoginModel) -> requests.Response:
        return self._MakePost(obj)
    def Update(self, obj: LoginModel) -> Any:
        return self._MakePut(obj)
    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para ServiceOrder")
    def SelectAll(self) -> List[LoginModel]:
        return cast(List[LoginModel], self._SearchAll())
    def SelectByFilter(self, search: Any) -> List[LoginModel]:
        return cast(List[LoginModel], self.getByFilter(search))
    def SelectByFilterAssync(self, search: SearchModule, page_size: int = 172) -> Iterator[LoginModel]:
        return cast(Iterator[LoginModel], super().cursorByFilter(search, page_size))
    def SelectAllAssync(self) -> Iterator[LoginModel]:
        return cast(Iterator[LoginModel], super()._SelectAllAssync())