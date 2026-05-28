
from dotenv import load_dotenv

from ORM_IXC.models.tableModels.contratoDoClienteModel import ContratoDoClienteModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule
from ORM_IXC.context.contextModels.contratoDoCliente import ContratoDoCliente
from ORM_IXC.statemants.select import select
from ORM_IXC.context.request import Manager
import os

from ORM_IXC.utils.makejson import makeJson

load_dotenv()

host = str(os.getenv("IXC_HOST"))
token = str(os.getenv("IXC_TOKEN"))

manager = Manager(host, token)
serviceOrder = ContratoDoCliente(manager)
query = select(serviceOrder)\
                        .where(ContratoDoClienteModel.id > 0)\
                        .limit(1000)\
                        .execute()

print(query[0].id_cliente)

makeJson("neymarJr", query)

