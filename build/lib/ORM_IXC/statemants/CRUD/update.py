from typing import Any, TypeVar, Generic

from ORM_IXC.enums.operators import Operators
from ORM_IXC.interfaces import IContext, IModel
from ORM_IXC.models.searchUtils.gridParamModel import GridParam
from ORM_IXC.models.searchUtils.searchModel import SearchModule

T = TypeVar('T', bound=IModel)
U = TypeVar('U', bound=IModel)

class Update(Generic[T, U]):

    def __init__(self, context: IContext[T, U]):
        self.context: IContext[T, U] = context
        self.search: SearchModule | None = None
        self.payload: U | None = None

    def where(self, *conditions: SearchModule) -> "Update":
        """Define as condições de filtro para o UPDATE (como em SELECT)"""
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

    def values(self, payload: U) -> "Update":
        """Define o objeto com os valores a serem atualizados"""
        if not isinstance(payload, IModel):
            raise TypeError(f"Expected an IModel instance, got {type(payload).__name__}")
        self.payload = payload
        return self

    def to_dict(self) -> dict[str, Any]:
        """Retorna os dados do UPDATE em formato de dicionário"""
        result = {}
        
        if self.search is not None:
            result['where'] = self.search.to_dict()
        
        if self.payload is not None:
            result['values'] = self.payload.to_dict()
        
        return result

    def execute(self) -> list[T]:
        """Executa o UPDATE com pesquisa"""
        if self.search is None:
            raise ValueError("Nenhuma condição definida para update(). Use .where(...) antes de .execute().")
        
        if self.payload is None:
            raise ValueError("Nenhum payload informado para update(). Use .values(...) antes de .execute().")

        return self.context.Update(self.payload, self.search)

def update(context: IContext[T, U]) -> Update[T, U]:
    """Factory function para criar uma instância de Update"""
    return Update(context)



