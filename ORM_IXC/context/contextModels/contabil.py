from typing import Any, List, Iterator, cast

from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.contaContabilSintetica import ContaContabilSinteticaModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule

class ContaContabilSintetica(IContext[ContaContabilSinteticaModel, ContaContabilSinteticaModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, ContaContabilSinteticaModel, manager)
    def Add(self, obj: ContaContabilSinteticaModel) -> Any:
        return self._MakePost(obj)
    def Update(self, obj: ContaContabilSinteticaModel) -> Any:
        return self._MakePut(obj)
    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para ServiceOrder")
    def SelectAll(self) -> List[ContaContabilSinteticaModel]:
        return cast(List[ContaContabilSinteticaModel], self._SearchAll())
    def SelectByFilter(self, search: Any) -> List[ContaContabilSinteticaModel]:
        return cast(List[ContaContabilSinteticaModel], self.getByFilter(search))
    def SelectByFilterAssync(self, search: SearchModule, page_size: int = 172) -> Iterator[ContaContabilSinteticaModel]:
        return cast(Iterator[ContaContabilSinteticaModel], super().cursorByFilter(search, page_size))
    def SelectAllAssync(self) -> Iterator[ContaContabilSinteticaModel]:
        return cast(Iterator[ContaContabilSinteticaModel], super()._SelectAllAssync())
