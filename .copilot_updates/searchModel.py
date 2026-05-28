from __future__ import annotations

from typing import Optional


from ORM_IXC.enums import operators, sortOrder as sortOrder_module
from ORM_IXC.interfaces.IModel import IModel
from ORM_IXC.models.searchUtils.gridParamModel import GridParam

import json


class SearchModule(IModel):
    def __init__(
        self,
        searchField: str,
        query: str,
        oper: operators.Operators,
        context_model: Mapped[IModel | None] = Field("context_model", IModel | None, None,)
        sortName: Mapped[str] = Field("sortName", str, "id",)
        amount: Mapped[int] = Field("amount", int, 9999,)
        page: Mapped[int] = Field("page", int, 1,)
        sort_order: Mapped[sortOrder_module.SortOrder] = Field("sort_order", sortOrder_module.SortOrder, sortOrder_module.SortOrder.ASC)
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
        self.page = str(page)
        self.amount = str(amount)
        self.sortName = f"{table_prefix}{sortName}"
        self.sortOrder = sort_order.value
        self.grid_param: list[GridParam] = []

    def setaAmount(self, amount: int) -> None:
        self.amount = str(amount)
    def setPage(self, page: int) -> None:
        self.page = str(page)

    @property
    def table(self) -> str:
        if self._context_model is not None:
            return self._context_model.table
        return self._table

    def appendGridParams(self, gridParam: GridParam) -> None:
        self.grid_param.append(gridParam)

    def _setGridParams(self) -> str:
        return json.dumps([x.to_dict() for x in self.grid_param])

    @classmethod
    def dto_convert(cls_, data: dict[str, str]) -> IModel:
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
        if len(self.grid_param) == 0:
            return dict_class
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
    def __and__(self, other: SearchModule) -> SearchModule:
        if not isinstance(other, SearchModule):
            raise NotImplementedError()
        if other is None:
            raise ValueError("O operador AND requer outro SearchModule como operando.")
        self.appendGridParams(GridParam(
                    other.searchField,
                    operators.Operators(other.oper),
                    other.query
                ))
        return self
