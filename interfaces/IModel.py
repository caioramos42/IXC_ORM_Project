from typing import Protocol
from abc import ABC, abstractmethod

class IModel(Protocol):
    @abstractmethod
    def to_dict(self):
        pass