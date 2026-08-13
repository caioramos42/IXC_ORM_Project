from enum import Enum


class AtivoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Enable_totp_groupEnum(Enum):
    SIM = '1'
    NAO = '0'
    PADRAO = '2'

class Permite_atualizarEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Permissao_tipoEnum(Enum):
    HABILITAR = 'L'
    ESCONDER = 'B'

class Permissao_bt_formEnum(Enum):
    HABILITAR = 'H'
    ESCONDER = 'E'

class Permissao_campo_formEnum(Enum):
    HABILITAR = 'H'
    SOMENTE_LEITURA = 'S'
    ESCONDER = 'E'

class Acesso_upvoty_ixcEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Expire_passwordEnum(Enum):
    NUNCA = '0'
    MESES_03 = '3'
    MESES_06 = '6'
    MESES_09 = '9'
    MESES_12 = '12'
    MESES_01 = '1'
    MESES_02 = '2'
    PERSONALIZAVEL_ = 'P'

class Tempo_limite_sessao_minutosEnum(Enum):
    PADRAO = '0'
    MINUTOS_15 = '15'
    MINUTOS_30 = '30'
    HORA_1 = '60'
    HORAS_1_5 = '90'
    HORAS_2 = '120'
    HORAS_2_5 = '150'
    HORAS_3 = '180'
    HORAS_4 = '240'
    HORAS_5 = '300'
    HORAS_12 = '720'
    DIA_1 = '1440'
    DIAS_3 = '4320'

class Acesso_querybuilderEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Acesso_avancado_querybuilderEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Dashboard_padraoEnum(Enum):
    PRINCIPAL = 'dash_principal'
    FINANCEIRO = 'dash_financeiro'
    ORDEM_DE_SERVICO = 'dash_ordem_servico'
    ACESSOS = 'dash_acessos'
    ATENDIMENTO = 'dash_atendimento'
    CRM = 'dash_crm'
    CONTRATOS = 'dash_contratos'
    COBRANCAS = 'dash_cobrancas'
    INFORMACOES_DO_SERVIDOR = 'dash_serverinfo'
    VENDEDOR = 'dash_crm_user'
    DASHBOARD_CLIENTE_CHAVE = 'dash_cliente_chave'
    SERVIDOR = 'dash_serverinfo'
    TECNICO_SUPORTE = 'dash_ordem_servico_user'
    CONTAS_A_RECEBER = 'dash_contas_a_receber'
    DASH_FATURAS = 'dash_faturas'

class Dash_principalEnum(Enum):
    PADRAO_DO_FORMULARIO = 'P'
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Dash_contratosEnum(Enum):
    PADRAO_DO_FORMULARIO = 'P'
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Dash_cobrancasEnum(Enum):
    PADRAO_DO_FORMULARIO = 'P'
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Dash_financeiroEnum(Enum):
    PADRAO_DO_FORMULARIO = 'P'
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Dash_contas_a_receberEnum(Enum):
    PADRAO_DO_FORMULARIO = 'P'
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Dash_contas_a_pagarEnum(Enum):
    PADRAO_DO_FORMULARIO = 'P'
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Dash_cliente_chaveEnum(Enum):
    PADRAO_DO_FORMULARIO = 'P'
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Dash_acessosEnum(Enum):
    PADRAO_DO_FORMULARIO = 'P'
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Dash_atendimentoEnum(Enum):
    PADRAO_DO_FORMULARIO = 'P'
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Dash_ordem_servicoEnum(Enum):
    PADRAO_DO_FORMULARIO = 'P'
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Dash_ordem_servico_userEnum(Enum):
    PADRAO_DO_FORMULARIO = 'P'
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Dash_crmEnum(Enum):
    PADRAO_DO_FORMULARIO = 'P'
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Dash_crm_pessoa_fisicaEnum(Enum):
    PADRAO_DO_FORMULARIO = 'P'
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Dash_crm_corporativoEnum(Enum):
    PADRAO_DO_FORMULARIO = 'P'
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Dash_crm_userEnum(Enum):
    PADRAO_DO_FORMULARIO = 'P'
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Dash_negociacoesEnum(Enum):
    PADRAO_DO_FORMULARIO = 'P'
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Dash_serverinfoEnum(Enum):
    PADRAO_DO_FORMULARIO = 'P'
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Dash_radiusEnum(Enum):
    PADRAO_DO_FORMULARIO = 'P'
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Dash_monitoramento_fibraEnum(Enum):
    PADRAO_DO_FORMULARIO = 'P'
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Dash_faturasEnum(Enum):
    PADRAO_DO_FORMULARIO = 'P'
    MOSTRAR = 'M'
    ESCONDER = 'E'

