
from dotenv import load_dotenv
from ORM_IXC.context.contextModels.login import Login
from ORM_IXC.models.tableModels.loginModel import LoginModel
from ORM_IXC.statemants.CRUD.select import select
from ORM_IXC.context.request import Manager
import os

from ORM_IXC.utils.makejson import makeJson

load_dotenv()

host = str(os.getenv("IXC_HOST"))
token = str(os.getenv("IXC_TOKEN"))

manager = Manager(host, token)
login = Login(manager)
query = select(login)\
            .where(LoginModel.id == 37)\
            .limit(500)\
            .order_by("id")\
            .execute()
print([i.id for i in query])
makeJson("neymarJr", query)

