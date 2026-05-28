
from dotenv import load_dotenv

from ORM_IXC.models.tableModels.contasAReceber import ContasAReceberModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule
from ORM_IXC.context.contextModels.areceber import AReceber
from ORM_IXC.statemants.select import select
from ORM_IXC.context.request import Manager
import os

from ORM_IXC.utils.makejson import makeJsonStream

load_dotenv()

host = str(os.getenv("IXC_HOST"))
token = str(os.getenv("IXC_TOKEN"))

manager = Manager(host, token)
aReceber = AReceber(manager)
query = select(aReceber)\
                        .where(ContasAReceberModel.id > 0)\
                        .limit(300)\
                        .order_by("id")\
                        .cursor()

makeJsonStream("neymarJr", query)

