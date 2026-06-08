from enum import Enum

class TipoEnum(Enum):
    CLIENTE = 'C'
    ESTRUTURA_PROPRIA = 'E'

class Origem_enderecoEnum(Enum):
    CLIENTE = 'C'
    LOGIN = 'L'
    CONTRATO = 'CC'
    MANUAL = 'M'

class Origem_endereco_estruturaEnum(Enum):
    ESTRUTURA = 'E'
    MANUAL = 'M'

class PrioridadeEnum(Enum):
    BAIXA = 'B'
    NORMAL = 'M'
    ALTA = 'A'
    CRITICA = 'C'

class Melhor_horario_reservaEnum(Enum):
    MANHA = 'M'
    TARDE = 'T'
    NOITE = 'N'
    QUALQUER = 'Q'

class Id_ticket_origemEnum(Enum):
    INTERNA = 'I'
    HOTSITE = 'H'

class Interacao_pendenteEnum(Enum):
    EXTERNA = 'E'
    INTERNA = 'I'
    NENHUMA = 'N'
    AMBOS = 'A'

class Su_statusEnum(Enum):
    NOVO = 'N'
    PENDENTE = 'P'
    EM_PROGRESSO = 'EP'
    SOLUCIONADO = 'S'
    CANCELADO = 'C'