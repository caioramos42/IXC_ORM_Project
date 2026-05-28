import os

from dotenv import load_dotenv

from ORM_IXC.context.request.manager import Manager
from ORM_IXC.context.contextModels.serviceOrder import ServiceOrder
from ORM_IXC.models.tableModels.serviceOrderModel import ServiceOrderModel
from ORM_IXC.statemants.insert import insert

load_dotenv()

host = str(os.getenv("IXC_HOST"))
token = str(os.getenv("IXC_TOKEN"))
def test_create_service_order_insert_builder():
    manager = Manager(host, token)
    service_order = ServiceOrder(manager)

    # O construtor preenchido com base no dicionário fornecido
    query = insert(service_order).values(
        ServiceOrderModel(
            id = None,
            id_assunto = 217,
            id_atendente = '',
            id_cliente = 32099,
            tipo='C',
            id_filial=1,
            origem_endereco='M',
            origem_endereco_estrutura='E',
            prioridade='N',
            melhor_horario_agenda='Q',
            setor=2,
            mensagem='Teste Api',
            status='A',
            status_assinatura='A',
            gera_comissao='S',
            liberado='1',
            impresso='N',
            origem_cadastro='P',
            origem_os_aberta='C',
            valor_unit_comissao='0,00',
            valor_total_comissao='0,00',
        )
    ).execute()
    print(query[0].text)
test_create_service_order_insert_builder()