from enum import Enum


class TipoEnum(Enum):
    INTERNET = 'I'
    TELEFONIA = 'T'
    SERVICOS = 'S'
    SVA = 'SVA'
    TV = 'TV'
    MVNO_TELEFONIA_MOVEL = 'SMP'

class Tipo_descontoEnum(Enum):
    VALOR = 'V'
    PERCENTUAL = 'P'

class RepetirEnum(Enum):
    QUANTIDADE = 'V'
    SEMPRE = 'S'

class Fixar_ipEnum(Enum):
    SIM = '1'
    NAO = '0'

