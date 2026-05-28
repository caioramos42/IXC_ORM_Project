from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.atendimentoModel import AtendimentoModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule

class Atendimento(IContext[AtendimentoModel, AtendimentoModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, AtendimentoModel, manager)
    def Add(self, obj: AtendimentoModel) -> Any:
        return self._MakePost(obj)
    def Update(self, obj: AtendimentoModel) -> Any:
        return self._MakePut(obj)
    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para ServiceOrder")
    def SelectAll(self) -> List[AtendimentoModel]:
        return cast(List[AtendimentoModel], self._SearchAll())
    def SelectByFilter(self, search: Any) -> List[AtendimentoModel]:
        return cast(List[AtendimentoModel], self.getByFilter(search))
    def SelectByFilterAssync(self, search: SearchModule, page_size: int = 172) -> Iterator[AtendimentoModel]:
        return cast(Iterator[AtendimentoModel], super().cursorByFilter(search, page_size))
    def SelectAllAssync(self) -> Iterator[AtendimentoModel]:
        return cast(Iterator[AtendimentoModel], super()._SelectAllAssync())

