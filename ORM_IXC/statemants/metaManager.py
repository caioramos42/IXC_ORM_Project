# import annotationlib
# from typing import Any

# from ORM_IXC.interfaces.IModel import IModelWithId

# from typing import get_origin, get_args, Union
# from enum import Enum
# import types

# def convert_value(field_type, value):

#     if value is None:
#         return None

#     origin = get_origin(field_type)

#     # Optional[T]
#     if origin is Union or origin is types.UnionType:

#         args = [
#             arg for arg in get_args(field_type)
#             if arg is not type(None)
#         ]

#         if len(args) == 1:
#             return convert_value(args[0], value)

#     # Enum
#     if isinstance(field_type, type) and issubclass(field_type, Enum):
#         return field_type(value)

#     # int
#     if field_type == int:
#         return int(value)

#     # float
#     if field_type == float:
#         return float(value)

#     # bool
#     if field_type == bool:
#         return bool(value)

#     # str
#     if field_type == str:
#         return str(value)

#     return value

# # def MetaModels(cls): 
    
# #     from ORM_IXC.statemants.classBase import Field

    
# #     #cls.__bases__ += (IModelWithId,)
# #     cls_annotations: dict[str, Any | annotationlib.ForwardRef] = annotationlib.get_annotations(
# #         cls, format = annotationlib.Format.FORWARDREF)
# #     for k, v in cls_annotations.items():
# #         setattr(cls, k, Field(k, v))
    
# #     init: str = "def __init__(self, " + ", ".join([f"{k}: Field[{str(v).replace('<class \'', '').replace('\'>','')}]" for k, v in cls_annotations.items()]) + "):\n"
# #     init += "\n".join([f"\tself.{k} = Field(\"{k}\", {str(v).replace('<class \'', '').replace('\'>','')}, {k})" for k, v in cls_annotations.items()])
# #     namespace: dict = {}
# #     exec(init, globals(), namespace)
# #     generated_init = namespace['__init__']
# #     cls.__init__ = generated_init
    
# #     # dto_convert
# #     annotations = cls.__annotations__
# #     @classmethod
# #     def dto_convert(cls_, data: dict[str, str]):

# #         values = {}

# #         for name, tp in annotations.items():

# #             raw = data.get(name)

# #             values[name] = convert_value(tp, raw)

# #         return cls_(**values)

# #     cls.dto_convert = dto_convert
    
# #     return cls



# def MetaModels(cls):
#     from ORM_IXC.statemants.classBase import Field

#     cls_annotations: dict[str, Any] = annotationlib.get_annotations(
#         cls, format=annotationlib.Format.FORWARDREF
#     )

#     for k, v in cls_annotations.items():
#         setattr(cls, k, Field(k, v))

#     # Injeta Field explicitamente no namespace do exec
#     exec_globals = {**globals(), "Field": Field}

#     init: str = (
#         "def __init__(self, "
#         + ", ".join([f"{k}=None" for k in cls_annotations])
#         + "):\n"
#     )
#     init += "\n".join(
#         [f"\tself.{k} = {k}" for k in cls_annotations]
#     )

#     namespace: dict = {}
#     exec(init, exec_globals, namespace)
#     cls.__init__ = namespace["__init__"]

#     annotations = cls.__annotations__

#     @classmethod
#     def dto_convert(cls_, data: dict[str, str]):
#         values = {}
#         for name, tp in annotations.items():
#             raw = data.get(name)
#             # string vazia vira None (padrão do seu to_dict)
#             values[name] = convert_value(tp, raw) if raw else None
#         return cls_(**values)
    

#     cls.dto_convert = dto_convert
#     return cls


import annotationlib
from typing import Any, get_origin, get_args, get_type_hints, Union
from enum import Enum
import types


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


def MetaModels(cls):
    from ORM_IXC.statemants.classBase import Field

    cls_annotations: dict[str, Any] = get_type_hints(cls)

    for k, v in cls_annotations.items():
        setattr(cls, k, Field(k, v))

    exec_globals = {**globals(), "Field": Field}

    init: str = (
        "def __init__(self, "
        + ", ".join([f"{k}=None" for k in cls_annotations])
        + "):\n"
    )
    init += "\n".join([f"\tself.{k} = {k}" for k in cls_annotations])

    namespace: dict = {}
    exec(init, exec_globals, namespace)
    cls.__init__ = namespace["__init__"]

    annotations = cls_annotations

    @classmethod
    def dto_convert(cls_, data: dict[str, str]):
        values = {}
        for name, tp in annotations.items():
            raw = data.get(name)
            # Converte o valor cru para o tipo correto; __set__ do Field
            # vai encapsulá-lo automaticamente em um Field
            values[name] = convert_value(tp, raw) if raw is not None else None
        return cls_(**values)

    cls.dto_convert = dto_convert
    return cls
