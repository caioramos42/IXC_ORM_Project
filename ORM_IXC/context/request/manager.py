import requests
import base64
from ORM_IXC.enums.methods import Actions
import urllib3
from ORM_IXC.interfaces.IModel import IModel

class Manager:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    def __init__(self, host: str, token: str):
        self.host = "https://{}/webservice/v1/".format(host)
        self.token = token
        self.header = {
            'Authorization': 'Basic {}'.format(base64.b64encode(token.encode('utf-8')).decode('utf-8')),
            'Content-Type': 'application/json'
        }
    def insertTable(self, method: Actions, table):
        self.header['ixcsoft'] = method.value.data
        self.host += "{}".format(table)
        
    def make_request(self, request:IModel, method:Actions):
        hostBefore = self.host
        self.insertTable(method, request.table)
        try:
            match method:
                case Actions.DELETE:
                    return requests.post(
                        "{}/{}".format(self.host,request.id),
                        headers=self.header,
                        verify=False
                    )
                case Actions.EDIT:
                    return requests.put(
                        "{}/{}".format(self.host,request.id),
                        json=request.to_dict(),
                        headers=self.header,
                        verify=False
                    )
                case _:
                    return requests.post(
                        self.host,
                        json=request.to_dict(),
                        headers=self.header,
                        verify=False
                    )
        except Exception as e:
            print(e)
        finally:
            self.host = hostBefore
        
