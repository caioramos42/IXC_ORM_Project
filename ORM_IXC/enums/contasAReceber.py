from enum import Enum

class PrevisaoEnum(Enum):
    COMPETENCIA_ = 'N'
    CAIXA_ = 'S'
    MANUAL = 'M'

class Tipo_recebimentoEnum(Enum):
    BOLETO = 'Boleto'
    CHEQUE = 'Cheque'
    CARTAO_DE_CREDITO = 'CartA£o'
    DINHEIRO = 'Dinheiro'
    DEPOSITO = 'DepA³sito'
    GATEWAY = 'Gateway'
    DEBITO_EM_CONTA = 'DA©bito'
    FATURA = 'Fatura'
    ARRECADACAO_RECEBIMENTO = 'ArrecadacaoRecebimento'
    TRANSFERENCIA = 'Transferencia'
    PIX = 'Pix'

class StatusEnum(Enum):
    A_RECEBER = 'A'
    RECEBIDO = 'R'
    PARCIAL = 'P'
    CANCELADO = 'C'

class ImpressoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Arquivo_remessa_baixadoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Forma_recebimentoEnum(Enum):
    RECEBIDO_DE_FORMA_MANUAL = 'M'
    RECEBIDO_AUTOMATICAMENTE = 'R'

class Tipo_cobrancaEnum(Enum):
    PADRAO = 'P'
    IMPRESSO = 'I'
    E_MAIL = 'E'

class Titulo_protestadoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Titulo_renegociadoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Etapa_envio_reguaEnum(Enum):
    LEMBRETE_DE_PAGAMENTO = 'LP'
    NO_VENCIMENTO = 'CV'
    AVISO_DE_COBRANCA = 'AC'
    INFORMATIVO_DE_PENDENCIA = 'IP'
    AGENDAR_PAGAMENTO = 'AP'
    COBRANCA_AUTOMATICA_E_PRESENCIAL = 'CAP'
    NEGATIVAR_CLIENTES = 'NC'
    RECEBIMENTO_DE_CONTAS_A_RECEBER = 'RCA'
    CANCELAMENTO_DE_CONTAS_A_RECEBER = 'CCA'
    RENEGOCIACAO_DE_CONTAS_A_RECEBER = 'RCB'
    REMOVER_NEGATIVACOES = 'RN'

class Status_cobranca_reguaEnum(Enum):
    ABERTA = 'A'
    FINALIZADA = 'F'

class Em_cobrancaEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Titulo_importadoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Aguardando_confirmacao_pagamentoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Parcelado_cartaoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Recebido_via_pixEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Recebido_por_recorrenciaEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class EstornadoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Motivo_alteracaoEnum(Enum):
    CANCELAMENTO_DE_DESCONTO = '08'
    DISPENSAR_COBRANCA_DE_MULTA = '15'
    ALTERACAO_DO_VALOR_DE_DESCONTO = '16'
    NAO_CONCEDER_DESCONTO = '17'
    PROTESTO_PARA_FINS_FALIMENTARES = '03'
    CONCESSAO_DE_ABATIMENTO = '04'
    CANCELAMENTO_DE_ABATIMENTO = '05'
    ALTERACAO_DE_VENCIMENTO = '06'
    CONCESSAO_DE_DESCONTO = '07'
    PROTESTAR = '09'
    SUSTAR_PROTESTO_E_BAIXAR_TITULO = '10'
    SUSTAR_PROTESTO_E_MANTER_EM_CARTEIRA = '11'
    ALTERACAO_DE_JUROS_DE_MORA = '12'
    DISPENSAR_COBRANCA_DE_JUROS_DE_MORA = '13'
    ALTERACAO_DE_VALOR_PERCENTUAL_DE_MULTA = '14'
    ALTERACAO_DO_VALOR_DE_ABATIMENTO = '18'
    PRAZO_LIMITE_DE_RECEBIMENTO_ALTERAR = '19'
    PRAZO_LIMITE_DE_RECEBIMENTO_DISPENSAR = '20'
    ALTERAR_NUMERO_DO_TITULO_DADO_PELO_BENEFICIARIO_21 = '21'
    ALTERAR_NUMERO_DO_TITULO_DADO_PELO_BENEFICIARIO_22= '22'
    ALTERAR_DADOS_DO_PAGADOR = '23'
    ALTERAR_DADOS_DO_SACADOR_AVALISTA = '24'
    RECUSA_DA_ALEGACAO_DO_PAGADOR = '30'
    ALTERACAO_DE_OUTROS_DADOS = '31'
    ALTERACAO_DOS_DADOS_DO_RATEIO_DE_CREDITO = '33'
    PEDIDO_DE_CANCELAMENTO_DOS_DADOS_DO_RATEIO_DE_CREDITO = '34'
    PEDIDO_DE_DESAGENDAMENTO_DO_DEBITO_AUTOMATICO = '35'
    ALTERACAO_DE_CARTEIRA = '40'
    CANCELAR_PROTESTO = '41'
    ALTERACAO_DE_ESPECIE_DE_TITULO = '42'
    TRANSFERENCIA_DE_CARTEIRA_MODALIDADE_DE_COBRANCA = '43'
    ALTERACAO_DE_CONTRATO_DE_COBRANCA = '44'
    NEGATIVACAO_SEM_PROTESTO = '45'
    SOLICITACAO_DE_BAIXA_DE_TITULO_NEGATIVADO_SEM_PROTESTO = '46'
    ALTERACAO_DE_DADOS_EXTRAS_MULTA = '49'

class Tipo_cobranca_pixEnum(Enum):
    COM_VENCIMENTO = 'COM_VENCIMENTO'
    IMEDIATA = 'IMEDIATA'

class Pix_status_recorrenteEnum(Enum):
    CRIADO = 'CRIADA'
    ATIVO = 'ATIVA'
    CONCLUIDO = 'CONCLUIDA'
    EXPIRADO = 'EXPIRADA'
    REJEITADO = 'REJEITADA'
    CANCELADO = 'CANCELADA'

class Libera_periodoEnum(Enum):
    SIM = 'S'
    NAO = 'N'