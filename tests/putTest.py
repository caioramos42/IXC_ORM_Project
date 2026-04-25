from ORM_IXC.context.serviceOrder import ServiceOrder
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.models.defaultModel import DefaultPayload
from dotenv import load_dotenv
import sys
import os

load_dotenv()
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def test_put():
    manager = Manager(os.getenv("IXC_HOST"), os.getenv("IXC_TOKEN"))
    service_order = ServiceOrder(manager)
    print(service_order.Update(
        DefaultPayload({
            "mensagem_resposta": "",
            "data_hora_analise": "0000-00-00 00:00:00",
            "data_hora_encaminhado": "0000-00-00 00:00:00",
            "data_hora_assumido": "0000-00-00 00:00:00",
            "data_hora_execucao": "0000-00-00 00:00:00",
            "id_contrato_kit": "",
            "preview": "",
            "data_agenda_final": "0000-00-00 00:00:00",
            "status_assinatura": "A",
            "habilita_assinatura_cliente": "N",
            "status_pesquisa_satisfacao": "2",
            "id_receber": "",
            "id": "",
            "tipo": "C",
            "id_filial": "1",
            "id_wfl_tarefa": "0",
            "status_sla": "N",
            "data_abertura": "2026-04-25 09:02:48",
            "melhor_horario_agenda": "Q",
            "liberado": "1",
            "status": "A",
            "id_cliente": "",
            "id_assunto": "",
            "setor": "2",
            "id_cidade": "0",
            "id_tecnico": "0",
            "prioridade": "N",
            "origem_os_aberta": "CRM",
            "mensagem": "EXECU\u00c7\u00c3O AUTOM\u00c1TICA PASSO 2.",
            "protocolo": "202604166934",
            "endereco": "",
            "complemento": "",
            "id_condominio": "0",
            "latitude": "",
            "bloco": "",
            "longitude": "",
            "apartamento": "",
            "bairro": "",
            "referencia": "",
            "impresso": "N",
            "data_inicio": "0000-00-00 00:00:00",
            "data_agenda": "0000-00-00 00:00:00",
            "data_final": "0000-00-00 00:00:00",
            "data_fechamento": "0000-00-00 00:00:00",
            "id_wfl_param_os": "0",
            "valor_outras_despesas": "0.00",
            "valor_total_comissao": "0.00",
            "valor_total": "0.00",
            "gera_comissao": "S",
            "idx": "0",
            "valor_unit_comissao": "0.00",
            "id_su_diagnostico": "0",
            "id_estrutura": "0",
            "id_login": "32887",
            "data_prazo_limite": "0000-00-00 00:00:00",
            "data_reservada": "0000-00-00",
            "id_ticket": "0",
            "origem_endereco": "M",
            "justificativa_sla_atrasado": "",
            "origem_endereco_estrutura": "M",
            "data_reagendar": "0000-00-00 00:00:00",
            "data_prev_final": "0000-00-00 00:00:00",
            "origem_cadastro": "P",
            "ultima_atualizacao": "2026-04-25 09:02:48",
            "id_cobranca": ""
        })
    ).json())
test_put()