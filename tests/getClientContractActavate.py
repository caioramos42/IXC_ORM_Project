# from ORM_IXC.context.request.manager import Manager
# from ORM_IXC.context.clienteContratoAtivar import ClienteContratoAtivar
# from ORM_IXC.models.searchUtils import SearchModule
# from ORM_IXC.enums.operators import Operators
# import sys
# import os
# from dotenv import load_dotenv

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# load_dotenv()


# def getClientContractActivate():
#     manager = Manager(os.getenv("IXC_HOST"), os.getenv("IXC_TOKEN"))
#     client_contract_activate = ClienteContratoAtivar(manager)
#     return client_contract_activate.getByFilter(search=SearchModule('id','0',Operators.MORETHAN,page=1,amount=20)).json()
# print(getClientContractActivate())

import sys
import os
from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
load_dotenv()

import requests
import base64
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host = os.getenv("IXC_HOST")
url = "https://{}/webservice/v1/cliente_contrato_ativar_cliente".format(host)
token = os.getenv("IXC_TOKEN").encode('utf-8')
#'id': 'cliente_contrato_ativar_cliente.id',
payload = {
    'qtype': 'cliente_contrato_ativar_cliente.id',
    'id_contrato': 'id_contrato'
}

headers = {
    'ixcsoft': 'listar',
    'Authorization': 'Basic {}'.format(base64.b64encode(token).decode('utf-8')),
    'Content-Type': 'application/json'
}

response = requests.post(url, json=payload, headers=headers, verify=False)

print(response.text)
