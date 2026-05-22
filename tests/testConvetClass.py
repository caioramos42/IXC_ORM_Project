
from dotenv import load_dotenv

from ORM_IXC.context.login import Login
from ORM_IXC.models.loginModel import LoginModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule
from ORM_IXC.statemants.select import select
from ORM_IXC.context.request import Manager
import os

from ORM_IXC.utils.makejson import makeJson

load_dotenv()

host = str(os.getenv("IXC_HOST"))
token = str(os.getenv("IXC_TOKEN"))

manager = Manager(host, token)
login = Login(manager)
query: SearchModule = select(login).where(LoginModel.id == 29917, LoginModel.tipo_conexao_mapa == 'F')\
                        .limit(2)\
                        .order_by("id")\
                        .execute()

#print(query.to_dict())
makeJson("neymarJr", query)

