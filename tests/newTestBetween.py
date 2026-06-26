import os

from dotenv import load_dotenv

from ORM_IXC.context.contextModels.login import Login
from ORM_IXC.context.request import Manager
from ORM_IXC.models.tableModels.loginModel import LoginModel
from ORM_IXC.statemants.CRUD.select import select
from ORM_IXC.utils.makejson import makeJson

load_dotenv()

host = str(os.getenv("IXC_HOST"))
token = str(os.getenv("IXC_TOKEN"))

manager = Manager(host, token)
context = Login(manager)

query = (
    select(context)
    .where(LoginModel.id.Between(36, 40))
    .limit(500)
)

print(query.to_dict())

responses = query.execute()

print(responses)
makeJson("testBetween", responses)
