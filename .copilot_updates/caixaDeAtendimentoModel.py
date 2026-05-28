from __future__ import annotations
from typing import Optional
from ORM_IXC.enums.caixaDeAtendimento import *
from ORM_IXC.interfaces import IModel, IModelWithId
from ORM_IXC.statemants.classBase import Field
from ORM_IXC.statemants.mapper import Mapped
from ORM_IXC.statemants.metaManager import MetaModels
from ORM_IXC.models.defaultModel import BaseModel

@MetaModels
class CaixaDeAtendimentoModel(IModelWithId, BaseModel):
    id: int
    descricao: str
    id_projeto: int
    tipo: Mapped[Optional[TipoEnum]] = Field("tipo", TipoEnum, TipoEnum.PROPRIA)
    id_transmissor: Mapped[Optional[int]] = Field("id_transmissor", int, None)
    id_interface: Mapped[Optional[int]] = Field("id_interface", int, None)
    id_tecnologia: Mapped[Optional[int]] = Field("id_tecnologia", int, None)
    capacidade: Mapped[Optional[str]] = Field("capacidade", str, '')
    codigo_estilo_caixa: Mapped[Codigo_estilo_caixaEnum] = Field("codigo_estilo_caixa", Codigo_estilo_caixaEnum, Codigo_estilo_caixaEnum.CAIXA_PRETA_)
    obs_caixa_ftth: Mapped[Optional[str]] = Field("obs_caixa_ftth", str, '')
    status: Mapped[Optional[StatusEnum]] = Field("status", StatusEnum, StatusEnum.ATIVO)
    idx: Mapped[Optional[str]] = Field("idx", str, '')
    ultima_atualizacao: Mapped[Optional[str]] = Field("ultima_atualizacao", str, '')
    cep: Mapped[Optional[str]] = Field("cep", str, '')
    endereco: Mapped[Optional[str]] = Field("endereco", str, '')
    numero: Mapped[Optional[str]] = Field("numero", str, '')
    bairro: Mapped[Optional[str]] = Field("bairro", str, '')
    id_cidade: Mapped[Optional[int]] = Field("id_cidade", int, None)
    latitude: Mapped[Optional[str]] = Field("latitude", str, '')
    longitude: Mapped[Optional[str]] = Field("longitude", str, '')

    @property
    def table(self) -> str:
        return "rad_caixa_ftth"
    
    def to_dict(self) -> dict:
        def serialize(value) -> str:
            if value is None:
                return ''
            raw = getattr(value, 'value', value)
            return '' if raw is None else str(raw)

        data = {
            'id': str(self.id),
            'descricao': self.descricao if self.descricao is not None else '',
            'id_projeto': str(self.id_projeto) if self.id_projeto is not None else '',
            'tipo': self.tipo.value if self.tipo is not None else '',
            'id_transmissor': str(self.id_transmissor) if self.id_transmissor is not None else '',
            'id_interface': str(self.id_interface) if self.id_interface is not None else '',
            'id_tecnologia': str(self.id_tecnologia) if self.id_tecnologia is not None else '',
            'capacidade': self.capacidade if self.capacidade is not None else '',
            'codigo_estilo_caixa': self.codigo_estilo_caixa.value if self.codigo_estilo_caixa is not None else '',
            'obs_caixa_ftth': self.obs_caixa_ftth if self.obs_caixa_ftth is not None else '',
            'status': self.status.value if self.status is not None else '',
            'idx': self.idx if self.idx is not None else '',
            'ultima_atualizacao': self.ultima_atualizacao if self.ultima_atualizacao is not None else '',
            'cep': self.cep if self.cep is not None else '',
            'endereco': self.endereco if self.endereco is not None else '',
            'numero': self.numero if self.numero is not None else '',
            'bairro': self.bairro if self.bairro is not None else '',
            'id_cidade': str(self.id_cidade) if self.id_cidade is not None else '',
            'latitude': self.latitude if self.latitude is not None else '',
            'longitude': self.longitude if self.longitude is not None else '',
        }
        return {key: serialize(value) for key, value in data.items()}


    def is_valid(self) -> bool:
        return self.id is not None and self.descricao is not None and self.id_projeto is not None

    def __repr__(self) -> str:
        return f"CaixaDeAtendimento(id={self.id!r}, descricao={self.descricao!r}, id_projeto={self.id_projeto!r})"
