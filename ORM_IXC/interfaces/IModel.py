from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class IModel(Protocol):
    @property
    def table(self) -> str: ...
    def to_dict(self) -> dict[str, str]: ...
    def dto_convert(self, data:dict[str, str]) -> IModel: ...


@runtime_checkable
class IModelWithId(IModel, Protocol):
    id_autoincrement: int
