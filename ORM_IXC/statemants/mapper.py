from enum import Enum
from typing import Any, TypeAlias, TypeVar

from ORM_IXC.statemants.classBase import Field

AceptTypes: TypeAlias = int | float | bool | str | Enum | None

T = TypeVar("T", bound=AceptTypes)

# Public typing alias to be used in model annotations: `id: Mapped[int]`.
# This makes class attribute access type as Field[T], so operator overloads
# like `ClientModel.id > 0` are understood as returning SearchModule.
# It also allows enum-backed fields to accept strings and convert them at runtime.
Mapped: TypeAlias = Field[T | str]

def field(default=None):
    return Mapped(value=default)