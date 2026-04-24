from ORM_IXC.enums import operators, sortOrder
from ORM_IXC.interfaces.IModel import IModel
from ORM_IXC.models.searchUtils.gridParamModel import GridParam
import json

class SearchModule(IModel):
    def __init__(self, searchField: str, query: str, oper: operators.Operators, table='', sortName="id", amount = 9999, page = 1, sortOrder = sortOrder.SortOrder.ASC):
        self.searchField = "{}.{}".format(table,searchField) if table != '' else searchField
        self.query = query
        self.oper = oper.value
        self.table = table
        self.page = str(page)
        self.amount = str(amount)
        self.sortName = "{}.{}".format(table,sortName) if table != '' else sortName
        self.sortOrder = sortOrder.value
        self.grid_param = []
        
    def appendGridParams(self, gridParam: GridParam):
        self.grid_param.append(gridParam)
        
    def _setGridParams(self) ->list[dict]: 
        return json.dumps([x.to_dict() for x in self.grid_param])
         
     
    def to_dict(self) -> dict:
        dict_class = {
            'qtype': self.searchField,
            'query': self.query,
            'oper': self.oper,
            'page': self.page,
            'rp': self.amount,
            'sortname': self.sortName,
            'sortorder': self.sortOrder
        }
        if len(self.grid_param) == 0:
            return dict_class
        dict_class['grid_param'] = self._setGridParams()
        return dict_class
    
    def set_table(self, table: str):
        self.table = table
        
        if not self.searchField.startswith(f"{table}."):
            self.searchField = f"{table}.{self.searchField}"
            
        if not self.sortName.startswith(f"{table}."):
            self.sortName = f"{table}.{self.sortName}"
