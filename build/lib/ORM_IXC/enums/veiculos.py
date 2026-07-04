from enum import Enum


class StatusEnum(Enum):
    SIM = 'A'
    NAO = 'I'

class Placa_tipoEnum(Enum):
    SIM = 'MERCOSUL'
    NAO = 'PADRAO'

class Categoria_veiculoEnum(Enum):
    MOTO = 'MOTO'
    CARRO = 'CARRO'
    CAMINHAO = 'CAMINHAO'

class Caminhao_qtde_eixosEnum(Enum):
    EIXOS_2 = '2'
    EIXOS_3 = '3'
    EIXOS_4 = '4'
    EIXOS_5 = '5'
    EIXOS_6 = '7'
    EIXOS_7 = '9'

class Combustivel_tipoEnum(Enum):
    GAS = 'GAS'
    ALCOOL = 'ALCOOL'
    GASOLINA = 'GASOLINA'
    DIESEL = 'DIESEL'
    ELETRICO = 'ELETRICO'
    HIBRIDO = 'HIBRIDO'

class Tipo_rodadoEnum(Enum):
    TRUCK = '01'
    TOCO = '02'
    CAVALO_MECANICO = '03'
    VAN = '04'
    UTILITARIO = '05'
    OUTROS = '06'

class Tipo_carroceriaEnum(Enum):
    NAO_APLICAVEL = '00'
    ABERTA = '01'
    FECHADA_BAU = '02'
    GRANELERA = '03'
    PORTA_CONTAINER = '04'
    SIDER = '05'

class Centro_custo_regra_rateioEnum(Enum):
    CENTRO_DE_CUSTOS = 'CE'
    CRITERIO_DE_RATEIO = 'CR'

class Status_veiculosEnum(Enum):
    DESCONECTADO = 'off'
    CONECTADO = 'on'

