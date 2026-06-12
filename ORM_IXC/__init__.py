"""ORM_IXC package entry point.

Este pacote é publicado como `ORM_IXC`, mas os módulos internos usam
importações absolutas baseadas em `IXC_ORM_Project.*`.
"""

import sys

# Compatibilidade com imports absolutos
sys.modules.setdefault("IXC_ORM_Project", sys.modules[__name__])

from dotenv import load_dotenv

from .context.contextModels.areceber import AReceber
from .context.contextModels.atendimento import Atendimento
from .context.contextModels.caixaDeAtendimento import CaixaDeAtendimento
from .context.contextModels.cliente import Cliente
from .context.contextModels.contratoDoCliente import ContratoDoCliente
from .context.contextModels.fiberClient import ClienteFibra
from .context.contextModels.login import Login
from .context.contextModels.serviceOrder import ServiceOrder

from .context.request import Manager
from .context.request.manager import Manager as ManagerClass

from .enums.methods import Actions
from .enums.operators import Operators
from .enums.sortOrder import SortOrder

from .models.tableModels.defaultModel import DefaultPayload
from .models.tableModels.contratoDoClienteModel import ContratoDoClienteModel
from .models.tableModels.clienteModel import ClientModel
from .models.tableModels.contasAReceber import ContasAReceberModel
from .models.tableModels.vendedorModel import VendedorModel

from .models.searchUtils.gridParamModel import GridParam
from .models.searchUtils.searchModel import SearchModule

from .statemants.CRUD.select import select
from .utils.makejson import makeJson

from datetime import datetime, timedelta
import os

from .statemants.maps.mapper import Mapped

from .statemants import *
Contrato = ContratoDoCliente

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
    "select",
    "Mapped"
]