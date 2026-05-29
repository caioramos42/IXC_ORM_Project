from __future__ import annotations
from typing import Any, Optional
from ORM_IXC.enums.carteiraDeCobranca import *
from ORM_IXC.interfaces import IModel, IModelWithId
from ORM_IXC.statemants.classBase import Field
from ORM_IXC.statemants.mapper import Mapped, field as mapped_field
from ORM_IXC.statemants.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel


@MetaModels
class CarteiraDeCobrancaModel(IModelWithId, BaseModel):
    id :Mapped[Optional[int]] = mapped_field()
    descricao :Mapped[str] = mapped_field()
    id_conta :Mapped[int] = mapped_field()
    remover_fundo_capa_carteira :Mapped[str] = mapped_field()
    tipo_recebimento :Mapped[Tipo_recebimentoEnum] = mapped_field(Tipo_recebimentoEnum.BOLETO)
    envia_email_ao_gerar_finan :Mapped[Optional[Envia_email_ao_gerar_finanEnum]] = mapped_field(Envia_email_ao_gerar_finanEnum.NAO)
    envia_push_ao_gerar_finan :Mapped[Optional[Envia_push_ao_gerar_finanEnum]] = mapped_field(Envia_push_ao_gerar_finanEnum.NAO)
    imprime_ligacoes_voip :Mapped[Optional[str]] = mapped_field('')
    registrado :Mapped[RegistradoEnum] = mapped_field(RegistradoEnum.SIM)
    ativo :Mapped[AtivoEnum] = mapped_field(AtivoEnum.SIM)
    filial_id :Mapped[Optional[int]] = mapped_field(None)
    id_config_alt_pagamento :Mapped[Optional[int]] = mapped_field(None)
    planejamento_tarifa :Mapped[Optional[int]] = mapped_field(None)
    lancamento_tarifa :Mapped[Lancamento_tarifaEnum] = mapped_field(Lancamento_tarifaEnum.NA_DATA_DO_PAGAMENTO)
    reseller_authorization_code :Mapped[Optional[str]] = mapped_field('')
    dias_vencimento_fatura :Mapped[Optional[str]] = mapped_field('')
    carteira_padrao_fatura :Mapped[Optional[int]] = mapped_field(None)
    ultima_atualizacao :Mapped[Optional[str]] = mapped_field('')
    pedido_baixa_automatico_recorencia_cartao :Mapped[Pedido_baixa_automatico_recorencia_cartaoEnum] = mapped_field(Pedido_baixa_automatico_recorencia_cartaoEnum.SIM)
    aceite :Mapped[Optional[str]] = mapped_field('')
    especie :Mapped[Optional[EspecieEnum]] = mapped_field(EspecieEnum.RS)
    especie_doc :Mapped[Optional[str]] = mapped_field('')
    taxa :Mapped[Optional[str]] = mapped_field('')
    quem_emite :Mapped[Optional[str]] = mapped_field('')
    quem_distribui :Mapped[Optional[Quem_distribuiEnum]] = mapped_field(Quem_distribuiEnum.EMPRESA)
    endereco_envio_cobranca :Mapped[Optional[Endereco_envio_cobrancaEnum]] = mapped_field(Endereco_envio_cobrancaEnum.COBRANCA)
    boleto_local_atualiza :Mapped[Optional[Boleto_local_atualizaEnum]] = mapped_field(Boleto_local_atualizaEnum.SISTEMA)
    local_pagamento :Mapped[Optional[str]] = mapped_field('')
    contador_nn :Mapped[Optional[int]] = mapped_field(None)
    classe_funcoes :Mapped[Optional[Classe_funcoesEnum]] = mapped_field(None)
    versao_integracao_banrisul :Mapped[Optional[Versao_integracao_banrisulEnum]] = mapped_field(Versao_integracao_banrisulEnum.V1)
    n_convenio :Mapped[Optional[str]] = mapped_field('')
    c_cedente :Mapped[Optional[str]] = mapped_field('')
    operacao :Mapped[Optional[str]] = mapped_field('')
    codigo_edi7 :Mapped[Optional[str]] = mapped_field('')
    carteira :Mapped[Optional[str]] = mapped_field('')
    sigla_arquivo_remessa :Mapped[Optional[str]] = mapped_field('')
    variacao_carteira :Mapped[Optional[str]] = mapped_field('')
    modalidade_cobranca :Mapped[Optional[str]] = mapped_field('')
    sicredi_byte :Mapped[Optional[str]] = mapped_field('')
    sicredi_posto :Mapped[Optional[str]] = mapped_field('')
    inicio_nosso_numero :Mapped[Optional[str]] = mapped_field('')
    nosso_numero_const1 :Mapped[Optional[str]] = mapped_field('')
    nosso_numero_const2 :Mapped[Optional[str]] = mapped_field('')
    nosso_numero1 :Mapped[Optional[str]] = mapped_field('')
    nosso_numero2 :Mapped[Optional[str]] = mapped_field('')
    conta_cosmos :Mapped[Optional[str]] = mapped_field('')
    tipo_carteira :Mapped[Optional[Tipo_carteiraEnum]] = mapped_field(Tipo_carteiraEnum.SIMPLES)
    tipo :Mapped[Optional[TipoEnum]] = mapped_field(None)
    utliza_numero_parcela_fixo :Mapped[Optional[Utliza_numero_parcela_fixoEnum]] = mapped_field(Utliza_numero_parcela_fixoEnum.SIM)
    pedido_baixa_automatico :Mapped[Optional[Pedido_baixa_automaticoEnum]] = mapped_field(Pedido_baixa_automaticoEnum.SIM)
    enviar_pedido_baixa_renegociados :Mapped[Optional[Enviar_pedido_baixa_renegociadosEnum]] = mapped_field(Enviar_pedido_baixa_renegociadosEnum.SIM)
    pedido_baixa_automatico_rec_manual :Mapped[Optional[Pedido_baixa_automatico_rec_manualEnum]] = mapped_field(Pedido_baixa_automatico_rec_manualEnum.SIM)
    pedido_baixa_automatico_rec_cartao :Mapped[Optional[Pedido_baixa_automatico_rec_cartaoEnum]] = mapped_field(Pedido_baixa_automatico_rec_cartaoEnum.SIM)
    pedido_baixa_automatico_rec_pix :Mapped[Optional[Pedido_baixa_automatico_rec_pixEnum]] = mapped_field(Pedido_baixa_automatico_rec_pixEnum.SIM)
    adiciona_remessa_auto_alt_data :Mapped[Optional[Adiciona_remessa_auto_alt_dataEnum]] = mapped_field(Adiciona_remessa_auto_alt_dataEnum.NAO)
    remessa_com_mensagem :Mapped[Optional[Remessa_com_mensagemEnum]] = mapped_field(Remessa_com_mensagemEnum.NAO)
    validar_vencidos_remessa :Mapped[Optional[Validar_vencidos_remessaEnum]] = mapped_field(Validar_vencidos_remessaEnum.SIM)
    validar_recebidos_remessa :Mapped[Optional[Validar_recebidos_remessaEnum]] = mapped_field(Validar_recebidos_remessaEnum.SIM)
    validar_clientes_bloqueados :Mapped[Optional[Validar_clientes_bloqueadosEnum]] = mapped_field(Validar_clientes_bloqueadosEnum.NAO)
    validar_clientes_negativados_remessa :Mapped[Optional[Validar_clientes_negativados_remessaEnum]] = mapped_field(Validar_clientes_negativados_remessaEnum.NAO)
    l_remessa :Mapped[Optional[L_remessaEnum]] = mapped_field(None)
    l_retorno :Mapped[Optional[L_retornoEnum]] = mapped_field(None)
    codigo_flash :Mapped[Optional[str]] = mapped_field('')
    contabiliza_retorno_filial_emissao :Mapped[Optional[Contabiliza_retorno_filial_emissaoEnum]] = mapped_field(Contabiliza_retorno_filial_emissaoEnum.NAO)
    filtra_inicio_nn :Mapped[Filtra_inicio_nnEnum] = mapped_field(Filtra_inicio_nnEnum.SIM)
    baixa_automatica :Mapped[Optional[Baixa_automaticaEnum]] = mapped_field(Baixa_automaticaEnum.SIM)
    baixa_automatica_dias :Mapped[Optional[str]] = mapped_field('')
    utilizar_baixa_apos_vencimento :Mapped[Optional[Utilizar_baixa_apos_vencimentoEnum]] = mapped_field(Utilizar_baixa_apos_vencimentoEnum.NAO)
    enviar_pedido_baixa_vencimento :Mapped[Optional[str]] = mapped_field('')
    gateway_nome :Mapped[Optional[Gateway_nomeEnum]] = mapped_field(None)
    codigo_carteira :Mapped[Optional[str]] = mapped_field('')
    workspace_id :Mapped[Optional[str]] = mapped_field('')
    versao_api :Mapped[Optional[Versao_apiEnum]] = mapped_field(Versao_apiEnum.V1)
    importado_gateway :Mapped[Optional[Importado_gatewayEnum]] = mapped_field(Importado_gatewayEnum.NAO)
    nova_api :Mapped[Optional[Nova_apiEnum]] = mapped_field(Nova_apiEnum.SIM)
    ambiente_homologacao_gateway :Mapped[Optional[Ambiente_homologacao_gatewayEnum]] = mapped_field(Ambiente_homologacao_gatewayEnum.PRODUCAO)
    utiliza_carne :Mapped[Optional[Utiliza_carneEnum]] = mapped_field(Utiliza_carneEnum.NAO)
    gerencia_client_id :Mapped[Optional[str]] = mapped_field('')
    gerencia_client_secret :Mapped[Optional[Any]] = mapped_field(None)
    developer_application_key :Mapped[Optional[str]] = mapped_field('')
    webhook_id :Mapped[Optional[str]] = mapped_field('')
    gerencia_ip_callback :Mapped[Optional[str]] = mapped_field('')
    gerencia_identificador_conta :Mapped[Optional[str]] = mapped_field('')
    nova_int_fortunus :Mapped[Optional[Nova_int_fortunusEnum]] = mapped_field(Nova_int_fortunusEnum.NAO)
    gateway_token :Mapped[Optional[Any]] = mapped_field(None)
    carteira_widepay :Mapped[Optional[str]] = mapped_field('')
    gateway_tipo_impressao :Mapped[Optional[Gateway_tipo_impressaoEnum]] = mapped_field(Gateway_tipo_impressaoEnum.CARNE)
    data_credito_pix :Mapped[Optional[str]] = mapped_field('')
    data_credito_boleto :Mapped[Optional[str]] = mapped_field('')
    gateway_retorno :Mapped[Optional[str]] = mapped_field('')
    adiciona_obs_descricao :Mapped[Optional[Adiciona_obs_descricaoEnum]] = mapped_field(Adiciona_obs_descricaoEnum.NAO)
    adiciona_venc_descricao :Mapped[Optional[Adiciona_venc_descricaoEnum]] = mapped_field(Adiciona_venc_descricaoEnum.NAO)
    dias_limite_pagamento_apos_vencimento :Mapped[Optional[str]] = mapped_field('')
    envia_email_gerencia :Mapped[Optional[Envia_email_gerenciaEnum]] = mapped_field(Envia_email_gerenciaEnum.NAO)
    numero_conta_f2b :Mapped[Optional[str]] = mapped_field('')
    n_convenio_credisis :Mapped[Optional[str]] = mapped_field('')
    url_callback :Mapped[Optional[str]] = mapped_field('')
    use_webhook_url_callback :Mapped[Use_webhook_url_callbackEnum] = mapped_field(Use_webhook_url_callbackEnum.NAO)
    webhook_url_callback :Mapped[Optional[str]] = mapped_field('')
    data_ultima_atualizacao :Mapped[Optional[str]] = mapped_field('')
    galaxPayId :Mapped[Optional[str]] = mapped_field('')
    galaxPayHash :Mapped[Optional[str]] = mapped_field('')
    recebimento_parcial_gateway :Mapped[Optional[Recebimento_parcial_gatewayEnum]] = mapped_field(Recebimento_parcial_gatewayEnum.NAO)
    finalizar_cob_bf :Mapped[Optional[Finalizar_cob_bfEnum]] = mapped_field(Finalizar_cob_bfEnum.SIM)
    especie_documento_gerencianet :Mapped[Optional[str]] = mapped_field('')
    gera_pix_gateway :Mapped[Optional[Gera_pix_gatewayEnum]] = mapped_field(Gera_pix_gatewayEnum.NAO)
    enviar_cobranca_pix_whatsapp :Mapped[Enviar_cobranca_pix_whatsappEnum] = mapped_field(Enviar_cobranca_pix_whatsappEnum.NAO)
    tipo_chave_pix :Mapped[Optional[Tipo_chave_pixEnum]] = mapped_field(None)
    pix_chave_santander :Mapped[Optional[str]] = mapped_field('')
    dica_chave_pix_gateway :Mapped[Optional[str]] = mapped_field('')
    lanca_tarifa_gateway :Mapped[Optional[Lanca_tarifa_gatewayEnum]] = mapped_field(Lanca_tarifa_gatewayEnum.NAO_LANCA)
    valor_tarifa_gateway :Mapped[Optional[str]] = mapped_field('')
    lanca_tarifa_pix :Mapped[Optional[Lanca_tarifa_pixEnum]] = mapped_field(Lanca_tarifa_pixEnum.NAO)
    valor_tarifa_pix :Mapped[Optional[str]] = mapped_field('')
    timeout :Mapped[Optional[TimeoutEnum]] = mapped_field(TimeoutEnum.T60)
    expire_at :Mapped[Optional[str]] = mapped_field('')
    creditcard_gateway :Mapped[Optional[Creditcard_gatewayEnum]] = mapped_field(None)
    creditCard_ambiente :Mapped[Optional[CreditCard_ambienteEnum]] = mapped_field(CreditCard_ambienteEnum.TESTE)
    versao_api_cartao :Mapped[Optional[Versao_api_cartaoEnum]] = mapped_field(None)
    habilitar_recorrencia_cartao :Mapped[Optional[Habilitar_recorrencia_cartaoEnum]] = mapped_field(Habilitar_recorrencia_cartaoEnum.NAO)
    creditcard_user :Mapped[Optional[str]] = mapped_field('')
    creditcard_senha :Mapped[Optional[str]] = mapped_field('')
    creditcard_senhassl :Mapped[Optional[str]] = mapped_field('')
    creditCard_loja :Mapped[Optional[str]] = mapped_field('')
    creditCard_chave :Mapped[Optional[str]] = mapped_field('')
    gerencia_identificador_conta_card :Mapped[Optional[str]] = mapped_field('')
    gateway_token_card :Mapped[Optional[Any]] = mapped_field(None)
    gerencia_client_id_card :Mapped[Optional[str]] = mapped_field('')
    gerencia_client_secret_card :Mapped[Optional[Any]] = mapped_field(None)
    gerencia_ip_callback_card :Mapped[Optional[str]] = mapped_field('')
    id_plano_vindi :Mapped[Optional[str]] = mapped_field('')
    galaxPayIdCard :Mapped[Optional[str]] = mapped_field('')
    galaxPayHashCard :Mapped[Optional[str]] = mapped_field('')
    galaxpay_ip_callback_card :Mapped[Optional[str]] = mapped_field('')
    timeoutCreditCard :Mapped[Optional[TimeoutCreditCardEnum]] = mapped_field(TimeoutCreditCardEnum.T60)
    creditcard_sslcert :Mapped[Optional[Any]] = mapped_field(None)
    creditcard_sslkey :Mapped[Optional[Any]] = mapped_field(None)
    creditCard_local :Mapped[Optional[CreditCard_localEnum]] = mapped_field(CreditCard_localEnum.BUY_PAGE_LOJA)
    creditCard_autenticar :Mapped[Optional[str]] = mapped_field('')
    creditCard_capturar :Mapped[Optional[str]] = mapped_field('')
    creditCard_autorizar :Mapped[Optional[CreditCard_autorizarEnum]] = mapped_field(CreditCard_autorizarEnum.AUTORIZAR_DIRETO)
    credit_card_tipo :Mapped[Optional[str]] = mapped_field('')
    creditCard_parcelamento :Mapped[Optional[CreditCard_parcelamentoEnum]] = mapped_field(CreditCard_parcelamentoEnum.ADMINISTRADORA)
    creditCard_Nparcelas :Mapped[Optional[str]] = mapped_field('')
    creditCard_juro :Mapped[Optional[str]] = mapped_field('')
    credit_card_repassar_taxa :Mapped[Credit_card_repassar_taxaEnum] = mapped_field(Credit_card_repassar_taxaEnum.NAO)
    tip_fee_transfer :Mapped[Optional[str]] = mapped_field('')
    credit_card_taxa_em_pagamentos :Mapped[Credit_card_taxa_em_pagamentosEnum] = mapped_field(Credit_card_taxa_em_pagamentosEnum.AMBOS)
    credit_card_porcentagem_taxa :Mapped[Optional[str]] = mapped_field('')
    credit_card_valor_taxa :Mapped[Optional[str]] = mapped_field('')
    creditcard_banceira_vi :Mapped[Optional[str]] = mapped_field('')
    creditcard_banceira_ma :Mapped[Optional[str]] = mapped_field('')
    creditcard_banceira_am :Mapped[Optional[str]] = mapped_field('')
    creditcard_banceira_el :Mapped[Optional[str]] = mapped_field('')
    creditcard_banceira_dn :Mapped[Optional[str]] = mapped_field('')
    creditcard_banceira_dc :Mapped[Optional[str]] = mapped_field('')
    creditcard_banceira_jc :Mapped[Optional[str]] = mapped_field('')
    creditcard_banceira_au :Mapped[Optional[str]] = mapped_field('')
    creditcard_banceira_ca :Mapped[Optional[str]] = mapped_field('')
    debito_convenio :Mapped[Optional[str]] = mapped_field('')
    debito_carteira_vinculada :Mapped[Optional[int]] = mapped_field(None)
    debito_classe :Mapped[Optional[Debito_classeEnum]] = mapped_field(None)
    validar_vencidos_remessa_D :Mapped[Optional[Validar_vencidos_remessa_DEnum]] = mapped_field(Validar_vencidos_remessa_DEnum.SIM)
    data_credito_debito_em_conta :Mapped[Optional[str]] = mapped_field('')
    valor_tarifa :Mapped[Optional[str]] = mapped_field('')
    substrair_tarifa :Mapped[Optional[str]] = mapped_field('')
    pix_gateway :Mapped[Optional[Pix_gatewayEnum]] = mapped_field(None)
    pix_ambiente :Mapped[Optional[Pix_ambienteEnum]] = mapped_field(Pix_ambienteEnum.PRODUCAO)
    pix_chave :Mapped[Optional[str]] = mapped_field('')
    pix_client_id :Mapped[Optional[str]] = mapped_field('')
    pix_client_secret :Mapped[Optional[Any]] = mapped_field(None)
    pix_tempo_validade :Mapped[Optional[str]] = mapped_field('')
    pix_certificado :Mapped[Optional[Any]] = mapped_field(None)
    pix_gerencia_ip_callback :Mapped[Optional[str]] = mapped_field('')
    pix_modalidade :Mapped[Optional[Pix_modalidadeEnum]] = mapped_field(Pix_modalidadeEnum.IMEDIATA)
    permite_pagamento_por_chave_pix :Mapped[Permite_pagamento_por_chave_pixEnum] = mapped_field(Permite_pagamento_por_chave_pixEnum.SIM)
    enviar_cobranca_pix_whatsapp_carteiras_pix :Mapped[Enviar_cobranca_pix_whatsapp_carteiras_pixEnum] = mapped_field(Enviar_cobranca_pix_whatsapp_carteiras_pixEnum.NAO)
    tipo_chave_pix_carteiras_pix :Mapped[Optional[Tipo_chave_pix_carteiras_pixEnum]] = mapped_field(None)
    utiliza_pix_recorrente :Mapped[Optional[Utiliza_pix_recorrenteEnum]] = mapped_field(Utiliza_pix_recorrenteEnum.NAO)
    permite_retentativas_pix_recorrente :Mapped[Optional[Permite_retentativas_pix_recorrenteEnum]] = mapped_field(Permite_retentativas_pix_recorrenteEnum.SIM)
    fieldset_dica_configuracoes_pix :Mapped[Optional[str]] = mapped_field('')
    lanca_tarifa_pix_modobank :Mapped[Lanca_tarifa_pix_modobankEnum] = mapped_field(Lanca_tarifa_pix_modobankEnum.NAO)
    valor_tarifa_pix_modobank :Mapped[Optional[str]] = mapped_field('')
    jurop_mes :Mapped[Optional[str]] = mapped_field('')
    juros_boleto_juno :Mapped[Optional[str]] = mapped_field('')
    jurop :Mapped[Optional[str]] = mapped_field('')
    jurov :Mapped[Optional[str]] = mapped_field('')
    multap :Mapped[Optional[str]] = mapped_field('')
    multav :Mapped[Optional[str]] = mapped_field('')
    desconto_v :Mapped[Optional[str]] = mapped_field('')
    desconto_p :Mapped[Optional[str]] = mapped_field('')
    desconto_condicional_valor :Mapped[Optional[str]] = mapped_field('')
    desconto_condicional_percentual :Mapped[Optional[str]] = mapped_field('')
    data_validade_condicional :Mapped[Optional[str]] = mapped_field('')
    desconto_proporcional :Mapped[Optional[str]] = mapped_field('')
    protestar :Mapped[Optional[str]] = mapped_field('')
    atraso :Mapped[Optional[str]] = mapped_field('')
    calcular_juros :Mapped[Optional[Calcular_jurosEnum]] = mapped_field(Calcular_jurosEnum.ATE_O_DIA_ATUAL)
    permite_atualizar_boleto_apos_data_ixc :Mapped[Optional[str]] = mapped_field('')
    instrucao1 :Mapped[Optional[str]] = mapped_field('')
    instrucao2 :Mapped[Optional[str]] = mapped_field('')
    instrucao3 :Mapped[Optional[str]] = mapped_field('')
    instrucao4 :Mapped[Optional[str]] = mapped_field('')
    instrucao5 :Mapped[Optional[str]] = mapped_field('')
    instrucao6 :Mapped[Optional[str]] = mapped_field('')
    instrucao7 :Mapped[Optional[str]] = mapped_field('')
    instrucao8 :Mapped[Optional[str]] = mapped_field('')
    imp_inst_vencido :Mapped[Optional[str]] = mapped_field('')
    imp_inst_proporcional :Mapped[Optional[str]] = mapped_field('')
    obs_fn_areceber :Mapped[Optional[Obs_fn_areceberEnum]] = mapped_field(Obs_fn_areceberEnum.SIM)
    obs_anterior :Mapped[Optional[str]] = mapped_field('')
    obs_posterior :Mapped[Optional[str]] = mapped_field('')
    l_impressao :Mapped[Optional[L_impressaoEnum]] = mapped_field(None)
    formato_detalhamento_fatura :Mapped[Optional[Formato_detalhamento_faturaEnum]] = mapped_field(Formato_detalhamento_faturaEnum.PLANO)
    cor_fatura :Mapped[Optional[str]] = mapped_field('')
    informative_text :Mapped[Optional[str]] = mapped_field('')
    imprimir_filial_venda :Mapped[Optional[Imprimir_filial_vendaEnum]] = mapped_field(Imprimir_filial_vendaEnum.CONTA)
    imprimir_filial_conta :Mapped[Optional[Imprimir_filial_contaEnum]] = mapped_field(Imprimir_filial_contaEnum.VENDA)
    considerar_modelo_nao_fiscal :Mapped[Optional[Considerar_modelo_nao_fiscalEnum]] = mapped_field(Considerar_modelo_nao_fiscalEnum.NAO)
    imprime_endereco_boleto :Mapped[Optional[Imprime_endereco_boletoEnum]] = mapped_field(Imprime_endereco_boletoEnum.SIM)
    imprime_fone_fatura_d :Mapped[Optional[Imprime_fone_fatura_dEnum]] = mapped_field(Imprime_fone_fatura_dEnum.NAO)
    imp_nome_sacador_avalista :Mapped[Optional[Imp_nome_sacador_avalistaEnum]] = mapped_field(Imp_nome_sacador_avalistaEnum.SIM)
    imprime_prod_val_zero :Mapped[Optional[Imprime_prod_val_zeroEnum]] = mapped_field(Imprime_prod_val_zeroEnum.SIM)
    imprime_tipo_resolucao_anatel :Mapped[Optional[Imprime_tipo_resolucao_anatelEnum]] = mapped_field(Imprime_tipo_resolucao_anatelEnum.NAO)
    mask_cpf_cnpj_impressao_boleto :Mapped[Optional[Mask_cpf_cnpj_impressao_boletoEnum]] = mapped_field(Mask_cpf_cnpj_impressao_boletoEnum.NAO)
    mostra_cep_beneficiario_impressao :Mapped[Optional[Mostra_cep_beneficiario_impressaoEnum]] = mapped_field(Mostra_cep_beneficiario_impressaoEnum.NAO)
    agrupar_produtos_por_descricao :Mapped[Optional[Agrupar_produtos_por_descricaoEnum]] = mapped_field(Agrupar_produtos_por_descricaoEnum.NAO)
    imprimir_beneficiario_gateway :Mapped[Optional[Imprimir_beneficiario_gatewayEnum]] = mapped_field(Imprimir_beneficiario_gatewayEnum.RAZAO_SOCIAL)
    obs_adicional_boleto :Mapped[Optional[str]] = mapped_field('')
    imp_nome_beneficiario :Mapped[Imp_nome_beneficiarioEnum] = mapped_field(Imp_nome_beneficiarioEnum.RAZAO_SOCIAL)
    imp_nome_beneficiario_recibo :Mapped[Optional[Imp_nome_beneficiario_reciboEnum]] = mapped_field(Imp_nome_beneficiario_reciboEnum.RAZAO_SOCIAL)
    boletos_capa_contratos :Mapped[Optional[Boletos_capa_contratosEnum]] = mapped_field(Boletos_capa_contratosEnum.NAO)
    boleto_capa :Mapped[Optional[str]] = mapped_field('')
    boleto_capa_cliente_referencia :Mapped[Optional[str]] = mapped_field('')
    fone_cliente_capa :Mapped[Optional[str]] = mapped_field('')
    boleto_capa_local :Mapped[Optional[Boleto_capa_localEnum]] = mapped_field(Boleto_capa_localEnum.NO_INICIO)
    boleto_capa_imagem :Mapped[Optional[Any]] = mapped_field(None)
    boleto_capa_x :Mapped[Optional[str]] = mapped_field('')
    boleto_capa_y :Mapped[Optional[str]] = mapped_field('')
    tamanho_quadro_endereco_x :Mapped[Optional[str]] = mapped_field('')
    tamanho_quadro_endereco_y :Mapped[Optional[str]] = mapped_field('')
    tipo_baixa :Mapped[Optional[Tipo_baixaEnum]] = mapped_field(Tipo_baixaEnum.DESCONTO)
    validar_juros_multa :Mapped[Optional[Validar_juros_multaEnum]] = mapped_field(Validar_juros_multaEnum.NAO)
    id_produto_cob_adicional :Mapped[Optional[int]] = mapped_field(None)
    id_fn_areceber_modelo :Mapped[Optional[int]] = mapped_field(None)

    @property
    def table(self) -> str:
        return "fn_carteira_cobranca"
    
    def _serialize_enum(self, value) -> str:
        """Serializa um valor de enum ou retorna string vazia se None"""
        if value is None:
            return ''
        if hasattr(value, 'value'):
            return str(value.value)
        return str(value) 
    
    def to_dict(self) -> dict:
        def serialize(value) -> str:
            if value is None:
                return ''
            raw = getattr(value, 'value', value)
            return '' if raw is None else str(raw)

        data = {
            'id': str(self.id),
            'descricao': self.descricao if self.descricao is not None else '',
            'id_conta': str(self.id_conta) if self.id_conta is not None else '',
            'remover_fundo_capa_carteira': self.remover_fundo_capa_carteira if self.remover_fundo_capa_carteira is not None else '',
            'tipo_recebimento': self._serialize_enum(self.tipo_recebimento) if self.tipo_recebimento is not None else '',
            'envia_email_ao_gerar_finan': self._serialize_enum(self.envia_email_ao_gerar_finan) if self.envia_email_ao_gerar_finan is not None else '',
            'envia_push_ao_gerar_finan': self._serialize_enum(self.envia_push_ao_gerar_finan) if self.envia_push_ao_gerar_finan is not None else '',
            'imprime_ligacoes_voip': self.imprime_ligacoes_voip if self.imprime_ligacoes_voip is not None else '',
            'registrado': self._serialize_enum(self.registrado) if self.registrado is not None else '',
            'ativo': self._serialize_enum(self.ativo) if self.ativo is not None else '',
            'filial_id': str(self.filial_id) if self.filial_id is not None else '',
            'id_config_alt_pagamento': str(self.id_config_alt_pagamento) if self.id_config_alt_pagamento is not None else '',
            'planejamento_tarifa': str(self.planejamento_tarifa) if self.planejamento_tarifa is not None else '',
            'lancamento_tarifa': self._serialize_enum(self.lancamento_tarifa) if self.lancamento_tarifa is not None else '',
            'reseller_authorization_code': self.reseller_authorization_code if self.reseller_authorization_code is not None else '',
            'dias_vencimento_fatura': self.dias_vencimento_fatura if self.dias_vencimento_fatura is not None else '',
            'carteira_padrao_fatura': str(self.carteira_padrao_fatura) if self.carteira_padrao_fatura is not None else '',
            'ultima_atualizacao': self.ultima_atualizacao if self.ultima_atualizacao is not None else '',
            'pedido_baixa_automatico_recorencia_cartao': self._serialize_enum(self.pedido_baixa_automatico_recorencia_cartao) if self.pedido_baixa_automatico_recorencia_cartao is not None else '',
            'aceite': self.aceite if self.aceite is not None else '',
            'especie': self._serialize_enum(self.especie) if self.especie is not None else '',
            'especie_doc': self.especie_doc if self.especie_doc is not None else '',
            'taxa': self.taxa if self.taxa is not None else '',
            'quem_emite': self.quem_emite if self.quem_emite is not None else '',
            'quem_distribui': self._serialize_enum(self.quem_distribui) if self.quem_distribui is not None else '',
            'endereco_envio_cobranca': self._serialize_enum(self.endereco_envio_cobranca) if self.endereco_envio_cobranca is not None else '',
            'boleto_local_atualiza': self._serialize_enum(self.boleto_local_atualiza) if self.boleto_local_atualiza is not None else '',
            'local_pagamento': self.local_pagamento if self.local_pagamento is not None else '',
            'contador_nn': str(self.contador_nn) if self.contador_nn is not None else '',
            'classe_funcoes': self._serialize_enum(self.classe_funcoes) if self.classe_funcoes is not None else '',
            'versao_integracao_banrisul': self._serialize_enum(self.versao_integracao_banrisul) if self.versao_integracao_banrisul is not None else '',
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
            'tipo_carteira': self._serialize_enum(self.tipo_carteira) if self.tipo_carteira is not None else '',
            'tipo': self._serialize_enum(self.tipo) if self.tipo is not None else '',
            'utliza_numero_parcela_fixo': self._serialize_enum(self.utliza_numero_parcela_fixo) if self.utliza_numero_parcela_fixo is not None else '',
            'pedido_baixa_automatico': self._serialize_enum(self.pedido_baixa_automatico) if self.pedido_baixa_automatico is not None else '',
            'enviar_pedido_baixa_renegociados': self._serialize_enum(self.enviar_pedido_baixa_renegociados) if self.enviar_pedido_baixa_renegociados is not None else '',
            'pedido_baixa_automatico_rec_manual': self._serialize_enum(self.pedido_baixa_automatico_rec_manual) if self.pedido_baixa_automatico_rec_manual is not None else '',
            'pedido_baixa_automatico_rec_cartao': self._serialize_enum(self.pedido_baixa_automatico_rec_cartao) if self.pedido_baixa_automatico_rec_cartao is not None else '',
            'pedido_baixa_automatico_rec_pix': self._serialize_enum(self.pedido_baixa_automatico_rec_pix) if self.pedido_baixa_automatico_rec_pix is not None else '',
            'adiciona_remessa_auto_alt_data': self._serialize_enum(self.adiciona_remessa_auto_alt_data) if self.adiciona_remessa_auto_alt_data is not None else '',
            'remessa_com_mensagem': self._serialize_enum(self.remessa_com_mensagem) if self.remessa_com_mensagem is not None else '',
            'validar_vencidos_remessa': self._serialize_enum(self.validar_vencidos_remessa) if self.validar_vencidos_remessa is not None else '',
            'validar_recebidos_remessa': self._serialize_enum(self.validar_recebidos_remessa) if self.validar_recebidos_remessa is not None else '',
            'validar_clientes_bloqueados': self._serialize_enum(self.validar_clientes_bloqueados) if self.validar_clientes_bloqueados is not None else '',
            'validar_clientes_negativados_remessa': self._serialize_enum(self.validar_clientes_negativados_remessa) if self.validar_clientes_negativados_remessa is not None else '',
            'l_remessa': self._serialize_enum(self.l_remessa) if self.l_remessa is not None else '',
            'l_retorno': self._serialize_enum(self.l_retorno) if self.l_retorno is not None else '',
            'codigo_flash': self.codigo_flash if self.codigo_flash is not None else '',
            'contabiliza_retorno_filial_emissao': self._serialize_enum(self.contabiliza_retorno_filial_emissao) if self.contabiliza_retorno_filial_emissao is not None else '',
            'filtra_inicio_nn': self._serialize_enum(self.filtra_inicio_nn) if self.filtra_inicio_nn is not None else '',
            'baixa_automatica': self._serialize_enum(self.baixa_automatica) if self.baixa_automatica is not None else '',
            'baixa_automatica_dias': self.baixa_automatica_dias if self.baixa_automatica_dias is not None else '',
            'utilizar_baixa_apos_vencimento': self._serialize_enum(self.utilizar_baixa_apos_vencimento) if self.utilizar_baixa_apos_vencimento is not None else '',
            'enviar_pedido_baixa_vencimento': self.enviar_pedido_baixa_vencimento if self.enviar_pedido_baixa_vencimento is not None else '',
            'gateway_nome': self._serialize_enum(self.gateway_nome) if self.gateway_nome is not None else '',
            'codigo_carteira': self.codigo_carteira if self.codigo_carteira is not None else '',
            'workspace_id': self.workspace_id if self.workspace_id is not None else '',
            'versao_api': self._serialize_enum(self.versao_api) if self.versao_api is not None else '',
            'importado_gateway': self._serialize_enum(self.importado_gateway) if self.importado_gateway is not None else '',
            'nova_api': self._serialize_enum(self.nova_api) if self.nova_api is not None else '',
            'ambiente_homologacao_gateway': self._serialize_enum(self.ambiente_homologacao_gateway) if self.ambiente_homologacao_gateway is not None else '',
            'utiliza_carne': self._serialize_enum(self.utiliza_carne) if self.utiliza_carne is not None else '',
            'gerencia_client_id': self.gerencia_client_id if self.gerencia_client_id is not None else '',
            'gerencia_client_secret': self.gerencia_client_secret if self.gerencia_client_secret is not None else '',
            'developer_application_key': self.developer_application_key if self.developer_application_key is not None else '',
            'webhook_id': self.webhook_id if self.webhook_id is not None else '',
            'gerencia_ip_callback': self.gerencia_ip_callback if self.gerencia_ip_callback is not None else '',
            'gerencia_identificador_conta': self.gerencia_identificador_conta if self.gerencia_identificador_conta is not None else '',
            'nova_int_fortunus': self._serialize_enum(self.nova_int_fortunus) if self.nova_int_fortunus is not None else '',
            'gateway_token': self.gateway_token if self.gateway_token is not None else '',
            'carteira_widepay': self.carteira_widepay if self.carteira_widepay is not None else '',
            'gateway_tipo_impressao': self._serialize_enum(self.gateway_tipo_impressao) if self.gateway_tipo_impressao is not None else '',
            'data_credito_pix': self.data_credito_pix if self.data_credito_pix is not None else '',
            'data_credito_boleto': self.data_credito_boleto if self.data_credito_boleto is not None else '',
            'gateway_retorno': self.gateway_retorno if self.gateway_retorno is not None else '',
            'adiciona_obs_descricao': self._serialize_enum(self.adiciona_obs_descricao) if self.adiciona_obs_descricao is not None else '',
            'adiciona_venc_descricao': self._serialize_enum(self.adiciona_venc_descricao) if self.adiciona_venc_descricao is not None else '',
            'dias_limite_pagamento_apos_vencimento': self.dias_limite_pagamento_apos_vencimento if self.dias_limite_pagamento_apos_vencimento is not None else '',
            'envia_email_gerencia': self._serialize_enum(self.envia_email_gerencia) if self.envia_email_gerencia is not None else '',
            'numero_conta_f2b': self.numero_conta_f2b if self.numero_conta_f2b is not None else '',
            'n_convenio_credisis': self.n_convenio_credisis if self.n_convenio_credisis is not None else '',
            'url_callback': self.url_callback if self.url_callback is not None else '',
            'use_webhook_url_callback': self._serialize_enum(self.use_webhook_url_callback) if self.use_webhook_url_callback is not None else '',
            'webhook_url_callback': self.webhook_url_callback if self.webhook_url_callback is not None else '',
            'data_ultima_atualizacao': self.data_ultima_atualizacao if self.data_ultima_atualizacao is not None else '',
            'galaxPayId': self.galaxPayId if self.galaxPayId is not None else '',
            'galaxPayHash': self.galaxPayHash if self.galaxPayHash is not None else '',
            'recebimento_parcial_gateway': self._serialize_enum(self.recebimento_parcial_gateway) if self.recebimento_parcial_gateway is not None else '',
            'finalizar_cob_bf': self._serialize_enum(self.finalizar_cob_bf) if self.finalizar_cob_bf is not None else '',
            'especie_documento_gerencianet': self.especie_documento_gerencianet if self.especie_documento_gerencianet is not None else '',
            'gera_pix_gateway': self._serialize_enum(self.gera_pix_gateway) if self.gera_pix_gateway is not None else '',
            'enviar_cobranca_pix_whatsapp': self._serialize_enum(self.enviar_cobranca_pix_whatsapp) if self.enviar_cobranca_pix_whatsapp is not None else '',
            'tipo_chave_pix': self._serialize_enum(self.tipo_chave_pix) if self.tipo_chave_pix is not None else '',
            'pix_chave_santander': self.pix_chave_santander if self.pix_chave_santander is not None else '',
            'dica_chave_pix_gateway': self.dica_chave_pix_gateway if self.dica_chave_pix_gateway is not None else '',
            'lanca_tarifa_gateway': self._serialize_enum(self.lanca_tarifa_gateway) if self.lanca_tarifa_gateway is not None else '',
            'valor_tarifa_gateway': self.valor_tarifa_gateway if self.valor_tarifa_gateway is not None else '',
            'lanca_tarifa_pix': self._serialize_enum(self.lanca_tarifa_pix) if self.lanca_tarifa_pix is not None else '',
            'valor_tarifa_pix': self.valor_tarifa_pix if self.valor_tarifa_pix is not None else '',
            'timeout': self._serialize_enum(self.timeout) if self.timeout is not None else '',
            'expire_at': self.expire_at if self.expire_at is not None else '',
            'creditcard_gateway': self._serialize_enum(self.creditcard_gateway) if self.creditcard_gateway is not None else '',
            'creditCard_ambiente': self._serialize_enum(self.creditCard_ambiente) if self.creditCard_ambiente is not None else '',
            'versao_api_cartao': self._serialize_enum(self.versao_api_cartao) if self.versao_api_cartao is not None else '',
            'habilitar_recorrencia_cartao': self._serialize_enum(self.habilitar_recorrencia_cartao) if self.habilitar_recorrencia_cartao is not None else '',
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
            'timeoutCreditCard': self._serialize_enum(self.timeoutCreditCard) if self.timeoutCreditCard is not None else '',
            'creditcard_sslcert': self.creditcard_sslcert if self.creditcard_sslcert is not None else '',
            'creditcard_sslkey': self.creditcard_sslkey if self.creditcard_sslkey is not None else '',
            'creditCard_local': self._serialize_enum(self.creditCard_local) if self.creditCard_local is not None else '',
            'creditCard_autenticar': self.creditCard_autenticar if self.creditCard_autenticar is not None else '',
            'creditCard_capturar': self.creditCard_capturar if self.creditCard_capturar is not None else '',
            'creditCard_autorizar': self._serialize_enum(self.creditCard_autorizar) if self.creditCard_autorizar is not None else '',
            'credit_card_tipo': self.credit_card_tipo if self.credit_card_tipo is not None else '',
            'creditCard_parcelamento': self._serialize_enum(self.creditCard_parcelamento) if self.creditCard_parcelamento is not None else '',
            'creditCard_Nparcelas': self.creditCard_Nparcelas if self.creditCard_Nparcelas is not None else '',
            'creditCard_juro': self.creditCard_juro if self.creditCard_juro is not None else '',
            'credit_card_repassar_taxa': self._serialize_enum(self.credit_card_repassar_taxa) if self.credit_card_repassar_taxa is not None else '',
            'tip_fee_transfer': self.tip_fee_transfer if self.tip_fee_transfer is not None else '',
            'credit_card_taxa_em_pagamentos': self._serialize_enum(self.credit_card_taxa_em_pagamentos) if self.credit_card_taxa_em_pagamentos is not None else '',
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
            'debito_classe': self._serialize_enum(self.debito_classe) if self.debito_classe is not None else '',
            'validar_vencidos_remessa_D': self._serialize_enum(self.validar_vencidos_remessa_D) if self.validar_vencidos_remessa_D is not None else '',
            'data_credito_debito_em_conta': self.data_credito_debito_em_conta if self.data_credito_debito_em_conta is not None else '',
            'valor_tarifa': self.valor_tarifa if self.valor_tarifa is not None else '',
            'substrair_tarifa': self.substrair_tarifa if self.substrair_tarifa is not None else '',
            'pix_gateway': self._serialize_enum(self.pix_gateway) if self.pix_gateway is not None else '',
            'pix_ambiente': self._serialize_enum(self.pix_ambiente) if self.pix_ambiente is not None else '',
            'pix_chave': self.pix_chave if self.pix_chave is not None else '',
            'pix_client_id': self.pix_client_id if self.pix_client_id is not None else '',
            'pix_client_secret': self.pix_client_secret if self.pix_client_secret is not None else '',
            'pix_tempo_validade': self.pix_tempo_validade if self.pix_tempo_validade is not None else '',
            'pix_certificado': self.pix_certificado if self.pix_certificado is not None else '',
            'pix_gerencia_ip_callback': self.pix_gerencia_ip_callback if self.pix_gerencia_ip_callback is not None else '',
            'pix_modalidade': self._serialize_enum(self.pix_modalidade) if self.pix_modalidade is not None else '',
            'permite_pagamento_por_chave_pix': self._serialize_enum(self.permite_pagamento_por_chave_pix) if self.permite_pagamento_por_chave_pix is not None else '',
            'enviar_cobranca_pix_whatsapp_carteiras_pix': self._serialize_enum(self.enviar_cobranca_pix_whatsapp_carteiras_pix) if self.enviar_cobranca_pix_whatsapp_carteiras_pix is not None else '',
            'tipo_chave_pix_carteiras_pix': self._serialize_enum(self.tipo_chave_pix_carteiras_pix) if self.tipo_chave_pix_carteiras_pix is not None else '',
            'utiliza_pix_recorrente': self._serialize_enum(self.utiliza_pix_recorrente) if self.utiliza_pix_recorrente is not None else '',
            'permite_retentativas_pix_recorrente': self._serialize_enum(self.permite_retentativas_pix_recorrente) if self.permite_retentativas_pix_recorrente is not None else '',
            'fieldset_dica_configuracoes_pix': self.fieldset_dica_configuracoes_pix if self.fieldset_dica_configuracoes_pix is not None else '',
            'lanca_tarifa_pix_modobank': self._serialize_enum(self.lanca_tarifa_pix_modobank) if self.lanca_tarifa_pix_modobank is not None else '',
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
            'calcular_juros': self._serialize_enum(self.calcular_juros) if self.calcular_juros is not None else '',
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
            'obs_fn_areceber': self._serialize_enum(self.obs_fn_areceber) if self.obs_fn_areceber is not None else '',
            'obs_anterior': self.obs_anterior if self.obs_anterior is not None else '',
            'obs_posterior': self.obs_posterior if self.obs_posterior is not None else '',
            'l_impressao': self._serialize_enum(self.l_impressao) if self.l_impressao is not None else '',
            'formato_detalhamento_fatura': self._serialize_enum(self.formato_detalhamento_fatura) if self.formato_detalhamento_fatura is not None else '',
            'cor_fatura': self.cor_fatura if self.cor_fatura is not None else '',
            'informative_text': self.informative_text if self.informative_text is not None else '',
            'imprimir_filial_venda': self._serialize_enum(self.imprimir_filial_venda) if self.imprimir_filial_venda is not None else '',
            'imprimir_filial_conta': self._serialize_enum(self.imprimir_filial_conta) if self.imprimir_filial_conta is not None else '',
            'considerar_modelo_nao_fiscal': self._serialize_enum(self.considerar_modelo_nao_fiscal) if self.considerar_modelo_nao_fiscal is not None else '',
            'imprime_endereco_boleto': self._serialize_enum(self.imprime_endereco_boleto) if self.imprime_endereco_boleto is not None else '',
            'imprime_fone_fatura_d': self._serialize_enum(self.imprime_fone_fatura_d) if self.imprime_fone_fatura_d is not None else '',
            'imp_nome_sacador_avalista': self._serialize_enum(self.imp_nome_sacador_avalista) if self.imp_nome_sacador_avalista is not None else '',
            'imprime_prod_val_zero': self._serialize_enum(self.imprime_prod_val_zero) if self.imprime_prod_val_zero is not None else '',
            'imprime_tipo_resolucao_anatel': self._serialize_enum(self.imprime_tipo_resolucao_anatel) if self.imprime_tipo_resolucao_anatel is not None else '',
            'mask_cpf_cnpj_impressao_boleto': self._serialize_enum(self.mask_cpf_cnpj_impressao_boleto) if self.mask_cpf_cnpj_impressao_boleto is not None else '',
            'mostra_cep_beneficiario_impressao': self._serialize_enum(self.mostra_cep_beneficiario_impressao) if self.mostra_cep_beneficiario_impressao is not None else '',
            'agrupar_produtos_por_descricao': self._serialize_enum(self.agrupar_produtos_por_descricao) if self.agrupar_produtos_por_descricao is not None else '',
            'imprimir_beneficiario_gateway': self._serialize_enum(self.imprimir_beneficiario_gateway) if self.imprimir_beneficiario_gateway is not None else '',
            'obs_adicional_boleto': self.obs_adicional_boleto if self.obs_adicional_boleto is not None else '',
            'imp_nome_beneficiario': self._serialize_enum(self.imp_nome_beneficiario) if self.imp_nome_beneficiario is not None else '',
            'imp_nome_beneficiario_recibo': self._serialize_enum(self.imp_nome_beneficiario_recibo) if self.imp_nome_beneficiario_recibo is not None else '',
            'boletos_capa_contratos': self._serialize_enum(self.boletos_capa_contratos) if self.boletos_capa_contratos is not None else '',
            'boleto_capa': self.boleto_capa if self.boleto_capa is not None else '',
            'boleto_capa_cliente_referencia': self.boleto_capa_cliente_referencia if self.boleto_capa_cliente_referencia is not None else '',
            'fone_cliente_capa': self.fone_cliente_capa if self.fone_cliente_capa is not None else '',
            'boleto_capa_local': self._serialize_enum(self.boleto_capa_local) if self.boleto_capa_local is not None else '',
            'boleto_capa_imagem': self.boleto_capa_imagem if self.boleto_capa_imagem is not None else '',
            'boleto_capa_x': self.boleto_capa_x if self.boleto_capa_x is not None else '',
            'boleto_capa_y': self.boleto_capa_y if self.boleto_capa_y is not None else '',
            'tamanho_quadro_endereco_x': self.tamanho_quadro_endereco_x if self.tamanho_quadro_endereco_x is not None else '',
            'tamanho_quadro_endereco_y': self.tamanho_quadro_endereco_y if self.tamanho_quadro_endereco_y is not None else '',
            'tipo_baixa': self._serialize_enum(self.tipo_baixa) if self.tipo_baixa is not None else '',
            'validar_juros_multa': self._serialize_enum(self.validar_juros_multa) if self.validar_juros_multa is not None else '',
            'id_produto_cob_adicional': str(self.id_produto_cob_adicional) if self.id_produto_cob_adicional is not None else '',
            'id_fn_areceber_modelo': str(self.id_fn_areceber_modelo) if self.id_fn_areceber_modelo is not None else '',
        }
        return {key: serialize(value) for key, value in data.items()}
    def is_valid(self) -> bool:
        return self.id is not None and self.descricao is not None and self.id_conta is not None and self.remover_fundo_capa_carteira is not None
