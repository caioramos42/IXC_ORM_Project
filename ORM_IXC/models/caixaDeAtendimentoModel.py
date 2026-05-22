from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from ORM_IXC.enums.caixaDeAtendimento import *
from ORM_IXC.interfaces import IModel, IModelWithId

@dataclass(kw_only=True)
class CaixaDeAtendimentoModel(IModelWithId):
    id_autoincrement: int
    descricao: str
    id_projeto: int
    tipo: Optional[TipoEnum] = TipoEnum.PROPRIA
    id_transmissor: Optional[int] = None
    id_interface: Optional[int] = None
    id_tecnologia: Optional[int] = None
    capacidade: Optional[str] = ''
    codigo_estilo_caixa: Codigo_estilo_caixaEnum = Codigo_estilo_caixaEnum.CAIXA_PRETA_
    obs_caixa_ftth: Optional[str] = ''
    status: Optional[StatusEnum] = StatusEnum.ATIVO
    idx: Optional[str] = ''
    ultima_atualizacao: Optional[str] = ''
    cep: Optional[str] = ''
    endereco: Optional[str] = ''
    numero: Optional[str] = ''
    bairro: Optional[str] = ''
    id_cidade: Optional[int] = None
    latitude: Optional[str] = ''
    longitude: Optional[str] = ''

    @property
    def id(self) -> str:
        return str(self.id_autoincrement)

    @property
    def table(self) -> str:
        return "rad_caixa_ftth"

    def to_dict(self) -> dict:
        return {
            'id_autoincrement': str(self.id_autoincrement),
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

    def is_valid(self) -> bool:
        return self.id_autoincrement is not None and self.descricao is not None and self.id_projeto is not None

    def __repr__(self) -> str:
        return f"CaixaDeAtendimento(id_autoincrement={self.id_autoincrement!r}, descricao={self.descricao!r}, id_projeto={self.id_projeto!r})"

#------------------------------ CONVERSOR DTO ------------------------------#
    def dto_convert(self, data: dict[str, str]) -> IModel:
        return CaixaDeAtendimentoModel(
            id_autoincrement=int(data.get('id_autoincrement', 0)),
            descricao=data.get('descricao', ''),
            id_projeto=int(data['id_projeto']),
            tipo=TipoEnum(data['tipo']) if data.get('tipo') else None,
            id_transmissor=int(data['id_transmissor']) if data.get('id_transmissor') else None,
            id_interface=int(data['id_interface']) if data.get('id_interface') else None,
            id_tecnologia=int(data['id_tecnologia']) if data.get('id_tecnologia') else None,
            capacidade=data.get('capacidade', ''),
            codigo_estilo_caixa=Codigo_estilo_caixaEnum(data['codigo_estilo_caixa']),
            obs_caixa_ftth=data.get('obs_caixa_ftth', ''),
            status=StatusEnum(data['status']) if data.get('status') else None,
            idx=data.get('idx', ''),
            ultima_atualizacao=data.get('ultima_atualizacao', ''),
            cep=data.get('cep', ''),
            endereco=data.get('endereco', ''),
            numero=data.get('numero', ''),
            bairro=data.get('bairro', ''),
            id_cidade=int(data['id_cidade']) if data.get('id_cidade') else None,
            latitude=data.get('latitude', ''),
            longitude=data.get('longitude', ''),
        )
