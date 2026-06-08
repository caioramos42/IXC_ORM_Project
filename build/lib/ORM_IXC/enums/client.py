from enum import Enum


#-------------------------------- ENUMERADORES --------------------------------#
class AtivoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Tipo_cliente_scmEnum(Enum):
    COMERCIAL = '01'
    INDUSTRIAL = '02'
    RESIDENCIAL_PESSOA_FISICA = '03'
    PRODUTOR_RURAL = '04'
    ORGAO_DA_ADMINISTRACAO_PUBLICA_ESTADUAL_DIRETA_E_SUAS_FUNDACOES_E_AUTARQUIAS_QUANDO_MANTIDAS_PELO_PODER_PUBLICO_ESTADUAL_E_REGIDAS_POR_NORMAS_DE_DIREITO_PUBLICO_TERMOS_DO_CONVENIO_ICMS_107_95 = '05'
    PRESTADOR_DE_SERVICO_DE_TELECOMUNICACAO_RESPONSAVEL_PELO_RECOLHIMENTO_DO_IMPOSTO_INCIDENTE_SOBRE_A_CESSAO_DOS_MEIOS_DE_REDE_DO_PRESTADOR_DO_SERVICO_AO_USUARIO_FINAL_TERMOS_DO_CONVENIO_ICMS_17_13 = '06'
    MISSOES_DIPLOMATICAS_REPARTICOES_CONSULARES_E_ORGANISMOS_INTERNACIONAIS_NOS_TERMOS_DO_CONVENIO_ICMS_158_94 = '07'
    IGREJAS_E_TEMPLOS_DE_QUALQUER_NATUREZA = '08'
    OUTROS_NAO_ESPECIFICADOS_ANTERIORMENTE = '99'
    GRANDE_CONTRIBUINTE = '0-13'
    AUTO_RETENTOR = '0-15'
    AGENTE_DE_RETENCAO_IVA = '0-23'
    REGIME_SIMPLES_DE_TRIBUTACAO = '0-47'
    OUTROS = 'R-99-PN'

class Tipo_ente_governamentalEnum(Enum):
    UNIAO = '1'
    ESTADO = '2'
    DISTRITO_FEDERAL = '3'
    MUNICIPIO = '4'

class Tipo_pessoaEnum(Enum):
    FISICA = 'F'
    JURIDICA = 'J'
    ESTRANGEIRO = 'E'
    JURIDICA2 = '1'
    NATURAL = '2'
    ESTRANGEIRO2 = '3'

class Regime_fiscal_colEnum(Enum):
    RESPONSABLE_DE_IVA = '48'
    NO_RESPONSABLE_DE_IVA = '49'

class Tipo_documento_identificacaoEnum(Enum):
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
    REGISTRO_UNICO_DE_CONTRIBUYENTES = 'RUC'
    CEDULA_DE_IDENTIDAD = 'CI'
    CARTAO_DE_RESIDENCIA = '4'
    INNOMINADO = '5'
    CARTAO_DE_ISENCAO_DE_IMPOSTO_DIPLOMATICO = '6'
    OUTRO = '9'
    CUIT = 'CUIT'
    CARNET_DE_IDENTIDAD = 'CIBOL'
    ROL_UNICO_TRIBUTARIO = 'RUT'
    TAX_IDENTIFICATION_NUMBER = 'TIN'
    REGISTRO_DE_INFORMACION_FISCAL_ = 'RIF'
    DOCUMENTO_NACIONAL_DE_INDENTIDAD = 'DNI'
    NUMERO_DE_SECURITE_SOCIALE = 'NIR'
    SYSTEME_D_IDENTIFICATION_DU_REPERTOIRE_DES_ENTREPRISES = 'SIREN'
    REGISTRO_UNICO_DE_TRIBUTARIO = 'RUTURU'

class Contribuinte_icmsEnum(Enum):
    SIM = 'S'
    NAO = 'N'
    ISENTO = 'I'
    EXCLUIDO = 'E'

class SexoEnum(Enum):
    FEMININO = 'F'
    MASCULINO = 'M'
    NAO_BINARIO = 'NB'
    OUTRO = 'O'
    PREFIRO_NAO_DIZER = 'PNI'

class Estado_civilEnum(Enum):
    CASADO = 'Casado'
    SOLTEIRO = 'Solteiro'
    DIVORCIADO = 'Divorciado'
    VIUVO = 'Viúvo'

class Tipo_assinanteEnum(Enum):
    COMERCIAL_INDUSTRIAL = '1'
    PODER_PUBLICO = '2'
    RESIDENCIAL_PESSOA_FISICA = '3'
    PUBLICO = '4'
    SEMI_PUBLICO = '5'
    OUTROS = '6'

class Filtra_filialEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Ativo_serasaEnum(Enum):
    SIM = '1'
    NAO = '2'
    INDEFINIDO = '0'

class Convert_cliente_fornEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Grau_satisfacaoEnum(Enum):
    NADA_SATISFEITO = '1'
    POUCO_SATISFEITO = '2'
    SATISFEITO = '3'
    MUITO_SATISFEITO = '4'
    COMPLETAMENTE_SATISFEITO = '5'

class MoradiaEnum(Enum):
    PROPRIA = 'P'
    ALUGADA = 'A'

class Tipo_localidadeEnum(Enum):
    ZONA_RURAL = 'R'
    ZONA_URBANA = 'U'

class Acesso_automatico_centralEnum(Enum):
    SIM = 'S'
    NAO = 'N'
    PADRAO = 'P'

class Alterar_senha_primeiro_acessoEnum(Enum):
    SIM = 'S'
    NAO = 'N'
    PADRAO = 'P'

class Senha_hotsite_md5Enum(Enum):
    SIM = 'S'
    NAO = 'N'

class CrmEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Cadastrado_via_viabilidadeEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Status_prospeccaoEnum(Enum):
    NOVO = 'C'
    SONDAGEM = 'S'
    APRESENTANDO = 'A'
    NEGOCIANDO = 'N'
    VENCEMOS = 'V'
    PERDEMOS = 'P'
    ABORTAMOS = 'AB'
    SEM_VIABILIDADE = 'SV'
    SEM_PORTA_DISPONIVEL = 'SP'

class Participa_pre_cobrancaEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Cob_envia_emailEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Cob_envia_smsEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Tipo_pessoa_titular_contaEnum(Enum):
    FISICA = 'F'
    JURIDICA = 'J'

class Regua_cobranca_consideraEnum(Enum):
    SIM = 'S'
    NAO = 'N'
    PADRAO = 'P'

class Regua_cobranca_wppEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Regua_cobranca_notificacaoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Orgao_publicoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Iss_classificacao_padraoEnum(Enum):
    NORMAL = '00'
    RETIDO = '01'
    SUBSTITUTA = '02'
    ISENTO = '03'
    PADRAO = '99'

class Desconto_irrf_valor_inferiorEnum(Enum):
    SIM = 'S'
    NAO = 'N'