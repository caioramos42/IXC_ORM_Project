from dotenv import load_dotenv

from ORM_IXC.models.tableModels.contratoDoClienteModel import ContratoDoClienteModel
from ORM_IXC.context.contextModels.contratoDoCliente import ContratoDoCliente
from ORM_IXC.context.contextModels.cliente import Cliente
from ORM_IXC.models.tableModels.clienteModel import ClientModel
from ORM_IXC.context.contextModels.areceber import AReceber
from ORM_IXC.models.tableModels.contasAReceber import ContasAReceberModel
from ORM_IXC.statemants.CRUD.select import select
from ORM_IXC.context.request import Manager
from datetime import datetime, timedelta
import os

from ORM_IXC.utils.makejson import makeJson

load_dotenv()
host = str(os.getenv("IXC_HOST"))
token = str(os.getenv("IXC_TOKEN"))

quantityDays = 3

maturity = datetime.today() - timedelta(days=quantityDays)

manager = Manager(host, token)
contratoClient = ContratoDoCliente(manager)
carteiraCobranca = AReceber(manager)
cliente = Cliente(manager)


query = select(cliente)\
            .where(ClientModel.id.In(
                   select(carteiraCobranca)\
                   .where(ContasAReceberModel.id_contrato.In(
                            select(contratoClient)\
                            .where(ContratoDoClienteModel.contrato == "LIKE SAT BASIC")\
                            .limit(500), "id"))\
                   .limit(300),"id_cliente"))\
            .limit(500)\
            .order_by("id")\
            .execute()

print([i.razao.value for i in query])

makeJson("file", query)



