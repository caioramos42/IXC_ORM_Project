from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.classeFinanceiraAnalitica import ClasseFinanceiraAnaliticaModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule

class ClasseFinanceiraAnalitica(IContext[ClasseFinanceiraAnaliticaModel, ClasseFinanceiraAnaliticaModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, ClasseFinanceiraAnaliticaModel, manager)
    def Add(self, obj: ClasseFinanceiraAnaliticaModel) -> Any:
        return self._MakePost(obj)
    def Update(self, obj: ClasseFinanceiraAnaliticaModel) -> Any:
        return self._MakePut(obj)
    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para ServiceOrder")
    def SelectAll(self) -> List[ClasseFinanceiraAnaliticaModel]:
        return cast(List[ClasseFinanceiraAnaliticaModel], self._SearchAll())
    def SelectByFilter(self, search: Any) -> List[ClasseFinanceiraAnaliticaModel]:
        return cast(List[ClasseFinanceiraAnaliticaModel], self.getByFilter(search))
    def SelectByFilterAssync(self, search: SearchModule, page_size: int = 172) -> Iterator[ClasseFinanceiraAnaliticaModel]:
        return cast(Iterator[ClasseFinanceiraAnaliticaModel], super().cursorByFilter(search, page_size))
    def SelectAllAssync(self) -> Iterator[ClasseFinanceiraAnaliticaModel]:
        return cast(Iterator[ClasseFinanceiraAnaliticaModel], super()._SelectAllAssync())