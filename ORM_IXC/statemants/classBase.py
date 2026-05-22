# from ctypes import Union
# from enum import Enum
# import types
# from typing import Any, Protocol, get_args
# from typing_extensions import get_origin
# from ORM_IXC.models.searchUtils.searchModel import SearchModule
# from ORM_IXC.enums.operators import Operators
# from typing import TypeAlias

# AceptTypes: TypeAlias = int | str | Enum | None

# class Field():
#     def __init__(self, name: str = "", fieldType: type = object, value: AceptTypes = None) -> None:
#         self.name = name
#         self.python_type = fieldType
#         self._val = value
#         self.model = None

#     def setup(self, fieldType: type, name: str, value: AceptTypes) -> None:
#         self.name = name
#         self.python_type = fieldType
#         self._val = value
        
#          # chamado automaticamente pela classe
#     def __set_name__(self, owner, name):
#         self.name = name

#     def __get__(self, obj, objtype=None):
#         if obj is None:
#             return self
#         return obj.__dict__.get(self.name)

#     def __set__(self, obj, value):
#         if value is not None and not self._tipo_valido(value, self.python_type):
#             raise TypeError(
#                 f"Campo '{self.name}' esperava {self.python_type}, recebeu {type(value)}"
#             )
#         obj.__dict__[self.name] = value

#     def _tipo_valido(self, value, tp) -> bool:
#         origin = get_origin(tp)

#         # Optional[T] ou Union[T, None]
#         if origin is Union or origin is types.UnionType:
#             return any(
#                 self._tipo_valido(value, arg)
#                 for arg in get_args(tp)
#                 if arg is not type(None)
#             )

#         # Tipo simples (int, str, subclasse de Enum, etc.)
#         if isinstance(tp, type):
#             return isinstance(value, tp)

#         # Fallback: pula validação para genéricos complexos
#         return True

#     def __repr__(self) -> str: # type: ignore
#         return f"<Field {self.name}>"
   
#     def __getattr__(self, name: str) -> Any:
#         if name == 'value':
#             if isinstance(self._val, Enum):
#                 return self._val.value
#             return self._val

#         raise AttributeError(
#             f"'{self.__class__.__name__}' não possui '{name}'"
#         )

#     # =========================
#     # CONVERSÕES NATIVAS
#     # =========================
#     def __str__(self) -> str:
#         return str(self._val) if self._val is not None else self.key

#     def __repr__(self) -> str:
#         return self.__str__()

#     def __int__(self) -> int:
#         if self.python_type == float or self.python_type == int:
#             return int(self._val)
#         elif self.python_type == str:
#             if not str(self._val).lstrip('-').isdigit():
#                 raise ValueError("Este valor não pode ser convertido em int")
#             return int(self._val)
#         raise ValueError("Esse valor não pode ser convertido em int")

#     def __float__(self) -> float:
#         return float(self._val)

#     def __bool__(self) -> bool:
#         return bool(self._val)

#     # =========================
#     # OPERAÇÕES MATEMÁTICAS
#     # =========================

#     # +
#     def __add__(self, other):
#         return self._val + self._extract(other)

#     def __radd__(self, other):
#         return self._extract(other) + self._val

#     # -
#     def __sub__(self, other):
#         return self._val - self._extract(other)

#     def __rsub__(self, other):
#         return self._extract(other) - self._val

#     # *
#     def __mul__(self, other):
#         return self._val * self._extract(other)

#     def __rmul__(self, other):
#         return self._extract(other) * self._val

#     # /
#     def __truediv__(self, other):
#         return self._val / self._extract(other)

#     def __rtruediv__(self, other):
#         return self._extract(other) / self._val

#     # //
#     def __floordiv__(self, other):
#         return self._val // self._extract(other)

#     # %
#     def __mod__(self, other):
#         return self._val % self._extract(other)

#     # **
#     def __pow__(self, other):
#         return self._val ** self._extract(other)

#     # =========================
#     # OPERAÇÕES DE STRING
#     # =========================

#     def upper(self):
#         return str(self._val).upper()

#     def lower(self):
#         return str(self._val).lower()

#     def replace(self, old, new):
#         return str(self._val).replace(old, new)

#     def split(self, sep=None):
#         return str(self._val).split(sep)

#     def strip(self):
#         return str(self._val).strip()

#     def startswith(self, value):
#         return str(self._val).startswith(value)

#     def endswith(self, value):
#         return str(self._val).endswith(value)

#     # =========================
#     # COMPARAÇÕES SQL-LIKE
#     # =========================

#     def __eq__(self, value: Any) -> SearchModule: # type: ignore
#         return SearchModule(self.name, value, Operators.EQUALS)

#     def __lt__(self, value: Any) -> SearchModule:
#         return SearchModule(self.name, value, Operators.LASTTHAN)

#     def __gt__(self, value: Any) -> SearchModule:
#         return SearchModule(self.name, value, Operators.MORETHAN)

#     def __ne__(self, value: Any) -> SearchModule: # type: ignore
#         return SearchModule(self.name, value, Operators.DIFFERENT)

#     # =========================
#     # AUXILIAR
#     # =========================

#     def _extract(self, value):
#         if isinstance(value, Field):
#             return value._val
#         return value

#     # =========================
#     # Sequence obrigatório
#     # =========================

#     def __getitem__(self, index):
#         return str(self._val)[index]

#     def __len__(self):
#         return len(str(self._val))


from enum import Enum
import types
from typing import Any, Generic, TypeAlias, TypeVar, get_args, overload, Union
from typing_extensions import get_origin
from ORM_IXC.models.searchUtils.searchModel import SearchModule
from ORM_IXC.enums.operators import Operators
AceptTypes: TypeAlias = int | str | Enum | None
T = TypeVar("T", bound=AceptTypes)

class Field(Generic[T]):
    def __init__(self, name: str = "", fieldType: Any = object, value: T | None = None) -> None:
        self.name = name
        self.python_type = fieldType
        self._val = value
        self.model = None

    def setup(self, fieldType: Any, name: str, value: T | None) -> None:
        self.name = name
        self.python_type = fieldType
        self._val = value

    def __set_name__(self, owner: type[Any], name: str) -> None:
        self.name = name

    @overload
    def __get__(self, obj: None, objtype: type[Any] | None = None) -> "Field[T]": ...

    @overload
    def __get__(self, obj: Any, objtype: type[Any] | None = None) -> "Field[T] | None": ...

    def __get__(self, obj: Any | None, objtype: type[Any] | None = None) -> "Field[T] | None":
        if obj is None:
            return self
        # Retorna o Field armazenado na instância, não o valor cru
        stored = obj.__dict__.get(self.name)
        return stored

    def __set__(self, obj: Any, value: T | "Field[T]" | None) -> None:
        if isinstance(value, Field):
            # Já é um Field — armazena diretamente
            obj.__dict__[self.name] = value
            return

        # Valor cru — cria um Field encapsulando o valor
        if value is not None and not self._tipo_valido(value, self.python_type):
            raise TypeError(
                f"Campo '{self.name}' esperava {self.python_type}, recebeu {type(value)}"
            )
        field_instance = Field(self.name, self.python_type, value)
        obj.__dict__[self.name] = field_instance

    def _tipo_valido(self, value, tp) -> bool:
        origin = get_origin(tp)

        if origin is Union or origin is types.UnionType:
            return any(
                self._tipo_valido(value, arg)
                for arg in get_args(tp)
                if arg is not type(None)
            )

        if isinstance(tp, type):
            return isinstance(value, tp)

        return True

    def __getattr__(self, name: str) -> Any:
        if name == 'value':
            if isinstance(self._val, Enum):
                return self._val.value
            return self._val

        raise AttributeError(
            f"'{self.__class__.__name__}' não possui '{name}'"
        )

    # =========================
    # CONVERSÕES NATIVAS
    # =========================
    def __str__(self) -> str:
        if isinstance(self._val, Enum):
            return str(self._val.value)
        return str(self._val) if self._val is not None else ""

    def __repr__(self) -> str:
        return f"<Field {self.name}={self._val!r}>"

    def __int__(self) -> int:
        if isinstance(self._val, Enum):
            return int(self._val.value)
        if self.python_type in (float, int):
            return int(self._val)
        if self.python_type == str:
            if not str(self._val).lstrip('-').isdigit():
                raise ValueError("Este valor não pode ser convertido em int")
            return int(self._val)
        raise ValueError("Esse valor não pode ser convertido em int")

    def __float__(self) -> float:
        if isinstance(self._val, Enum):
            return float(self._val.value)
        return float(self._val)

    def __bool__(self) -> bool:
        if isinstance(self._val, Enum):
            return bool(self._val.value)
        return bool(self._val)

    # =========================
    # OPERAÇÕES MATEMÁTICAS
    # =========================
    def __add__(self, other):
        return self._val + self._extract(other)

    def __radd__(self, other):
        return self._extract(other) + self._val

    def __sub__(self, other):
        return self._val - self._extract(other)

    def __rsub__(self, other):
        return self._extract(other) - self._val

    def __mul__(self, other):
        return self._val * self._extract(other)

    def __rmul__(self, other):
        return self._extract(other) * self._val

    def __truediv__(self, other):
        return self._val / self._extract(other)

    def __rtruediv__(self, other):
        return self._extract(other) / self._val

    def __floordiv__(self, other):
        return self._val // self._extract(other)

    def __mod__(self, other):
        return self._val % self._extract(other)

    def __pow__(self, other):
        return self._val ** self._extract(other)

    # =========================
    # OPERAÇÕES DE STRING
    # =========================
    def upper(self):
        return str(self._val).upper()

    def lower(self):
        return str(self._val).lower()

    def replace(self, old, new):
        return str(self._val).replace(old, new)

    def split(self, sep=None):
        return str(self._val).split(sep)

    def strip(self):
        return str(self._val).strip()

    def startswith(self, value):
        return str(self._val).startswith(value)

    def endswith(self, value):
        return str(self._val).endswith(value)

    # =========================
    # COMPARAÇÕES SQL-LIKE
    # =========================
    def __eq__(self, value: Any) -> SearchModule:  # type: ignore
        return SearchModule(self.name, value, Operators.EQUALS)

    def __lt__(self, value: Any) -> SearchModule:
        return SearchModule(self.name, value, Operators.LASTTHAN)

    def __gt__(self, value: Any) -> SearchModule:
        return SearchModule(self.name, value, Operators.MORETHAN)

    def __ne__(self, value: Any) -> SearchModule:  # type: ignore
        return SearchModule(self.name, value, Operators.DIFFERENT)

    # =========================
    # AUXILIAR
    # =========================
    def _extract(self, value):
        if isinstance(value, Field):
            return value._val
        return value

    # =========================
    # Sequence obrigatório
    # =========================
    def __getitem__(self, index):
        if isinstance(self._val, Enum):
            return str(self._val.value)[index]
        return str(self._val)[index]

    def __len__(self):
        if isinstance(self._val, Enum):
            return len(str(self._val.value))
        return len(str(self._val))
