from enum import Enum


class StatusEnum(Enum):
    ATIVO = 'A'
    INATIVO = 'I'

class Tipo_acessoEnum(Enum):
    AMBOS = 'A'
    WEB = 'W'
    MOBILE = 'M'

class TemplateEnum(Enum):
    PADRAO = 'd'
    MODERNO = 'vg'

class SchemeEnum(Enum):
    MODO_CLARO = 'light'
    MODO_ESCURO = 'dark'

class CallcenterEnum(Enum):
    ___ = '---'
    ACTIONCALL = 'actioncall'
    BELLUNO = 'belluno'
    PHONEVOX_GROUP_TECHNOLOGY = 'lvnetwork'
    APRIMORAR_SUPORTE_TECNICO_E_TELEATENDIMENTO = 'aprimorar'
    BASE_ATENDIMENTO = 'unocena'
    METRO_NETWORK = 'metro_network'
    GLOBAL_SOURCE = 'global_source'
    SPEED_GROWTH_ISP = 'speed_growth'

class LanguageEnum(Enum):
    PT_BR = 'Pt-Br'
    EN_US = 'En-Us'
    ES_ES = 'Es-Es'

class Recebimentos_dia_atualEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Pagamentos_dia_atualEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Lancamentos_dia_atualEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Filtrar_plano_venda_filial_contratoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Permitir_alterar_versao_chavesEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Desc_parc_atrasoEnum(Enum):
    SIM = 'S'
    NAO = 'N'
    PADRAO = 'P'

class Permite_alterar_comunicacao_fn_apagarEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Filtra_departamento_ticketEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Filtra_funcionario_ticketEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Mostrar_ticket_sem_funcionarioEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Filtra_setorEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Filtra_funcionarioEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Mostrar_os_sem_funcionarioEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Administrador_kanbanEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Permite_inutilizar_patrimonioEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Permite_ver_diferencaEnum(Enum):
    SIM = 'S'
    NAO = 'N'

