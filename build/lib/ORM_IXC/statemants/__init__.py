__all__ = [
    "delete",
    "insert",
    "select",
    "update",
    "Mapped",
]


def __getattr__(name):
    if name == "delete":
        from .CRUD.delete import delete
        return delete
    if name == "insert":
        from .CRUD.insert import insert
        return insert
    if name == "select":
        from .CRUD.select import select
        return select
    if name == "update":
        from .CRUD.update import update
        return update
    if name == "Mapped":
        from .maps.mapper import Mapped
        return Mapped
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")