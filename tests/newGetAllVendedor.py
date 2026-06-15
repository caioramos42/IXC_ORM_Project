from ORM_IXC.context.contextModels.vendedor import Vendedor
from ORM_IXC.models.tableModels.vendedorModel import VendedorModel
from ORM_IXC.context.request.manager import Manager
from dotenv import load_dotenv
from ORM_IXC.statemants.CRUD.select import select
from ORM_IXC.utils.makejson import makeJsonStream

import os
load_dotenv()

host = str(os.getenv("IXC_HOST"))
token = str(os.getenv("IXC_TOKEN"))


manager = Manager(host, token)
vendedor = Vendedor(manager)

makeJsonStream("vendedorList", 
               select(vendedor)\
                   .where(VendedorModel.id > 0).cursor()
            )