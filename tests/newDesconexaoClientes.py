from datetime import datetime, timedelta

from ORM_IXC.models.tableModels.contratoDoClienteModel import ContratoDoClienteModel
from ORM_IXC.context.contextModels.contratoDoCliente import ContratoDoCliente
from ORM_IXC.context.contextModels.radacct import Radacct
from ORM_IXC.models.tableModels.radacctModel import RadacctModel
from ORM_IXC.context.contextModels.login import Login
from ORM_IXC.models.tableModels.loginModel import LoginModel
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.statemants.CRUD.select import select
import os
from dotenv import load_dotenv
from ORM_IXC.utils.makejson import makeJson
from ORM_IXC.utils.pythonFormats import to_pandas_dataframe

load_dotenv()

host = str(os.getenv("IXC_HOST"))
token = str(os.getenv("IXC_TOKEN"))   

manager = Manager(host, token)
radacct = Radacct(manager)
contrato = ContratoDoCliente(manager)
login = Login(manager)
yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y/%m/%d')



query = select(radacct)\
    .columns(RadacctModel.username)\
    .where((RadacctModel.acctstoptime >= yesterday + ' 00:00:00') &
           (RadacctModel.acctstoptime <= yesterday + ' 23:59:59'))\
    .limit(3000)\
    .order_by("username")\
    .execute()

search = LoginModel.login == query[0].username.value
for q in query[1:]:
    search |= (LoginModel.login == q.username.value)

query2 = select(login)\
            .where(search)\
            .limit(3000)\
            .execute()


#makeJson("desconections", query)
pandasFormat = to_pandas_dataframe(query)
makeJson("logins", query2)
print(query2)



