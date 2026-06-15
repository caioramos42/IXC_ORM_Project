
from dotenv import load_dotenv
from ORM_IXC.statemants.CRUD.select import select
from ORM_IXC.context.request import Manager
from ORM_IXC.context.contextModels.tipoDocumento import TipoDocumento
from ORM_IXC.models.tableModels.tipoDocumentoModel import TipoDocumentoModel
import os

from ORM_IXC.utils.makejson import makeJson

load_dotenv()

host = str(os.getenv("IXC_HOST"))
token = str(os.getenv("IXC_TOKEN"))

manager = Manager(host, token)
login = TipoDocumento(manager)
query = select(login)\
            .where(TipoDocumentoModel.id  > 0)\
            .limit(500)\
            .order_by("id")\
            .execute()
print([i.id for i in query])
makeJson("neymarJr", query)

