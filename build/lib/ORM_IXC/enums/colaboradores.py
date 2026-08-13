from enum import Enum


class AtivoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Ctps_selecionaEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Cpf_selecionaEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Tipo_documento_identificacao_colEnum(Enum):
    REGISTRO_CIVIL = '11'
    TARJETA_DE_IDENTIDAD = '12'
    CEDULA_DE_CIUDADANIA = '13'
    TARJETA_DE_EXTRANJERIA = '21'
    CEDULA_DE_EXTRANJERIA = '22'
    NIT = '31'
    PASAPORTE = '41'
    DOCUMENTO_DE_IDENTIFICACION_EXTRANJERO = '42'
    PEP = '47'
    NIT_DE_OTRO_PAIS = '50'
    NUIP = '91'
    NUIT = 'NUIT'
    REGISTRO_UNICO_CONTRIBUINTE = 'RUC'
    CEDULA_DE_IDENTIDIADE = 'CI'

class Pis_selecionaEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Rg_selecionaEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Cnh_selecionaEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Titulo_eleitoral_selecionaEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Mostrar_no_quadro_kanbanEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Exibir_colaborador_inmapEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Rastreador_tipoEnum(Enum):
    EXTERNO = 'S'
    INMAP_SERVICE = 'N'

class Obrigar_marcar_quilometragemEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Estado_civilEnum(Enum):
    SOLTEIRO = 'S'
    CASADO = 'C'
    UNIAO_ESTAVEL = 'UE'
    DIVORCIADO = 'D'
    VIUVO = 'V'
    SEPARADO = 'SE'

class Cor_racaEnum(Enum):
    AMARELO = 'A'
    BRANCO = 'B'
    INDIGENA = 'I'
    PARDO = 'P'
    NEGRO = 'N'
    OUTRO = 'O'
    RROM = 'N'
    RAIZAL_DO_ARQUIPELAGO = 'A'
    PALENQUERO = 'B'
    NEGRO_MULATO_AFROCOLOMBIANO_OU_AFRODESCENDENTE = 'P'
    NENHUM_GRUPO_ETNICO = 'O'

class CamisetaEnum(Enum):
    P = 'P'
    PP = 'PP'
    M = 'M'
    G = 'G'
    GG = 'GG'
    O = 'O'
    XS = 'PP'
    S = 'P'
    L = 'G'
    XL = 'GG'
    XL2_OU_MAIOR = 'O'

class Possui_deficienciaEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Tipo_deficienciaEnum(Enum):
    FISICA = 'F'
    AUDITIVA = 'A'
    VISUAL = 'V'
    MENTAL = 'M'
    MULTIPLO_REABILITADO = 'MR'
    INTELECTUAL = 'I'
    PSICOSOCIAL = 'P'
    SENSORIAL = 'S'

class Grau_escolaridadeEnum(Enum):
    ENSINO_FUNDAMENTAL = 'EF'
    ENSINO_MEDIO = 'EM'
    ENSINO_SUPERIOR = 'ES'
    POS_GRADUACAO = 'PG'
    MESTRADO = 'M'
    DOUTORADO = 'D'
    EDUCACAO_INFANTIL = 'D'
    EDUCACAO_PROFISSIONAL_E_TECNOLOGICA_ = 'ES'
    GRADUACAO = 'M'

class Estagio_escolaridadeEnum(Enum):
    COMPLETO = 'C'
    CURSANDO = 'CR'
    INCOMPLETO = 'I'

class Periodo_escolaridadeEnum(Enum):
    MATUTINO = 'M'
    VESPERTINO = 'V'
    NOTURNO = 'N'

class Tipo_chave_pixEnum(Enum):
    CPF_CNPJ = 'cpf_cnpj'
    CELULAR = 'celular'
    E_MAIL = 'email'
    ALEATORIA = 'aleatoria'
    CODIGO_COPIA_E_COLA = 'codigo_copia_cola'

class Tipo_recebimentoEnum(Enum):
    CHEQUE = 'C'
    TRANSFERENCIA = 'B'
    DINHEIRO = 'D'
    PIX = 'P'

class Camara_centralizadoraEnum(Enum):
    TED_ = '018'
    DOC_ = '700'

class Regra_centro_rateioEnum(Enum):
    CENTRO_DE_CUSTO = 'CE'
    CRITERIO_DE_RATEIO = 'CR'

class Envia_email_osEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Envia_sms_osEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Integracao_calendarioEnum(Enum):
    SIM = 'S'
    NAO = 'N'

