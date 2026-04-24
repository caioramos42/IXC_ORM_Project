from typing import Protocol

class IContext(Protocol):
    def Add(self, obj):
        """add obj in ixc server"""
    def Update(self, obj):
       """Update obj in ixc server""" 
    def DeleteById(self, id:int):
        """delete obj in ixc server by ID"""
    def SelectAll():
        """delete obj in ixc server by ID"""