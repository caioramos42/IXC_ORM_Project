from ORM_IXC.statemants.CRUD.select import select
from ORM_IXC.statemants.sqlFunctions.count import count
from ORM_IXC.statemants.maps.classBase import Field
from ORM_IXC.models.searchUtils.searchModel import SearchModule
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.context.contextModels.cliente import Cliente
from ORM_IXC.models.tableModels.clienteModel import ClientModel
from dotenv import load_dotenv
import os
from ORM_IXC.utils.makejson import makeJson
load_dotenv()

host = str(os.getenv("IXC_HOST"))
token = str(os.getenv("IXC_TOKEN"))

manager = Manager(host, token)
cliente = Cliente(manager)

result = select(count(cliente, ClientModel.razao, "contador")).where(ClientModel.id == 27560).groupby(ClientModel.razao).execute()
makeJson("testCount",result)