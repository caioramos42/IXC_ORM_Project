import os
from dotenv import load_dotenv
from ORM_IXC.context.contextModels.serviceOrder import ServiceOrder
from ORM_IXC.context.request import Manager
from ORM_IXC.models.tableModels.serviceOrderModel import ServiceOrderModel
from ORM_IXC.statemants.delete import delete

load_dotenv()

host = str(os.getenv("IXC_HOST"))
token = str(os.getenv("IXC_TOKEN"))

manager = Manager(host, token)

context = ServiceOrder(manager)

responses = delete(context)\
    .where(ServiceOrderModel.id == 308364)\
    .execute()
print(responses[0].text)