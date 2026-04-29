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

class Status_conexaoEnum(Enum):
	ONLINE = 'S'
	OFFLINE = 'N'

class PrioridadeEnum(Enum):
	BAIXA = 'B'
	NORMAL = 'N'
	ALTA = 'A'
	CRITICA = 'C'

class Melhor_horario_agendaEnum(Enum):
	MANHA = 'M'
	TARDE = 'T'
	NOITE = 'N'
	QUALQUER = 'Q'

class Status_pesquisa_satisfacaoEnum(Enum):
	ENVIADO = '1'
	RESPONDIDA = '2'
	EXPIRADA = '3'

class StatusEnum(Enum):
	ABERTA = 'A'
	ANALISE = 'AN'
	ENCAMINHADA = 'EN'
	ASSUMIDA = 'AS'
	AGENDADA = 'AG'
	DESLOCAMENTO = 'DS'
	EXECUCAO = 'EX'
	FINALIZADA = 'F'
	AGUARDANDO_AGENDAMENTO = 'RAG'

class Status_assinaturaEnum(Enum):
	PENDENTE = 'A'
	ASSINADA = 'F'

class Gera_comissaoEnum(Enum):
	SIM = 'S'
	NAO = 'N'

class LiberadoEnum(Enum):
	SIM = '1'
	NAO = '2'

class ImpressoEnum(Enum):
	SIM = 'S'
	NAO = 'N'

class Origem_cadastroEnum(Enum):
	P = 'P'
	SV = 'SV'

class Origem_os_abertaEnum(Enum):
	MANUAL = 'M'
	PROCESSO = 'P'
	COBRANCA = 'CRM'
	CANCELAMENTO_DE_CONTRATO = 'CC'