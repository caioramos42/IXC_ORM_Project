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
            .columns(LoginModel.id,
                     LoginModel.login)\
            .where(
                   (LoginModel.id == 36) &
                   (LoginModel.login == "julio.permuta.01@brasillike.com.br") |
                   (LoginModel.id == 37) |
                   (LoginModel.id == 40)
            )\
            .limit(500)\
            .order_by("id", "desc")\
            .execute()
            
print(query[1].output_dict())
print([i.id for i in query])
makeJson("neymarJr", query)

