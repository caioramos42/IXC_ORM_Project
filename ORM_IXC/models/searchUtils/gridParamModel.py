from ORM_IXC.enums import operators

class GridParam():
    def __init__(self, searchField: str, oper: operators.Operators, query: str, logicOperator: str = "AND"):
        self.searchField = searchField
        self.oper = oper.value
        self.query = query
        self.logicOperator = logicOperator
    def to_dict(self):
        return {
            'TB': self.searchField,
            'OP': self.oper,
            'C': self.logicOperator,
            'P': self.query
        }