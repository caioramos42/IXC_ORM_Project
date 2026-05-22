import json

class DefaultPayload:
    def __init__(self, payload: dict, table: str):
        if 'id' in payload:
            self.id = payload['id']
            payload.pop('id')
        self.payload = payload
        self.table = table
    def to_dict(self):
        return self.payload
    def dto_convert(self):
        """Funcao para converter o payload em um DTO específico, dependendo do contexto."""