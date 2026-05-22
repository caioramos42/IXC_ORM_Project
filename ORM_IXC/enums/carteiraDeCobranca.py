from enum import Enum

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
    PIX = 'Pix'

class Envia_email_ao_gerar_finanEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Envia_push_ao_gerar_finanEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class RegistradoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class AtivoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Lancamento_tarifaEnum(Enum):
    NA_DATA_DO_PAGAMENTO = 'L'
    NA_DATA_DO_CREDITO = 'C'

class Pedido_baixa_automatico_recorencia_cartaoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class EspecieEnum(Enum):
    RS = 'R$'
    USS = 'US$'
    GS = 'Gs'
    S = '$'

class Quem_distribuiEnum(Enum):
    BANCO = '1'
    EMPRESA = '2'
    BANCO_ENVIA_E_MAIL = '3'
    BANCO_ENVIA_SMS = '4'

class Endereco_envio_cobrancaEnum(Enum):
    COBRANCA = '1'
    CLIENTE = '2'

class Boleto_local_atualizaEnum(Enum):
    SISTEMA = 'S'
    SITE_DO_BANCO = 'B'

class Classe_funcoesEnum(Enum):
    BANCOOB_SICOOB = 'funcoes_bancoob'
    BANCO_DO_BRASIL = 'funcoes_bb'
    BANCO_ITAU = 'funcoes_itau'
    BANCO_BRADESCO = 'funcoes_bradesco'
    CAIXA_ECONOMICA_FEDERAL_SICOB11 = 'funcoes_caixa'
    CAIXA_ECONOMICA_FEDERAL_SIGCB = 'funcoes_caixa_sigcb'
    BANCO_SANTANDER = 'funcoes_santander'
    CARNE = 'funcoes_carne'
    SICREDI = 'funcoes_sicredi'
    CAIXA_ECONOMICA_FEDERAL_CICOB16 = 'funcoes_caixa_sicob'
    BANCO_UNICRED = 'funcoes_unicred'
    CECRED = 'funcoes_cecred'
    BANCO_BANESE = 'funcoes_banese'
    BANCO_BANPARA = 'funcoes_banpara'
    BANCO_BANRISUL = 'funcoes_banrisul'
    BANCO_DE_BRASILIA = 'funcoes_bancobrasilia'
    BANCO_HSBC = 'funcoes_hsbc'
    BANCO_DA_AMAZONIA = 'funcoes_bancoamazonia'
    BANCO_DO_NORDESTE = 'funcoes_banconordeste'
    CREDISIS = 'funcoes_credisis'
    BANCO_DO_ESPIRITO_SANTO = 'funcoes_banestes'
    BANCO_UNICRED___091 = 'funcoes_unicred_091'
    BANCO_SAFRA = 'funcoes_safra'
    BANCO_UNIPRIME = 'funcoes_uniprime'
    BANCO_UNICRED_136 = 'funcoes_unicred_136'
    CRESOL = 'funcoes_cresol'
    BANCO_UNIPRIME_084 = 'funcoes_uniprime_084'
    BANCO_CREDISAN = 'funcoes_credisan'
    BANCO_DAYCOVAL = 'funcoes_daycoval'
    BANCO_CITIBANK = 'funcoes_citibank'
    BANCO_QI_TECH = 'funcoes_qitech'
    INVOICE = 'funcoes_invoice'
    BANCO_BMP_MONEY_PLUS = 'funcoes_bmp'
    MOCAMBIQUE_LAYOUT = 'funcoes_mozambique'

class Versao_integracao_banrisulEnum(Enum):
    V1 = 'v1'
    V2 = 'v2'

class Tipo_carteiraEnum(Enum):
    SIMPLES = '1'
    VINCULADA = '2'
    CAUCIONADA = '3'
    VENDOR = '4'
    ECR = '5'

class TipoEnum(Enum):
    B = 'B'

class Utliza_numero_parcela_fixoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Pedido_baixa_automaticoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Enviar_pedido_baixa_renegociadosEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Pedido_baixa_automatico_rec_manualEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Pedido_baixa_automatico_rec_cartaoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Pedido_baixa_automatico_rec_pixEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Adiciona_remessa_auto_alt_dataEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Remessa_com_mensagemEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Validar_vencidos_remessaEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Validar_recebidos_remessaEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Validar_clientes_bloqueadosEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Validar_clientes_negativados_remessaEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class L_remessaEnum(Enum):
    CNAB_240 = 'cnab240'
    CNAB_400 = 'cnab400'

class L_retornoEnum(Enum):
    CNAB_240_SICOOB = 'cnab240_retorno_sicoob'
    CNAB_240_BANCO_DO_BRASIL = 'cnab240_retorno_bb'
    CNAB_240_CAIXA_ECONOMICA_FEDERAL = 'cnab240_retorno_caixa'
    CNAB_240_SANTANDER = 'cnab240_retorno_santander'
    CNAB_400_SICREDI = 'cnab400_retorno_sicredi'
    CNAB_400_BRADESCO = 'cnab400_retorno_bradesco'
    CNAB_400_CAIXA_ECONOMICA_FEDERAL = 'cnab400_retorno_caixa'
    CNAB_400_BANCO_DO_BRASIL = 'CBR643_bb'
    CNAB_240_CECRED = 'cnab240_retorno_cecred'
    CNAB_400_ITAU = 'cnab400_retorno_itau'
    CNAB_400_BANCOOB = 'cnab400_retorno_bancoob'
    CNAB_400_BANESE = 'cnab400_retorno_banese'
    CNAB_240_BANPARA = 'cnab240_retorno_banpara'
    CNAB_400_BANCO_DE_BRASILIA = 'cnab400_retorno_bancobrasilia'
    CNAB_240_HSBC = 'cnab240_retorno_hsbc'
    CNAB_240_BANRISUL = 'cnab240_retorno_banrisul'
    CNAB_240_ITAU = 'cnab240_retorno_itau'
    CNAB_240_BANCO_DO_NORDESTE = 'cnab240_retorno_banconordeste'
    CNAB_400_SANTANDER = 'cnab400_retorno_santander'
    CNAB_400_CREDISIS = 'cnab400_retorno_credisis'
    CNAB_400_BANCO_DO_ESPIRITO_SANTO = 'cnab400_retorno_banestes'
    CNAB_240_BANCO_DA_AMAZONIA = 'cnab240_retorno_amazonia'
    CNAB_240_CREDISIS = 'cnab240_retorno_credisis'
    CNAB_240_BRADESCO = 'cnab240_retorno_bradesco'
    CNAB_240_UNICRED = 'cnab240_retorno_unicred'
    CNAB_400_BANCO_DO_NORDESTE = 'cnab400_retorno_banconordeste'
    CNAB_240_BANCO_SAFRA = 'cnab240_retorno_safra'
    CNAB_400_UNIPRIME = 'cnab400_retorno_uniprime'
    CNAB_240_BANESE = 'cnab240_retorno_banese'
    CNAB_400_UNICRED = 'cnab400_retorno_unicred'
    ARRECADACAO_RECEBIMENTO = 'arrecadacao_recebimento'
    CNAB_400_CREDISAN = 'cnab400_retorno_credisan'
    CNAB_400_DAYCOVAL = 'cnab400_retorno_daycoval'
    CNAB_400_CRESOL = 'cnab400_retorno_cresol'
    CNAB_400_CITIBANK = 'cnab400_retorno_citibank'
    CNAB_400_QI_TECH = 'cnab400_retorno_qitech'
    CNAB_400_BMP = 'cnab400_retorno_bmp'
    CNAB_240_SICREDI = 'cnab240_retorno_sicredi'

class Contabiliza_retorno_filial_emissaoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Filtra_inicio_nnEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Baixa_automaticaEnum(Enum):
    SIM = 'S'
    NAO = 'N'
    USAR_PERFIL_DO_BENEFICIARIO = 'C'

class Utilizar_baixa_apos_vencimentoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Gateway_nomeEnum(Enum):
    EFI = 'fortunus'
    WIDEPAY = 'widepay'
    JUNO_ = 'boleto_facil'
    CREDISIS = 'credi_sis'
    CEL_PAYMENTS = 'galaxPay'
    SICOOB_API = 'sicoobApi'
    SICREDI_API = 'sicrediApi'
    BANCO_DO_BRASIL = 'bb_api'
    IUGU = 'iugu'
    SANTANDER = 'santander'
    LYTEX = 'lytex'
    ASAAS = 'asaas'
    BTG_PACTUAL = 'btg'
    BRADESCO = 'bradesco'

class Versao_apiEnum(Enum):
    V1 = 'v1'
    V2 = 'v2'
    V3 = 'v3'

class Importado_gatewayEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Nova_apiEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Ambiente_homologacao_gatewayEnum(Enum):
    HOMOLOGACAO = 'S'
    PRODUCAO = 'N'

class Utiliza_carneEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Nova_int_fortunusEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Gateway_tipo_impressaoEnum(Enum):
    CARNE = 'CAR'
    FATURA = 'FAT'
    IMPORTACAO = 'IMP'

class Adiciona_obs_descricaoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Adiciona_venc_descricaoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Envia_email_gerenciaEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Use_webhook_url_callbackEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Recebimento_parcial_gatewayEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Finalizar_cob_bfEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Gera_pix_gatewayEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Enviar_cobranca_pix_whatsappEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Tipo_chave_pixEnum(Enum):
    CPF_CNPJ = 'CPF_CNPJ'
    CELULAR = 'CELULAR'
    E_MAIL = 'EMAIL'
    ALEATORIA = 'ALEATORIA'
    COPIA_E_COLA = 'COPIA_E_COLA'

class Lanca_tarifa_gatewayEnum(Enum):
    NAO_LANCA = 'N'
    NA_IMPRESSAO = 'I'
    NO_RECEBIMENTO = 'R'

class Lanca_tarifa_pixEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class TimeoutEnum(Enum):
    T30 = '30'
    T60 = '60'

class Creditcard_gatewayEnum(Enum):
    BIN = 'BI'
    CIELO_3 = 'C3'
    YAPAY = 'YA'
    EFI = 'GN'
    CEL_PAYMENTS = 'GP'
    VINDI = 'VD'
    IUGU = 'IG'
    ASAAS = 'AS'
    MODOBANK = 'MB'

class CreditCard_ambienteEnum(Enum):
    HOMOLOGACAO = 'H'
    PRODUCAO = 'P'
    TESTE = 'T'

class Versao_api_cartaoEnum(Enum):
    V1 = 'v1'
    V2 = 'v2'
    V3 = 'v3'

class Habilitar_recorrencia_cartaoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class TimeoutCreditCardEnum(Enum):
    T60 = '60'
    T30 = '30'

class CreditCard_localEnum(Enum):
    BUY_PAGE_LOJA = 'L'
    BUY_PAGE_CIELO = 'C'

class CreditCard_autorizarEnum(Enum):
    AUTORIZAR_DIRETO = '3'
    AUTORIZAR_TRANSACAO_AUTENTICADA_E_NAO_AUTENTICADA = '2'
    SOMENTE_AUTENTICAR_A_TRANSACAO = '0'
    AUTORIZAR_TRANSACAO_SOMENTE_SE_AUTENTICADA = '1'

class CreditCard_parcelamentoEnum(Enum):
    LOJA = 'L'
    ADMINISTRADORA = 'C'

class Credit_card_repassar_taxaEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Credit_card_taxa_em_pagamentosEnum(Enum):
    INDIVIDUAIS = 'I'
    RECORRENTES = 'R'
    AMBOS = 'A'

class Debito_classeEnum(Enum):
    DEBITO_AUTOMATICO_V04 = 'debito_automatico_V04'
    DEBITO_AUTOMATICO_V05 = 'debito_automatico_V05'
    DEBITO_AUTOMATICO_SIACC = 'debito_automatico_siacc'
    DEBITO_AUTOMATICO_ITAU_240_V04 = 'debito_automatico_itau_240_V04'

class Validar_vencidos_remessa_DEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Pix_gatewayEnum(Enum):
    EFI = 'GN'
    MODOBANK = 'MB'
    SICOOB = 'SB'

class Pix_ambienteEnum(Enum):
    HOMOLOGACAO = 'H'
    PRODUCAO = 'P'

class Pix_modalidadeEnum(Enum):
    IMEDIATA = 'I'
    COBRANCA = 'C'

class Permite_pagamento_por_chave_pixEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Enviar_cobranca_pix_whatsapp_carteiras_pixEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Tipo_chave_pix_carteiras_pixEnum(Enum):
    CPF_CNPJ = 'CPF_CNPJ'
    CELULAR = 'CELULAR'
    E_MAIL = 'EMAIL'
    ALEATORIA = 'ALEATORIA'

class Utiliza_pix_recorrenteEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Permite_retentativas_pix_recorrenteEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Lanca_tarifa_pix_modobankEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Calcular_jurosEnum(Enum):
    ATE_O_DIA_ATUAL = 'D'
    ATE_O_NOVO_VENCIMENTO = 'V'

class Obs_fn_areceberEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class L_impressaoEnum(Enum):
    POR_PAGINA_3 = 'boleto_mini'
    PAGINA_2 = 'boleto_dois_por_pagina'
    PAGINA_1 = 'boleto_um_por_pagina'
    BOLETO_NF = 'boleto_nf_vinteum'
    CARNE_ = 'carne_simples'
    BOLETO_FATURA_DETALHADA = 'boleto_fatura_d'
    CARNE_DETALHADO_ = 'carne_detalhado'
    FATURA_DETALHADA_BOLETO_NF = 'fatura_detalhada_boleto_nf'
    PAGINA_3_COM_MARGEM_MENOR = 'boleto_mini_margem_menor'
    PAGINA_4 = 'quatro_por_pagina'
    BOLETO_NF_VARIOS_PRODUTOS = 'boleto_nf_vinteum'
    BOLETO_FATURA_DETALHADA_COM_CONSUMO = 'boleto_fatura_d_consumo'
    DETALHAMENTO_COM_BOLETO = 'detalhamentoBoleto'
    EXTRATO_FECHADO = 'extratoFechado'
    BOLETO_FATURA_DETALHADA_PIX_COBRANCA = 'boleto_faturad_modobank'
    INVOICE = 'invoice'
    FATURA_PERSONALIZADA_BOLETO_PIX_COBRANCA = 'personalizada_boleto_modobank'
    PAGINA_3_PIX_COBRANCA = 'tres_pagina_modobank'
    FATURA_PERSONALIZADA_PIX_COBRANCA = 'personalizada_modobank'
    PAGINA_3_PERSONALIZAVEL_PIX_COBRANCA = 'tres_pagina_personalizada_modobank'
    BOLETO_NF_PIX_COBRANCA = 'boleto_nf_modobank'
    BOLETO_FATURA_DETALHADA_COM_CONSUMO_PIX_COBRANCA = 'boleto_fatura_d_consumo_modobank'
    FATURA_PIX_COBRANCA_NF = 'modobank_nf'
    FATURA_DETALHADA = 'mocambique_billet'

class Formato_detalhamento_faturaEnum(Enum):
    PLANO = 'plano'
    PRODUTO = 'produto'

class Imprimir_filial_vendaEnum(Enum):
    VENDA = 'S'
    CONTA = 'N'

class Imprimir_filial_contaEnum(Enum):
    VENDA = 'N'
    CONTA = 'S'

class Considerar_modelo_nao_fiscalEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Imprime_endereco_boletoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Imprime_fone_fatura_dEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Imp_nome_sacador_avalistaEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Imprime_prod_val_zeroEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Imprime_tipo_resolucao_anatelEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Mask_cpf_cnpj_impressao_boletoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Mostra_cep_beneficiario_impressaoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Agrupar_produtos_por_descricaoEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Imprimir_beneficiario_gatewayEnum(Enum):
    RAZAO_SOCIAL = 'C'
    GATEWAY = 'G'
    RAZAO_SOCIAL_GATEWAY = 'A'
    NOME_FANTASIA = 'N'
    NOME_FANTASIA_GATEWAY = 'F'

class Imp_nome_beneficiarioEnum(Enum):
    RAZAO_SOCIAL = 'R'
    NOME_FANTASIA = 'F'

class Imp_nome_beneficiario_reciboEnum(Enum):
    RAZAO_SOCIAL = 'R'
    NOME_FANTASIA = 'F'

class Boletos_capa_contratosEnum(Enum):
    SIM = 'S'
    NAO = 'N'

class Boleto_capa_localEnum(Enum):
    NO_INICIO = 'I'
    NO_FIM = 'F'

class Tipo_baixaEnum(Enum):
    DESCONTO = 'D'
    INCLUIR_NA_PROXIMA_FATURA_ = 'P'
    BAIXA_PARCIAL = 'B'

class Validar_juros_multaEnum(Enum):
    SIM = 'S'
    NAO = 'N'
