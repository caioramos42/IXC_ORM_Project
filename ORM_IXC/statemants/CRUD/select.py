from ORM_IXC.enums.sortOrder import SortOrder
from ORM_IXC.interfaces import IContext, IModel
from ORM_IXC.models.tableModels.contratoDoClienteModel import ContratoDoClienteModel
from ORM_IXC.models.searchUtils.gridParamModel import GridParam
from ORM_IXC.models.searchUtils.searchModel import SearchModule
from ORM_IXC.enums.operators import Operators
from typing import Iterator, TypeVar, Generic, Callable, Optional, List, Any

from ORM_IXC.statemants.sqlOperations.inner import formatInner

T = TypeVar('T', bound=IModel)
U = TypeVar('U', bound=IModel)

class Select(Generic[T, U]):

    def __init__(self, context: IContext[T, U]):
        self.context: IContext[T, U] = context
        self.search: Optional[SearchModule] = None
        self._instructions: List[Callable[["Select", list[Any]], None]] = []
        self._results: Optional[list[T]] = None
        self._inner_results: List[list[Any]] = []
        self.inners: Optional[SearchModule] = None

    def where(self, *conditions: SearchModule) -> "Select":
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

    def limit(self, value: int) -> "Select":
        if self.search is not None:
            self.search.setaAmount(value)
        return self

    def page(self, value: int) -> "Select":
        if self.search is not None:
            self.search.setPage(value)
        return self

    def order_by(self, field: str, direction: str = "asc") -> "Select":
        if self.search is not None:
            self.search.sortName = field
            self.search.sortOrder = SortOrder(direction).value
        return self

    def to_dict(self):
        if self.search is None:
            return {}
        return self.search.to_dict()

    # Recomendado para requisições curtas, mais direto que cursor
    def execute(self) -> list[T]:
        if self.search is None:
            raise ValueError("Nenhuma pesquisa definida para execute(). Use .where(...) antes de execute().")

        results = self.context.SelectByFilter(self.search)
        self._results = results

        for instr in self._instructions:
            instr(self, results)

        return results
    
    # Recomendado para requisições grandes por reculperar os dados via Iterators de forma assincrona
    # Menos direto que execute
    def cursor(self, page_size: int = 172) -> Iterator[T]:
        if self.search is None:
            raise ValueError("Nenhuma pesquisa definida para cursor(). Use .where(...) antes de cursor().")
        return self.context.SelectByFilterAssync(self.search, page_size)
    
    # Este é um processo lento e caro, recomendado apenas se tiverem poucos campos na pesquisa
    # Não é possivel limitar o resultado por .limit()!!!
    def all(self) -> list[T]:
        return self.context.SelectAll()
    
    # Recomendado para requisições grandes por reculperar os dados via Iterators de forma assincrona
    # Não é possivel limitar o resultado por .limit()!!!
    def allAssync(self) -> Iterator[T]:
        return self.context.SelectAllAssync()
    
    def first(self):
        self.limit(1)
        results = self.execute()
        return results[0] if results else None
    
    def last(self):
        self.order_by('id', 'desc').limit(1)
        results = self.execute()
        return results[0] if results else None
    
    def inner(self, searchContext: IContext[T, U], search: SearchModule, *searchModel: SearchModule) -> "Select":
        def instruction(select_self: "Select", previous_results: list[Any]) -> None:
            cm = searchContext._get_context_model()
            search.set_context_model(cm)
            try:
                search.set_table(cm.table)
            except Exception:
                pass

            # Preferir usar previous_results quando disponível para formar o IN
            if previous_results:
                inner_query = formatInner(previous_results)
            else:
                # executar a busca interna no contexto fornecido
                inner_items = searchContext.SelectByFilter(search)
                inner_query = formatInner(inner_items)

            # montar SearchModule que filtra pelo IN(ids)
            inner_search = SearchModule(
                "id",
                inner_query,
                Operators.IN,
                cm,
            )

            # anexar parâmetros enviados no cabeçalho para a search interna
            for s in searchModel:
                inner_search.appendGridParams(
                    GridParam(
                        s.searchField,
                        Operators(s.oper),
                        s.query,
                    )
                )

            # executar a busca interna (cada inner é independente)
            try:
                inner_items = searchContext.SelectByFilter(inner_search)
            except Exception:
                inner_items = []

            select_self._inner_results.append(inner_items)

        self._instructions.append(instruction)
        return self


        
        
def select(context: IContext[T, U]) -> Select[T, U]:
    return Select(context)
