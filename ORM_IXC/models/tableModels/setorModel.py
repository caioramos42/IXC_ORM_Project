from __future__ import annotations
from typing import Optional
from ORM_IXC.interfaces import IModelWithId
from ORM_IXC.enums.setor import *
from ORM_IXC.statemants.maps.mapper import Mapped, field as mapped_field
from ORM_IXC.statemants.maps.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel


@MetaModels
class SetorModel(IModelWithId, BaseModel):
    ativo :Mapped[AtivoEnum]
    setor :Mapped[str]
    id :Mapped[Optional[int]]
    cor :Mapped[Optional[str]] = mapped_field('')
    id_depto :Mapped[Optional[int]] = mapped_field(None)
    recebe_telegram_setor :Mapped[Optional[str]] = mapped_field('')
    token_bot_telegram_setor :Mapped[Optional[str]] = mapped_field('')
    empresa_setor_chatid_telegram :Mapped[Optional[str]] = mapped_field('')

    @property
    def table(self) -> str:
        return "empresa_setor"

    def _serialize_enum_and_str(self, value) -> str:
        """Serializa um valor de enum ou retorna string vazia se None"""
        if value is None:
            return ''
        if hasattr(value, 'value'):
            return str(value.value)
        return str(value)

    def to_dict(self) -> dict:
        def serialize(value) -> str:
            if value is None:
                return ''
            raw = getattr(value, 'value', value)
            return '' if raw is None else str(raw)

        data = {
            'ativo': self._serialize_enum_and_str(self.ativo) if self.ativo is not None else '',
            'setor': self._serialize_enum_and_str(self.setor) if self.setor is not None else '',
            'id': str(self.id) if self.id is not None else '',
            'cor': self._serialize_enum_and_str(self.cor) if self.cor is not None else '',
            'id_depto': str(self.id_depto) if self.id_depto is not None else '',
            'recebe_telegram_setor': self._serialize_enum_and_str(self.recebe_telegram_setor) if self.recebe_telegram_setor is not None else '',
            'token_bot_telegram_setor': self._serialize_enum_and_str(self.token_bot_telegram_setor) if self.token_bot_telegram_setor is not None else '',
            'empresa_setor_chatid_telegram': self._serialize_enum_and_str(self.empresa_setor_chatid_telegram) if self.empresa_setor_chatid_telegram is not None else '',
        }
        return {key: serialize(value) for key, value in data.items()}

    def is_valid(self) -> bool:
        return self.ativo is not None and self.setor is not None
