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
        
        class CloseServiceOrder():
            def __init__(self,
                            id_chamado: int,
                            data_inicio: str,
                            data_final: str,
                            mensagem: str,
                            gera_comissao: str,
                            finaliza_processo: str,
                            status: str,
                            id_tecnico: str
                            ):
                self.id_chamado: int = id_chamado
                self.data_inicio: str = data_inicio
                self.data_final: str = data_final
                self.mensagem: str = mensagem
                self.gera_comissao: str = gera_comissao
                self.finaliza_processo: str = finaliza_processo
                self.status: str = status
                self.id_tecnico: str = id_tecnico
                
            def to_dict(self) -> dict:
                def serialize(value) -> str:
                    if value is None:
                        return ''
                    raw = getattr(value, 'value', value)
                    return '' if raw is None else str(raw)

                data = {
                    'id_chamado': str(self.id_chamado),
                    'data_inicio': self.data_inicio,
                    'data_final': self.data_final,
                    'mensagem': self.mensagem,
                    'gera_comissao': self.gera_comissao,
                    'finaliza_processo': self.finaliza_processo,
                    'status': self.status,
                    'id_tecnico': self.id_tecnico
                }
                return {key: serialize(value) for key, value in data.items()}
            
        
        data_inicio = self.SearchById(modelForSend.id.value)[0].data_inicio # type: ignore
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        redefinedModel = CloseServiceOrder(
            modelForSend.id,
            data_inicio,
            now,
            str(modelForSend.mensagem),
            modelForSend.gera_comissao,
            'S',
            'F',
            modelForSend.id_tecnico
        )
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
        
