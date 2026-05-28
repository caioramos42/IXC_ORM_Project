from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.carteiraDeCobrancaModel import CarteiraDeCobrancaModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule

class CarteiraDeConbranca(IContext[CarteiraDeCobrancaModel, CarteiraDeCobrancaModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, CarteiraDeCobrancaModel, manager)
    def Add(self, obj: CarteiraDeCobrancaModel) -> Any:
        return self._MakePost(obj)
    def Update(self, obj: CarteiraDeCobrancaModel) -> Any:
        return self._MakePut(obj)
    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para ServiceOrder")
    def SelectAll(self) -> List[CarteiraDeCobrancaModel]:
        return cast(List[CarteiraDeCobrancaModel], self._SearchAll())
    def SelectByFilter(self, search: Any) -> List[CarteiraDeCobrancaModel]:
        return cast(List[CarteiraDeCobrancaModel], self.getByFilter(search))
    def SelectByFilterAssync(self, search: SearchModule, page_size: int = 172) -> Iterator[CarteiraDeCobrancaModel]:
        return cast(Iterator[CarteiraDeCobrancaModel], super().cursorByFilter(search, page_size))
    def SelectAllAssync(self) -> Iterator[CarteiraDeCobrancaModel]:
        return cast(Iterator[CarteiraDeCobrancaModel], super()._SelectAllAssync())
