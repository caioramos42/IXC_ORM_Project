from enum import Enum


class SituacaoEnum(Enum):
    COMODATO = '4'
    VENDIDO = '3'
    DISPONIVEL = '1'
    INUTILIZADO = '5'
    ALOCADO = '6'
    DISPONIVEL_TECNICO = '7'
    INDISPONIVEL = '8'

class EstadoEnum(Enum):
    BOM = '1'
    RUIM = '2'
    MEDIO = '3'
    TROCAR = '4'

class Em_laboratorioEnum(Enum):
    SIM = '1'
    NAO = '2'

class Aguardando_instalacaoEnum(Enum):
    SIM = '1'
    NAO = '2'

class Finalidade_indisponivelEnum(Enum):
    ENTRADA = 'E'
    VENDA = 'V'
    PEDIDO_DE_OS = 'OS'
    TRANSF_ENTRE_ALMOXARIFADOS = 'TA'
    TRANSF_COM_CONFIRMACAO = 'TM'
    REQUISICAO_DE_MATERIAL = 'RE'

