"""Interfaces do ORM IXC."""

from importlib import import_module

__all__ = ["IContext", "IModel", "IModelWithId"]


def __getattr__(name):
    if name == "IContext":
        return import_module(".IContext", __name__).IContext
    if name in {"IModel", "IModelWithId"}:
        return getattr(import_module(".IModel", __name__), name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
