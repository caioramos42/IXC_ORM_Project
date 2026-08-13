from ORM_IXC.enums.sortOrder import SortOrder
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.interfaces.IModel import IModel
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
        self._joins: list[tuple[IContext[Any, Any], JoinCondition, list[SearchNode], str]] = []
        self._group_fields: list[str] = []
        self._having: Optional[SearchModule] = None
        self._count_requested: bool = getattr(context, "_count_enabled", False)
        self._count_field: Any = getattr(context, "_count_field", None)
        self._count_alias: str = getattr(context, "_count_alias", "count")

        sql_funcs = getattr(context, "_sql_functions", []) or []
        for func in sql_funcs:
            if callable(func):
                self._instructions.append(cast(Callable[["Select", list[Any]], None], func))
        # clear functions on context so they don't persist across Select instances
        try:
            setattr(context, "_sql_functions", [])
        except Exception:
            pass

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
            if tree.oper == Operators.BETWEEN.value or tree.oper == Operators.NOTBETWEEN.value:
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

    def groupby(self, *fields: Any) -> "Select":
        from ORM_IXC.statemants.sqlFunctions.groupby import groupby as build_groupby

        self._group_fields = []
        for f in fields:
            if isinstance(f, Field):
                self._group_fields.append(f.name)
            elif hasattr(f, "name"):
                self._group_fields.append(getattr(f, "name"))
            elif isinstance(f, str):
                self._group_fields.append(f)
            else:
                self._group_fields.append(str(f))

        # append groupby so that aggregation functions (count/sum/avg)
        # run against full result set before deduplication
        self._instructions.append(build_groupby(*fields))
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
        # apply HAVING-like filters after post-query SQL functions (aggregations)
        results = self._apply_having(results)
        self._results = results
        return results
    
    # Recomendado para requisições grandes por reculperar os dados via Iterators de forma assincrona
    # Menos direto que execute
    def cursor(self, page_size: int = 172) -> Iterator[T]:
        if self.search is None:
            raise ValueError("Nenhuma pesquisa definida para cursor(). Use .where(...) antes de cursor().")
        self._setField()
        # materialize iterator to allow applying joins and instructions
        iterator = self.context.SelectByFilterAssync(self.search, page_size)
        results = list(iterator)
        results = self._apply_joins(results)
        self._results = results

        for instr in self._instructions:
            instr(self, results)

        # apply HAVING-like filters after post-query SQL functions (aggregations)
        results = self._apply_having(results)
        self._results = results

        return iter(results)
    
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

    def having(self, *conditions: SearchNode) -> "Select":
        """Apply a HAVING-style filter that runs after aggregations.

        Accepts the same `SearchModule`/`SearchFilter` nodes as `where()` but
        will be evaluated in-memory after SQL function instructions (count/sum/avg).
        """
        if not conditions:
            raise ValueError("É necessário informar ao menos uma condição para having().")

        tree = conditions[0]
        for cond in conditions[1:]:
            tree = tree & cond

        if isinstance(tree, SearchFilter):
            self._having = SearchModule.from_tree(tree)
        elif isinstance(tree, SearchModule):
            self._having = tree
        return self

    def _apply_having(self, results: list[T]) -> list[T]:
        if self._having is None or not results:
            return results

        def _parse_literal(val: str):
            try:
                return int(val)
            except Exception:
                try:
                    return float(val)
                except Exception:
                    return val

        def _get_field_value(row: Any, field_name: str):
            if isinstance(field_name, str) and "." in field_name:
                field_name = field_name.split(".")[-1]
            try:
                return self._raw_value(row, field_name)
            except Exception:
                return getattr(row, field_name, None)

        # mapping operator token -> comparator function(value, q_val, module)
        comparators: dict[str, Callable[[Any, Any, SearchModule], bool]] = {
            Operators.MORETHAN.value: lambda v, q, m: (v is not None) and (v > q),
            Operators.MORETHANEQUALS.value: lambda v, q, m: (v is not None) and (v >= q),
            Operators.LASTTHAN.value: lambda v, q, m: (v is not None) and (v < q),
            Operators.LASTTHANEQUALS.value: lambda v, q, m: (v is not None) and (v <= q),
            Operators.EQUALS.value: lambda v, q, m: (v is not None) and (str(v) == str(q)),
            Operators.DIFFERENT.value: lambda v, q, m: (v is not None) and (str(v) != str(q)),
            Operators.LIKE.value: lambda v, q, m: (v is not None) and (str(q) in str(v)),
            Operators.NOTLIKE.value: lambda v, q, m: (v is not None) and (str(q) not in str(v)),
            Operators.IN.value: lambda v, q, m: (v is not None) and (str(v) in [x.strip() for x in str(q).split(",")]),
            Operators.NOTIN.value: lambda v, q, m: (v is not None) and (str(v) not in [x.strip() for x in str(q).split(",")]),
            # BETWEEN expects module.secondParameter to be the high value
            Operators.BETWEEN.value: lambda v, q, m: _between_helper(v, q, m),
            Operators.NOTBETWEEN.value: lambda v, q, m: not _between_helper(v, q, m),
        }

        def _between_helper(v, q, module: SearchModule):
            if v is None:
                return False
            low = _parse_literal(q)
            high = _parse_literal(module.secondParameter) if module.secondParameter is not None else None
            try:
                return float(low) <= float(v) <= float(high)
            except Exception:
                return str(low) <= str(v) <= str(high)

        def _match_module(module: SearchModule, row: Any) -> bool:
            value = _get_field_value(row, module.searchField)
            q_raw = module.query
            q_val = None if q_raw is None else _parse_literal(q_raw)

            # handle explicit None comparisons for equality
            if value is None:
                if module.oper == Operators.EQUALS.value:
                    return q_val in (None, "")
                return False

            # try to coerce numeric types when both look numeric
            try:
                if isinstance(value, (int, float)) and isinstance(q_val, (int, float)):
                    cmp_val = value
                    cmp_q = q_val
                else:
                    cmp_val = value
                    cmp_q = q_val
            except Exception:
                cmp_val = value
                cmp_q = q_val

            comparator = comparators.get(module.oper)
            if comparator is None:
                # unknown operator — treat as non-match
                return False

            try:
                return bool(comparator(cmp_val, cmp_q, module))
            except Exception:
                return False

        def _match(node: SearchNode, row: Any) -> bool:
            if isinstance(node, SearchModule):
                return _match_module(node, row)
            # SearchFilter
            left_ok = _match(node.left, row)
            right_ok = _match(node.right, row)
            if node.operator == "AND":
                return left_ok and right_ok
            return left_ok or right_ok

        filtered = [row for row in results if _match(self._having, row)]
        return filtered
    
    def columns(self, *fields: Any) -> "Select":
        if len(fields) > 0:
            for field in fields:
                self.selected_fields.append(cast(Field, field))
        return self

    def join(self, context: IContext[Any, Any], on: object, *filters: Any, join_type: str | None = None) -> "Select":
        if not isinstance(on, JoinCondition):
            raise TypeError("join() espera uma condição no formato Modelo.campo == OutroModelo.campo")

        normalized_filters: list[SearchNode] = []
        resolved_join_type = "inner"

        for item in filters:
            if isinstance(item, str) and item.lower() in {"left", "inner"}:
                resolved_join_type = item.lower()
                continue
            if not isinstance(item, (SearchModule, SearchFilter)):
                raise TypeError("join() aceita apenas filtros do tipo SearchModule ou SearchFilter")
            normalized_filters.append(item)

        if join_type is not None:
            resolved_join_type = join_type.lower()

        self._joins.append((context, on, normalized_filters, resolved_join_type))
        return self
    
    def _setField(self):
        if len(self.selected_fields) > 0 and self.search is not None:
            main_fields = self._selected_fields_for_context(self.context)
            if main_fields:
                self.search.setColumns(*main_fields)
        return self

    def _apply_joins(self, results: list[T]) -> list[T]:
        joined_results: list[Any] = results

        for join_context, condition, join_filters, join_type in self._joins:
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

            base_join_filter = SearchModule(
                searchField=join_field.name,
                query=", ".join(str(value) for value in main_values),
                oper=Operators.IN,
                sortName=join_field.name,
            )

            if join_filters:
                tree = base_join_filter
                for filter_node in join_filters:
                    tree = tree & filter_node
                join_search = SearchModule.from_tree(tree)
            else:
                join_search = base_join_filter

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

                if matches:
                    for match in matches:
                        row_copy = self._clone_with_inners(row)
                        row_copy.inner(match)
                        next_results.append(row_copy)
                elif join_type == "left":
                    row_copy = self._clone_with_inners(row)
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
