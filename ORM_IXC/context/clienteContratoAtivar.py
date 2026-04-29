from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.enums.methods import Actions

class ClienteContratoAtivar(IContext, DefaultActions):
    def __init__(self, manager:Manager):
        self.table = "cliente_contrato_ativar_cliente"
        self.manager = manager
    def Add(self, obj):
        pass
    def Update(obj):
        pass
    def DeleteById(id:int):
        pass
    def AtivarContrato(self, contrato_id:int):
        query = ClienteContratoAtivarResponse(payload = {
            'qtype': 'cliente_contrato_ativar_cliente.id',
            'id_contrato': str(contrato_id)
        })
        return self.manager.make_request(query, Actions.LIST)
        
        
class ClienteContratoAtivarResponse:
    def __init__(self, response: dict):
        self.response = response
    def to_dict(self):
        return self.response