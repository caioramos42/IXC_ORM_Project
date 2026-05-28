from typing import Any

from ORM_IXC.interfaces import IModel


class Insert:
    def __init__(self, context):
        self.context = context
        self.payloads: list[IModel] = []

    def values(self, *payloads: IModel) -> "Insert":
        for payload in payloads:
            if not isinstance(payload, IModel):
                raise TypeError(f"Expected an IModel instance, got {type(payload).__name__}")
            self.payloads.append(payload)
        return self

    def to_dict(self) -> list[dict[str, Any]]:
        return [payload.to_dict() for payload in self.payloads]

    def execute(self):
        if not self.payloads:
            raise ValueError("Nenhum payload informado para insert. Use .values(...) antes de .execute().")
        
        results = []
        for payload in self.payloads:
            results.append(self.context.Add(payload))
        return results


def insert(context) -> Insert:
    return Insert(context)