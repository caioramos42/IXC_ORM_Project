from ORM_IXC.enums import operators

class GridParam():
    def __init__(self, searchField: str, oper: operators.Operators, query: str, logicOperator: str = "AND", secondParameter = None):
        self.searchField = searchField
        self.oper = oper
        self.query = query
        self.logicOperator = logicOperator
        self.secondParameter = secondParameter
    def to_dict(self):
        dictGrid = {
            'TB': self.searchField,
            'OP': self.oper.value,
            'C': self.logicOperator,
            'P': self.query
        }
        if self.secondParameter is not None:
            if self.oper == operators.Operators.BETWEEN:
                dictGrid['P2'] = self.secondParameter
            else:
                raise ValueError("Esta operação não aceita um segundo parâmentro")
        return dictGrid

