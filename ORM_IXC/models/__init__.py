"""Modelos de dados para ORM IXC."""

from .clienteModel import Client
from .defaultModel import DefaultPayload
from .loginModel import *

__all__ = ["Client", "DefaultPayload"]
