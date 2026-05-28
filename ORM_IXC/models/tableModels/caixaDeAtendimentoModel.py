from __future__ import annotations
from typing import Optional
from ORM_IXC.enums.caixaDeAtendimento import *
from ORM_IXC.interfaces import IModel, IModelWithId
from ORM_IXC.statemants.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel
from ORM_IXC.statemants.mapper import Mapped, field as mapped_field

@MetaModels
class CaixaDeAtendimentoModel(IModelWithId, BaseModel):
    id: Mapped[Optional[int]]
    descricao: Mapped[str]
    id_projeto: Mapped[int]
    tipo: Mapped[Optional[TipoEnum]] = mapped_field(TipoEnum.PROPRIA)
    id_transmissor: Mapped[Optional[int]] = mapped_field(None)
    id_interface: Mapped[Optional[int]] = mapped_field(None)
    id_tecnologia: Mapped[Optional[int]] = mapped_field(None)
    capacidade: Mapped[Optional[str]] = mapped_field('')
    codigo_estilo_caixa: Mapped[Codigo_estilo_caixaEnum] = mapped_field(Codigo_estilo_caixaEnum.CAIXA_PRETA_)
    obs_caixa_ftth: Mapped[Optional[str]] = mapped_field('')
    status: Mapped[Optional[StatusEnum]] = mapped_field(StatusEnum.ATIVO)
    idx: Mapped[Optional[str]] = mapped_field('')
    ultima_atualizacao: Mapped[Optional[str]] = mapped_field('')
    cep: Mapped[Optional[str]] = mapped_field('')
    endereco: Mapped[Optional[str]] = mapped_field('')
    numero: Mapped[Optional[str]] = mapped_field('')
    bairro: Mapped[Optional[str]] = mapped_field('')
    id_cidade: Mapped[Optional[int]] = mapped_field(None)
    latitude: Mapped[Optional[str]] = mapped_field('')
    longitude: Mapped[Optional[str]] = mapped_field('')

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
