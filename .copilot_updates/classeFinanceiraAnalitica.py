from __future__ import annotations
from typing import Optional

from ORM_IXC.interfaces import IModel, IModelWithId
from ORM_IXC.models.defaultModel import BaseModel
from ORM_IXC.statemants.mapper import Mapped
from ORM_IXC.statemants.classBase import Field
from ORM_IXC.statemants.mapper import Mapped
from ORM_IXC.statemants.metaManager import MetaModels

@MetaModels
class ClasseFinanceiraAnaliticaModel(IModelWithId, BaseModel):
    id: Mapped[int]
    id_planejamento_finan: int
    planejamento_analitico: str
    classificacao: Mapped[Optional[str]] = Field("classificacao", str, '')
    conta: Mapped[Optional[str]] = Field("conta", str, '')
    tipo: Mapped[Optional[str]] = Field("tipo", str, '')
    auxiliar: Mapped[Optional[str]] = Field("auxiliar", str, '')
    contador: Mapped[Optional[str]] = Field("contador", str, '')
    tipo_aux: Mapped[Optional[str]] = Field("tipo_aux", str, '')
    plan_aux: Mapped[Optional[str]] = Field("plan_aux", str, '')

    @property
    def table(self) -> str:
        return "planejamento_analitico_finan"

    def to_dict(self) -> dict:
        def serialize(value) -> str:
            if value is None:
                return ''
            raw = getattr(value, 'value', value)
            return '' if raw is None else str(raw)

        data = {
            'id': str(self.id),
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
        return {key: serialize(value) for key, value in data.items()}
    
    def is_valid(self) -> bool:
        return self.id is not None and self.id_planejamento_finan is not None and self.planejamento_analitico is not None
