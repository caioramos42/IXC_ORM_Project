from __future__ import annotations

from typing import Optional, Union, Any


from ORM_IXC.enums import operators, sortOrder as sortOrder_module
from ORM_IXC.interfaces.IModel import IModel
from ORM_IXC.models.searchUtils.gridParamModel import GridParam
import copy
import json

from ORM_IXC.statemants.maps.classBase import Field


class SearchModule(IModel):
    def __init__(
        self,
        searchField: str,
        query: str,
        oper: operators.Operators,
        context_model: IModel | None = None,
        sortName: str = "id",
        amount: int = 9999,
        page: int = 1,
        sort_order: sortOrder_module.SortOrder = sortOrder_module.SortOrder.ASC,
        secondParameter: str | None = None
        ):

        self._context_model: Optional[IModel] = context_model
        self._table: str = context_model.table if context_model is not None else ""

        table_prefix = f"{self._table}." if self._table else ""
        self.searchField = f"{table_prefix}{searchField}"
        self.query: str
        if not isinstance(query, str):
            self.query = str(query)
        else:
            self.query = query
        self.oper = oper.value
        self.secondParameter = str(secondParameter) if secondParameter is not None else None
        self.page = str(page)
        self.amount = str(amount)
        self.sortName = f"{table_prefix}{sortName}"
        self.sortOrder = sort_order.value
        self.grid_param: Optional[list[GridParam]] = None
        self._filter_tree: list[dict[str, Any]] | None = None
        self.alias = None
        self.columns : list[str] = []
        

    def setColumns(self, *columns: Field):
        if len(columns) > 0:
            for column in columns:
                self.columns.append(column.name)

    def setaAmount(self, amount: int) -> None:
        self.amount = str(amount)
    def setPage(self, page: int) -> None:
        self.page = str(page)
    def setAlias(self, alias: str) -> None:
        self.alias = alias

    @property
    def table(self) -> str:
        if self._context_model is not None:
            return self._context_model.table
        return self._table

    @classmethod
    def set_alias(cls_, alias: str):
        """Placeholder classmethod to satisfy IModel protocol.

        Actual per-instance behavior is provided by binding `self.dto_convert`
        in `set_context_model` to delegate to the concrete context model.
        """
        raise NotImplementedError("SearchModule.dto_convert is a placeholder")


    def appendGridParams(self, gridParam: GridParam) -> None:
        if self.grid_param is not None:
            self.grid_param.append(gridParam)

    def _setGridParams(self) -> str:
        if self.grid_param is not None:
            return json.dumps([x.to_dict() for x in self.grid_param])
        else:
            return ""

    @classmethod
    def dto_convert(cls_, data: dict[str, str], columns: list[str]) -> IModel:
        """Placeholder classmethod to satisfy IModel protocol.

        Actual per-instance behavior is provided by binding `self.dto_convert`
        in `set_context_model` to delegate to the concrete context model.
        """
        raise NotImplementedError("SearchModule.dto_convert is a placeholder")

    def to_dict(self) -> dict[str, str]:
        dict_class = {
            "qtype": self.searchField,
            "query": self.query,
            "oper": self.oper,
            "page": self.page,
            "rp": self.amount,
            "sortname": self.sortName,
            "sortorder": self.sortOrder,
        }
        if self._filter_tree:
            # Nova lógica — árvore via with_filters()
            dict_class["grid_param"] = json.dumps(self._filter_tree)

        elif self.grid_param:
            # Legada — lista via appendGridParams()
            dict_class["grid_param"] = self._setGridParams()
        return dict_class

    # dto_convert is provided at instance-level by `set_context_model`
    # to delegate to the provided context model. This avoids classmethod
    # signature conflicts with IModel while keeping per-instance behavior.

    def set_context_model(self, context_model: IModel):
        self._context_model = context_model
        # bind instance-level dto_convert to delegate to the provided context model
        try:
            self.dto_convert = context_model.dto_convert  # type: ignore[assignment]
        except Exception:
            pass

    def set_table(self, table: str):
        self._table = table

        if not self.searchField.startswith(f"{table}.") and self.searchField != "":
            self.searchField = f"{table}.{self.searchField}"

        if not self.sortName.startswith(f"{table}.") and self.sortName != "":
            self.sortName = f"{table}.{self.sortName}"
   
    def with_filters(self, tree: SearchNode) -> SearchModule:
        """Retorna cópia de self com a árvore de filtros aplicada."""
        flat = _flatten_tree(tree)

        # O primeiro item da lista vira o envelope principal
        envelope = flat[0]
        novo = copy.deepcopy(self)
        novo.searchField = envelope["TB"]
        novo.oper        = envelope["OP"]
        novo.query       = envelope["P"]
        novo.secondParameter = envelope.get("P2")

        # O restante vira grid_param
        novo._filter_tree = flat[1:] if len(flat) > 1 else []
        return novo
    
    @staticmethod
    def from_tree(tree: SearchNode) -> "SearchModule":
        flat = _flatten_tree(tree)
        between_count = sum(1 for item in flat if item["OP"] == operators.Operators.BETWEEN.value)

        if between_count > 1:
            raise ValueError("Apenas uma pesquisa BETWEEN pode ser usada em grid_param.")

        if flat[0]["OP"] == operators.Operators.BETWEEN.value or flat[0]["OP"] == operators.Operators.NOTBETWEEN.value:
            envelope = {
                "TB": "id",
                "OP": operators.Operators.MORETHAN.value,
                "P": "0",
            }
            flat[0]["C"] = flat[0].get("C") or "AND"
            flat.insert(0, envelope)

        envelope = flat[0]

        novo = SearchModule(
            searchField=envelope["TB"],
            query=envelope["P"],
            oper=operators.Operators(envelope["OP"]),
            secondParameter=envelope.get("P2")
        )
        novo._filter_tree = flat[1:]  # ← lista plana, não a árvore!
        return novo
       
    def __and__(self, other: SearchNode) -> SearchFilter:
        if not isinstance(other, (SearchModule, SearchFilter)):
            raise TypeError(f"AND não suportado com {type(other)}")
        return SearchFilter(self, "AND", other)

    def __or__(self, other: SearchNode) -> SearchFilter:
        if not isinstance(other, (SearchModule, SearchFilter)):
            raise TypeError(f"OR não suportado com {type(other)}")
        return SearchFilter(self, "OR", other)



class SearchFilter:
    """Nó interno da árvore: representa (left OP right)."""

    def __init__(self, left: SearchNode, operator: str, right: SearchNode) -> None:
        self.left = left
        self.operator = operator
        self.right = right

    def __and__(self, other: SearchNode) -> SearchFilter:
        return SearchFilter(self, "AND", other)

    def __or__(self, other: SearchNode) -> SearchFilter:
        return SearchFilter(self, "OR", other)


SearchNode = Union["SearchModule", SearchFilter]


def _flatten_tree(node: SearchNode, logic_op: str = "") -> list[dict[str, Any]]:
    """
    Traversal in-order da árvore → lista plana de GridParams.

    - O nó mais à esquerda vira o envelope principal (sem 'C').
    - Cada demais nó recebe o 'C' do operador do pai que o introduziu.

    Exemplo: (A & B) | (C & D)
        A → envelope (sem C)
        B → C = "AND"
        C → C = "OR"
        D → C = "AND"
    """
    if isinstance(node, SearchModule):
        search = {"TB": node.searchField, "OP": node.oper, "C": logic_op, "P": node.query}
        if node.secondParameter is not None:
            search["P2"] = node.secondParameter
        return [search]

    # Nó interno: desce left com o operador herdado do pai,
    # desce right com o operador deste nó.
    return (
        _flatten_tree(node.left, logic_op) +
        _flatten_tree(node.right, node.operator)
    )
