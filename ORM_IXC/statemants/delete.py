from typing import Any, List, TypeVar, Generic

from ORM_IXC.enums.operators import Operators
from ORM_IXC.interfaces import IContext, IModel
from ORM_IXC.models.searchUtils.gridParamModel import GridParam
from ORM_IXC.models.searchUtils.searchModel import SearchModule
import requests


T = TypeVar('T', bound=IModel)
U = TypeVar('U', bound=IModel)


class Delete(Generic[T, U]):

    def __init__(self, context: IContext[T, U]):
        self.context: IContext[T, U] = context
        self.search: SearchModule | None = None

    def where(self, *conditions: SearchModule) -> "Delete[T, U]":
        for i, condition in enumerate(conditions):
            if i == 0:
                if isinstance(condition, SearchModule):
                    self.search = condition
                continue
            if self.search is not None:
                self.search.appendGridParams(
                    GridParam(
                        condition.searchField,
                        Operators(condition.oper),
                        condition.query
                    )
                )
        return self

    def execute(self) -> List[requests.Response]:
        if self.search is None:
            raise ValueError("Nenhuma condição definida para delete(). Use .where(...) antes de .execute().")

        return self.context.Delete(self.search)

def delete(context: IContext[T, U]) -> Delete[T, U]:
    """Factory function para criar uma instância de Delete"""
    return Delete(context)