"""ORM_IXC package entry point.

Este pacote é publicado como `ORM_IXC`, mas os módulos internos usam
importações absolutas baseadas em `IXC_ORM_Project.*`.
"""

import sys

from .context.contextModels.areceber import AReceber
from .context.contextModels.atendimento import Atendimento
from .context.contextModels.caixaDeAtendimento import CaixaDeAtendimento
from .context.contextModels.cliente import Cliente
from .context.contextModels.contratoDoCliente import ContratoDoCliente
from .context.contextModels.fiberClient import ClienteFibra
from .context.contextModels.login import Login
from .context.request.manager import Manager
from .context.contextModels.serviceOrder import ServiceOrder

from .enums.methods import Actions
from .enums.operators import Operators
from .enums.sortOrder import SortOrder

from .models.tableModels.defaultModel import DefaultPayload
from .models.searchUtils.gridParamModel import GridParam
from .models.searchUtils.searchModel import SearchModule

Contrato = ContratoDoCliente

__all__ = [
    "Manager",
    "Cliente",
    "Login",
    "Contrato",
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
]

# Compatibilidade com os imports absolutos usados dentro do código do pacote.
sys.modules.setdefault("IXC_ORM_Project", sys.modules[__name__])