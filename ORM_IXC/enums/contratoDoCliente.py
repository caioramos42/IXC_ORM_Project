from enum import Enum

class TipoEnum(Enum):
    INTERNET = 'I'
    TELEFONIA = 'T'
    SERVICOS = 'S'
    SVA = 'SVA'

class Estrato_social_colEnum(Enum):
    ES1 = '1'
    ES2 = '2'
    ES3 = '3'
    ES4 = '4'
    ES5 = '5'
    ES6 = '6'

class Assinatura_digitalEnum(Enum):
    SIM = 'S'
    NAO = 'N'
    PADRAO = 'P'

class Integracao_assinatura_digitalEnum(Enum):
    SIM = 'S'
    NAO = 'N'
    PADRAO = 'P'

class Liberacao_bloqueio_manualEnum(Enum):
    SIM = 'S'
    NAO = 'N'
    PADRAO = 'P'

class Isentar_contratoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class StatusEnum(Enum):
    PRE_CONTRATO = 'P'
    ATIVO = 'A'
    INATIVO = 'I'
    NEGATIVADO = 'N'
    DESISTIU = 'D'

class Status_internetEnum(Enum):
    ATIVO = 'A'
    DESATIVADO = 'D'
    BLOQUEIO_MANUAL = 'CM'
    BLOQUEIO_AUTOMATICO = 'CA'
    FINANCEIRO_EM_ATRASO = 'FA'
    AGUARDANDO_ASSINATURA = 'AA'

class Status_velocidadeEnum(Enum):
    NORMAL = 'N'
    REDUZIDA = 'R'

class Motivo_inclusaoEnum(Enum):
    INSTALACAO = 'I'
    UPGRADE = 'U'
    DOWNGRADE = 'D'
    MUDANCA_DE_ENDERECO = 'M'
    MUDANCA_DE_TECNOLOGIA = 'T'
    MUDANCA_DE_TITULARIDADE = 'L'
    NEGOCIACAO = 'N'
    REATIVACAO = 'R'

class Cc_previsaoEnum(Enum):
    CONFIGURACAO_PADRAO_ = 'P'
    COMPETENCIA_ = 'N'
    CAIXA_ = 'S'
    MANUAL = 'M'

class Tipo_cobrancaEnum(Enum):
    CONFIGURACAO_PADRAO = 'P'
    IMPRESSO = 'I'
    E_MAIL = 'E'

class Renovacao_automaticaEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Gerar_finan_assin_digital_contratoEnum(Enum):
    SIM = 'S'
    NAO = 'N'
    PADRAO = 'P'

class Agrupar_financeiro_contratoEnum(Enum):
    SIM = 'S'
    NAO = 'N'
    PADRAO = 'P'

class Aplicar_desconto_tempo_bloqueioEnum(Enum):
    SIM = 'S'
    NAO = 'N'
    PADRAO = 'P'

class Contrato_recorrenciaEnum(Enum):
    PIX_AUTOMATICO = 'PIX'
    CARTAO_DE_CREDITO = 'CREDIT'
    SEM_RECORRENCIA_ATIVA = 'N'

class Status_recorrenciaEnum(Enum):
    AGUARDANDO_APROVACAO = 'AGUARDANDO_APROVACAO'
    APROVADA = 'APROVADA'
    REJEITADA = 'REJEITADA'
    EXPIRADA = 'EXPIRADA'
    CANCELADA = 'CANCELADA'

class Base_geracao_tipo_docEnum(Enum):
    DOCUMENTO_OPCIONAL_DO_CONTRATO = 'OPC'
    DOCUMENTO_DO_PRODUTO_DO_CONTRATO = 'PROD'
    PADRAO = 'P'

class Bloqueio_automaticoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Aviso_atrasoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Desbloqueio_confiancaEnum(Enum):
    HABILITADO = 'S'
    DESABILITADO = 'N'
    PADRAO = 'P'

class Desbloqueio_confianca_ativoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Restricao_auto_desbloqueioEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Liberacao_suspensao_parcialEnum(Enum):
    HABILITADO = 'H'
    DESABILITADO = 'D'
    PADRAO = 'P'

class Utilizando_auto_libera_susp_parcEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Restricao_auto_libera_susp_parcialEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Contrato_suspensoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Origem_cancelamentoEnum(Enum):
    MANUAL = 'M'
    AUTOMATICO = 'A'

class Imp_realizadoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Imp_carteiraEnum(Enum):
    REALIZADA = 'S'
    EM_ANDAMENTO = 'N'

class Imp_importacaoEnum(Enum):
    REALIZADA = 'S'
    EM_ANDAMENTO = 'N'

class Imp_treinamentoEnum(Enum):
    REALIZADO = 'S'
    EM_ANDAMENTO = 'N'

class Imp_redeEnum(Enum):
    REALIZADA = 'S'
    EM_ANDAMENTO = 'N'

class Imp_bkpEnum(Enum):
    REALIZADO = 'S'
    EM_ANDAMENTO = 'N'

class Imp_statusEnum(Enum):
    FINALIZADA = 'F'
    EM_ANDAMENTO = 'A'

class Tipo_localidadeEnum(Enum):
    ZONA_RURAL = 'R'
    ZONA_URBANA = 'U'

class Document_photoEnum(Enum):
    SIM = 'S'
    NAO = 'N'
    PADRAO = 'P'

class Selfie_photoEnum(Enum):
    SIM = 'S'
    NAO = 'N'
    PADRAO = 'P'