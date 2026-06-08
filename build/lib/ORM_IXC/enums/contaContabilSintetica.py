from enum import Enum
#-------------------------------- ENUMERADORES --------------------------------#
class TipoEnum(Enum):
    ATIVO = 'A'
    PASSIVO = 'P'
    RECEITAS = 'R'
    DESPESAS = 'D'
    CUSTO = 'C'
    PATRIMONIO = 'PT'

class SubtipoEnum(Enum):
    CUSTO_FIXO = 'CF'
    CUSTO_VARIAVEL = 'CV'
    DESPESA_FIXA = 'DF'
    DESPESA_VARIAVEL = 'DV'
    DEPRECIACAO_AMORTIZACAO = 'DA'