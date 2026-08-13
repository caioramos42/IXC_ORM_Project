from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.tableModels.produtosModel import ProdutosModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule
import requests


class Produtos(IContext[ProdutosModel, ProdutosModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, ProdutosModel, manager)

    def Add(self, obj: ProdutosModel) -> Any:
        return self._MakePost(obj)

    def Update(self, obj: ProdutosModel, search: SearchModule) -> list[requests.Response]:
        return self._MakeUpdate(obj, search)

    def Delete(self, search: SearchModule) -> List[requests.Response]:
        return super()._MakeDelete(search)

    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para Produtos")

    def SelectAll(self) -> List[ProdutosModel]:
        return cast(List[ProdutosModel], self._SearchAll())

    def SelectByFilter(self, search: Any) -> List[ProdutosModel]:
        return cast(List[ProdutosModel], self.getByFilter(search))

    def SelectByFilterAssync(
        self,
        search: SearchModule,
        page_size: int = 172
    ) -> Iterator[ProdutosModel]:
        return cast(Iterator[ProdutosModel], super().cursorByFilter(search, page_size))

    def SelectAllAssync(self) -> Iterator[ProdutosModel]:
        return cast(Iterator[ProdutosModel], super()._SelectAllAssync())
