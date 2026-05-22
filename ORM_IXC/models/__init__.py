"""Modelos de dados para ORM IXC."""

from .clienteModel import ClientModel
from .defaultModel import DefaultPayload
from .loginModel import LoginModel
from .serviceOrderModel import ServiceOrderModel

Client = ClientModel
Login = LoginModel
OrdemDeServico = ServiceOrderModel

__all__ = [
    "ClientModel",
    "DefaultPayload",
    "LoginModel",
    "ServiceOrderModel",
    "Client",
    "Login",
    "OrdemDeServico",
]
