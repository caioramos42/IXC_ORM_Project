from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Optional
from ORM_IXC.enums.carteiraDeCobranca import *
from ORM_IXC.interfaces import IModel, IModelWithId


@dataclass(kw_only=True)
class CarteiraDeCobrancaModel(IModelWithId):
    id_autoincrement: int
    descricao: str
    id_conta: int
    remover_fundo_capa_carteira: str
    tipo_recebimento: Tipo_recebimentoEnum = Tipo_recebimentoEnum.BOLETO
    envia_email_ao_gerar_finan: Optional[Envia_email_ao_gerar_finanEnum] = Envia_email_ao_gerar_finanEnum.NAO
    envia_push_ao_gerar_finan: Optional[Envia_push_ao_gerar_finanEnum] = Envia_push_ao_gerar_finanEnum.NAO
    imprime_ligacoes_voip: Optional[str] = ''
    registrado: RegistradoEnum = RegistradoEnum.SIM
    ativo: AtivoEnum = AtivoEnum.SIM
    filial_id: Optional[int] = None
    id_config_alt_pagamento: Optional[int] = None
    planejamento_tarifa: Optional[int] = None
    lancamento_tarifa: Lancamento_tarifaEnum = Lancamento_tarifaEnum.NA_DATA_DO_PAGAMENTO
    reseller_authorization_code: Optional[str] = ''
    dias_vencimento_fatura: Optional[str] = ''
    carteira_padrao_fatura: Optional[int] = None
    ultima_atualizacao: Optional[str] = ''
    pedido_baixa_automatico_recorencia_cartao: Pedido_baixa_automatico_recorencia_cartaoEnum = Pedido_baixa_automatico_recorencia_cartaoEnum.SIM
    aceite: Optional[str] = ''
    especie: Optional[EspecieEnum] = EspecieEnum.RS
    especie_doc: Optional[str] = ''
    taxa: Optional[str] = ''
    quem_emite: Optional[str] = ''
    quem_distribui: Optional[Quem_distribuiEnum] = Quem_distribuiEnum.EMPRESA
    endereco_envio_cobranca: Optional[Endereco_envio_cobrancaEnum] = Endereco_envio_cobrancaEnum.COBRANCA
    boleto_local_atualiza: Optional[Boleto_local_atualizaEnum] = Boleto_local_atualizaEnum.SISTEMA
    local_pagamento: Optional[str] = ''
    contador_nn: Optional[int] = None
    classe_funcoes: Optional[Classe_funcoesEnum] = None
    versao_integracao_banrisul: Optional[Versao_integracao_banrisulEnum] = Versao_integracao_banrisulEnum.V1
    n_convenio: Optional[str] = ''
    c_cedente: Optional[str] = ''
    operacao: Optional[str] = ''
    codigo_edi7: Optional[str] = ''
    carteira: Optional[str] = ''
    sigla_arquivo_remessa: Optional[str] = ''
    variacao_carteira: Optional[str] = ''
    modalidade_cobranca: Optional[str] = ''
    sicredi_byte: Optional[str] = ''
    sicredi_posto: Optional[str] = ''
    inicio_nosso_numero: Optional[str] = ''
    nosso_numero_const1: Optional[str] = ''
    nosso_numero_const2: Optional[str] = ''
    nosso_numero1: Optional[str] = ''
    nosso_numero2: Optional[str] = ''
    conta_cosmos: Optional[str] = ''
    tipo_carteira: Optional[Tipo_carteiraEnum] = Tipo_carteiraEnum.SIMPLES
    tipo: Optional[TipoEnum] = None
    utliza_numero_parcela_fixo: Optional[Utliza_numero_parcela_fixoEnum] = Utliza_numero_parcela_fixoEnum.SIM
    pedido_baixa_automatico: Optional[Pedido_baixa_automaticoEnum] = Pedido_baixa_automaticoEnum.SIM
    enviar_pedido_baixa_renegociados: Optional[Enviar_pedido_baixa_renegociadosEnum] = Enviar_pedido_baixa_renegociadosEnum.SIM
    pedido_baixa_automatico_rec_manual: Optional[Pedido_baixa_automatico_rec_manualEnum] = Pedido_baixa_automatico_rec_manualEnum.SIM
    pedido_baixa_automatico_rec_cartao: Optional[Pedido_baixa_automatico_rec_cartaoEnum] = Pedido_baixa_automatico_rec_cartaoEnum.SIM
    pedido_baixa_automatico_rec_pix: Optional[Pedido_baixa_automatico_rec_pixEnum] = Pedido_baixa_automatico_rec_pixEnum.SIM
    adiciona_remessa_auto_alt_data: Optional[Adiciona_remessa_auto_alt_dataEnum] = Adiciona_remessa_auto_alt_dataEnum.NAO
    remessa_com_mensagem: Optional[Remessa_com_mensagemEnum] = Remessa_com_mensagemEnum.NAO
    validar_vencidos_remessa: Optional[Validar_vencidos_remessaEnum] = Validar_vencidos_remessaEnum.SIM
    validar_recebidos_remessa: Optional[Validar_recebidos_remessaEnum] = Validar_recebidos_remessaEnum.SIM
    validar_clientes_bloqueados: Optional[Validar_clientes_bloqueadosEnum] = Validar_clientes_bloqueadosEnum.NAO
    validar_clientes_negativados_remessa: Optional[Validar_clientes_negativados_remessaEnum] = Validar_clientes_negativados_remessaEnum.NAO
    l_remessa: Optional[L_remessaEnum] = None
    l_retorno: Optional[L_retornoEnum] = None
    codigo_flash: Optional[str] = ''
    contabiliza_retorno_filial_emissao: Optional[Contabiliza_retorno_filial_emissaoEnum] = Contabiliza_retorno_filial_emissaoEnum.NAO
    filtra_inicio_nn: Filtra_inicio_nnEnum = Filtra_inicio_nnEnum.SIM
    baixa_automatica: Optional[Baixa_automaticaEnum] = Baixa_automaticaEnum.SIM
    baixa_automatica_dias: Optional[str] = ''
    utilizar_baixa_apos_vencimento: Optional[Utilizar_baixa_apos_vencimentoEnum] = Utilizar_baixa_apos_vencimentoEnum.NAO
    enviar_pedido_baixa_vencimento: Optional[str] = ''
    gateway_nome: Optional[Gateway_nomeEnum] = None
    codigo_carteira: Optional[str] = ''
    workspace_id: Optional[str] = ''
    versao_api: Optional[Versao_apiEnum] = Versao_apiEnum.V1
    importado_gateway: Optional[Importado_gatewayEnum] = Importado_gatewayEnum.NAO
    nova_api: Optional[Nova_apiEnum] = Nova_apiEnum.SIM
    ambiente_homologacao_gateway: Optional[Ambiente_homologacao_gatewayEnum] = Ambiente_homologacao_gatewayEnum.PRODUCAO
    utiliza_carne: Optional[Utiliza_carneEnum] = Utiliza_carneEnum.NAO
    gerencia_client_id: Optional[str] = ''
    gerencia_client_secret: Optional[Any] = None
    developer_application_key: Optional[str] = ''
    webhook_id: Optional[str] = ''
    gerencia_ip_callback: Optional[str] = ''
    gerencia_identificador_conta: Optional[str] = ''
    nova_int_fortunus: Optional[Nova_int_fortunusEnum] = Nova_int_fortunusEnum.NAO
    gateway_token: Optional[Any] = None
    carteira_widepay: Optional[str] = ''
    gateway_tipo_impressao: Optional[Gateway_tipo_impressaoEnum] = Gateway_tipo_impressaoEnum.CARNE
    data_credito_pix: Optional[str] = ''
    data_credito_boleto: Optional[str] = ''
    gateway_retorno: Optional[str] = ''
    adiciona_obs_descricao: Optional[Adiciona_obs_descricaoEnum] = Adiciona_obs_descricaoEnum.NAO
    adiciona_venc_descricao: Optional[Adiciona_venc_descricaoEnum] = Adiciona_venc_descricaoEnum.NAO
    dias_limite_pagamento_apos_vencimento: Optional[str] = ''
    envia_email_gerencia: Optional[Envia_email_gerenciaEnum] = Envia_email_gerenciaEnum.NAO
    numero_conta_f2b: Optional[str] = ''
    n_convenio_credisis: Optional[str] = ''
    url_callback: Optional[str] = ''
    use_webhook_url_callback: Use_webhook_url_callbackEnum = Use_webhook_url_callbackEnum.NAO
    webhook_url_callback: Optional[str] = ''
    data_ultima_atualizacao: Optional[str] = ''
    galaxPayId: Optional[str] = ''
    galaxPayHash: Optional[str] = ''
    recebimento_parcial_gateway: Optional[Recebimento_parcial_gatewayEnum] = Recebimento_parcial_gatewayEnum.NAO
    finalizar_cob_bf: Optional[Finalizar_cob_bfEnum] = Finalizar_cob_bfEnum.SIM
    especie_documento_gerencianet: Optional[str] = ''
    gera_pix_gateway: Optional[Gera_pix_gatewayEnum] = Gera_pix_gatewayEnum.NAO
    enviar_cobranca_pix_whatsapp: Enviar_cobranca_pix_whatsappEnum = Enviar_cobranca_pix_whatsappEnum.NAO
    tipo_chave_pix: Optional[Tipo_chave_pixEnum] = None
    pix_chave_santander: Optional[str] = ''
    dica_chave_pix_gateway: Optional[str] = ''
    lanca_tarifa_gateway: Optional[Lanca_tarifa_gatewayEnum] = Lanca_tarifa_gatewayEnum.NAO_LANCA
    valor_tarifa_gateway: Optional[str] = ''
    lanca_tarifa_pix: Optional[Lanca_tarifa_pixEnum] = Lanca_tarifa_pixEnum.NAO
    valor_tarifa_pix: Optional[str] = ''
    timeout: Optional[TimeoutEnum] = TimeoutEnum.T60
    expire_at: Optional[str] = ''
    creditcard_gateway: Optional[Creditcard_gatewayEnum] = None
    creditCard_ambiente: Optional[CreditCard_ambienteEnum] = CreditCard_ambienteEnum.TESTE
    versao_api_cartao: Optional[Versao_api_cartaoEnum] = None
    habilitar_recorrencia_cartao: Optional[Habilitar_recorrencia_cartaoEnum] = Habilitar_recorrencia_cartaoEnum.NAO
    creditcard_user: Optional[str] = ''
    creditcard_senha: Optional[str] = ''
    creditcard_senhassl: Optional[str] = ''
    creditCard_loja: Optional[str] = ''
    creditCard_chave: Optional[str] = ''
    gerencia_identificador_conta_card: Optional[str] = ''
    gateway_token_card: Optional[Any] = None
    gerencia_client_id_card: Optional[str] = ''
    gerencia_client_secret_card: Optional[Any] = None
    gerencia_ip_callback_card: Optional[str] = ''
    id_plano_vindi: Optional[str] = ''
    galaxPayIdCard: Optional[str] = ''
    galaxPayHashCard: Optional[str] = ''
    galaxpay_ip_callback_card: Optional[str] = ''
    timeoutCreditCard: Optional[TimeoutCreditCardEnum] = TimeoutCreditCardEnum.T60
    creditcard_sslcert: Optional[Any] = None
    creditcard_sslkey: Optional[Any] = None
    creditCard_local: Optional[CreditCard_localEnum] = CreditCard_localEnum.BUY_PAGE_LOJA
    creditCard_autenticar: Optional[str] = ''
    creditCard_capturar: Optional[str] = ''
    creditCard_autorizar: Optional[CreditCard_autorizarEnum] = CreditCard_autorizarEnum.AUTORIZAR_DIRETO
    credit_card_tipo: Optional[str] = ''
    creditCard_parcelamento: Optional[CreditCard_parcelamentoEnum] = CreditCard_parcelamentoEnum.ADMINISTRADORA
    creditCard_Nparcelas: Optional[str] = ''
    creditCard_juro: Optional[str] = ''
    credit_card_repassar_taxa: Credit_card_repassar_taxaEnum = Credit_card_repassar_taxaEnum.NAO
    tip_fee_transfer: Optional[str] = ''
    credit_card_taxa_em_pagamentos: Credit_card_taxa_em_pagamentosEnum = Credit_card_taxa_em_pagamentosEnum.AMBOS
    credit_card_porcentagem_taxa: Optional[str] = ''
    credit_card_valor_taxa: Optional[str] = ''
    creditcard_banceira_vi: Optional[str] = ''
    creditcard_banceira_ma: Optional[str] = ''
    creditcard_banceira_am: Optional[str] = ''
    creditcard_banceira_el: Optional[str] = ''
    creditcard_banceira_dn: Optional[str] = ''
    creditcard_banceira_dc: Optional[str] = ''
    creditcard_banceira_jc: Optional[str] = ''
    creditcard_banceira_au: Optional[str] = ''
    creditcard_banceira_ca: Optional[str] = ''
    debito_convenio: Optional[str] = ''
    debito_carteira_vinculada: Optional[int] = None
    debito_classe: Optional[Debito_classeEnum] = None
    validar_vencidos_remessa_D: Optional[Validar_vencidos_remessa_DEnum] = Validar_vencidos_remessa_DEnum.SIM
    data_credito_debito_em_conta: Optional[str] = ''
    valor_tarifa: Optional[str] = ''
    substrair_tarifa: Optional[str] = ''
    pix_gateway: Optional[Pix_gatewayEnum] = None
    pix_ambiente: Optional[Pix_ambienteEnum] = Pix_ambienteEnum.PRODUCAO
    pix_chave: Optional[str] = ''
    pix_client_id: Optional[str] = ''
    pix_client_secret: Optional[Any] = None
    pix_tempo_validade: Optional[str] = ''
    pix_certificado: Optional[Any] = None
    pix_gerencia_ip_callback: Optional[str] = ''
    pix_modalidade: Optional[Pix_modalidadeEnum] = Pix_modalidadeEnum.IMEDIATA
    permite_pagamento_por_chave_pix: Permite_pagamento_por_chave_pixEnum = Permite_pagamento_por_chave_pixEnum.SIM
    enviar_cobranca_pix_whatsapp_carteiras_pix: Enviar_cobranca_pix_whatsapp_carteiras_pixEnum = Enviar_cobranca_pix_whatsapp_carteiras_pixEnum.NAO
    tipo_chave_pix_carteiras_pix: Optional[Tipo_chave_pix_carteiras_pixEnum] = None
    utiliza_pix_recorrente: Optional[Utiliza_pix_recorrenteEnum] = Utiliza_pix_recorrenteEnum.NAO
    permite_retentativas_pix_recorrente: Optional[Permite_retentativas_pix_recorrenteEnum] = Permite_retentativas_pix_recorrenteEnum.SIM
    fieldset_dica_configuracoes_pix: Optional[str] = ''
    lanca_tarifa_pix_modobank: Lanca_tarifa_pix_modobankEnum = Lanca_tarifa_pix_modobankEnum.NAO
    valor_tarifa_pix_modobank: Optional[str] = ''
    jurop_mes: Optional[str] = ''
    juros_boleto_juno: Optional[str] = ''
    jurop: Optional[str] = ''
    jurov: Optional[str] = ''
    multap: Optional[str] = ''
    multav: Optional[str] = ''
    desconto_v: Optional[str] = ''
    desconto_p: Optional[str] = ''
    desconto_condicional_valor: Optional[str] = ''
    desconto_condicional_percentual: Optional[str] = ''
    data_validade_condicional: Optional[str] = ''
    desconto_proporcional: Optional[str] = ''
    protestar: Optional[str] = ''
    atraso: Optional[str] = ''
    calcular_juros: Optional[Calcular_jurosEnum] = Calcular_jurosEnum.ATE_O_DIA_ATUAL
    permite_atualizar_boleto_apos_data_ixc: Optional[str] = ''
    instrucao1: Optional[str] = ''
    instrucao2: Optional[str] = ''
    instrucao3: Optional[str] = ''
    instrucao4: Optional[str] = ''
    instrucao5: Optional[str] = ''
    instrucao6: Optional[str] = ''
    instrucao7: Optional[str] = ''
    instrucao8: Optional[str] = ''
    imp_inst_vencido: Optional[str] = ''
    imp_inst_proporcional: Optional[str] = ''
    obs_fn_areceber: Optional[Obs_fn_areceberEnum] = Obs_fn_areceberEnum.SIM
    obs_anterior: Optional[str] = ''
    obs_posterior: Optional[str] = ''
    l_impressao: Optional[L_impressaoEnum] = None
    formato_detalhamento_fatura: Optional[Formato_detalhamento_faturaEnum] = Formato_detalhamento_faturaEnum.PLANO
    cor_fatura: Optional[str] = ''
    informative_text: Optional[str] = ''
    imprimir_filial_venda: Optional[Imprimir_filial_vendaEnum] = Imprimir_filial_vendaEnum.CONTA
    imprimir_filial_conta: Optional[Imprimir_filial_contaEnum] = Imprimir_filial_contaEnum.VENDA
    considerar_modelo_nao_fiscal: Optional[Considerar_modelo_nao_fiscalEnum] = Considerar_modelo_nao_fiscalEnum.NAO
    imprime_endereco_boleto: Optional[Imprime_endereco_boletoEnum] = Imprime_endereco_boletoEnum.SIM
    imprime_fone_fatura_d: Optional[Imprime_fone_fatura_dEnum] = Imprime_fone_fatura_dEnum.NAO
    imp_nome_sacador_avalista: Optional[Imp_nome_sacador_avalistaEnum] = Imp_nome_sacador_avalistaEnum.SIM
    imprime_prod_val_zero: Optional[Imprime_prod_val_zeroEnum] = Imprime_prod_val_zeroEnum.SIM
    imprime_tipo_resolucao_anatel: Optional[Imprime_tipo_resolucao_anatelEnum] = Imprime_tipo_resolucao_anatelEnum.NAO
    mask_cpf_cnpj_impressao_boleto: Optional[Mask_cpf_cnpj_impressao_boletoEnum] = Mask_cpf_cnpj_impressao_boletoEnum.NAO
    mostra_cep_beneficiario_impressao: Optional[Mostra_cep_beneficiario_impressaoEnum] = Mostra_cep_beneficiario_impressaoEnum.NAO
    agrupar_produtos_por_descricao: Optional[Agrupar_produtos_por_descricaoEnum] = Agrupar_produtos_por_descricaoEnum.NAO
    imprimir_beneficiario_gateway: Optional[Imprimir_beneficiario_gatewayEnum] = Imprimir_beneficiario_gatewayEnum.RAZAO_SOCIAL
    obs_adicional_boleto: Optional[str] = ''
    imp_nome_beneficiario: Imp_nome_beneficiarioEnum = Imp_nome_beneficiarioEnum.RAZAO_SOCIAL
    imp_nome_beneficiario_recibo: Optional[Imp_nome_beneficiario_reciboEnum] = Imp_nome_beneficiario_reciboEnum.RAZAO_SOCIAL
    boletos_capa_contratos: Optional[Boletos_capa_contratosEnum] = Boletos_capa_contratosEnum.NAO
    boleto_capa: Optional[str] = ''
    boleto_capa_cliente_referencia: Optional[str] = ''
    fone_cliente_capa: Optional[str] = ''
    boleto_capa_local: Optional[Boleto_capa_localEnum] = Boleto_capa_localEnum.NO_INICIO
    boleto_capa_imagem: Optional[Any] = None
    boleto_capa_x: Optional[str] = ''
    boleto_capa_y: Optional[str] = ''
    tamanho_quadro_endereco_x: Optional[str] = ''
    tamanho_quadro_endereco_y: Optional[str] = ''
    tipo_baixa: Optional[Tipo_baixaEnum] = Tipo_baixaEnum.DESCONTO
    validar_juros_multa: Optional[Validar_juros_multaEnum] = Validar_juros_multaEnum.NAO
    id_produto_cob_adicional: Optional[int] = None
    id_fn_areceber_modelo: Optional[int] = None

    @property
    def id(self) -> str:
        return str(self.id_autoincrement)

    @property
    def table(self) -> str:
        return "fn_carteira_cobranca"

    def to_dict(self) -> dict[str, str]:
        return {
            'id_autoincrement': str(self.id_autoincrement),
            'descricao': self.descricao if self.descricao is not None else '',
            'id_conta': str(self.id_conta) if self.id_conta is not None else '',
            'remover_fundo_capa_carteira': self.remover_fundo_capa_carteira if self.remover_fundo_capa_carteira is not None else '',
            'tipo_recebimento': self.tipo_recebimento.value if self.tipo_recebimento is not None else '',
            'envia_email_ao_gerar_finan': self.envia_email_ao_gerar_finan.value if self.envia_email_ao_gerar_finan is not None else '',
            'envia_push_ao_gerar_finan': self.envia_push_ao_gerar_finan.value if self.envia_push_ao_gerar_finan is not None else '',
            'imprime_ligacoes_voip': self.imprime_ligacoes_voip if self.imprime_ligacoes_voip is not None else '',
            'registrado': self.registrado.value if self.registrado is not None else '',
            'ativo': self.ativo.value if self.ativo is not None else '',
            'filial_id': str(self.filial_id) if self.filial_id is not None else '',
            'id_config_alt_pagamento': str(self.id_config_alt_pagamento) if self.id_config_alt_pagamento is not None else '',
            'planejamento_tarifa': str(self.planejamento_tarifa) if self.planejamento_tarifa is not None else '',
            'lancamento_tarifa': self.lancamento_tarifa.value if self.lancamento_tarifa is not None else '',
            'reseller_authorization_code': self.reseller_authorization_code if self.reseller_authorization_code is not None else '',
            'dias_vencimento_fatura': self.dias_vencimento_fatura if self.dias_vencimento_fatura is not None else '',
            'carteira_padrao_fatura': str(self.carteira_padrao_fatura) if self.carteira_padrao_fatura is not None else '',
            'ultima_atualizacao': self.ultima_atualizacao if self.ultima_atualizacao is not None else '',
            'pedido_baixa_automatico_recorencia_cartao': self.pedido_baixa_automatico_recorencia_cartao.value if self.pedido_baixa_automatico_recorencia_cartao is not None else '',
            'aceite': self.aceite if self.aceite is not None else '',
            'especie': self.especie.value if self.especie is not None else '',
            'especie_doc': self.especie_doc if self.especie_doc is not None else '',
            'taxa': self.taxa if self.taxa is not None else '',
            'quem_emite': self.quem_emite if self.quem_emite is not None else '',
            'quem_distribui': self.quem_distribui.value if self.quem_distribui is not None else '',
            'endereco_envio_cobranca': self.endereco_envio_cobranca.value if self.endereco_envio_cobranca is not None else '',
            'boleto_local_atualiza': self.boleto_local_atualiza.value if self.boleto_local_atualiza is not None else '',
            'local_pagamento': self.local_pagamento if self.local_pagamento is not None else '',
            'contador_nn': str(self.contador_nn) if self.contador_nn is not None else '',
            'classe_funcoes': self.classe_funcoes.value if self.classe_funcoes is not None else '',
            'versao_integracao_banrisul': self.versao_integracao_banrisul.value if self.versao_integracao_banrisul is not None else '',
            'n_convenio': self.n_convenio if self.n_convenio is not None else '',
            'c_cedente': self.c_cedente if self.c_cedente is not None else '',
            'operacao': self.operacao if self.operacao is not None else '',
            'codigo_edi7': self.codigo_edi7 if self.codigo_edi7 is not None else '',
            'carteira': self.carteira if self.carteira is not None else '',
            'sigla_arquivo_remessa': self.sigla_arquivo_remessa if self.sigla_arquivo_remessa is not None else '',
            'variacao_carteira': self.variacao_carteira if self.variacao_carteira is not None else '',
            'modalidade_cobranca': self.modalidade_cobranca if self.modalidade_cobranca is not None else '',
            'sicredi_byte': self.sicredi_byte if self.sicredi_byte is not None else '',
            'sicredi_posto': self.sicredi_posto if self.sicredi_posto is not None else '',
            'inicio_nosso_numero': self.inicio_nosso_numero if self.inicio_nosso_numero is not None else '',
            'nosso_numero_const1': self.nosso_numero_const1 if self.nosso_numero_const1 is not None else '',
            'nosso_numero_const2': self.nosso_numero_const2 if self.nosso_numero_const2 is not None else '',
            'nosso_numero1': self.nosso_numero1 if self.nosso_numero1 is not None else '',
            'nosso_numero2': self.nosso_numero2 if self.nosso_numero2 is not None else '',
            'conta_cosmos': self.conta_cosmos if self.conta_cosmos is not None else '',
            'tipo_carteira': self.tipo_carteira.value if self.tipo_carteira is not None else '',
            'tipo': self.tipo.value if self.tipo is not None else '',
            'utliza_numero_parcela_fixo': self.utliza_numero_parcela_fixo.value if self.utliza_numero_parcela_fixo is not None else '',
            'pedido_baixa_automatico': self.pedido_baixa_automatico.value if self.pedido_baixa_automatico is not None else '',
            'enviar_pedido_baixa_renegociados': self.enviar_pedido_baixa_renegociados.value if self.enviar_pedido_baixa_renegociados is not None else '',
            'pedido_baixa_automatico_rec_manual': self.pedido_baixa_automatico_rec_manual.value if self.pedido_baixa_automatico_rec_manual is not None else '',
            'pedido_baixa_automatico_rec_cartao': self.pedido_baixa_automatico_rec_cartao.value if self.pedido_baixa_automatico_rec_cartao is not None else '',
            'pedido_baixa_automatico_rec_pix': self.pedido_baixa_automatico_rec_pix.value if self.pedido_baixa_automatico_rec_pix is not None else '',
            'adiciona_remessa_auto_alt_data': self.adiciona_remessa_auto_alt_data.value if self.adiciona_remessa_auto_alt_data is not None else '',
            'remessa_com_mensagem': self.remessa_com_mensagem.value if self.remessa_com_mensagem is not None else '',
            'validar_vencidos_remessa': self.validar_vencidos_remessa.value if self.validar_vencidos_remessa is not None else '',
            'validar_recebidos_remessa': self.validar_recebidos_remessa.value if self.validar_recebidos_remessa is not None else '',
            'validar_clientes_bloqueados': self.validar_clientes_bloqueados.value if self.validar_clientes_bloqueados is not None else '',
            'validar_clientes_negativados_remessa': self.validar_clientes_negativados_remessa.value if self.validar_clientes_negativados_remessa is not None else '',
            'l_remessa': self.l_remessa.value if self.l_remessa is not None else '',
            'l_retorno': self.l_retorno.value if self.l_retorno is not None else '',
            'codigo_flash': self.codigo_flash if self.codigo_flash is not None else '',
            'contabiliza_retorno_filial_emissao': self.contabiliza_retorno_filial_emissao.value if self.contabiliza_retorno_filial_emissao is not None else '',
            'filtra_inicio_nn': self.filtra_inicio_nn.value if self.filtra_inicio_nn is not None else '',
            'baixa_automatica': self.baixa_automatica.value if self.baixa_automatica is not None else '',
            'baixa_automatica_dias': self.baixa_automatica_dias if self.baixa_automatica_dias is not None else '',
            'utilizar_baixa_apos_vencimento': self.utilizar_baixa_apos_vencimento.value if self.utilizar_baixa_apos_vencimento is not None else '',
            'enviar_pedido_baixa_vencimento': self.enviar_pedido_baixa_vencimento if self.enviar_pedido_baixa_vencimento is not None else '',
            'gateway_nome': self.gateway_nome.value if self.gateway_nome is not None else '',
            'codigo_carteira': self.codigo_carteira if self.codigo_carteira is not None else '',
            'workspace_id': self.workspace_id if self.workspace_id is not None else '',
            'versao_api': self.versao_api.value if self.versao_api is not None else '',
            'importado_gateway': self.importado_gateway.value if self.importado_gateway is not None else '',
            'nova_api': self.nova_api.value if self.nova_api is not None else '',
            'ambiente_homologacao_gateway': self.ambiente_homologacao_gateway.value if self.ambiente_homologacao_gateway is not None else '',
            'utiliza_carne': self.utiliza_carne.value if self.utiliza_carne is not None else '',
            'gerencia_client_id': self.gerencia_client_id if self.gerencia_client_id is not None else '',
            'gerencia_client_secret': self.gerencia_client_secret if self.gerencia_client_secret is not None else '',
            'developer_application_key': self.developer_application_key if self.developer_application_key is not None else '',
            'webhook_id': self.webhook_id if self.webhook_id is not None else '',
            'gerencia_ip_callback': self.gerencia_ip_callback if self.gerencia_ip_callback is not None else '',
            'gerencia_identificador_conta': self.gerencia_identificador_conta if self.gerencia_identificador_conta is not None else '',
            'nova_int_fortunus': self.nova_int_fortunus.value if self.nova_int_fortunus is not None else '',
            'gateway_token': self.gateway_token if self.gateway_token is not None else '',
            'carteira_widepay': self.carteira_widepay if self.carteira_widepay is not None else '',
            'gateway_tipo_impressao': self.gateway_tipo_impressao.value if self.gateway_tipo_impressao is not None else '',
            'data_credito_pix': self.data_credito_pix if self.data_credito_pix is not None else '',
            'data_credito_boleto': self.data_credito_boleto if self.data_credito_boleto is not None else '',
            'gateway_retorno': self.gateway_retorno if self.gateway_retorno is not None else '',
            'adiciona_obs_descricao': self.adiciona_obs_descricao.value if self.adiciona_obs_descricao is not None else '',
            'adiciona_venc_descricao': self.adiciona_venc_descricao.value if self.adiciona_venc_descricao is not None else '',
            'dias_limite_pagamento_apos_vencimento': self.dias_limite_pagamento_apos_vencimento if self.dias_limite_pagamento_apos_vencimento is not None else '',
            'envia_email_gerencia': self.envia_email_gerencia.value if self.envia_email_gerencia is not None else '',
            'numero_conta_f2b': self.numero_conta_f2b if self.numero_conta_f2b is not None else '',
            'n_convenio_credisis': self.n_convenio_credisis if self.n_convenio_credisis is not None else '',
            'url_callback': self.url_callback if self.url_callback is not None else '',
            'use_webhook_url_callback': self.use_webhook_url_callback.value if self.use_webhook_url_callback is not None else '',
            'webhook_url_callback': self.webhook_url_callback if self.webhook_url_callback is not None else '',
            'data_ultima_atualizacao': self.data_ultima_atualizacao if self.data_ultima_atualizacao is not None else '',
            'galaxPayId': self.galaxPayId if self.galaxPayId is not None else '',
            'galaxPayHash': self.galaxPayHash if self.galaxPayHash is not None else '',
            'recebimento_parcial_gateway': self.recebimento_parcial_gateway.value if self.recebimento_parcial_gateway is not None else '',
            'finalizar_cob_bf': self.finalizar_cob_bf.value if self.finalizar_cob_bf is not None else '',
            'especie_documento_gerencianet': self.especie_documento_gerencianet if self.especie_documento_gerencianet is not None else '',
            'gera_pix_gateway': self.gera_pix_gateway.value if self.gera_pix_gateway is not None else '',
            'enviar_cobranca_pix_whatsapp': self.enviar_cobranca_pix_whatsapp.value if self.enviar_cobranca_pix_whatsapp is not None else '',
            'tipo_chave_pix': self.tipo_chave_pix.value if self.tipo_chave_pix is not None else '',
            'pix_chave_santander': self.pix_chave_santander if self.pix_chave_santander is not None else '',
            'dica_chave_pix_gateway': self.dica_chave_pix_gateway if self.dica_chave_pix_gateway is not None else '',
            'lanca_tarifa_gateway': self.lanca_tarifa_gateway.value if self.lanca_tarifa_gateway is not None else '',
            'valor_tarifa_gateway': self.valor_tarifa_gateway if self.valor_tarifa_gateway is not None else '',
            'lanca_tarifa_pix': self.lanca_tarifa_pix.value if self.lanca_tarifa_pix is not None else '',
            'valor_tarifa_pix': self.valor_tarifa_pix if self.valor_tarifa_pix is not None else '',
            'timeout': self.timeout.value if self.timeout is not None else '',
            'expire_at': self.expire_at if self.expire_at is not None else '',
            'creditcard_gateway': self.creditcard_gateway.value if self.creditcard_gateway is not None else '',
            'creditCard_ambiente': self.creditCard_ambiente.value if self.creditCard_ambiente is not None else '',
            'versao_api_cartao': self.versao_api_cartao.value if self.versao_api_cartao is not None else '',
            'habilitar_recorrencia_cartao': self.habilitar_recorrencia_cartao.value if self.habilitar_recorrencia_cartao is not None else '',
            'creditcard_user': self.creditcard_user if self.creditcard_user is not None else '',
            'creditcard_senha': self.creditcard_senha if self.creditcard_senha is not None else '',
            'creditcard_senhassl': self.creditcard_senhassl if self.creditcard_senhassl is not None else '',
            'creditCard_loja': self.creditCard_loja if self.creditCard_loja is not None else '',
            'creditCard_chave': self.creditCard_chave if self.creditCard_chave is not None else '',
            'gerencia_identificador_conta_card': self.gerencia_identificador_conta_card if self.gerencia_identificador_conta_card is not None else '',
            'gateway_token_card': self.gateway_token_card if self.gateway_token_card is not None else '',
            'gerencia_client_id_card': self.gerencia_client_id_card if self.gerencia_client_id_card is not None else '',
            'gerencia_client_secret_card': self.gerencia_client_secret_card if self.gerencia_client_secret_card is not None else '',
            'gerencia_ip_callback_card': self.gerencia_ip_callback_card if self.gerencia_ip_callback_card is not None else '',
            'id_plano_vindi': self.id_plano_vindi if self.id_plano_vindi is not None else '',
            'galaxPayIdCard': self.galaxPayIdCard if self.galaxPayIdCard is not None else '',
            'galaxPayHashCard': self.galaxPayHashCard if self.galaxPayHashCard is not None else '',
            'galaxpay_ip_callback_card': self.galaxpay_ip_callback_card if self.galaxpay_ip_callback_card is not None else '',
            'timeoutCreditCard': self.timeoutCreditCard.value if self.timeoutCreditCard is not None else '',
            'creditcard_sslcert': self.creditcard_sslcert if self.creditcard_sslcert is not None else '',
            'creditcard_sslkey': self.creditcard_sslkey if self.creditcard_sslkey is not None else '',
            'creditCard_local': self.creditCard_local.value if self.creditCard_local is not None else '',
            'creditCard_autenticar': self.creditCard_autenticar if self.creditCard_autenticar is not None else '',
            'creditCard_capturar': self.creditCard_capturar if self.creditCard_capturar is not None else '',
            'creditCard_autorizar': self.creditCard_autorizar.value if self.creditCard_autorizar is not None else '',
            'credit_card_tipo': self.credit_card_tipo if self.credit_card_tipo is not None else '',
            'creditCard_parcelamento': self.creditCard_parcelamento.value if self.creditCard_parcelamento is not None else '',
            'creditCard_Nparcelas': self.creditCard_Nparcelas if self.creditCard_Nparcelas is not None else '',
            'creditCard_juro': self.creditCard_juro if self.creditCard_juro is not None else '',
            'credit_card_repassar_taxa': self.credit_card_repassar_taxa.value if self.credit_card_repassar_taxa is not None else '',
            'tip_fee_transfer': self.tip_fee_transfer if self.tip_fee_transfer is not None else '',
            'credit_card_taxa_em_pagamentos': self.credit_card_taxa_em_pagamentos.value if self.credit_card_taxa_em_pagamentos is not None else '',
            'credit_card_porcentagem_taxa': self.credit_card_porcentagem_taxa if self.credit_card_porcentagem_taxa is not None else '',
            'credit_card_valor_taxa': self.credit_card_valor_taxa if self.credit_card_valor_taxa is not None else '',
            'creditcard_banceira_vi': self.creditcard_banceira_vi if self.creditcard_banceira_vi is not None else '',
            'creditcard_banceira_ma': self.creditcard_banceira_ma if self.creditcard_banceira_ma is not None else '',
            'creditcard_banceira_am': self.creditcard_banceira_am if self.creditcard_banceira_am is not None else '',
            'creditcard_banceira_el': self.creditcard_banceira_el if self.creditcard_banceira_el is not None else '',
            'creditcard_banceira_dn': self.creditcard_banceira_dn if self.creditcard_banceira_dn is not None else '',
            'creditcard_banceira_dc': self.creditcard_banceira_dc if self.creditcard_banceira_dc is not None else '',
            'creditcard_banceira_jc': self.creditcard_banceira_jc if self.creditcard_banceira_jc is not None else '',
            'creditcard_banceira_au': self.creditcard_banceira_au if self.creditcard_banceira_au is not None else '',
            'creditcard_banceira_ca': self.creditcard_banceira_ca if self.creditcard_banceira_ca is not None else '',
            'debito_convenio': self.debito_convenio if self.debito_convenio is not None else '',
            'debito_carteira_vinculada': str(self.debito_carteira_vinculada) if self.debito_carteira_vinculada is not None else '',
            'debito_classe': self.debito_classe.value if self.debito_classe is not None else '',
            'validar_vencidos_remessa_D': self.validar_vencidos_remessa_D.value if self.validar_vencidos_remessa_D is not None else '',
            'data_credito_debito_em_conta': self.data_credito_debito_em_conta if self.data_credito_debito_em_conta is not None else '',
            'valor_tarifa': self.valor_tarifa if self.valor_tarifa is not None else '',
            'substrair_tarifa': self.substrair_tarifa if self.substrair_tarifa is not None else '',
            'pix_gateway': self.pix_gateway.value if self.pix_gateway is not None else '',
            'pix_ambiente': self.pix_ambiente.value if self.pix_ambiente is not None else '',
            'pix_chave': self.pix_chave if self.pix_chave is not None else '',
            'pix_client_id': self.pix_client_id if self.pix_client_id is not None else '',
            'pix_client_secret': self.pix_client_secret if self.pix_client_secret is not None else '',
            'pix_tempo_validade': self.pix_tempo_validade if self.pix_tempo_validade is not None else '',
            'pix_certificado': self.pix_certificado if self.pix_certificado is not None else '',
            'pix_gerencia_ip_callback': self.pix_gerencia_ip_callback if self.pix_gerencia_ip_callback is not None else '',
            'pix_modalidade': self.pix_modalidade.value if self.pix_modalidade is not None else '',
            'permite_pagamento_por_chave_pix': self.permite_pagamento_por_chave_pix.value if self.permite_pagamento_por_chave_pix is not None else '',
            'enviar_cobranca_pix_whatsapp_carteiras_pix': self.enviar_cobranca_pix_whatsapp_carteiras_pix.value if self.enviar_cobranca_pix_whatsapp_carteiras_pix is not None else '',
            'tipo_chave_pix_carteiras_pix': self.tipo_chave_pix_carteiras_pix.value if self.tipo_chave_pix_carteiras_pix is not None else '',
            'utiliza_pix_recorrente': self.utiliza_pix_recorrente.value if self.utiliza_pix_recorrente is not None else '',
            'permite_retentativas_pix_recorrente': self.permite_retentativas_pix_recorrente.value if self.permite_retentativas_pix_recorrente is not None else '',
            'fieldset_dica_configuracoes_pix': self.fieldset_dica_configuracoes_pix if self.fieldset_dica_configuracoes_pix is not None else '',
            'lanca_tarifa_pix_modobank': self.lanca_tarifa_pix_modobank.value if self.lanca_tarifa_pix_modobank is not None else '',
            'valor_tarifa_pix_modobank': self.valor_tarifa_pix_modobank if self.valor_tarifa_pix_modobank is not None else '',
            'jurop_mes': self.jurop_mes if self.jurop_mes is not None else '',
            'juros_boleto_juno': self.juros_boleto_juno if self.juros_boleto_juno is not None else '',
            'jurop': self.jurop if self.jurop is not None else '',
            'jurov': self.jurov if self.jurov is not None else '',
            'multap': self.multap if self.multap is not None else '',
            'multav': self.multav if self.multav is not None else '',
            'desconto_v': self.desconto_v if self.desconto_v is not None else '',
            'desconto_p': self.desconto_p if self.desconto_p is not None else '',
            'desconto_condicional_valor': self.desconto_condicional_valor if self.desconto_condicional_valor is not None else '',
            'desconto_condicional_percentual': self.desconto_condicional_percentual if self.desconto_condicional_percentual is not None else '',
            'data_validade_condicional': self.data_validade_condicional if self.data_validade_condicional is not None else '',
            'desconto_proporcional': self.desconto_proporcional if self.desconto_proporcional is not None else '',
            'protestar': self.protestar if self.protestar is not None else '',
            'atraso': self.atraso if self.atraso is not None else '',
            'calcular_juros': self.calcular_juros.value if self.calcular_juros is not None else '',
            'permite_atualizar_boleto_apos_data_ixc': self.permite_atualizar_boleto_apos_data_ixc if self.permite_atualizar_boleto_apos_data_ixc is not None else '',
            'instrucao1': self.instrucao1 if self.instrucao1 is not None else '',
            'instrucao2': self.instrucao2 if self.instrucao2 is not None else '',
            'instrucao3': self.instrucao3 if self.instrucao3 is not None else '',
            'instrucao4': self.instrucao4 if self.instrucao4 is not None else '',
            'instrucao5': self.instrucao5 if self.instrucao5 is not None else '',
            'instrucao6': self.instrucao6 if self.instrucao6 is not None else '',
            'instrucao7': self.instrucao7 if self.instrucao7 is not None else '',
            'instrucao8': self.instrucao8 if self.instrucao8 is not None else '',
            'imp_inst_vencido': self.imp_inst_vencido if self.imp_inst_vencido is not None else '',
            'imp_inst_proporcional': self.imp_inst_proporcional if self.imp_inst_proporcional is not None else '',
            'obs_fn_areceber': self.obs_fn_areceber.value if self.obs_fn_areceber is not None else '',
            'obs_anterior': self.obs_anterior if self.obs_anterior is not None else '',
            'obs_posterior': self.obs_posterior if self.obs_posterior is not None else '',
            'l_impressao': self.l_impressao.value if self.l_impressao is not None else '',
            'formato_detalhamento_fatura': self.formato_detalhamento_fatura.value if self.formato_detalhamento_fatura is not None else '',
            'cor_fatura': self.cor_fatura if self.cor_fatura is not None else '',
            'informative_text': self.informative_text if self.informative_text is not None else '',
            'imprimir_filial_venda': self.imprimir_filial_venda.value if self.imprimir_filial_venda is not None else '',
            'imprimir_filial_conta': self.imprimir_filial_conta.value if self.imprimir_filial_conta is not None else '',
            'considerar_modelo_nao_fiscal': self.considerar_modelo_nao_fiscal.value if self.considerar_modelo_nao_fiscal is not None else '',
            'imprime_endereco_boleto': self.imprime_endereco_boleto.value if self.imprime_endereco_boleto is not None else '',
            'imprime_fone_fatura_d': self.imprime_fone_fatura_d.value if self.imprime_fone_fatura_d is not None else '',
            'imp_nome_sacador_avalista': self.imp_nome_sacador_avalista.value if self.imp_nome_sacador_avalista is not None else '',
            'imprime_prod_val_zero': self.imprime_prod_val_zero.value if self.imprime_prod_val_zero is not None else '',
            'imprime_tipo_resolucao_anatel': self.imprime_tipo_resolucao_anatel.value if self.imprime_tipo_resolucao_anatel is not None else '',
            'mask_cpf_cnpj_impressao_boleto': self.mask_cpf_cnpj_impressao_boleto.value if self.mask_cpf_cnpj_impressao_boleto is not None else '',
            'mostra_cep_beneficiario_impressao': self.mostra_cep_beneficiario_impressao.value if self.mostra_cep_beneficiario_impressao is not None else '',
            'agrupar_produtos_por_descricao': self.agrupar_produtos_por_descricao.value if self.agrupar_produtos_por_descricao is not None else '',
            'imprimir_beneficiario_gateway': self.imprimir_beneficiario_gateway.value if self.imprimir_beneficiario_gateway is not None else '',
            'obs_adicional_boleto': self.obs_adicional_boleto if self.obs_adicional_boleto is not None else '',
            'imp_nome_beneficiario': self.imp_nome_beneficiario.value if self.imp_nome_beneficiario is not None else '',
            'imp_nome_beneficiario_recibo': self.imp_nome_beneficiario_recibo.value if self.imp_nome_beneficiario_recibo is not None else '',
            'boletos_capa_contratos': self.boletos_capa_contratos.value if self.boletos_capa_contratos is not None else '',
            'boleto_capa': self.boleto_capa if self.boleto_capa is not None else '',
            'boleto_capa_cliente_referencia': self.boleto_capa_cliente_referencia if self.boleto_capa_cliente_referencia is not None else '',
            'fone_cliente_capa': self.fone_cliente_capa if self.fone_cliente_capa is not None else '',
            'boleto_capa_local': self.boleto_capa_local.value if self.boleto_capa_local is not None else '',
            'boleto_capa_imagem': self.boleto_capa_imagem if self.boleto_capa_imagem is not None else '',
            'boleto_capa_x': self.boleto_capa_x if self.boleto_capa_x is not None else '',
            'boleto_capa_y': self.boleto_capa_y if self.boleto_capa_y is not None else '',
            'tamanho_quadro_endereco_x': self.tamanho_quadro_endereco_x if self.tamanho_quadro_endereco_x is not None else '',
            'tamanho_quadro_endereco_y': self.tamanho_quadro_endereco_y if self.tamanho_quadro_endereco_y is not None else '',
            'tipo_baixa': self.tipo_baixa.value if self.tipo_baixa is not None else '',
            'validar_juros_multa': self.validar_juros_multa.value if self.validar_juros_multa is not None else '',
            'id_produto_cob_adicional': str(self.id_produto_cob_adicional) if self.id_produto_cob_adicional is not None else '',
            'id_fn_areceber_modelo': str(self.id_fn_areceber_modelo) if self.id_fn_areceber_modelo is not None else '',
        }

    def is_valid(self) -> bool:
        return self.id_autoincrement is not None and self.descricao is not None and self.id_conta is not None and self.remover_fundo_capa_carteira is not None

    #def __repr__(self) -> str:
        #return f"CarteiraDeCobrança(id_autoincrement={self.id_autoincrement!r}, descricao={self.descricao!r}, id_conta={self.id_conta!r}, remover_fundo_capa_carteira={self.remover_fundo_capa_carteira!r})"

    #------------------------------ CONVERSOR DTO ------------------------------#
    def dto_convert(self, data: dict[str, str]) -> IModel:
        return CarteiraDeCobrancaModel(
            id_autoincrement=int(data.get('id_autoincrement', 0)),
            descricao=data.get('descricao', ''),
            id_conta=int(data['id_conta']),
            remover_fundo_capa_carteira=data.get('remover_fundo_capa_carteira', ''),
            tipo_recebimento=Tipo_recebimentoEnum(data['tipo_recebimento']),
            envia_email_ao_gerar_finan=Envia_email_ao_gerar_finanEnum(data['envia_email_ao_gerar_finan']) if data.get('envia_email_ao_gerar_finan') else None,
            envia_push_ao_gerar_finan=Envia_push_ao_gerar_finanEnum(data['envia_push_ao_gerar_finan']) if data.get('envia_push_ao_gerar_finan') else None,
            imprime_ligacoes_voip=data.get('imprime_ligacoes_voip', ''),
            registrado=RegistradoEnum(data['registrado']),
            ativo=AtivoEnum(data['ativo']),
            filial_id=int(data['filial_id']) if data.get('filial_id') else None,
            id_config_alt_pagamento=int(data['id_config_alt_pagamento']) if data.get('id_config_alt_pagamento') else None,
            planejamento_tarifa=int(data['planejamento_tarifa']) if data.get('planejamento_tarifa') else None,
            lancamento_tarifa=Lancamento_tarifaEnum(data['lancamento_tarifa']),
            reseller_authorization_code=data.get('reseller_authorization_code', ''),
            dias_vencimento_fatura=data.get('dias_vencimento_fatura', ''),
            carteira_padrao_fatura=int(data['carteira_padrao_fatura']) if data.get('carteira_padrao_fatura') else None,
            ultima_atualizacao=data.get('ultima_atualizacao', ''),
            pedido_baixa_automatico_recorencia_cartao=Pedido_baixa_automatico_recorencia_cartaoEnum(data['pedido_baixa_automatico_recorencia_cartao']),
            aceite=data.get('aceite', ''),
            especie=EspecieEnum(data['especie']) if data.get('especie') else None,
            especie_doc=data.get('especie_doc', ''),
            taxa=data.get('taxa', ''),
            quem_emite=data.get('quem_emite', ''),
            quem_distribui=Quem_distribuiEnum(data['quem_distribui']) if data.get('quem_distribui') else None,
            endereco_envio_cobranca=Endereco_envio_cobrancaEnum(data['endereco_envio_cobranca']) if data.get('endereco_envio_cobranca') else None,
            boleto_local_atualiza=Boleto_local_atualizaEnum(data['boleto_local_atualiza']) if data.get('boleto_local_atualiza') else None,
            local_pagamento=data.get('local_pagamento', ''),
            contador_nn=int(data['contador_nn']) if data.get('contador_nn') else None,
            classe_funcoes=Classe_funcoesEnum(data['classe_funcoes']) if data.get('classe_funcoes') else None,
            versao_integracao_banrisul=Versao_integracao_banrisulEnum(data['versao_integracao_banrisul']) if data.get('versao_integracao_banrisul') else None,
            n_convenio=data.get('n_convenio', ''),
            c_cedente=data.get('c_cedente', ''),
            operacao=data.get('operacao', ''),
            codigo_edi7=data.get('codigo_edi7', ''),
            carteira=data.get('carteira', ''),
            sigla_arquivo_remessa=data.get('sigla_arquivo_remessa', ''),
            variacao_carteira=data.get('variacao_carteira', ''),
            modalidade_cobranca=data.get('modalidade_cobranca', ''),
            sicredi_byte=data.get('sicredi_byte', ''),
            sicredi_posto=data.get('sicredi_posto', ''),
            inicio_nosso_numero=data.get('inicio_nosso_numero', ''),
            nosso_numero_const1=data.get('nosso_numero_const1', ''),
            nosso_numero_const2=data.get('nosso_numero_const2', ''),
            nosso_numero1=data.get('nosso_numero1', ''),
            nosso_numero2=data.get('nosso_numero2', ''),
            conta_cosmos=data.get('conta_cosmos', ''),
            tipo_carteira=Tipo_carteiraEnum(data['tipo_carteira']) if data.get('tipo_carteira') else None,
            tipo=TipoEnum(data['tipo']) if data.get('tipo') else None,
            utliza_numero_parcela_fixo=Utliza_numero_parcela_fixoEnum(data['utliza_numero_parcela_fixo']) if data.get('utliza_numero_parcela_fixo') else None,
            pedido_baixa_automatico=Pedido_baixa_automaticoEnum(data['pedido_baixa_automatico']) if data.get('pedido_baixa_automatico') else None,
            enviar_pedido_baixa_renegociados=Enviar_pedido_baixa_renegociadosEnum(data['enviar_pedido_baixa_renegociados']) if data.get('enviar_pedido_baixa_renegociados') else None,
            pedido_baixa_automatico_rec_manual=Pedido_baixa_automatico_rec_manualEnum(data['pedido_baixa_automatico_rec_manual']) if data.get('pedido_baixa_automatico_rec_manual') else None,
            pedido_baixa_automatico_rec_cartao=Pedido_baixa_automatico_rec_cartaoEnum(data['pedido_baixa_automatico_rec_cartao']) if data.get('pedido_baixa_automatico_rec_cartao') else None,
            pedido_baixa_automatico_rec_pix=Pedido_baixa_automatico_rec_pixEnum(data['pedido_baixa_automatico_rec_pix']) if data.get('pedido_baixa_automatico_rec_pix') else None,
            adiciona_remessa_auto_alt_data=Adiciona_remessa_auto_alt_dataEnum(data['adiciona_remessa_auto_alt_data']) if data.get('adiciona_remessa_auto_alt_data') else None,
            remessa_com_mensagem=Remessa_com_mensagemEnum(data['remessa_com_mensagem']) if data.get('remessa_com_mensagem') else None,
            validar_vencidos_remessa=Validar_vencidos_remessaEnum(data['validar_vencidos_remessa']) if data.get('validar_vencidos_remessa') else None,
            validar_recebidos_remessa=Validar_recebidos_remessaEnum(data['validar_recebidos_remessa']) if data.get('validar_recebidos_remessa') else None,
            validar_clientes_bloqueados=Validar_clientes_bloqueadosEnum(data['validar_clientes_bloqueados']) if data.get('validar_clientes_bloqueados') else None,
            validar_clientes_negativados_remessa=Validar_clientes_negativados_remessaEnum(data['validar_clientes_negativados_remessa']) if data.get('validar_clientes_negativados_remessa') else None,
            l_remessa=L_remessaEnum(data['l_remessa']) if data.get('l_remessa') else None,
            l_retorno=L_retornoEnum(data['l_retorno']) if data.get('l_retorno') else None,
            codigo_flash=data.get('codigo_flash', ''),
            contabiliza_retorno_filial_emissao=Contabiliza_retorno_filial_emissaoEnum(data['contabiliza_retorno_filial_emissao']) if data.get('contabiliza_retorno_filial_emissao') else None,
            filtra_inicio_nn=Filtra_inicio_nnEnum(data['filtra_inicio_nn']),
            baixa_automatica=Baixa_automaticaEnum(data['baixa_automatica']) if data.get('baixa_automatica') else None,
            baixa_automatica_dias=data.get('baixa_automatica_dias', ''),
            utilizar_baixa_apos_vencimento=Utilizar_baixa_apos_vencimentoEnum(data['utilizar_baixa_apos_vencimento']) if data.get('utilizar_baixa_apos_vencimento') else None,
            enviar_pedido_baixa_vencimento=data.get('enviar_pedido_baixa_vencimento', ''),
            gateway_nome=Gateway_nomeEnum(data['gateway_nome']) if data.get('gateway_nome') else None,
            codigo_carteira=data.get('codigo_carteira', ''),
            workspace_id=data.get('workspace_id', ''),
            versao_api=Versao_apiEnum(data['versao_api']) if data.get('versao_api') else None,
            importado_gateway=Importado_gatewayEnum(data['importado_gateway']) if data.get('importado_gateway') else None,
            nova_api=Nova_apiEnum(data['nova_api']) if data.get('nova_api') else None,
            ambiente_homologacao_gateway=Ambiente_homologacao_gatewayEnum(data['ambiente_homologacao_gateway']) if data.get('ambiente_homologacao_gateway') else None,
            utiliza_carne=Utiliza_carneEnum(data['utiliza_carne']) if data.get('utiliza_carne') else None,
            gerencia_client_id=data.get('gerencia_client_id', ''),
            gerencia_client_secret=data.get('gerencia_client_secret', ''),
            developer_application_key=data.get('developer_application_key', ''),
            webhook_id=data.get('webhook_id', ''),
            gerencia_ip_callback=data.get('gerencia_ip_callback', ''),
            gerencia_identificador_conta=data.get('gerencia_identificador_conta', ''),
            nova_int_fortunus=Nova_int_fortunusEnum(data['nova_int_fortunus']) if data.get('nova_int_fortunus') else None,
            gateway_token=data.get('gateway_token', ''),
            carteira_widepay=data.get('carteira_widepay', ''),
            gateway_tipo_impressao=Gateway_tipo_impressaoEnum(data['gateway_tipo_impressao']) if data.get('gateway_tipo_impressao') else None,
            data_credito_pix=data.get('data_credito_pix', ''),
            data_credito_boleto=data.get('data_credito_boleto', ''),
            gateway_retorno=data.get('gateway_retorno', ''),
            adiciona_obs_descricao=Adiciona_obs_descricaoEnum(data['adiciona_obs_descricao']) if data.get('adiciona_obs_descricao') else None,
            adiciona_venc_descricao=Adiciona_venc_descricaoEnum(data['adiciona_venc_descricao']) if data.get('adiciona_venc_descricao') else None,
            dias_limite_pagamento_apos_vencimento=data.get('dias_limite_pagamento_apos_vencimento', ''),
            envia_email_gerencia=Envia_email_gerenciaEnum(data['envia_email_gerencia']) if data.get('envia_email_gerencia') else None,
            numero_conta_f2b=data.get('numero_conta_f2b', ''),
            n_convenio_credisis=data.get('n_convenio_credisis', ''),
            url_callback=data.get('url_callback', ''),
            use_webhook_url_callback=Use_webhook_url_callbackEnum(data['use_webhook_url_callback']),
            webhook_url_callback=data.get('webhook_url_callback', ''),
            data_ultima_atualizacao=data.get('data_ultima_atualizacao', ''),
            galaxPayId=data.get('galaxPayId', ''),
            galaxPayHash=data.get('galaxPayHash', ''),
            recebimento_parcial_gateway=Recebimento_parcial_gatewayEnum(data['recebimento_parcial_gateway']) if data.get('recebimento_parcial_gateway') else None,
            finalizar_cob_bf=Finalizar_cob_bfEnum(data['finalizar_cob_bf']) if data.get('finalizar_cob_bf') else None,
            especie_documento_gerencianet=data.get('especie_documento_gerencianet', ''),
            gera_pix_gateway=Gera_pix_gatewayEnum(data['gera_pix_gateway']) if data.get('gera_pix_gateway') else None,
            enviar_cobranca_pix_whatsapp=Enviar_cobranca_pix_whatsappEnum(data['enviar_cobranca_pix_whatsapp']),
            tipo_chave_pix=Tipo_chave_pixEnum(data['tipo_chave_pix']) if data.get('tipo_chave_pix') else None,
            pix_chave_santander=data.get('pix_chave_santander', ''),
            dica_chave_pix_gateway=data.get('dica_chave_pix_gateway', ''),
            lanca_tarifa_gateway=Lanca_tarifa_gatewayEnum(data['lanca_tarifa_gateway']) if data.get('lanca_tarifa_gateway') else None,
            valor_tarifa_gateway=data.get('valor_tarifa_gateway', ''),
            lanca_tarifa_pix=Lanca_tarifa_pixEnum(data['lanca_tarifa_pix']) if data.get('lanca_tarifa_pix') else None,
            valor_tarifa_pix=data.get('valor_tarifa_pix', ''),
            timeout=TimeoutEnum(data['timeout']) if data.get('timeout') else None,
            expire_at=data.get('expire_at', ''),
            creditcard_gateway=Creditcard_gatewayEnum(data['creditcard_gateway']) if data.get('creditcard_gateway') else None,
            creditCard_ambiente=CreditCard_ambienteEnum(data['creditCard_ambiente']) if data.get('creditCard_ambiente') else None,
            versao_api_cartao=Versao_api_cartaoEnum(data['versao_api_cartao']) if data.get('versao_api_cartao') else None,
            habilitar_recorrencia_cartao=Habilitar_recorrencia_cartaoEnum(data['habilitar_recorrencia_cartao']) if data.get('habilitar_recorrencia_cartao') else None,
            creditcard_user=data.get('creditcard_user', ''),
            creditcard_senha=data.get('creditcard_senha', ''),
            creditcard_senhassl=data.get('creditcard_senhassl', ''),
            creditCard_loja=data.get('creditCard_loja', ''),
            creditCard_chave=data.get('creditCard_chave', ''),
            gerencia_identificador_conta_card=data.get('gerencia_identificador_conta_card', ''),
            gateway_token_card=data.get('gateway_token_card', ''),
            gerencia_client_id_card=data.get('gerencia_client_id_card', ''),
            gerencia_client_secret_card=data.get('gerencia_client_secret_card', ''),
            gerencia_ip_callback_card=data.get('gerencia_ip_callback_card', ''),
            id_plano_vindi=data.get('id_plano_vindi', ''),
            galaxPayIdCard=data.get('galaxPayIdCard', ''),
            galaxPayHashCard=data.get('galaxPayHashCard', ''),
            galaxpay_ip_callback_card=data.get('galaxpay_ip_callback_card', ''),
            timeoutCreditCard=TimeoutCreditCardEnum(data['timeoutCreditCard']) if data.get('timeoutCreditCard') else None,
            creditcard_sslcert=data.get('creditcard_sslcert', ''),
            creditcard_sslkey=data.get('creditcard_sslkey', ''),
            creditCard_local=CreditCard_localEnum(data['creditCard_local']) if data.get('creditCard_local') else None,
            creditCard_autenticar=data.get('creditCard_autenticar', ''),
            creditCard_capturar=data.get('creditCard_capturar', ''),
            creditCard_autorizar=CreditCard_autorizarEnum(data['creditCard_autorizar']) if data.get('creditCard_autorizar') else None,
            credit_card_tipo=data.get('credit_card_tipo', ''),
            creditCard_parcelamento=CreditCard_parcelamentoEnum(data['creditCard_parcelamento']) if data.get('creditCard_parcelamento') else None,
            creditCard_Nparcelas=data.get('creditCard_Nparcelas', ''),
            creditCard_juro=data.get('creditCard_juro', ''),
            credit_card_repassar_taxa=Credit_card_repassar_taxaEnum(data['credit_card_repassar_taxa']),
            tip_fee_transfer=data.get('tip_fee_transfer', ''),
            credit_card_taxa_em_pagamentos=Credit_card_taxa_em_pagamentosEnum(data['credit_card_taxa_em_pagamentos']),
            credit_card_porcentagem_taxa=data.get('credit_card_porcentagem_taxa', ''),
            credit_card_valor_taxa=data.get('credit_card_valor_taxa', ''),
            creditcard_banceira_vi=data.get('creditcard_banceira_vi', ''),
            creditcard_banceira_ma=data.get('creditcard_banceira_ma', ''),
            creditcard_banceira_am=data.get('creditcard_banceira_am', ''),
            creditcard_banceira_el=data.get('creditcard_banceira_el', ''),
            creditcard_banceira_dn=data.get('creditcard_banceira_dn', ''),
            creditcard_banceira_dc=data.get('creditcard_banceira_dc', ''),
            creditcard_banceira_jc=data.get('creditcard_banceira_jc', ''),
            creditcard_banceira_au=data.get('creditcard_banceira_au', ''),
            creditcard_banceira_ca=data.get('creditcard_banceira_ca', ''),
            debito_convenio=data.get('debito_convenio', ''),
            debito_carteira_vinculada=int(data['debito_carteira_vinculada']) if data.get('debito_carteira_vinculada') else None,
            debito_classe=Debito_classeEnum(data['debito_classe']) if data.get('debito_classe') else None,
            validar_vencidos_remessa_D=Validar_vencidos_remessa_DEnum(data['validar_vencidos_remessa_D']) if data.get('validar_vencidos_remessa_D') else None,
            data_credito_debito_em_conta=data.get('data_credito_debito_em_conta', ''),
            valor_tarifa=data.get('valor_tarifa', ''),
            substrair_tarifa=data.get('substrair_tarifa', ''),
            pix_gateway=Pix_gatewayEnum(data['pix_gateway']) if data.get('pix_gateway') else None,
            pix_ambiente=Pix_ambienteEnum(data['pix_ambiente']) if data.get('pix_ambiente') else None,
            pix_chave=data.get('pix_chave', ''),
            pix_client_id=data.get('pix_client_id', ''),
            pix_client_secret=data.get('pix_client_secret', ''),
            pix_tempo_validade=data.get('pix_tempo_validade', ''),
            pix_certificado=data.get('pix_certificado', ''),
            pix_gerencia_ip_callback=data.get('pix_gerencia_ip_callback', ''),
            pix_modalidade=Pix_modalidadeEnum(data['pix_modalidade']) if data.get('pix_modalidade') else None,
            permite_pagamento_por_chave_pix=Permite_pagamento_por_chave_pixEnum(data['permite_pagamento_por_chave_pix']),
            enviar_cobranca_pix_whatsapp_carteiras_pix=Enviar_cobranca_pix_whatsapp_carteiras_pixEnum(data['enviar_cobranca_pix_whatsapp_carteiras_pix']),
            tipo_chave_pix_carteiras_pix=Tipo_chave_pix_carteiras_pixEnum(data['tipo_chave_pix_carteiras_pix']) if data.get('tipo_chave_pix_carteiras_pix') else None,
            utiliza_pix_recorrente=Utiliza_pix_recorrenteEnum(data['utiliza_pix_recorrente']) if data.get('utiliza_pix_recorrente') else None,
            permite_retentativas_pix_recorrente=Permite_retentativas_pix_recorrenteEnum(data['permite_retentativas_pix_recorrente']) if data.get('permite_retentativas_pix_recorrente') else None,
            fieldset_dica_configuracoes_pix=data.get('fieldset_dica_configuracoes_pix', ''),
            lanca_tarifa_pix_modobank=Lanca_tarifa_pix_modobankEnum(data['lanca_tarifa_pix_modobank']),
            valor_tarifa_pix_modobank=data.get('valor_tarifa_pix_modobank', ''),
            jurop_mes=data.get('jurop_mes', ''),
            juros_boleto_juno=data.get('juros_boleto_juno', ''),
            jurop=data.get('jurop', ''),
            jurov=data.get('jurov', ''),
            multap=data.get('multap', ''),
            multav=data.get('multav', ''),
            desconto_v=data.get('desconto_v', ''),
            desconto_p=data.get('desconto_p', ''),
            desconto_condicional_valor=data.get('desconto_condicional_valor', ''),
            desconto_condicional_percentual=data.get('desconto_condicional_percentual', ''),
            data_validade_condicional=data.get('data_validade_condicional', ''),
            desconto_proporcional=data.get('desconto_proporcional', ''),
            protestar=data.get('protestar', ''),
            atraso=data.get('atraso', ''),
            calcular_juros=Calcular_jurosEnum(data['calcular_juros']) if data.get('calcular_juros') else None,
            permite_atualizar_boleto_apos_data_ixc=data.get('permite_atualizar_boleto_apos_data_ixc', ''),
            instrucao1=data.get('instrucao1', ''),
            instrucao2=data.get('instrucao2', ''),
            instrucao3=data.get('instrucao3', ''),
            instrucao4=data.get('instrucao4', ''),
            instrucao5=data.get('instrucao5', ''),
            instrucao6=data.get('instrucao6', ''),
            instrucao7=data.get('instrucao7', ''),
            instrucao8=data.get('instrucao8', ''),
            imp_inst_vencido=data.get('imp_inst_vencido', ''),
            imp_inst_proporcional=data.get('imp_inst_proporcional', ''),
            obs_fn_areceber=Obs_fn_areceberEnum(data['obs_fn_areceber']) if data.get('obs_fn_areceber') else None,
            obs_anterior=data.get('obs_anterior', ''),
            obs_posterior=data.get('obs_posterior', ''),
            l_impressao=L_impressaoEnum(data['l_impressao']) if data.get('l_impressao') else None,
            formato_detalhamento_fatura=Formato_detalhamento_faturaEnum(data['formato_detalhamento_fatura']) if data.get('formato_detalhamento_fatura') else None,
            cor_fatura=data.get('cor_fatura', ''),
            informative_text=data.get('informative_text', ''),
            imprimir_filial_venda=Imprimir_filial_vendaEnum(data['imprimir_filial_venda']) if data.get('imprimir_filial_venda') else None,
            imprimir_filial_conta=Imprimir_filial_contaEnum(data['imprimir_filial_conta']) if data.get('imprimir_filial_conta') else None,
            considerar_modelo_nao_fiscal=Considerar_modelo_nao_fiscalEnum(data['considerar_modelo_nao_fiscal']) if data.get('considerar_modelo_nao_fiscal') else None,
            imprime_endereco_boleto=Imprime_endereco_boletoEnum(data['imprime_endereco_boleto']) if data.get('imprime_endereco_boleto') else None,
            imprime_fone_fatura_d=Imprime_fone_fatura_dEnum(data['imprime_fone_fatura_d']) if data.get('imprime_fone_fatura_d') else None,
            imp_nome_sacador_avalista=Imp_nome_sacador_avalistaEnum(data['imp_nome_sacador_avalista']) if data.get('imp_nome_sacador_avalista') else None,
            imprime_prod_val_zero=Imprime_prod_val_zeroEnum(data['imprime_prod_val_zero']) if data.get('imprime_prod_val_zero') else None,
            imprime_tipo_resolucao_anatel=Imprime_tipo_resolucao_anatelEnum(data['imprime_tipo_resolucao_anatel']) if data.get('imprime_tipo_resolucao_anatel') else None,
            mask_cpf_cnpj_impressao_boleto=Mask_cpf_cnpj_impressao_boletoEnum(data['mask_cpf_cnpj_impressao_boleto']) if data.get('mask_cpf_cnpj_impressao_boleto') else None,
            mostra_cep_beneficiario_impressao=Mostra_cep_beneficiario_impressaoEnum(data['mostra_cep_beneficiario_impressao']) if data.get('mostra_cep_beneficiario_impressao') else None,
            agrupar_produtos_por_descricao=Agrupar_produtos_por_descricaoEnum(data['agrupar_produtos_por_descricao']) if data.get('agrupar_produtos_por_descricao') else None,
            imprimir_beneficiario_gateway=Imprimir_beneficiario_gatewayEnum(data['imprimir_beneficiario_gateway']) if data.get('imprimir_beneficiario_gateway') else None,
            obs_adicional_boleto=data.get('obs_adicional_boleto', ''),
            imp_nome_beneficiario=Imp_nome_beneficiarioEnum(data['imp_nome_beneficiario']),
            imp_nome_beneficiario_recibo=Imp_nome_beneficiario_reciboEnum(data['imp_nome_beneficiario_recibo']) if data.get('imp_nome_beneficiario_recibo') else None,
            boletos_capa_contratos=Boletos_capa_contratosEnum(data['boletos_capa_contratos']) if data.get('boletos_capa_contratos') else None,
            boleto_capa=data.get('boleto_capa', ''),
            boleto_capa_cliente_referencia=data.get('boleto_capa_cliente_referencia', ''),
            fone_cliente_capa=data.get('fone_cliente_capa', ''),
            boleto_capa_local=Boleto_capa_localEnum(data['boleto_capa_local']) if data.get('boleto_capa_local') else None,
            boleto_capa_imagem=data.get('boleto_capa_imagem', ''),
            boleto_capa_x=data.get('boleto_capa_x', ''),
            boleto_capa_y=data.get('boleto_capa_y', ''),
            tamanho_quadro_endereco_x=data.get('tamanho_quadro_endereco_x', ''),
            tamanho_quadro_endereco_y=data.get('tamanho_quadro_endereco_y', ''),
            tipo_baixa=Tipo_baixaEnum(data['tipo_baixa']) if data.get('tipo_baixa') else None,
            validar_juros_multa=Validar_juros_multaEnum(data['validar_juros_multa']) if data.get('validar_juros_multa') else None,
            id_produto_cob_adicional=int(data['id_produto_cob_adicional']) if data.get('id_produto_cob_adicional') else None,
            id_fn_areceber_modelo=int(data['id_fn_areceber_modelo']) if data.get('id_fn_areceber_modelo') else None,
        )
