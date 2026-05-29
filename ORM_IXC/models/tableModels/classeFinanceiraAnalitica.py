from __future__ import annotations
from typing import Optional

from ORM_IXC.interfaces import IModelWithId
from ORM_IXC.models.tableModels.defaultModel import BaseModel
from ORM_IXC.statemants.mapper import Mapped, field as mapped_field
from ORM_IXC.statemants.metaManager import MetaModels

@MetaModels
class ClasseFinanceiraAnaliticaModel(IModelWithId, BaseModel):
    id: Mapped[Optional[int]]
    id_planejamento_finan: Mapped[int]
    planejamento_analitico: Mapped[str]
    classificacao: Mapped[Optional[str]] = mapped_field('')
    conta: Mapped[Optional[str]] = mapped_field('')
    tipo: Mapped[Optional[str]] = mapped_field('')
    auxiliar: Mapped[Optional[str]] = mapped_field('')
    contador: Mapped[Optional[str]] = mapped_field('')
    tipo_aux: Mapped[Optional[str]] = mapped_field('')
    plan_aux: Mapped[Optional[str]] = mapped_field('')

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
