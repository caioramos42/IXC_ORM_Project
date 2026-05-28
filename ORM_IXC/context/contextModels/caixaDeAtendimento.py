from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.caixaDeAtendimentoModel import CaixaDeAtendimentoModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule

class CaixaDeAtendimento(IContext[CaixaDeAtendimentoModel, CaixaDeAtendimentoModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, CaixaDeAtendimentoModel, manager)
    def Add(self, obj: CaixaDeAtendimentoModel) -> Any:
        return self._MakePost(obj)
    def Update(self, obj: CaixaDeAtendimentoModel) -> Any:
        return self._MakePut(obj)
    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para ServiceOrder")
    def SelectAll(self) -> List[CaixaDeAtendimentoModel]:
        return cast(List[CaixaDeAtendimentoModel], self._SearchAll())
    def SelectByFilter(self, search: Any) -> List[CaixaDeAtendimentoModel]:
        return cast(List[CaixaDeAtendimentoModel], self.getByFilter(search))
    def SelectByFilterAssync(self, search: SearchModule, page_size: int = 172) -> Iterator[CaixaDeAtendimentoModel]:
        return cast(Iterator[CaixaDeAtendimentoModel], super().cursorByFilter(search, page_size))
    def SelectAllAssync(self) -> Iterator[CaixaDeAtendimentoModel]:
        return cast(Iterator[CaixaDeAtendimentoModel], super()._SelectAllAssync())
