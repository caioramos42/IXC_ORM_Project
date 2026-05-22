"""Interfaces do ORM IXC."""

from .IContext import IContext
from .IModel import IModel, IModelWithId

__all__ = ["IContext", "IModel", "IModelWithId"]
