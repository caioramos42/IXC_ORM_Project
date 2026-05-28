
from dotenv import load_dotenv

from ORM_IXC.models.tableModels.contaContabilSintetica import ContaContabilSinteticaModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule
from ORM_IXC.context.contextModels.contabil import ContaContabilSintetica
from ORM_IXC.statemants.select import select
from ORM_IXC.context.request import Manager
import os

from ORM_IXC.utils.makejson import makeJsonStream

load_dotenv()

host = str(os.getenv("IXC_HOST"))
token = str(os.getenv("IXC_TOKEN"))

manager = Manager(host, token)
contabilSintetica = ContaContabilSintetica(manager)
query = select(contabilSintetica)\
                        .where(ContaContabilSinteticaModel.id > 0)\
                        .limit(300)\
                        .order_by("id")\
                        .cursor()

makeJsonStream("neymarJr", query)

