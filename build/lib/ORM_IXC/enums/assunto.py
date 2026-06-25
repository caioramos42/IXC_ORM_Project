from enum import Enum


class AtivoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class TipoEnum(Enum):
    CLIENTE = 'C'
    ESTRUTURA = 'E'
    AMBOS = 'A'

class FinalidadeEnum(Enum):
    ORDEM_DE_SERVICO = 'OS'
    ATENDIMENTO = 'AT'
    AMBOS = 'AM'

class Endereco_padraoEnum(Enum):
    CLIENTE = 'C'
    LOGIN = 'L'
    CONTRATO = 'CC'
    MANUAL = 'M'
    ESTRUTURA = 'E'

class Mostra_hotsiteEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Prioridade_padraoEnum(Enum):
    BAIXA = 'B'
    NORMAL = 'N'
    ALTA = 'A'
    CRITICA = 'C'

class Contrato_obrigatorioEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Login_obrigatorioEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Card_data_reservadaEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Obrigar_processo_atendimentoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Obrigar_preenchimento_canal_atendimentoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Obrigatorio_status_complementarEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Layout_impressaoEnum(Enum):
    ASSISTENCIA_DE_INTERNET_RADIO = '1'
    ASSISTENCIA_DE_INTERNET_FIBRA_OPTICA = '2'
    INSTALACAO_DE_INTERNET_RADIO = '3'
    INSTALACAO_DE_INTERNET_FIBRA_OPTICA = '4'
    SERVICO_DE_MANUTENCAO = '5'
    CHAMADO_TECNICO = '6'
    OS_SIMPLES = '7'
    OS_SIMPLES___MODELO_2 = '8'
    ASSISTENCIA___MODELO_2 = '9'
    OS_INSTALACAO___MODELO_2 = '10'
    INSTALACAO_DE_INTERNET_RADIO___MODELO_2 = '11'
    ORDEM_DE_SERVICO_FIBRA = '12'

class Habilita_assinatura_clienteEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Integracao_assinatura_digitalEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Permite_abrir_cliente_atrasoEnum(Enum):
    SIM = 'S'
    NAO = 'N'
    PADRAO = 'P'

class Validar_choque_horarios_agendamento_osEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Exige_fotos_finalizacao_osEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Exige_comodato_finalizar_osEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Exige_produto_finalizar_osEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Diagnostico_obrigatorio_finalizacao_osEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Localizacao_obrigatoria_cliente_finalizacao_osEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Localizacao_obrigatoria_login_finalizacao_osEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Fat_somente_finalizadaEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Tipo_comissaoEnum(Enum):
    FIXA = 'F'
    POR_HORA = 'H'

class Equipe_obrigatoria_finalizacao_osEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Sla_apenas_dias_uteisEnum(Enum):
    SIM = 'S'
    NAO = 'N'
    PADRAO = 'P'

class Considerar_slaEnum(Enum):
    ABERTURA = 'AB'
    AGENDAMENTO = 'AG'

class Wiz_comodatoEnum(Enum):
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Wiz_produtosEnum(Enum):
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Wiz_mensalidadeEnum(Enum):
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Wiz_autorizar_ONUEnum(Enum):
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Wiz_localizacaoEnum(Enum):
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Wiz_arquivosEnum(Enum):
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Wiz_resumo_osEnum(Enum):
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Wiz_servicoEnum(Enum):
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Mostrar_no_serviceEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Conceder_desconto_login_regiao_manutencaoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Mostrar_checklist_analise_riscoEnum(Enum):
    NO_INICIO_DA_OS = 'i'
    NO_FIM_DA_OS = 'F'
    NAO_MOSTRAR = 'N'

class Wiz_service_mobile_adicionaisEnum(Enum):
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Wiz_service_mobile_onuEnum(Enum):
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Wiz_service_mobile_config_dispositivoEnum(Enum):
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Wiz_service_mobile_locEnum(Enum):
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Wiz_service_mobile_anexosEnum(Enum):
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Wiz_service_mobile_checklistEnum(Enum):
    MOSTRAR = 'M'
    ESCONDER = 'E'

class Wiz_service_mobile_enviar_sms_deslocamentoEnum(Enum):
    NAO_NOTIFICAR = 'N'
    POR_SMS = 'S'
    WHATSAPP_ = 'O'

