from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

from ORM_IXC.interfaces import IModel, IModelWithId

@dataclass(kw_only=True)
class ClasseFinanceiraAnaliticaModel(IModelWithId):
    id_autoincrement: int
    id_planejamento_finan: int
    planejamento_analitico: str
    classificacao: Optional[str] = ''
    conta: Optional[str] = ''
    tipo: Optional[str] = ''
    auxiliar: Optional[str] = ''
    contador: Optional[str] = ''
    tipo_aux: Optional[str] = ''
    plan_aux: Optional[str] = ''

    @property
    def id(self) -> str:
        return str(self.id_autoincrement)

    @property
    def table(self) -> str:
        return "planejamento_analitico_finan"

    def to_dict(self) -> dict:
        return {
            'id_autoincrement': str(self.id_autoincrement),
            'id_planejamento_finan': str(self.id_planejamento_finan) if self.id_planejamento_finan is not None else '',
            'planejamento_analitico': self.planejamento_analitico if self.planejamento_analitico is not None else '',
            'classificacao': self.classificacao if self.classificacao is not None else '',
            'conta': self.conta if self.conta is not None else '',
            'tipo': self.tipo if self.tipo is not None else '',
            'auxiliar': self.auxiliar if self.auxiliar is not None else '',
            'contador': self.contador if self.contador is not None else '',
            'tipo_aux': self.tipo_aux if self.tipo_aux is not None else '',
            'plan_aux': self.plan_aux if self.plan_aux is not None else '',
        }

    def is_valid(self) -> bool:
        return self.id_autoincrement is not None and self.id_planejamento_finan is not None and self.planejamento_analitico is not None

    def __repr__(self) -> str:
        return f"ClasseFinanceiraAnalítica(id_autoincrement={self.id_autoincrement!r}, id_planejamento_finan={self.id_planejamento_finan!r}, planejamento_analitico={self.planejamento_analitico!r})"

#------------------------------ CONVERSOR DTO ------------------------------#
    def dto_convert(self, data: dict[str, str]) -> IModel:
        return ClasseFinanceiraAnaliticaModel(
            id_autoincrement=int(data.get('id_autoincrement', 0)),
            id_planejamento_finan=int(data['id_planejamento_finan']),
            planejamento_analitico=data.get('planejamento_analitico', ''),
            classificacao=data.get('classificacao', ''),
            conta=data.get('conta', ''),
            tipo=data.get('tipo', ''),
            auxiliar=data.get('auxiliar', ''),
            contador=data.get('contador', ''),
            tipo_aux=data.get('tipo_aux', ''),
            plan_aux=data.get('plan_aux', ''),
        )
