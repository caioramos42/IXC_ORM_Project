from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.movimentoDeProdutosModel import MovimentoDeProdutosModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule
import requests


class MovimentoDeProdutos(IContext[MovimentoDeProdutosModel, MovimentoDeProdutosModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, MovimentoDeProdutosModel, manager)

    def Add(self, obj: MovimentoDeProdutosModel) -> Any:
        return self._MakePost(obj)

    def Update(self, obj: MovimentoDeProdutosModel, search: SearchModule) -> list[requests.Response]:
        return self._MakeUpdate(obj, search)

    def Delete(self, search: SearchModule) -> List[requests.Response]:
        return super()._MakeDelete(search)

    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para MovimentoDeProdutos")

    def SelectAll(self) -> List[MovimentoDeProdutosModel]:
        return cast(List[MovimentoDeProdutosModel], self._SearchAll())

    def SelectByFilter(self, search: Any) -> List[MovimentoDeProdutosModel]:
        return cast(List[MovimentoDeProdutosModel], self.getByFilter(search))

    def SelectByFilterAssync(
        self,
        search: SearchModule,
        page_size: int = 172
    ) -> Iterator[MovimentoDeProdutosModel]:
        return cast(Iterator[MovimentoDeProdutosModel], super().cursorByFilter(search, page_size))

    def SelectAllAssync(self) -> Iterator[MovimentoDeProdutosModel]:
        return cast(Iterator[MovimentoDeProdutosModel], super()._SelectAllAssync())
