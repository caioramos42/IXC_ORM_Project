from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from ORM_IXC.interfaces import IModel, IModelWithId
from ORM_IXC.enums.contaContabilSintetica import *

@dataclass(kw_only=True)
class ContaContabilSinteticaModel(IModelWithId):
    id_autoincrement: int
    tipo: TipoEnum
    planejamento: str
    nivel_superior: Optional[int] = None
    subtipo: Optional[SubtipoEnum] = None
    cod_planejamento: Optional[str] = ''
    conta_dominio: Optional[str] = ''
    contador: Optional[str] = ''
    plan_aux: Optional[str] = ''
    tipo_aux: Optional[str] = ''

    @property
    def id(self) -> str:
        return str(self.id_autoincrement)

    @property
    def table(self) -> str:
        return "planejamento_analitico"
    
    def to_dict(self) -> dict:
        return {
            'id_autoincrement': str(self.id_autoincrement),
            'tipo': self.tipo.value if self.tipo is not None else '',
            'planejamento': self.planejamento if self.planejamento is not None else '',
            'nivel_superior': str(self.nivel_superior) if self.nivel_superior is not None else '',
            'subtipo': self.subtipo.value if self.subtipo is not None else '',
            'cod_planejamento': self.cod_planejamento if self.cod_planejamento is not None else '',
            'conta_dominio': self.conta_dominio if self.conta_dominio is not None else '',
            'contador': self.contador if self.contador is not None else '',
            'plan_aux': self.plan_aux if self.plan_aux is not None else '',
            'tipo_aux': self.tipo_aux if self.tipo_aux is not None else '',
        }

    def is_valid(self) -> bool:
        return self.id_autoincrement is not None and self.tipo is not None and self.planejamento is not None

    def __repr__(self) -> str:
        return f"ContaContábilSintética(id_autoincrement={self.id_autoincrement!r}, tipo={self.tipo!r}, planejamento={self.planejamento!r})"

    #------------------------------ CONVERSOR DTO ------------------------------#
    def dto_convert(self, data: dict[str, str]) -> IModel:
        return ContaContabilSinteticaModel(
            id_autoincrement=int(data.get('id_autoincrement', 0)),
            tipo=TipoEnum(data['tipo']),
            planejamento=data.get('planejamento', ''),
            nivel_superior=int(data['nivel_superior']) if data.get('nivel_superior') else None,
            subtipo=SubtipoEnum(data['subtipo']) if data.get('subtipo') else None,
            cod_planejamento=data.get('cod_planejamento', ''),
            conta_dominio=data.get('conta_dominio', ''),
            contador=data.get('contador', ''),
            plan_aux=data.get('plan_aux', ''),
            tipo_aux=data.get('tipo_aux', ''),
        )
