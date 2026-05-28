from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from ORM_IXC.interfaces import IModel, IModelWithId
from ORM_IXC.enums.contaContabilSintetica import *
from ORM_IXC.statemants.classBase import Field
from ORM_IXC.statemants.mapper import Mapped, field as mapped_field
from ORM_IXC.statemants.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel

@MetaModels
class ContaContabilSinteticaModel(IModelWithId, BaseModel):
    id :Mapped[Optional[int]]
    tipo :Mapped[TipoEnum]
    planejamento :Mapped[str]
    nivel_superior :Mapped[Optional[int]] = mapped_field(None)
    subtipo :Mapped[Optional[SubtipoEnum]] = mapped_field(None)
    cod_planejamento :Mapped[Optional[str]] = mapped_field('')
    conta_dominio :Mapped[Optional[str]] = mapped_field('')
    contador :Mapped[Optional[str]] = mapped_field('')
    plan_aux :Mapped[Optional[str]] = mapped_field('')
    tipo_aux :Mapped[Optional[str]] = mapped_field('')

    @property
    def table(self) -> str:
        return "planejamento_analitico"
    
    def to_dict(self) -> dict:
        def serialize(value) -> str:
            if value is None:
                return ''
            raw = getattr(value, 'value', value)
            return '' if raw is None else str(raw)

        data = {
            'id': str(self.id),
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
        return {key: serialize(value) for key, value in data.items()}
    def is_valid(self) -> bool:
        return self.id is not None and self.tipo is not None and self.planejamento is not None

