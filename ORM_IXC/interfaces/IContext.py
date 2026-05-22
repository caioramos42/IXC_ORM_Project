from typing import Any, Protocol, TypeVar

from ORM_IXC.interfaces.IModel import IModel

TAddModel = TypeVar("TAddModel", bound=IModel, contravariant=True)
TUpdateModel = TypeVar("TUpdateModel", bound=IModel, contravariant=True)


class IContext(Protocol[TAddModel, TUpdateModel]):
    def Add(self, obj: TAddModel) -> Any:
        """add obj in ixc server"""
        ...

    def Update(self, obj: TUpdateModel) -> Any:
        """Update obj in ixc server"""
        ...

    def DeleteById(self, id: int) -> Any:
        """delete obj in ixc server by ID"""
        ...

    def SelectAll(self) -> Any:
        """select all objs in ixc server"""
        ...
