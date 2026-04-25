from ORM_IXC.context.serviceOrder import ServiceOrder
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.defaultModel import DefaultPayload
from dotenv import load_dotenv
import sys
import os

load_dotenv()
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def test_create():
    manager = Manager(os.getenv("IXC_HOST"), os.getenv("IXC_TOKEN"))
    service_order = ServiceOrder(manager)
    print(service_order.Add(
        DefaultPayload({
            'tipo': 'C',
            'id_ticket': '',
            'protocolo': '',
            'id_assunto': '',
            'dica_assinatura_digital': '',
            'id_cliente': '',
            'id_estrutura': '',
            'id_filial': '1',
            'id_login': '',
            'id_contrato_kit': '',
            'origem_endereco': 'M',
            'origem_endereco_estrutura': 'E',
            'latitude': '',
            'longitude': '',
            'status_conexao': '',
            'prioridade': 'N',
            'melhor_horario_agenda': 'Q',
            'setor': '2',
            'id_tecnico': '',
            'mensagem': 'Teste',
            'id_receber': '',
            'idx': '',
            'status_pesquisa_satisfacao': '',
            'status': 'A',
            'habilita_assinatura_cliente': '',
            'status_assinatura': 'A',
            'gera_comissao': 'S',
            'liberado': '1',
            'id_atendente': '',
            'impresso': 'N',
            'preview': '',
            'id_wfl_param_os': '',
            'id_wfl_tarefa': '',
            'id_su_diagnostico': '',
            'regiao_manutencao': '',
            'origem_cadastro': 'P',
            'origem_change_endereco': 'default',
            'status_sla': 'NULL',
            'ultima_atualizacao': '',
            'ids_login_regiao_manutencao': '',
            'origem_os_aberta': 'C',
            'id_cidade': '',
            'bairro': '',
            'endereco': '',
            'complemento': '',
            'referencia': '',
            'id_condominio': '',
            'bloco': '',
            'apartamento': '',
            'data_abertura': '',
            'data_inicio': '',
            'data_hora_analise': '',
            'data_agenda': '',
            'data_agenda_final': '',
            'data_hora_encaminhado': '',
            'data_hora_assumido': '',
            'data_hora_execucao': '',
            'data_final': '',
            'data_fechamento': '',
            'data_prazo_limite': '',
            'data_reservada': '',
            'data_reagendar': '',
            'data_prev_final': '',
            'mensagem_resposta': '',
            'justificativa_sla_atrasado': '',
            'valor_total': '',
            'valor_outras_despesas': '',
            'valor_unit_comissao': '0,00',
            'valor_total_comissao': '0,00',
            "id_cobranca": ""
        })
    ).json())
test_create()