import json
from typing import Any
from ORM_IXC.interfaces.IModel import IModel
from ORM_IXC.statemants.classBase import Field


class DefaultPayload:
    def __init__(self, payload: dict, table: str):
        if 'id' in payload:
            self.id = payload['id']
            payload.pop('id')
        self.payload = payload
        self.table = table

    def to_dict(self):
        return self.payload

    def dto_convert(self):
        """Funcao para converter o payload em um DTO específico, dependendo do contexto."""


class BaseModel(IModel):
    _field_names: set[str] = set()

    def __setattr__(self, name: str, value: Any) -> None:
        field_names = getattr(type(self), '_field_names', None)
        if field_names is None:
            field_names = set()
        if name in field_names:
            changed = self.__dict__.get('_changed_fields')
            if changed is None:
                object.__setattr__(self, '_changed_fields', set())
                changed = self.__dict__['_changed_fields']
            changed.add(name)
        super().__setattr__(name, value)

    def changed_fields(self) -> set[str]:
        changed = getattr(self, '_changed_fields', None)
        return set(changed or set())

    def _raw_value(self, name: str) -> Any:
        value = getattr(self, name)
        if isinstance(value, Field):
            return value._val
        return value

    def changed_values(self) -> dict[str, Any]:
        return {
            name: self._raw_value(name)
            for name in self.changed_fields()
            if name not in ('id', 'id_autoincrement')
        }

    @classmethod
    def dto_convert(cls_, data: dict[str, str]) -> Any:  # pragma: no cover - stub for typing
        raise NotImplementedError()
    # common auto-increment id placeholder used by IXC models
    id_autoincrement: int | None = None