from enum import Enum


class TipoEnum(Enum):
    INTERNET = 'I'
    TELEFONIA = 'T'
    SERVICOS = 'S'
    SVA = 'SVA'

class Tipo_pessoaEnum(Enum):
    FISICA = 'F'
    JURIDICA = 'J'
    ESTRANGEIRO = 'E'
    TODOS = 'T'

class AtivoEnum(Enum):
    ATIVO = 'S'
    INATIVO = 'N'

class Base_geracao_por_tipo_docEnum(Enum):
    DOCUMENTO_OPCIONAL_DO_CONTRATO = 'OPC'
    DOCUMENTO_DO_PRODUTO_DO_CONTRATO = 'PROD'
    PADRAO = 'P'

class Utilizar_desconto_ate_vencimentoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Utilizar_desconto_por_repeticaoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Utilizar_desconto_no_produto_planoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

