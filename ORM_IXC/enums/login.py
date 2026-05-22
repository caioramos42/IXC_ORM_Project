#-------------------------------- ENUMERADORES --------------------------------#
from enum import Enum
class AutenticacaoEnum(Enum):
    PPPOE = 'L'
    HOTSPOT = 'H'
    IP_X_MAC = 'M'
    VLAN = 'V'
    IPOE = 'D'
    INTEGRACAO = 'I'
    EXTERNA = 'E'

class Tipo_conexao_mapaEnum(Enum):
    C58 = '58'
    C24 = '24'
    FIBRA = 'F'
    CABO = 'L'
    ADSL = 'A'
    LTE = 'LTE'
    LINK_DEDICADO = 'LDD'

class Senha_md5Enum(Enum):
    NAO = 'N'
    SIM = 'S'

class AtivoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class OnlineEnum(Enum):
    SIM = 'S'
    NAO = 'N'
    SEM_STATUS = 'SS'

class Auto_preencher_ipEnum(Enum):
    CONFIGURACAO_PADRAO = 'H'
    SEMPRE = 'S'
    NUNCA = 'N'

class Fixar_ipEnum(Enum):
    CONFIGURACAO_PADRAO = 'H'
    SEMPRE = 'S'
    NUNCA = 'N'

class Relacionar_ip_ao_loginEnum(Enum):
    CONFIGURACAO_PADRAO = 'H'
    SEMPRE = 'S'
    NUNCA = 'N'

class Framed_autopreencher_ipv6Enum(Enum):
    CONFIGURACAO_PADRAO = 'H'
    SEMPRE = 'S'
    NUNCA = 'N'

class Framed_fixar_ipv6Enum(Enum):
    CONFIGURACAO_PADRAO = 'H'
    SEMPRE = 'S'
    NUNCA = 'N'

class Framed_relacionar_ipv6_ao_loginEnum(Enum):
    CONFIGURACAO_PADRAO = 'H'
    SEMPRE = 'S'
    NUNCA = 'N'

class Auto_preencher_ipv6Enum(Enum):
    CONFIGURACAO_PADRAO = 'H'
    SEMPRE = 'S'
    NUNCA = 'N'

class Fixar_ipv6Enum(Enum):
    CONFIGURACAO_PADRAO = 'H'
    SEMPRE = 'S'
    NUNCA = 'N'

class Relacionar_ipv6_ao_loginEnum(Enum):
    CONFIGURACAO_PADRAO = 'H'
    SEMPRE = 'S'
    NUNCA = 'N'

class Autenticacao_por_macEnum(Enum):
    NAO = 'N'
    SIM = 'S'
    PADRAO = 'P'
    MIKROTIK = 'MK'
    UBNT = 'UN'
    WPA2_AES = 'WP'

class Auto_preencher_macEnum(Enum):
    CONFIGURACAO_PADRAO = 'H'
    SEMPRE = 'S'
    NUNCA = 'N'

class Relacionar_mac_ao_loginEnum(Enum):
    CONFIGURACAO_PADRAO = 'H'
    SEMPRE = 'S'
    NUNCA = 'N'

class Relacionar_concentrador_ao_loginEnum(Enum):
    CONFIGURACAO_PADRAO = 'H'
    SEMPRE = 'S'
    NUNCA = 'N'

class Tipo_vinculo_planoEnum(Enum):
    PADRAO = 'D'
    CONTRATO = 'C'
    PRE_PAGO = 'P'
    GRATIS = 'G'

class Tipo_acessoEnum(Enum):
    HTTPS = 'https'
    HTTP = 'http'

class Franquia_atingidaEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Onu_compartilhadaEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Tipo_equipamentoEnum(Enum):
    COMODATO = 'C'
    PROPRIO = 'P'

class Endereco_padrao_clienteEnum(Enum):
    PADRAO_CLIENTE = 'S'
    MANUAL = 'N'

class PontaEnum(Enum):
    A = 'A'
    B = 'B'
    C = 'C'