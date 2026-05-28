
from dotenv import load_dotenv

from ORM_IXC.context.contextModels.serviceOrder import ServiceOrder
from ORM_IXC.models.searchUtils.searchModel import SearchModule
from ORM_IXC.models.tableModels.serviceOrderModel import ServiceOrderModel
from ORM_IXC.statemants.select import select
from ORM_IXC.context.request import Manager
import os

from ORM_IXC.utils.makejson import makeJsonStream

load_dotenv()

host = str(os.getenv("IXC_HOST"))
token = str(os.getenv("IXC_TOKEN"))

manager = Manager(host, token)
serviceOrder = ServiceOrder(manager)
query = select(serviceOrder)\
                        .where(ServiceOrderModel.id > 0)\
                        .limit(1000)\
                        .order_by("id")\
                        .cursor()

print([i.id_assunto for i in query])

makeJsonStream("neymarJr", query)

