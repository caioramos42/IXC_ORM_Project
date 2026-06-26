from ORM_IXC.enums.sortOrder import SortOrder
from ORM_IXC.interfaces import IContext, IModel
from ORM_IXC.models.searchUtils.searchModel import SearchFilter, SearchModule, SearchNode
from ORM_IXC.enums.operators import Operators
from typing import Iterator, TypeVar, Generic, Callable, Optional, List, Any, cast
import copy

from ORM_IXC.statemants.maps.classBase import Field, JoinCondition

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
        self.selected_fields: list[Field] = []
        self._joins: list[tuple[IContext[Any, Any], JoinCondition]] = []

    def where(self, *conditions: SearchNode) -> "Select":
        if not conditions:
            raise ValueError("É necessário informar ao menos uma condição.")

        # junta tudo com AND
        tree = conditions[0]

        for cond in conditions[1:]:
            tree = tree & cond

        if isinstance(tree, SearchFilter):
            self.search = SearchModule.from_tree(tree)

        elif isinstance(tree, SearchModule):
            if tree.oper == Operators.BETWEEN.value:
                self.search = SearchModule.from_tree(tree)
            else:
                self.search = tree
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
        self._setField()
        results = self.context.SelectByFilter(self.search)
        results = self._apply_joins(results)
        self._results = results

        for instr in self._instructions:
            instr(self, results)
        return results
    
    # Recomendado para requisições grandes por reculperar os dados via Iterators de forma assincrona
    # Menos direto que execute
    def cursor(self, page_size: int = 172) -> Iterator[T]:
        if self.search is None:
            raise ValueError("Nenhuma pesquisa definida para cursor(). Use .where(...) antes de cursor().")
        self._setField()
        return self.context.SelectByFilterAssync(self.search, page_size)
    
    # Este é um processo lento e caro, recomendado apenas se tiverem poucos campos na pesquisa
    # Não é possivel limitar o resultado por .limit()!!!
    def all(self) -> list[T]:
        self._setField()
        return self.context.SelectAll()
    
    # Recomendado para requisições grandes por reculperar os dados via Iterators de forma assincrona
    # Não é possivel limitar o resultado por .limit()!!!
    def allAssync(self) -> Iterator[T]:
        self._setField()
        return self.context.SelectAllAssync()
    
    def first(self):
        self._setField()
        self.limit(1)
        results = self.execute()
        return results[0] if results else None
    
    def last(self):
        self._setField()
        self.order_by('id', 'desc').limit(1)
        results = self.execute()
        return results[0] if results else None
    
    def As(self, alias: str):
        if self.search is not None:
            self.search.alias = alias
        return self
    
    def columns(self, *fields: Any) -> "Select":
        if len(fields) > 0:
            for field in fields:
                self.selected_fields.append(cast(Field, field))
        return self

    def join(self, context: IContext[Any, Any], on: object) -> "Select":
        if not isinstance(on, JoinCondition):
            raise TypeError("join() espera uma condição no formato Modelo.campo == OutroModelo.campo")
        self._joins.append((context, on))
        return self
    
    def _setField(self):
        if len(self.selected_fields) > 0 and self.search is not None:
            main_fields = self._selected_fields_for_context(self.context)
            if main_fields:
                self.search.setColumns(*main_fields)
        return self

    def _apply_joins(self, results: list[T]) -> list[T]:
        joined_results: list[Any] = results

        for join_context, condition in self._joins:
            if not joined_results:
                return []

            main_field, join_field = self._resolve_join_fields(join_context, condition)
            main_values = [
                self._raw_value(row, main_field.name)
                for row in joined_results
            ]
            main_values = [value for value in main_values if value not in (None, "")]

            if not main_values:
                return []

            join_search = SearchModule(
                searchField=join_field.name,
                query=", ".join(str(value) for value in main_values),
                oper=Operators.IN,
                sortName=join_field.name,
            )
            join_fields = self._selected_fields_for_context(join_context)
            if join_fields:
                join_search.setColumns(*join_fields)
            join_rows = join_context.SelectByFilter(join_search)
            index: dict[str, list[Any]] = {}

            for join_row in join_rows:
                key = str(self._raw_value(join_row, join_field.name))
                index.setdefault(key, []).append(join_row)

            next_results: list[Any] = []
            for row in joined_results:
                key = str(self._raw_value(row, main_field.name))
                matches = index.get(key, [])

                for match in matches:
                    row_copy = self._clone_with_inners(row)
                    row_copy.inner(match)
                    next_results.append(row_copy)

            joined_results = next_results

        return joined_results

    def _resolve_join_fields(
        self,
        join_context: IContext[Any, Any],
        condition: JoinCondition,
    ) -> tuple[Field, Field]:
        join_model = self._context_model_type(join_context)

        if condition.right.model is join_model:
            return condition.left, condition.right
        if condition.left.model is join_model:
            return condition.right, condition.left

        return condition.left, condition.right

    def _context_model_type(self, context: IContext[Any, Any]) -> type[Any] | None:
        return getattr(context, "contextModel", None)

    def _selected_fields_for_context(self, context: IContext[Any, Any]) -> list[Field]:
        context_model = self._context_model_type(context)
        if context_model is None:
            return []

        return [
            field
            for field in self.selected_fields
            if field.model is context_model
        ]

    def _raw_value(self, row: Any, field_name: str) -> Any:
        if hasattr(row, "_raw_value"):
            return row._raw_value(field_name)

        value = getattr(row, field_name)
        if isinstance(value, Field):
            return value._val
        return value

    def _clone_with_inners(self, row: Any) -> Any:
        row_copy = copy.copy(row)
        row_copy.__dict__ = dict(getattr(row, "__dict__", {}))
        row_copy.__dict__["_inners"] = list(getattr(row, "_inners", []))
        return row_copy
        
def select(context: IContext[T, U]) -> Select[T, U]:
    return Select(context)
