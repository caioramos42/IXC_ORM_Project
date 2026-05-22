from __future__ import annotations

from typing import Optional

from ORM_IXC.enums import operators, sortOrder
from ORM_IXC.interfaces.IModel import IModel
from ORM_IXC.models.searchUtils.gridParamModel import GridParam

import json


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
        sortOrder: sortOrder.SortOrder = sortOrder.SortOrder.ASC
        ):

        self._context_model: Optional[IModel] = context_model
        self._table: str = context_model.table if context_model is not None else ""

        table_prefix = f"{self._table}." if self._table else ""
        self.searchField = f"{table_prefix}{searchField}"
        if not isinstance(query, str):
            self.query = str(query)
        else:
            self.query = query
        self.oper = oper.value
        self.page = str(page)
        self.amount = str(amount)
        self.sortName = f"{table_prefix}{sortName}"
        self.sortOrder = sortOrder.value
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

    def appendGridParams(self, gridParam: GridParam):
        self.grid_param.append(gridParam)

    def _setGridParams(self) -> str:
        return json.dumps([x.to_dict() for x in self.grid_param])

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

    def dto_convert(self, data: dict[str, str]) -> IModel:
        if self._context_model is None:
            raise ValueError(
                "SearchModule.dto_convert requer context_model (modelo de contexto) para delegar dto_convert."
            )
        return self._context_model.dto_convert(data)

    def set_context_model(self, context_model: IModel):
        self._context_model = context_model

    def set_table(self, table: str):
        self._table = table

        if not self.searchField.startswith(f"{table}.") and self.searchField != "":
            self.searchField = f"{table}.{self.searchField}"

        if not self.sortName.startswith(f"{table}.") and self.sortName != "":
            self.sortName = f"{table}.{self.sortName}"
