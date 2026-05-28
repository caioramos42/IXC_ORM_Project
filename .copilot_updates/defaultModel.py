import json
from typing import Any
from ORM_IXC.interfaces.IModel import IModel


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
    @classmethod
    def dto_convert(cls_, data: dict[str, str]) -> Any:  # pragma: no cover - stub for typing
        raise NotImplementedError()
    # common auto-increment id placeholder used by IXC models
    id_autoincrement: Mapped[int | None] = Field("id_autoincrement", int | None, None)
