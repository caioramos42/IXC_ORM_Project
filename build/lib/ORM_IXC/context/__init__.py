"""Pacote de contextos da ORM IXC."""

from .contextModels.areceber import AReceber
from .contextModels.atendimento import Atendimento
from .contextModels.caixaDeAtendimento import CaixaDeAtendimento
from .contextModels.carteiraCobranca import CarteiraDeConbranca
from .contextModels.cliente import Cliente
from .contextModels.contratoDoCliente import ContratoDoCliente
from .contextModels.fiberClient import ClienteFibra
from .contextModels.login import Login
from .contextModels.serviceOrder import ServiceOrder

__all__ = [
    "AReceber",
    "Atendimento",
    "CaixaDeAtendimento",
    "CarteiraCobranca",
    "Cliente",
    "Contrato",
    "ClienteFibra",
    "Login",
    "ServiceOrder",
]

CarteiraCobranca = CarteiraDeConbranca
Contrato = ContratoDoCliente
