import annotationlib
from typing import Any, dataclass_transform, get_origin, get_args, get_type_hints, Union
from enum import Enum
import types
import sys

from ORM_IXC.statemants.maps.classBase import Field as FieldType
from ORM_IXC.models.tableModels.defaultModel import BaseModel

def is_mapped(annotation) -> bool:
    origin = get_origin(annotation)

    # Field[T] (our Mapped alias) should be treated as mapped
    return origin is FieldType

def unwrap_mapped(annotation):
    origin = get_origin(annotation)
    if origin is FieldType:
        args = get_args(annotation)
        return args[0] if args else Any
    return annotation

def convert_value(field_type, value):
    if value is None or value == "":
        return None

    origin = get_origin(field_type)

    # Optional[T] / Union[T, None]
    if origin is Union or origin is types.UnionType:
        args = [arg for arg in get_args(field_type) if arg is not type(None)]
        if len(args) == 1:
            return convert_value(args[0], value)

    # Enum
    if isinstance(field_type, type) and issubclass(field_type, Enum):
        return field_type(value)

    if field_type == int:
        return int(value)

    if field_type == float:
        return float(value)

    if field_type == bool:
        return bool(value)

    if field_type == str:
        return str(value)

    return value

@dataclass_transform()
def MetaModels(cls):
    from ORM_IXC.statemants.maps.classBase import Field
    module_globals = vars(sys.modules[cls.__module__])

    # Pega TODAS as anotações resolvidas (incluindo herdadas)
    all_hints = get_type_hints(
        cls,
        globalns=module_globals,
        localns=module_globals,
    )

    # Filtra apenas as anotações definidas DIRETAMENTE na classe
    own_annotations = cls.__dict__.get("__annotations__", {})

    # Resolve os tipos das anotações próprias usando os hints já resolvidos
    cls_annotations = {k: all_hints[k] for k in own_annotations if k in all_hints}

    # Campos reservados que nunca devem virar Field
    RESERVED = {"_field_names", "alias", "columns", "_changed_fields", "_inners", "table"}

    for k, v in cls_annotations.items():
        if k in RESERVED:
            continue

        real_type = v
        if is_mapped(v):
            real_type = unwrap_mapped(v)

        default = getattr(cls, k, None)
        field = Field(k, real_type, default)
        field.model = cls
        setattr(cls, k, field)

    cls._field_names = set(k for k in cls_annotations if k not in RESERVED)

    # __init__ também filtra os reservados
    fields_for_init = [k for k in cls_annotations if k not in RESERVED]

    exec_globals = {**globals(), "Field": Field, "UNSET": object()}

    init: str = (
        "def __init__(self, "
        + ", ".join([f"{k}=UNSET" for k in fields_for_init])
        + "):\n"
    )

    init += "\tself.__dict__['_changed_fields'] = set()\n"
    init += "\tself.__dict__['_inners'] = []\n"
    for k in fields_for_init:
        init += f"\tif {k} is not UNSET:\n"
        init += f"\t\tself.{k} = {k}\n"
        init += f"\t\tself._changed_fields.add(\"{k}\")\n"
    init += "\tself.alias = \"\"\n"
    init += "\tself.columns = []\n"

    namespace: dict = {}
    exec(init, exec_globals, namespace)
    cls.__init__ = namespace["__init__"]

    cls.changed_fields = BaseModel.changed_fields
    cls.changed_values = BaseModel.changed_values

    annotations = cls_annotations

    @classmethod
    def dto_convert(cls_, data: dict[str, str], columns=None):
        values = {}

        for name, tp in annotations.items():
            raw = data.get(name)
            values[name] = convert_value(tp, raw) if raw is not None else None

        obj = cls_(**values)

        if columns:
            obj.columns = columns

        return obj
    
    #@classmethod
    def output_dict(self) -> dict:
        def serialize(value):
            if value is None:
                return ""

            # Caso seja um Field
            if hasattr(value, "_val"):
                raw = value._val
            else:
                raw = value

            if raw is None:
                return ""

            if isinstance(raw, Enum):
                return raw.name

            return str(raw)
        alias = getattr(self, "alias", "")
        table = getattr(self, "table", "")
        prefix_name = alias if alias is not None else table
        prefix = f"{prefix_name}." if prefix_name else ""

        field_names = self.__class__._field_names or set()

        # Normaliza self.columns para nomes string
        if self.columns:
            allowed = set()
            for col in self.columns:
                # Se for um Field descriptor, pega o nome
                name = getattr(col, "name", None) or getattr(col, "key", None) or str(col)
                allowed.add(name)
        else:
            allowed = None

        data = {
            f"{prefix}{field_name}": serialize(getattr(self, field_name, None))
            for field_name in field_names
            if allowed is None or field_name in allowed
        }

        for inner_model in getattr(self, "_inners", []):
            if hasattr(inner_model, "output_dict"):
                data.update(inner_model.output_dict())

        return data

    def set_alias(self, alias: str):
        self.alias = alias

    def set_columns(self, columns):
        self.columns = columns

    def inner(self, *models):
        for model in models:
            if isinstance(model, (list, tuple, set)):
                self._inners.extend(model)
            else:
                self._inners.append(model)
        return self
    
    cls.set_alias = set_alias
    cls.dto_convert = dto_convert
    cls.output_dict = output_dict
    cls.set_columns = set_columns
    cls.inner = inner
    return cls
