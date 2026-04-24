import json

class DefaultPayload:
    def __init__(self, payload: dict):
        if 'id' in payload:
            self.id = payload['id']
            payload.pop('id')
        self.payload = payload
    def to_dict(self):
        return self.payload