
from dotenv import load_dotenv

from ORM_IXC.models.tableModels.clienteModel import ClientModel
from ORM_IXC.context.contextModels.cliente import Cliente
from ORM_IXC.statemants.select import select
from ORM_IXC.context.request import Manager
import os

from ORM_IXC.utils.makejson import makeJsonStream

load_dotenv()

host = str(os.getenv("IXC_HOST"))
token = str(os.getenv("IXC_TOKEN"))

manager = Manager(host, token)
contabilSintetica = Cliente(manager)
query = select(contabilSintetica)\
                        .allAssync()

makeJsonStream("neymarJr", query)

