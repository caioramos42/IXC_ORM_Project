from typing import Any, TypeVar, Generic, Iterator
from abc import ABC, abstractmethod

from ORM_IXC.interfaces.IModel import IModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule

TAddModel = TypeVar("TAddModel", bound=IModel, contravariant=True)
TUpdateModel = TypeVar("TUpdateModel", bound=IModel, contravariant=True)


class IContext(ABC, Generic[TAddModel, TUpdateModel]):
    @abstractmethod
    def Add(self, obj: TAddModel) -> Any:
        """add obj in ixc server"""

    @abstractmethod
    def Update(self, obj: TUpdateModel) -> Any:
        """Update obj in ixc server"""

    @abstractmethod
    def DeleteById(self, id: int) -> Any:
        """delete obj in ixc server by ID"""

    @abstractmethod
    def SelectAll(self) -> list[TAddModel]:
        """select all objs in ixc server"""
    
    @abstractmethod
    def SelectAllAssync(self) -> Iterator[TAddModel]:
        """select all objs in ixc server"""
        
    @abstractmethod
    def SelectByFilter(self, search: SearchModule) -> list[TAddModel]:
        """search obj in ixc server by filter"""
        
    @abstractmethod
    def SelectByFilterAssync(self, search: SearchModule, page_size: int) -> Iterator[TAddModel]:
        """select obj in ixc server by filter assync"""
