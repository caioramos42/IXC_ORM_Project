from ORM_IXC.enums.sortOrder import SortOrder
from ORM_IXC.interfaces import IModel, IModelWithId
from ORM_IXC.models.searchUtils.gridParamModel import GridParam
from ORM_IXC.models.searchUtils.searchModel import SearchModule
from ORM_IXC.enums.operators import Operators

class Select:

    def __init__(self, context):
        self.context: IModelWithId = context
        self.search: SearchModule | None = None

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

    def execute(self):
        return self.context.getByFilter(self.search)
def select(context) -> Select:
    return Select(context)