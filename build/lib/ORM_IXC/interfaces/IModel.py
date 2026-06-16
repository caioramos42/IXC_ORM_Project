from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Protocol, runtime_checkable

if TYPE_CHECKING:
    from ORM_IXC.statemants.maps.mapper import Mapped

@runtime_checkable
class IModel(Protocol):
    @property
    def table(self) -> str: ...
    def to_dict(self) -> dict[str, str]: ...
    @classmethod
    def dto_convert(cls, data: dict[str, str]) -> "IModel": ...


@runtime_checkable
class IModelWithId(IModel, Protocol):
    id: Mapped[Optional[int]]# | int | None
    #def changed_fields(self) -> set[str]: ...
    #def changed_values(self) -> dict[str, object]: ...
