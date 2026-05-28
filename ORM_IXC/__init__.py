"""ORM_IXC package entry point.

Este pacote é publicado como `ORM_IXC`, mas os módulos internos usam
importações absolutas baseadas em `IXC_ORM_Project.*`.
"""

import sys

from ORM_IXC.context.areceber import AReceber
from ORM_IXC.context.atendimento import Atendimento
from ORM_IXC.context.caixaDeAtendimento import CaixaDeAtendimento
from ORM_IXC.context.cliente import Cliente
from ORM_IXC.context.contrato import Contrato
from ORM_IXC.context.fiberClient import ClienteFibra
from ORM_IXC.context.login import Login
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.context.serviceOrder import ServiceOrder

from ORM_IXC.enums.methods import Actions
from ORM_IXC.enums.operators import Operators
from ORM_IXC.enums.sortOrder import SortOrder

from ORM_IXC.models.defaultModel import DefaultPayload
from ORM_IXC.models.searchUtils.gridParamModel import GridParam
from ORM_IXC.models.searchUtils.searchModel import SearchModule

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
