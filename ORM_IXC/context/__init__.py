"""Pacote de contextos da ORM IXC."""

from .areceber import AReceber
from .atendimento import Atendimento
from .caixaDeAtendimento import CaixaDeAtendimento
from .carteiraCobranca import CarteiraDeConbranca
from .cliente import Cliente
from .contratoDoCliente import ContratoDoCliente
from .fiberClient import ClienteFibra
from .login import Login
from .serviceOrder import ServiceOrder

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
