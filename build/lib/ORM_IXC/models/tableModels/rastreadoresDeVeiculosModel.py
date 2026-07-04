from __future__ import annotations
from typing import Optional
from ORM_IXC.interfaces import IModelWithId
from ORM_IXC.statemants.maps.mapper import Mapped, field as mapped_field
from ORM_IXC.statemants.maps.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel


@MetaModels
class RastreadoresDeVeIculosModel(IModelWithId, BaseModel):
    rastreador :Mapped[str]
    lastupdate :Mapped[str]
    id :Mapped[Optional[int]]
    speed :Mapped[Optional[str]] = mapped_field('')
    latitude :Mapped[Optional[str]] = mapped_field('')
    longitude :Mapped[Optional[str]] = mapped_field('')
    gps_time :Mapped[Optional[str]] = mapped_field('')

    @property
    def table(self) -> str:
        return "veiculos_tracker"

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
            'rastreador': self._serialize_enum_and_str(self.rastreador) if self.rastreador is not None else '',
            'lastupdate': self._serialize_enum_and_str(self.lastupdate) if self.lastupdate is not None else '',
            'id': str(self.id) if self.id is not None else '',
            'speed': self._serialize_enum_and_str(self.speed) if self.speed is not None else '',
            'latitude': self._serialize_enum_and_str(self.latitude) if self.latitude is not None else '',
            'longitude': self._serialize_enum_and_str(self.longitude) if self.longitude is not None else '',
            'gps_time': self._serialize_enum_and_str(self.gps_time) if self.gps_time is not None else '',
        }
        return {key: serialize(value) for key, value in data.items()}

    def is_valid(self) -> bool:
        return self.rastreador is not None and self.lastupdate is not None
