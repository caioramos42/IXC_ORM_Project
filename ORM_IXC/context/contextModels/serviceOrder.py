from typing import Any, List, Iterator, cast
from ORM_IXC.interfaces.IContext import IContext
from ORM_IXC.context.defaultActions.defaultActions import DefaultActions
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.searchUtils.searchModel import SearchModule
from ORM_IXC.models.tableModels.serviceOrderModel import ServiceOrderModel
from datetime import datetime
import requests


class ServiceOrder(IContext[ServiceOrderModel, ServiceOrderModel], DefaultActions):
    def __init__(self, manager: Manager):
        DefaultActions.__init__(self, ServiceOrderModel, manager)
    def closeServiceOrder(self, modelForSend: ServiceOrderModel) -> list[requests.Response]:
        data_inicio = self.SearchById(modelForSend.id.value)[0].data_inicio # type: ignore
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        redefinedModel = {
            'id_chamado': modelForSend.id,
            'data_inicio': data_inicio,
            'data_final': now,
            'mensagem': modelForSend.mensagem,
            'gera_comissao': modelForSend.gera_comissao,
            'finaliza_processo': 'S',
            'status': 'F',
            'id_tecnico': modelForSend.id_tecnico
        }
        return super()._MakePost(redefinedModel) # type: ignore
    
    def Add(self, obj: ServiceOrderModel) -> Any:
        return self._MakePost(obj)
    
    def Update(self, obj: ServiceOrderModel, search: SearchModule) -> list[requests.Response]:
        if SearchModule.searchField == "status" and SearchModule.query == "F": # type: ignore
            return self.closeServiceOrder(obj)
        return self._MakeUpdate(obj, search)
    
    def Delete(self, search: SearchModule) -> List[requests.Response]:
        return super()._MakeDelete(search)
    
    def DeleteById(self, id: int) -> Any:
        raise NotImplementedError("DeleteById não implementado para ServiceOrder")
    
    def SelectAll(self) -> List[ServiceOrderModel]:
        return cast(List[ServiceOrderModel], self._SearchAll())
    
    def SelectByFilter(self, search: SearchModule) -> List[ServiceOrderModel]:
        return cast(List[ServiceOrderModel], super().getByFilter(search))
    
    def SelectByFilterAssync(self, search: SearchModule, page_size: int = 172) -> Iterator[ServiceOrderModel]:
        return cast(Iterator[ServiceOrderModel], super().cursorByFilter(search, page_size))
    
    def SelectAllAssync(self) -> Iterator[ServiceOrderModel]:
        return cast(Iterator[ServiceOrderModel], super()._SelectAllAssync())
        
