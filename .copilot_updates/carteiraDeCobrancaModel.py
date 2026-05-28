from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Optional
from ORM_IXC.enums.carteiraDeCobranca import *
from ORM_IXC.interfaces import IModel, IModelWithId
from ORM_IXC.statemants.classBase import Field
from ORM_IXC.statemants.metaManager import MetaModels
from ORM_IXC.models.defaultModel import BaseModel


@MetaModels
class CarteiraDeCobrancaModel(IModelWithId, BaseModel):
    id: int
    descricao: str
    id_conta: int
    remover_fundo_capa_carteira: str
    tipo_recebimento: Tipo_recebimentoEnum = Field("tipo_recebimento", Tipo_recebimentoEnum, Tipo_recebimentoEnum.BOLETO)
    envia_email_ao_gerar_finan: Optional[Envia_email_ao_gerar_finanEnum] = Field("envia_email_ao_gerar_finan", Envia_email_ao_gerar_finanEnum, Envia_email_ao_gerar_finanEnum.NAO)
    envia_push_ao_gerar_finan: Optional[Envia_push_ao_gerar_finanEnum] = Field("envia_push_ao_gerar_finan", Envia_push_ao_gerar_finanEnum, Envia_push_ao_gerar_finanEnum.NAO)
    imprime_ligacoes_voip: Mapped[Optional[str]] = Field("imprime_ligacoes_voip", str, '')
    registrado: RegistradoEnum = Field("registrado", RegistradoEnum, RegistradoEnum.SIM)
    ativo: AtivoEnum = Field("ativo", AtivoEnum, AtivoEnum.SIM)
    filial_id: Mapped[Optional[int]] = Field("filial_id", int, None)
    id_config_alt_pagamento: Mapped[Optional[int]] = Field("id_config_alt_pagamento", int, None)
    planejamento_tarifa: Mapped[Optional[int]] = Field("planejamento_tarifa", int, None)
    lancamento_tarifa: Lancamento_tarifaEnum = Field("lancamento_tarifa", Lancamento_tarifaEnum, Lancamento_tarifaEnum.NA_DATA_DO_PAGAMENTO)
    reseller_authorization_code: Mapped[Optional[str]] = Field("reseller_authorization_code", str, '')
    dias_vencimento_fatura: Mapped[Optional[str]] = Field("dias_vencimento_fatura", str, '')
    carteira_padrao_fatura: Mapped[Optional[int]] = Field("carteira_padrao_fatura", int, None)
    ultima_atualizacao: Mapped[Optional[str]] = Field("ultima_atualizacao", str, '')
    pedido_baixa_automatico_recorencia_cartao: Pedido_baixa_automatico_recorencia_cartaoEnum = Field("pedido_baixa_automatico_recorencia_cartao", Pedido_baixa_automatico_recorencia_cartaoEnum, Pedido_baixa_automatico_recorencia_cartaoEnum.SIM)
    aceite: Mapped[Optional[str]] = Field("aceite", str, '')
    especie: Optional[EspecieEnum] = Field("especie", EspecieEnum, EspecieEnum.RS)
    especie_doc: Mapped[Optional[str]] = Field("especie_doc", str, '')
    taxa: Mapped[Optional[str]] = Field("taxa", str, '')
    quem_emite: Mapped[Optional[str]] = Field("quem_emite", str, '')
    quem_distribui: Optional[Quem_distribuiEnum] = Field("quem_distribui", Quem_distribuiEnum, Quem_distribuiEnum.EMPRESA)
    endereco_envio_cobranca: Optional[Endereco_envio_cobrancaEnum] = Field("endereco_envio_cobranca", Endereco_envio_cobrancaEnum, Endereco_envio_cobrancaEnum.COBRANCA)
    boleto_local_atualiza: Optional[Boleto_local_atualizaEnum] = Field("boleto_local_atualiza", Boleto_local_atualizaEnum, Boleto_local_atualizaEnum.SISTEMA)
    local_pagamento: Mapped[Optional[str]] = Field("local_pagamento", str, '')
    contador_nn: Mapped[Optional[int]] = Field("contador_nn", int, None)
    classe_funcoes: Mapped[Optional[Classe_funcoesEnum]] = Field("classe_funcoes", Classe_funcoesEnum, None)
    versao_integracao_banrisul: Optional[Versao_integracao_banrisulEnum] = Field("versao_integracao_banrisul", Versao_integracao_banrisulEnum, Versao_integracao_banrisulEnum.V1)
    n_convenio: Mapped[Optional[str]] = Field("n_convenio", str, '')
    c_cedente: Mapped[Optional[str]] = Field("c_cedente", str, '')
    operacao: Mapped[Optional[str]] = Field("operacao", str, '')
    codigo_edi7: Mapped[Optional[str]] = Field("codigo_edi7", str, '')
    carteira: Mapped[Optional[str]] = Field("carteira", str, '')
    sigla_arquivo_remessa: Mapped[Optional[str]] = Field("sigla_arquivo_remessa", str, '')
    variacao_carteira: Mapped[Optional[str]] = Field("variacao_carteira", str, '')
    modalidade_cobranca: Mapped[Optional[str]] = Field("modalidade_cobranca", str, '')
    sicredi_byte: Mapped[Optional[str]] = Field("sicredi_byte", str, '')
    sicredi_posto: Mapped[Optional[str]] = Field("sicredi_posto", str, '')
    inicio_nosso_numero: Mapped[Optional[str]] = Field("inicio_nosso_numero", str, '')
    nosso_numero_const1: Mapped[Optional[str]] = Field("nosso_numero_const1", str, '')
    nosso_numero_const2: Mapped[Optional[str]] = Field("nosso_numero_const2", str, '')
    nosso_numero1: Mapped[Optional[str]] = Field("nosso_numero1", str, '')
    nosso_numero2: Mapped[Optional[str]] = Field("nosso_numero2", str, '')
    conta_cosmos: Mapped[Optional[str]] = Field("conta_cosmos", str, '')
    tipo_carteira: Optional[Tipo_carteiraEnum] = Field("tipo_carteira", Tipo_carteiraEnum, Tipo_carteiraEnum.SIMPLES)
    tipo: Mapped[Optional[TipoEnum]] = Field("tipo", TipoEnum, None)
    utliza_numero_parcela_fixo: Optional[Utliza_numero_parcela_fixoEnum] = Field("utliza_numero_parcela_fixo", Utliza_numero_parcela_fixoEnum, Utliza_numero_parcela_fixoEnum.SIM)
    pedido_baixa_automatico: Optional[Pedido_baixa_automaticoEnum] = Field("pedido_baixa_automatico", Pedido_baixa_automaticoEnum, Pedido_baixa_automaticoEnum.SIM)
    enviar_pedido_baixa_renegociados: Optional[Enviar_pedido_baixa_renegociadosEnum] = Field("enviar_pedido_baixa_renegociados", Enviar_pedido_baixa_renegociadosEnum, Enviar_pedido_baixa_renegociadosEnum.SIM)
    pedido_baixa_automatico_rec_manual: Optional[Pedido_baixa_automatico_rec_manualEnum] = Field("pedido_baixa_automatico_rec_manual", Pedido_baixa_automatico_rec_manualEnum, Pedido_baixa_automatico_rec_manualEnum.SIM)
    pedido_baixa_automatico_rec_cartao: Optional[Pedido_baixa_automatico_rec_cartaoEnum] = Field("pedido_baixa_automatico_rec_cartao", Pedido_baixa_automatico_rec_cartaoEnum, Pedido_baixa_automatico_rec_cartaoEnum.SIM)
    pedido_baixa_automatico_rec_pix: Optional[Pedido_baixa_automatico_rec_pixEnum] = Field("pedido_baixa_automatico_rec_pix", Pedido_baixa_automatico_rec_pixEnum, Pedido_baixa_automatico_rec_pixEnum.SIM)
    adiciona_remessa_auto_alt_data: Optional[Adiciona_remessa_auto_alt_dataEnum] = Field("adiciona_remessa_auto_alt_data", Adiciona_remessa_auto_alt_dataEnum, Adiciona_remessa_auto_alt_dataEnum.NAO)
    remessa_com_mensagem: Optional[Remessa_com_mensagemEnum] = Field("remessa_com_mensagem", Remessa_com_mensagemEnum, Remessa_com_mensagemEnum.NAO)
    validar_vencidos_remessa: Optional[Validar_vencidos_remessaEnum] = Field("validar_vencidos_remessa", Validar_vencidos_remessaEnum, Validar_vencidos_remessaEnum.SIM)
    validar_recebidos_remessa: Optional[Validar_recebidos_remessaEnum] = Field("validar_recebidos_remessa", Validar_recebidos_remessaEnum, Validar_recebidos_remessaEnum.SIM)
    validar_clientes_bloqueados: Optional[Validar_clientes_bloqueadosEnum] = Field("validar_clientes_bloqueados", Validar_clientes_bloqueadosEnum, Validar_clientes_bloqueadosEnum.NAO)
    validar_clientes_negativados_remessa: Optional[Validar_clientes_negativados_remessaEnum] = Field("validar_clientes_negativados_remessa", Validar_clientes_negativados_remessaEnum, Validar_clientes_negativados_remessaEnum.NAO)
    l_remessa: Mapped[Optional[L_remessaEnum]] = Field("l_remessa", L_remessaEnum, None)
    l_retorno: Mapped[Optional[L_retornoEnum]] = Field("l_retorno", L_retornoEnum, None)
    codigo_flash: Mapped[Optional[str]] = Field("codigo_flash", str, '')
    contabiliza_retorno_filial_emissao: Mapped[Optional[Contabiliza_retorno_filial_emissaoEnum]] = Field("contabiliza_retorno_filial_emissao", Contabiliza_retorno_filial_emissaoEnum, Contabiliza_retorno_filial_emissaoEnum.NAO)
    filtra_inicio_nn: Filtra_inicio_nnEnum = Field("filtra_inicio_nn", Filtra_inicio_nnEnum, Filtra_inicio_nnEnum.SIM)
    baixa_automatica: Optional[Baixa_automaticaEnum] = Field("baixa_automatica", Baixa_automaticaEnum, Baixa_automaticaEnum.SIM)
    baixa_automatica_dias: Mapped[Optional[str]] = Field("baixa_automatica_dias", str, '')
    utilizar_baixa_apos_vencimento: Optional[Utilizar_baixa_apos_vencimentoEnum] = Field("utilizar_baixa_apos_vencimento", Utilizar_baixa_apos_vencimentoEnum, Utilizar_baixa_apos_vencimentoEnum.NAO)
    enviar_pedido_baixa_vencimento: Mapped[Optional[str]] = Field("enviar_pedido_baixa_vencimento", str, '')
    gateway_nome: Mapped[Optional[Gateway_nomeEnum]] = Field("gateway_nome", Gateway_nomeEnum, None)
    codigo_carteira: Mapped[Optional[str]] = Field("codigo_carteira", str, '')
    workspace_id: Mapped[Optional[str]] = Field("workspace_id", str, '')
    versao_api: Mapped[Optional[Versao_apiEnum]] = Field("versao_api", Versao_apiEnum, Versao_apiEnum.V1)
    importado_gateway: Mapped[Optional[Importado_gatewayEnum]] = Field("importado_gateway", Importado_gatewayEnum, Importado_gatewayEnum.NAO)
    nova_api: Mapped[Optional[Nova_apiEnum]] = Field("nova_api", Nova_apiEnum, Nova_apiEnum.SIM)
    ambiente_homologacao_gateway: Mapped[Optional[Ambiente_homologacao_gatewayEnum]] = Field("ambiente_homologacao_gateway", Ambiente_homologacao_gatewayEnum, Ambiente_homologacao_gatewayEnum.PRODUCAO)
    utiliza_carne: Mapped[Optional[Utiliza_carneEnum]] = Field("utiliza_carne", Utiliza_carneEnum, Utiliza_carneEnum.NAO)
    gerencia_client_id: Mapped[Optional[str]] = Field("gerencia_client_id", str, '')
    gerencia_client_secret: Mapped[Optional[Any]] = Field("gerencia_client_secret", Any, None)
    developer_application_key: Mapped[Optional[str]] = Field("developer_application_key", str, '')
    webhook_id: Mapped[Optional[str]] = Field("webhook_id", str, '')
    gerencia_ip_callback: Mapped[Optional[str]] = Field("gerencia_ip_callback", str, '')
    gerencia_identificador_conta: Mapped[Optional[str]] = Field("gerencia_identificador_conta", str, '')
    nova_int_fortunus: Mapped[Optional[Nova_int_fortunusEnum]] = Field("nova_int_fortunus", Nova_int_fortunusEnum, Nova_int_fortunusEnum.NAO)
    gateway_token: Mapped[Optional[Any]] = Field("gateway_token", Any, None)
    carteira_widepay: Mapped[Optional[str]] = Field("carteira_widepay", str, '')
    gateway_tipo_impressao: Mapped[Optional[Gateway_tipo_impressaoEnum]] = Field("gateway_tipo_impressao", Gateway_tipo_impressaoEnum, Gateway_tipo_impressaoEnum.CARNE)
    data_credito_pix: Mapped[Optional[str]] = Field("data_credito_pix", str, '')
    data_credito_boleto: Mapped[Optional[str]] = Field("data_credito_boleto", str, '')
    gateway_retorno: Mapped[Optional[str]] = Field("gateway_retorno", str, '')
    adiciona_obs_descricao: Mapped[Optional[Adiciona_obs_descricaoEnum]] = Field("adiciona_obs_descricao", Adiciona_obs_descricaoEnum, Adiciona_obs_descricaoEnum.NAO)
    adiciona_venc_descricao: Mapped[Optional[Adiciona_venc_descricaoEnum]] = Field("adiciona_venc_descricao", Adiciona_venc_descricaoEnum, Adiciona_venc_descricaoEnum.NAO)
    dias_limite_pagamento_apos_vencimento: Mapped[Optional[str]] = Field("dias_limite_pagamento_apos_vencimento", str, '')
    envia_email_gerencia: Mapped[Optional[Envia_email_gerenciaEnum]] = Field("envia_email_gerencia", Envia_email_gerenciaEnum, Envia_email_gerenciaEnum.NAO)
    numero_conta_f2b: Mapped[Optional[str]] = Field("numero_conta_f2b", str, '')
    n_convenio_credisis: Mapped[Optional[str]] = Field("n_convenio_credisis", str, '')
    url_callback: Mapped[Optional[str]] = Field("url_callback", str, '')
    use_webhook_url_callback: Mapped[Use_webhook_url_callbackEnum] = Field("use_webhook_url_callback", Use_webhook_url_callbackEnum, Use_webhook_url_callbackEnum.NAO)
    webhook_url_callback: Mapped[Optional[str]] = Field("webhook_url_callback", str, '')
    data_ultima_atualizacao: Mapped[Optional[str]] = Field("data_ultima_atualizacao", str, '')
    galaxPayId: Mapped[Optional[str]] = Field("galaxPayId", str, '')
    galaxPayHash: Mapped[Optional[str]] = Field("galaxPayHash", str, '')
    recebimento_parcial_gateway: Mapped[Optional[Recebimento_parcial_gatewayEnum]] = Field("recebimento_parcial_gateway", Recebimento_parcial_gatewayEnum, Recebimento_parcial_gatewayEnum.NAO)
    finalizar_cob_bf: Mapped[Optional[Finalizar_cob_bfEnum]] = Field("finalizar_cob_bf", Finalizar_cob_bfEnum, Finalizar_cob_bfEnum.SIM)
    especie_documento_gerencianet: Mapped[Optional[str]] = Field("especie_documento_gerencianet", str, '')
    gera_pix_gateway: Mapped[Optional[Gera_pix_gatewayEnum]] = Field("gera_pix_gateway", Gera_pix_gatewayEnum, Gera_pix_gatewayEnum.NAO)
    enviar_cobranca_pix_whatsapp: Mapped[Enviar_cobranca_pix_whatsappEnum] = Field("enviar_cobranca_pix_whatsapp", Enviar_cobranca_pix_whatsappEnum, Enviar_cobranca_pix_whatsappEnum.NAO)
    tipo_chave_pix: Mapped[Optional[Tipo_chave_pixEnum]] = Field("tipo_chave_pix", Tipo_chave_pixEnum, None)
    pix_chave_santander: Mapped[Optional[str]] = Field("pix_chave_santander", str, '')
    dica_chave_pix_gateway: Mapped[Optional[str]] = Field("dica_chave_pix_gateway", str, '')
    lanca_tarifa_gateway: Mapped[Optional[Lanca_tarifa_gatewayEnum]] = Field("lanca_tarifa_gateway", Lanca_tarifa_gatewayEnum, Lanca_tarifa_gatewayEnum.NAO_LANCA)
    valor_tarifa_gateway: Mapped[Optional[str]] = Field("valor_tarifa_gateway", str, '')
    lanca_tarifa_pix: Mapped[Optional[Lanca_tarifa_pixEnum]] = Field("lanca_tarifa_pix", Lanca_tarifa_pixEnum, Lanca_tarifa_pixEnum.NAO)
    valor_tarifa_pix: Mapped[Optional[str]] = Field("valor_tarifa_pix", str, '')
    timeout: Mapped[Optional[TimeoutEnum]] = Field("timeout", TimeoutEnum, TimeoutEnum.T60)
    expire_at: Mapped[Optional[str]] = Field("expire_at", str, '')
    creditcard_gateway: Mapped[Optional[Creditcard_gatewayEnum]] = Field("creditcard_gateway", Creditcard_gatewayEnum, None)
    creditCard_ambiente: Mapped[Optional[CreditCard_ambienteEnum]] = Field("creditCard_ambiente", CreditCard_ambienteEnum, CreditCard_ambienteEnum.TESTE)
    versao_api_cartao: Mapped[Optional[Versao_api_cartaoEnum]] = Field("versao_api_cartao", Versao_api_cartaoEnum, None)
    habilitar_recorrencia_cartao: Mapped[Optional[Habilitar_recorrencia_cartaoEnum]] = Field("habilitar_recorrencia_cartao", Habilitar_recorrencia_cartaoEnum, Habilitar_recorrencia_cartaoEnum.NAO)
    creditcard_user: Mapped[Optional[str]] = Field("creditcard_user", str, '')
    creditcard_senha: Mapped[Optional[str]] = Field("creditcard_senha", str, '')
    creditcard_senhassl: Mapped[Optional[str]] = Field("creditcard_senhassl", str, '')
    creditCard_loja: Mapped[Optional[str]] = Field("creditCard_loja", str, '')
    creditCard_chave: Mapped[Optional[str]] = Field("creditCard_chave", str, '')
    gerencia_identificador_conta_card: Mapped[Optional[str]] = Field("gerencia_identificador_conta_card", str, '')
    gateway_token_card: Mapped[Optional[Any]] = Field("gateway_token_card", Any, None)
    gerencia_client_id_card: Mapped[Optional[str]] = Field("gerencia_client_id_card", str, '')
    gerencia_client_secret_card: Mapped[Optional[Any]] = Field("gerencia_client_secret_card", Any, None)
    gerencia_ip_callback_card: Mapped[Optional[str]] = Field("gerencia_ip_callback_card", str, '')
    id_plano_vindi: Mapped[Optional[str]] = Field("id_plano_vindi", str, '')
    galaxPayIdCard: Mapped[Optional[str]] = Field("galaxPayIdCard", str, '')
    galaxPayHashCard: Mapped[Optional[str]] = Field("galaxPayHashCard", str, '')
    galaxpay_ip_callback_card: Mapped[Optional[str]] = Field("galaxpay_ip_callback_card", str, '')
    timeoutCreditCard: Mapped[Optional[TimeoutCreditCardEnum]] = Field("timeoutCreditCard", TimeoutCreditCardEnum, TimeoutCreditCardEnum.T60)
    creditcard_sslcert: Mapped[Optional[Any]] = Field("creditcard_sslcert", Any, None)
    creditcard_sslkey: Mapped[Optional[Any]] = Field("creditcard_sslkey", Any, None)
    creditCard_local: Mapped[Optional[CreditCard_localEnum]] = Field("creditCard_local", CreditCard_localEnum, CreditCard_localEnum.BUY_PAGE_LOJA)
    creditCard_autenticar: Mapped[Optional[str]] = Field("creditCard_autenticar", str, '')
    creditCard_capturar: Mapped[Optional[str]] = Field("creditCard_capturar", str, '')
    creditCard_autorizar: Mapped[Optional[CreditCard_autorizarEnum]] = Field("creditCard_autorizar", CreditCard_autorizarEnum, CreditCard_autorizarEnum.AUTORIZAR_DIRETO)
    credit_card_tipo: Mapped[Optional[str]] = Field("credit_card_tipo", str, '')
    creditCard_parcelamento: Mapped[Optional[CreditCard_parcelamentoEnum]] = Field("creditCard_parcelamento", CreditCard_parcelamentoEnum, CreditCard_parcelamentoEnum.ADMINISTRADORA)
    creditCard_Nparcelas: Mapped[Optional[str]] = Field("creditCard_Nparcelas", str, '')
    creditCard_juro: Mapped[Optional[str]] = Field("creditCard_juro", str, '')
    credit_card_repassar_taxa: Mapped[Credit_card_repassar_taxaEnum] = Field("credit_card_repassar_taxa", Credit_card_repassar_taxaEnum, Credit_card_repassar_taxaEnum.NAO)
    tip_fee_transfer: Mapped[Optional[str]] = Field("tip_fee_transfer", str, '')
    credit_card_taxa_em_pagamentos: Mapped[Credit_card_taxa_em_pagamentosEnum] = Field("credit_card_taxa_em_pagamentos", Credit_card_taxa_em_pagamentosEnum, Credit_card_taxa_em_pagamentosEnum.AMBOS)
    credit_card_porcentagem_taxa: Mapped[Optional[str]] = Field("credit_card_porcentagem_taxa", str, '')
    credit_card_valor_taxa: Mapped[Optional[str]] = Field("credit_card_valor_taxa", str, '')
    creditcard_banceira_vi: Mapped[Optional[str]] = Field("creditcard_banceira_vi", str, '')
    creditcard_banceira_ma: Mapped[Optional[str]] = Field("creditcard_banceira_ma", str, '')
    creditcard_banceira_am: Mapped[Optional[str]] = Field("creditcard_banceira_am", str, '')
    creditcard_banceira_el: Mapped[Optional[str]] = Field("creditcard_banceira_el", str, '')
    creditcard_banceira_dn: Mapped[Optional[str]] = Field("creditcard_banceira_dn", str, '')
    creditcard_banceira_dc: Mapped[Optional[str]] = Field("creditcard_banceira_dc", str, '')
    creditcard_banceira_jc: Mapped[Optional[str]] = Field("creditcard_banceira_jc", str, '')
    creditcard_banceira_au: Mapped[Optional[str]] = Field("creditcard_banceira_au", str, '')
    creditcard_banceira_ca: Mapped[Optional[str]] = Field("creditcard_banceira_ca", str, '')
    debito_convenio: Mapped[Optional[str]] = Field("debito_convenio", str, '')
    debito_carteira_vinculada: Mapped[Optional[int]] = Field("debito_carteira_vinculada", int, None)
    debito_classe: Mapped[Optional[Debito_classeEnum]] = Field("debito_classe", Debito_classeEnum, None)
    validar_vencidos_remessa_D: Mapped[Optional[Validar_vencidos_remessa_DEnum]] = Field("validar_vencidos_remessa_D", Validar_vencidos_remessa_DEnum, Validar_vencidos_remessa_DEnum.SIM)
    data_credito_debito_em_conta: Mapped[Optional[str]] = Field("data_credito_debito_em_conta", str, '')
    valor_tarifa: Mapped[Optional[str]] = Field("valor_tarifa", str, '')
    substrair_tarifa: Mapped[Optional[str]] = Field("substrair_tarifa", str, '')
    pix_gateway: Mapped[Optional[Pix_gatewayEnum]] = Field("pix_gateway", Pix_gatewayEnum, None)
    pix_ambiente: Mapped[Optional[Pix_ambienteEnum]] = Field("pix_ambiente", Pix_ambienteEnum, Pix_ambienteEnum.PRODUCAO)
    pix_chave: Mapped[Optional[str]] = Field("pix_chave", str, '')
    pix_client_id: Mapped[Optional[str]] = Field("pix_client_id", str, '')
    pix_client_secret: Mapped[Optional[Any]] = Field("pix_client_secret", Any, None)
    pix_tempo_validade: Mapped[Optional[str]] = Field("pix_tempo_validade", str, '')
    pix_certificado: Mapped[Optional[Any]] = Field("pix_certificado", Any, None)
    pix_gerencia_ip_callback: Mapped[Optional[str]] = Field("pix_gerencia_ip_callback", str, '')
    pix_modalidade: Mapped[Optional[Pix_modalidadeEnum]] = Field("pix_modalidade", Pix_modalidadeEnum, Pix_modalidadeEnum.IMEDIATA)
    permite_pagamento_por_chave_pix: Mapped[Permite_pagamento_por_chave_pixEnum] = Field("permite_pagamento_por_chave_pix", Permite_pagamento_por_chave_pixEnum, Permite_pagamento_por_chave_pixEnum.SIM)
    enviar_cobranca_pix_whatsapp_carteiras_pix: Mapped[Enviar_cobranca_pix_whatsapp_carteiras_pixEnum] = Field("enviar_cobranca_pix_whatsapp_carteiras_pix", Enviar_cobranca_pix_whatsapp_carteiras_pixEnum, Enviar_cobranca_pix_whatsapp_carteiras_pixEnum.NAO)
    tipo_chave_pix_carteiras_pix: Mapped[Optional[Tipo_chave_pix_carteiras_pixEnum]] = Field("tipo_chave_pix_carteiras_pix", Tipo_chave_pix_carteiras_pixEnum, None)
    utiliza_pix_recorrente: Mapped[Optional[Utiliza_pix_recorrenteEnum]] = Field("utiliza_pix_recorrente", Utiliza_pix_recorrenteEnum, Utiliza_pix_recorrenteEnum.NAO)
    permite_retentativas_pix_recorrente: Mapped[Optional[Permite_retentativas_pix_recorrenteEnum]] = Field("permite_retentativas_pix_recorrente", Permite_retentativas_pix_recorrenteEnum, Permite_retentativas_pix_recorrenteEnum.SIM)
    fieldset_dica_configuracoes_pix: Mapped[Optional[str]] = Field("fieldset_dica_configuracoes_pix", str, '')
    lanca_tarifa_pix_modobank: Mapped[Lanca_tarifa_pix_modobankEnum] = Field("lanca_tarifa_pix_modobank", Lanca_tarifa_pix_modobankEnum, Lanca_tarifa_pix_modobankEnum.NAO)
    valor_tarifa_pix_modobank: Mapped[Optional[str]] = Field("valor_tarifa_pix_modobank", str, '')
    jurop_mes: Mapped[Optional[str]] = Field("jurop_mes", str, '')
    juros_boleto_juno: Mapped[Optional[str]] = Field("juros_boleto_juno", str, '')
    jurop: Mapped[Optional[str]] = Field("jurop", str, '')
    jurov: Mapped[Optional[str]] = Field("jurov", str, '')
    multap: Mapped[Optional[str]] = Field("multap", str, '')
    multav: Mapped[Optional[str]] = Field("multav", str, '')
    desconto_v: Mapped[Optional[str]] = Field("desconto_v", str, '')
    desconto_p: Mapped[Optional[str]] = Field("desconto_p", str, '')
    desconto_condicional_valor: Mapped[Optional[str]] = Field("desconto_condicional_valor", str, '')
    desconto_condicional_percentual: Mapped[Optional[str]] = Field("desconto_condicional_percentual", str, '')
    data_validade_condicional: Mapped[Optional[str]] = Field("data_validade_condicional", str, '')
    desconto_proporcional: Mapped[Optional[str]] = Field("desconto_proporcional", str, '')
    protestar: Mapped[Optional[str]] = Field("protestar", str, '')
    atraso: Mapped[Optional[str]] = Field("atraso", str, '')
    calcular_juros: Mapped[Optional[Calcular_jurosEnum]] = Field("calcular_juros", Calcular_jurosEnum, Calcular_jurosEnum.ATE_O_DIA_ATUAL)
    permite_atualizar_boleto_apos_data_ixc: Mapped[Optional[str]] = Field("permite_atualizar_boleto_apos_data_ixc", str, '')
    instrucao1: Mapped[Optional[str]] = Field("instrucao1", str, '')
    instrucao2: Mapped[Optional[str]] = Field("instrucao2", str, '')
    instrucao3: Mapped[Optional[str]] = Field("instrucao3", str, '')
    instrucao4: Mapped[Optional[str]] = Field("instrucao4", str, '')
    instrucao5: Mapped[Optional[str]] = Field("instrucao5", str, '')
    instrucao6: Mapped[Optional[str]] = Field("instrucao6", str, '')
    instrucao7: Mapped[Optional[str]] = Field("instrucao7", str, '')
    instrucao8: Mapped[Optional[str]] = Field("instrucao8", str, '')
    imp_inst_vencido: Mapped[Optional[str]] = Field("imp_inst_vencido", str, '')
    imp_inst_proporcional: Mapped[Optional[str]] = Field("imp_inst_proporcional", str, '')
    obs_fn_areceber: Mapped[Optional[Obs_fn_areceberEnum]] = Field("obs_fn_areceber", Obs_fn_areceberEnum, Obs_fn_areceberEnum.SIM)
    obs_anterior: Mapped[Optional[str]] = Field("obs_anterior", str, '')
    obs_posterior: Mapped[Optional[str]] = Field("obs_posterior", str, '')
    l_impressao: Mapped[Optional[L_impressaoEnum]] = Field("l_impressao", L_impressaoEnum, None)
    formato_detalhamento_fatura: Mapped[Optional[Formato_detalhamento_faturaEnum]] = Field("formato_detalhamento_fatura", Formato_detalhamento_faturaEnum, Formato_detalhamento_faturaEnum.PLANO)
    cor_fatura: Mapped[Optional[str]] = Field("cor_fatura", str, '')
    informative_text: Mapped[Optional[str]] = Field("informative_text", str, '')
    imprimir_filial_venda: Mapped[Optional[Imprimir_filial_vendaEnum]] = Field("imprimir_filial_venda", Imprimir_filial_vendaEnum, Imprimir_filial_vendaEnum.CONTA)
    imprimir_filial_conta: Mapped[Optional[Imprimir_filial_contaEnum]] = Field("imprimir_filial_conta", Imprimir_filial_contaEnum, Imprimir_filial_contaEnum.VENDA)
    considerar_modelo_nao_fiscal: Mapped[Optional[Considerar_modelo_nao_fiscalEnum]] = Field("considerar_modelo_nao_fiscal", Considerar_modelo_nao_fiscalEnum, Considerar_modelo_nao_fiscalEnum.NAO)
    imprime_endereco_boleto: Mapped[Optional[Imprime_endereco_boletoEnum]] = Field("imprime_endereco_boleto", Imprime_endereco_boletoEnum, Imprime_endereco_boletoEnum.SIM)
    imprime_fone_fatura_d: Mapped[Optional[Imprime_fone_fatura_dEnum]] = Field("imprime_fone_fatura_d", Imprime_fone_fatura_dEnum, Imprime_fone_fatura_dEnum.NAO)
    imp_nome_sacador_avalista: Mapped[Optional[Imp_nome_sacador_avalistaEnum]] = Field("imp_nome_sacador_avalista", Imp_nome_sacador_avalistaEnum, Imp_nome_sacador_avalistaEnum.SIM)
    imprime_prod_val_zero: Mapped[Optional[Imprime_prod_val_zeroEnum]] = Field("imprime_prod_val_zero", Imprime_prod_val_zeroEnum, Imprime_prod_val_zeroEnum.SIM)
    imprime_tipo_resolucao_anatel: Mapped[Optional[Imprime_tipo_resolucao_anatelEnum]] = Field("imprime_tipo_resolucao_anatel", Imprime_tipo_resolucao_anatelEnum, Imprime_tipo_resolucao_anatelEnum.NAO)
    mask_cpf_cnpj_impressao_boleto: Mapped[Optional[Mask_cpf_cnpj_impressao_boletoEnum]] = Field("mask_cpf_cnpj_impressao_boleto", Mask_cpf_cnpj_impressao_boletoEnum, Mask_cpf_cnpj_impressao_boletoEnum.NAO)
    mostra_cep_beneficiario_impressao: Mapped[Optional[Mostra_cep_beneficiario_impressaoEnum]] = Field("mostra_cep_beneficiario_impressao", Mostra_cep_beneficiario_impressaoEnum, Mostra_cep_beneficiario_impressaoEnum.NAO)
    agrupar_produtos_por_descricao: Mapped[Optional[Agrupar_produtos_por_descricaoEnum]] = Field("agrupar_produtos_por_descricao", Agrupar_produtos_por_descricaoEnum, Agrupar_produtos_por_descricaoEnum.NAO)
    imprimir_beneficiario_gateway: Mapped[Optional[Imprimir_beneficiario_gatewayEnum]] = Field("imprimir_beneficiario_gateway", Imprimir_beneficiario_gatewayEnum, Imprimir_beneficiario_gatewayEnum.RAZAO_SOCIAL)
    obs_adicional_boleto: Mapped[Optional[str]] = Field("obs_adicional_boleto", str, '')
    imp_nome_beneficiario: Mapped[Imp_nome_beneficiarioEnum] = Field("imp_nome_beneficiario", Imp_nome_beneficiarioEnum, Imp_nome_beneficiarioEnum.RAZAO_SOCIAL)
    imp_nome_beneficiario_recibo: Mapped[Optional[Imp_nome_beneficiario_reciboEnum]] = Field("imp_nome_beneficiario_recibo", Imp_nome_beneficiario_reciboEnum, Imp_nome_beneficiario_reciboEnum.RAZAO_SOCIAL)
    boletos_capa_contratos: Mapped[Optional[Boletos_capa_contratosEnum]] = Field("boletos_capa_contratos", Boletos_capa_contratosEnum, Boletos_capa_contratosEnum.NAO)
    boleto_capa: Mapped[Optional[str]] = Field("boleto_capa", str, '')
    boleto_capa_cliente_referencia: Mapped[Optional[str]] = Field("boleto_capa_cliente_referencia", str, '')
    fone_cliente_capa: Mapped[Optional[str]] = Field("fone_cliente_capa", str, '')
    boleto_capa_local: Mapped[Optional[Boleto_capa_localEnum]] = Field("boleto_capa_local", Boleto_capa_localEnum, Boleto_capa_localEnum.NO_INICIO)
    boleto_capa_imagem: Mapped[Optional[Any]] = Field("boleto_capa_imagem", Any, None)
    boleto_capa_x: Mapped[Optional[str]] = Field("boleto_capa_x", str, '')
    boleto_capa_y: Mapped[Optional[str]] = Field("boleto_capa_y", str, '')
    tamanho_quadro_endereco_x: Mapped[Optional[str]] = Field("tamanho_quadro_endereco_x", str, '')
    tamanho_quadro_endereco_y: Mapped[Optional[str]] = Field("tamanho_quadro_endereco_y", str, '')
    tipo_baixa: Mapped[Optional[Tipo_baixaEnum]] = Field("tipo_baixa", Tipo_baixaEnum, Tipo_baixaEnum.DESCONTO)
    validar_juros_multa: Mapped[Optional[Validar_juros_multaEnum]] = Field("validar_juros_multa", Validar_juros_multaEnum, Validar_juros_multaEnum.NAO)
    id_produto_cob_adicional: Mapped[Optional[int]] = Field("id_produto_cob_adicional", int, None)
    id_fn_areceber_modelo: Mapped[Optional[int]] = Field("id_fn_areceber_modelo", int, None)

    @property
    def table(self) -> str:
        return "fn_carteira_cobranca"
    
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
        return {key: serialize(value) for key, value in data.items()}
    def is_valid(self) -> bool:
        return self.id is not None and self.descricao is not None and self.id_conta is not None and self.remover_fundo_capa_carteira is not None
