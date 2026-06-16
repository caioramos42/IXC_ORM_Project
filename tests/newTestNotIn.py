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

print(host + " "  + token)
manager = Manager(host, token)

context = Login(manager)

print(LoginModel.id.NotIn(36,37,40).to_dict())

responses = select(context)\
    .where(LoginModel.id.NotIn(36,37,40))\
    .limit(500)\
    .execute()
    
makeJson("testBetween",responses)
