import annotationlib
from typing import Any, dataclass_transform, get_origin, get_args, get_type_hints, Union
from enum import Enum
import types

from ORM_IXC.statemants.classBase import Field
from ORM_IXC.statemants.classBase import Field as FieldType
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
    from ORM_IXC.statemants.classBase import Field

    cls_annotations: dict[str, Any] = get_type_hints(cls)

    for k, v in cls_annotations.items():

        real_type = v

        if is_mapped(v):
            real_type = unwrap_mapped(v)

        default = getattr(cls, k, None)

        setattr(
            cls,
            k,
            Field(
                k,
                real_type,
                default
            )
        )

    cls._field_names = set(cls_annotations)

    exec_globals = {**globals(), "Field": Field, "UNSET": object()}

    init: str = (
        "def __init__(self, "
        + ", ".join([f"{k}=UNSET" for k in cls_annotations])
        + "):\n"
    )
    init += "\tself.__dict__['_changed_fields'] = set()\n"
    for k in cls_annotations:
        init += f"\tif {k} is not UNSET:\n"
        init += f"\t\tself.{k} = {k}\n"
        init += f"\t\tself._changed_fields.add(\"{k}\")\n"
    namespace: dict = {}
    exec(init, exec_globals, namespace)
    cls.__init__ = namespace["__init__"]

    cls.changed_fields = BaseModel.changed_fields
    cls.changed_values = BaseModel.changed_values

    annotations = cls_annotations

    @classmethod
    def dto_convert(cls_, data: dict[str, str]):
        values = {}
        for name, tp in annotations.items():
            raw = data.get(name)
            # Converte o valor cru para o tipo correto; __set__ do Field
            # vai encapsulÃ¡-lo automaticamente em um Field
            values[name] = convert_value(tp, raw) if raw is not None else None
        return cls_(**values)

    cls.dto_convert = dto_convert
    return cls