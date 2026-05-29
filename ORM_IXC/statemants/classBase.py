from enum import Enum
import types
from typing import TYPE_CHECKING, Any, Generic, TypeAlias, TypeVar, get_args, overload, Union
from typing_extensions import get_origin
from ORM_IXC.enums.operators import Operators

AceptTypes: TypeAlias = int | str | Enum | None | float
MathTypes: TypeAlias = int | float
if TYPE_CHECKING:
    from ORM_IXC.models.searchUtils.searchModel import SearchModule
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
    def __get__(self, obj: Any, objtype: type[Any] | None = None) -> T | None: ...

    def __get__(self, obj: Any | None, objtype: type[Any] | None = None) -> "Field[T] | T | None":
        if obj is None:
            return self
        # Retorna o Field armazenado na instância, não o valor cru
        stored = obj.__dict__.get(self.name)
        return stored
    
    def changed_fields(self):
        return self.__dict__.get("_changed_fields", set())
    
    def __set__(self, obj: Any, value: AceptTypes | "Field[T]" | None) -> None:
        if isinstance(value, Field):
            # Já é um Field — armazena diretamente
            obj.__dict__[self.name] = value
            return
    
        if value is not None and isinstance(value, str):
            converted = self._convert_string(value, self.python_type)
            if converted is not None:
                value = converted

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

    def _convert_string(self, value: str, tp):
        origin = get_origin(tp)

        if origin is Union or origin is types.UnionType:
            for arg in get_args(tp):
                if arg is type(None):
                    continue
                converted = self._convert_string(value, arg)
                if converted is not None:
                    return converted
            return None

        if tp == int:
            if value.lstrip('-').isdigit():
                return int(value)
            return None

        if tp == float:
            try:
                return float(value)
            except ValueError:
                return None

        if tp == bool:
            lowered = value.strip().lower()
            if lowered in {"1", "true", "yes", "sim", "s", "on"}:
                return True
            if lowered in {"0", "false", "no", "n", "off"}:
                return False
            return None

        if isinstance(tp, type) and issubclass(tp, Enum):
            try:
                return tp(value)
            except Exception:
                return None

        if tp == str:
            return value

        return None

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
        if self._val is None:
            raise ValueError("Esse valor não pode ser convertido em int")
        if isinstance(self._val, Enum):
            return int(self._val.value)
        if self.python_type in (float, int):
            return int(self._val)
        if self.python_type == str:
            if not str(self._val).lstrip('-').isdigit():
                raise ValueError("Este valor nÃ£o pode ser convertido em int")
            return int(self._val)
        raise ValueError("Esse valor nÃ£o pode ser convertido em int")

    def __float__(self) -> float:
        if self._val is None:
            raise ValueError("Esse valor não pode ser convertido em float")
        if isinstance(self._val, Enum):
            return float(self._val.value)
        return float(self._val)

    def __bool__(self) -> bool:
        if isinstance(self._val, Enum):
            return bool(self._val.value)
        return bool(self._val)

    # =========================
    # Operadores Matemátios
    # =========================
    def __add__(self, other: Field) -> MathTypes | str:
        if not isinstance(other, Field):
            raise TypeError("Operação só suportada entre Fields")
        otherValue = self._extract(other)
        if isinstance(otherValue, MathTypes) and isinstance(self._val, MathTypes):
            return self._val + otherValue
        if isinstance(otherValue, str) and isinstance(self._val, str):
            return self._val + otherValue
        raise TypeError("Operação só suportada para tipos numéricos ou strings")

    def __radd__(self, other):
        if not isinstance(other, Field):
            raise TypeError("Operação só suportada entre Fields")
        otherValue = self._extract(other)
        if isinstance(otherValue, MathTypes) and isinstance(self._val, MathTypes):
            return otherValue + self._val
        if isinstance(otherValue, str) and isinstance(self._val, str):
            return otherValue + self._val
        raise TypeError("Operação só suportada para tipos numéricos ou strings")

    def __sub__(self, other):
        if not isinstance(other, Field):
            raise TypeError("Operação só suportada entre Fields")
        otherValue = self._extract(other)
        if isinstance(otherValue, MathTypes) and isinstance(self._val, MathTypes):
            return self._val - otherValue
        raise TypeError("Operação só suportada para tipos numéricos")

    def __rsub__(self, other):
        if not isinstance(other, Field):
            raise TypeError("Operação só suportada entre Fields")
        otherValue = self._extract(other)
        if isinstance(otherValue, MathTypes) and isinstance(self._val, MathTypes):
            return otherValue - self._val
        raise TypeError("Operação só suportada para tipos numéricos")

    def __mul__(self, other):
        if not isinstance(other, Field):
            raise TypeError("Operação só suportada entre Fields")
        otherValue = self._extract(other)
        if isinstance(otherValue, MathTypes) and isinstance(self._val, MathTypes):
            return self._val * otherValue
        if isinstance(otherValue, str) and isinstance(self._val, int):
            return self._val * otherValue
        raise TypeError("Operação só suportada para tipos numéricos ou strings")

    def __rmul__(self, other):
        if not isinstance(other, Field):
            raise TypeError("Operação só suportada entre Fields")
        otherValue = self._extract(other)
        if isinstance(otherValue, MathTypes) and isinstance(self._val, MathTypes):
            return otherValue * self._val
        if isinstance(otherValue, int) and isinstance(self._val, str):
            return otherValue * self._val
        raise TypeError("Operação só suportada para tipos numéricos ou strings")

    def __truediv__(self, other):
        if not isinstance(other, Field):
            raise TypeError("Operação só suportada entre Fields")
        otherValue = self._extract(other)
        if isinstance(otherValue, MathTypes) and isinstance(self._val, MathTypes):
            return self._val / otherValue
        raise TypeError("Operação só suportada para tipos numéricos")

    def __rtruediv__(self, other):
        if not isinstance(other, Field):
            raise TypeError("Operação só suportada entre Fields")
        otherValue = self._extract(other)
        if isinstance(otherValue, MathTypes) and isinstance(self._val, MathTypes):
            return otherValue / self._val
        raise TypeError("Operação só suportada para tipos numéricos")

    def __floordiv__(self, other):
        if not isinstance(other, Field):
            raise TypeError("Operação só suportada entre Fields")
        otherValue = self._extract(other)
        if isinstance(otherValue, MathTypes) and isinstance(self._val, MathTypes):
            return self._val // otherValue
        raise TypeError("Operação só suportada para tipos numéricos")

    def __mod__(self, other):
        if not isinstance(other, Field):
            raise TypeError("Operação só suportada entre Fields")
        otherValue = self._extract(other)
        if isinstance(otherValue, MathTypes) and isinstance(self._val, MathTypes):
            return self._val % otherValue
        raise TypeError("Operação só suportada para tipos numéricos")

    def __pow__(self, other):
        if not isinstance(other, Field):
            raise TypeError("Operação só suportada entre Fields")
        otherValue = self._extract(other)
        if isinstance(otherValue, MathTypes) and isinstance(self._val, MathTypes):
            return self._val ** otherValue
        raise TypeError("Operação só suportada para tipos numéricos")

    # =========================
    # Operadores String
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
    # Comparadores
    # =========================
    def __eq__(self, value: AceptTypes) -> "SearchModule":  # type: ignore[misc]
        from ORM_IXC.models.searchUtils.searchModel import SearchModule
        return SearchModule(self.name, str(value), Operators.EQUALS)

    def __lt__(self, value: AceptTypes) -> "SearchModule":
        from ORM_IXC.models.searchUtils.searchModel import SearchModule
        return SearchModule(self.name, str(value), Operators.LASTTHAN)

    def __gt__(self, value: AceptTypes) -> "SearchModule":
        from ORM_IXC.models.searchUtils.searchModel import SearchModule
        return SearchModule(self.name, str(value), Operators.MORETHAN)
    
    def __le__(self, value: AceptTypes) -> "SearchModule":
        from ORM_IXC.models.searchUtils.searchModel import SearchModule
        return SearchModule(self.name, str(value), Operators.LASTTHANEQUALS)
    
    def __ge__(self, value: AceptTypes) -> "SearchModule":
        from ORM_IXC.models.searchUtils.searchModel import SearchModule
        return SearchModule(self.name, str(value), Operators.MORETHANEQUALS)
    
    def __ne__(self, value: AceptTypes) -> "SearchModule":  # type: ignore[misc]
        from ORM_IXC.models.searchUtils.searchModel import SearchModule
        return SearchModule(self.name, str(value), Operators.DIFFERENT)

    # =========================
    # AUXILIAR
    # =========================
    def _extract(self, value) -> AceptTypes:
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

    def like(self, value: TypeAlias) -> "SearchModule":
        if isinstance(self._val, MathTypes):
            raise TypeError("Operação 'like' não suportada para tipos numéricos")    
        return SearchModule(self.name, str(value), Operators.LIKE)