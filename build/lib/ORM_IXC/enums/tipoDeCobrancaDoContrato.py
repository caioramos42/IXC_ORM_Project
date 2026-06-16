from enum import Enum


class AtivoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Tipo_pagamentoEnum(Enum):
    PRE_PAGO = 'Pre'
    POS_PAGO = 'Pos'

class Pagamento_antecipadoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Base_periodo_prestacaoEnum(Enum):
    DATA_VENCIMENTO = 'V'
    DATA_CONTRATO = 'C'
    PERIODO = 'P'

class PeriodoEnum(Enum):
    DIA = 'D'
    MES = 'M'
    ANO = 'A'

class Parcela_cobrar_proporcionalEnum(Enum):
    NAO_GERAR_PROPORCIONAL = '0'
    PRIMEIRA_PARCELA = '1'
    SEGUNDA_PARCELA = '2'

