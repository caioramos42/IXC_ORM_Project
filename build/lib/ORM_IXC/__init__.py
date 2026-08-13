"""ORM_IXC package entry point.

Este pacote é publicado como `ORM_IXC`, mas os módulos internos usam
importações absolutas baseadas em `IXC_ORM_Project.*`.
"""

import sys
from importlib import import_module

# Compatibilidade com imports absolutos
sys.modules.setdefault("IXC_ORM_Project", sys.modules[__name__])

__all__ = [
    "Manager",
    "ManagerClass",
    "Cliente",
    "Login",
    "Contrato",
    "ContratoDoCliente",
    "ContratoDoClienteModel",
    "ClientModel",
    "ContasAReceberModel",
    "Atendimento",
    "CaixaDeAtendimento",
    "AReceber",
    "ClienteFibra",
    "ServiceOrder",
    "DefaultPayload",
    "SearchModule",
    "GridParam",
    "Actions",
    "Operators",
    "SortOrder",
    "select",
    "makeJson",
    "load_dotenv",
    "datetime",
    "timedelta",
    "os",
    "delete",
    "insert",
    "update",
    "Mapped",
    "VendedorModel",
    "IModel",
]


def __getattr__(name):
    if name == "load_dotenv":
        from dotenv import load_dotenv
        return load_dotenv
    if name in {"Manager", "ManagerClass"}:
        module = import_module(".context.request", __name__)
        return getattr(module, name)
    if name in {"AReceber", "Atendimento", "CaixaDeAtendimento", "Cliente", "ContratoDoCliente", "ClienteFibra", "Login", "ServiceOrder"}:
        module = import_module(".context.contextModels", __name__)
        return getattr(module, name)
    if name == "Actions":
        return getattr(import_module(".enums.methods", __name__), name)
    if name == "Operators":
        return getattr(import_module(".enums.operators", __name__), name)
    if name == "SortOrder":
        return getattr(import_module(".enums.sortOrder", __name__), name)
    if name in {"DefaultPayload", "ContratoDoClienteModel", "ClientModel", "ContasAReceberModel", "VendedorModel"}:
        module = import_module(".models", __name__)
        return getattr(module, name)
    if name in {"GridParam", "SearchModule"}:
        module = import_module(".models.searchUtils", __name__)
        return getattr(module, name)
    if name in {"select", "delete", "insert", "update"}:
        module = import_module(".statemants", __name__)
        return getattr(module, name)
    if name == "makeJson":
        from .utils.makejson import makeJson
        return makeJson
    if name == "datetime":
        import datetime as _dt
        return _dt.datetime
    if name == "timedelta":
        import datetime as _dt
        return _dt.timedelta
    if name == "os":
        import os as _os
        return _os
    if name == "Mapped":
        from .statemants.maps.mapper import Mapped
        return Mapped
    if name == "IModel":
        from .interfaces.IModel import IModel
        return IModel
    if name == "Contrato":
        return __getattr__("ContratoDoCliente")
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")