
from dotenv import load_dotenv

from ORM_IXC.models.tableModels.clienteFibraModel import ClienteFibraModel
from ORM_IXC.context.contextModels.fiberClient import ClienteFibra
from ORM_IXC.statemants.select import select
from ORM_IXC.context.request import Manager
import os

from ORM_IXC.utils.makejson import makeJson

load_dotenv()

host = str(os.getenv("IXC_HOST"))
token = str(os.getenv("IXC_TOKEN"))

manager = Manager(host, token)
clienteFibra = ClienteFibra(manager)
query = select(clienteFibra)\
                        .where(ClienteFibraModel.id > 0)\
                        .limit(1000)\
                        .execute()

makeJson("neymarJr", query)