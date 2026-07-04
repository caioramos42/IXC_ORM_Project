from datetime import datetime, timedelta
from ORM_IXC.models.tableModels.contratoDoClienteModel import ContratoDoClienteModel
from ORM_IXC.context.contextModels.contratoDoCliente import ContratoDoCliente
from ORM_IXC.models.tableModels.clienteModel import ClientModel
from ORM_IXC.context.contextModels.cliente import Cliente
from ORM_IXC.models.tableModels.atendimentoModel import AtendimentoModel
from ORM_IXC.context.contextModels.atendimento import Atendimento
from ORM_IXC.context.contextModels.radacct import Radacct
from ORM_IXC.models.tableModels.radacctModel import RadacctModel
from ORM_IXC.context.contextModels.login import Login
from ORM_IXC.models.tableModels.loginModel import LoginModel
from ORM_IXC.context.contextModels.serviceOrder import ServiceOrder
from ORM_IXC.models.tableModels.serviceOrderModel import ServiceOrderModel
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.statemants.CRUD.select import select
from ORM_IXC.statemants.CRUD.insert import insert
from ORM_IXC.statemants.sqlFunctions.distinct import distinct
from ORM_IXC.statemants.sqlFunctions.count import count
import os
from dotenv import load_dotenv
from ORM_IXC.utils.makejson import makeJson

load_dotenv()

host = str(os.getenv("IXC_HOST"))
token = str(os.getenv("IXC_TOKEN"))   

manager = Manager(host, token)
radacct = Radacct(manager)
contrato = ContratoDoCliente(manager)
login = Login(manager)
atendimento = Atendimento(manager)
cliente = Cliente(manager)
service_order = ServiceOrder(manager)

yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

query = (
    select(count(radacct, RadacctModel.username, "contador"))
    .where(
        (RadacctModel.acctstoptime >= yesterday + " 00:00:00") &
        (RadacctModel.acctstoptime <= yesterday + " 23:59:59")
    )
    .groupby(RadacctModel.username)
    .having(radacct.contador >= 4)
    .order_by("acctsessionid")\
    .limit(3000)
    .execute()
)

if query:
    search = (LoginModel.login == query[0].username)
    for user in query[1:]:
        search |= (LoginModel.login == user.username)
        
    query2 = select(distinct(login, LoginModel.login))\
                .columns(LoginModel.id, LoginModel.login, ContratoDoClienteModel.id, ClientModel.id)\
                .where(search)\
                .join(
                    contrato,
                    LoginModel.id_contrato == ContratoDoClienteModel.id,
                    (ContratoDoClienteModel.status == 'A') & 
                    (ContratoDoClienteModel.contrato.like('%WIRELESS')),
                )\
                .join(
                    atendimento,
                    LoginModel.id == AtendimentoModel.id_login,
                    (AtendimentoModel.titulo == 'DESCONEXÕES RECENTES - VERIFICAR COM O CLIENTE') &
                    ((AtendimentoModel.su_status == 'P') |
                    (AtendimentoModel.su_status == 'EP') |
                    (AtendimentoModel.su_status == 'N')),
                    join_type='left'
                )\
                .join(
                    cliente,
                    LoginModel.id_cliente == ClientModel.id
                )\
                .limit(3000)\
                .execute()

    query2 = [q for q in query2 if len(q._inners) <= 2]
    print(query2[0].output_dict()['cliente_contrato.id'])
    makeJson("logins", query2)



    response = insert(atendimento).values(*[AtendimentoModel(
        id = 0,
        tipo="C",
        titulo="DESCONEXÕES RECENTES - VERIFICAR COM O CLIENTE",
        origem_endereco='L',
        origem_endereco_estrutura = 'L',
        atualizar_cliente = 'N',
        finalizar_atendimento = 'N',
        status = 'T',
        su_status = 'N',
        interacao_pendente = 'N',
        melhor_horario_reserva = 'Q',
        prioridade = 'M',
        id_ticket_setor = 7,
        menssagem = 'Cliente com desconexão com número acima de 4. Favor entrar em contato com o cliente para verificar o ocorrido.',
        id_login = q.output_dict()['login.id'],
        id_cliente = q.output_dict()['cliente.id'],
        id_contrato = q.output_dict()['cliente_contrato.id']
    ) for q in query2]).execute()

