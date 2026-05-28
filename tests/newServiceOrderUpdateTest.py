import os

from dotenv import load_dotenv

from ORM_IXC.context.contextModels.serviceOrder import ServiceOrder
from ORM_IXC.context.request import Manager
from ORM_IXC.models.tableModels.serviceOrderModel import ServiceOrderModel
from ORM_IXC.statemants.update import update

load_dotenv()

host = str(os.getenv("IXC_HOST"))
token = str(os.getenv("IXC_TOKEN"))

print(host + " "  + token)
manager = Manager(host, token)

context = ServiceOrder(manager)

responses = update(context)\
    .where(ServiceOrderModel.id == 308364)\
    .values(ServiceOrderModel(
        id_login = 29917
        ))\
    .execute()
print(responses[0].text)

#308364