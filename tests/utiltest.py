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


# Querys
query = select(contratoClient)\
            .where(ContratoDoClienteModel.contrato == "LIKE SAT BASIC")\
            .limit(500)\
            .order_by("id")\
            .execute()

idsList = [i.id.value for i in query]

query = select(carteiraCobranca)\
            .where(ContasAReceberModel.id_contrato.In(*idsList))\
            .limit(300)\
            .order_by("id")\
            .execute()

query = select(carteiraCobranca)\
            .where(ContasAReceberModel.id_contrato.In(*idsList),
                   ContasAReceberModel.valor_recebido == '0.00',
                   ContasAReceberModel.data_vencimento >= maturity.strftime('%Y-%m-%d') + " 00:00:00",
                   ContasAReceberModel.data_vencimento <= maturity.strftime('%Y-%m-%d') + " 23:59:59"
                   )\
            .limit(300)\
            .order_by("id")\
            .execute()
            
idsList = [i.id_cliente.value for i in query]

query = select(cliente)\
            .where(ClientModel.id.In(*idsList))\
            .limit(500)\
            .order_by("id")\
            .execute()

print([i.razao.value for i in query])

makeJson("neymarJr", query)