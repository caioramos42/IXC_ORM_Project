from IXC_ORM_Project.models.searchUtils.searchModel import SearchModule
from IXC_ORM_Project.enums.operators import Operators
from IXC_ORM_Project.enums.methods import Actions
from IXC_ORM_Project.interfaces.IModel import IModel

class DefaultActions:
    def SearchById(self, id: int):
        search = SearchModule(searchField="id", query=str(id), oper=Operators.EQUALS, sortName="id", table=self.table)
        return self.manager.make_request(search, Actions.LIST)
    
    def SearchAll(self):
        search = SearchModule(searchField="id", query="0", oper=Operators.MORETHAN, sortName="id", table=self.table)
        return self.manager.make_request(search, Actions.LIST)
    
    def getByFilter(self, search: SearchModule):
        search.set_table(self.table)
        if len(search.grid_param) != 0:
            for param in search.grid_param:
                if not param.searchField.startswith(f"{self.table}."):
                    param.searchField = f"{self.table}.{param.searchField}"
        return self.manager.make_request(search, Actions.LIST)
    
    def _MakePost(self, modelForSend):
        modelForSend.table = self.table
        return self.manager.make_request(modelForSend, Actions.INSERT)
    
    def _MakePut(self, modelForSend: IModel):
        if modelForSend.id == '':
            raise ValueError("Para editar, o ID deve ser preenchido")
        return self.manager.make_request(modelForSend, Actions.EDIT)
        
    
    
