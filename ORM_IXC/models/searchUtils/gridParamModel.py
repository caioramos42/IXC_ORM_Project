from IXC_ORM_Project.enums import operators
from IXC_ORM_Project.interfaces.IModel import IModel

class GridParam(IModel):
    def __init__(self, searchField: str, oper: operators.Operators, query: str):
        self.searchField = searchField
        self.oper = oper.value
        self.query = query
    def to_dict(self):
        return {
            'TB': self.searchField,
            'OP': self.oper,
            'P': self.query
        }