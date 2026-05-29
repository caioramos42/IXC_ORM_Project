from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.contasAReceber import ContasAReceberModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule
import requests

class AReceber(IContext[ContasAReceberModel, ContasAReceberModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, ContasAReceberModel, manager)
    def Add(self, obj: ContasAReceberModel) -> Any:
        return self._MakePost(obj)
    def Update(self, obj: ContasAReceberModel, search: SearchModule) -> list[requests.Response]:
        return self._MakeUpdate(obj, search)
    def Delete(self, search: SearchModule) -> List[requests.Response]:
        return super()._MakeDelete(search)
    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para ServiceOrder")
    def SelectAll(self) -> List[ContasAReceberModel]:
        return cast(List[ContasAReceberModel], self._SearchAll())
    def SelectByFilter(self, search: Any) -> List[ContasAReceberModel]:
        return cast(List[ContasAReceberModel], self.getByFilter(search))
    def SelectByFilterAssync(self, search: SearchModule, page_size: int = 172) -> Iterator[ContasAReceberModel]:
        return cast(Iterator[ContasAReceberModel], super().cursorByFilter(search, page_size))
    def SelectAllAssync(self) -> Iterator[ContasAReceberModel]:
        return cast(Iterator[ContasAReceberModel], super()._SelectAllAssync())
    # def MakeUpdate(self, modelForUpdate: IModel, search: SearchModule) -> list[requests.Response]:
    #     return 