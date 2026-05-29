from __future__ import annotations
from typing import Optional
from ORM_IXC.interfaces import IModelWithId
from ORM_IXC.enums.contratoDoCliente import *
from ORM_IXC.statemants.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel
from ORM_IXC.statemants.mapper import Mapped, field as mapped_field


@MetaModels
class ContratoDoClienteModel(IModelWithId, BaseModel):
    id :Mapped[Optional[int]]
    id_cliente :Mapped[int]
    id_vd_contrato :Mapped[int]
    contrato :Mapped[str]
    id_tipo_contrato :Mapped[int]
    id_modelo :Mapped[int]
    id_filial :Mapped[int]
    data :Mapped[str]
    id_tipo_documento :Mapped[int]
    id_carteira_cobranca :Mapped[int]
    id_vendedor :Mapped[int]
    endereco_padrao_cliente :Mapped[str]
    tipo :Mapped[TipoEnum] = mapped_field(TipoEnum.INTERNET)
    estrato_social_col :Mapped[Optional[Estrato_social_colEnum]] = mapped_field(None)
    descricao_aux_plano_venda :Mapped[Optional[str]] = mapped_field('')
    assinatura_digital :Mapped[Optional[Assinatura_digitalEnum]] = mapped_field(Assinatura_digitalEnum.PADRAO)
    integracao_assinatura_digital :Mapped[Optional[Integracao_assinatura_digitalEnum]] = mapped_field(Integracao_assinatura_digitalEnum.PADRAO)
    liberacao_bloqueio_manual :Mapped[Optional[Liberacao_bloqueio_manualEnum]] = mapped_field(Liberacao_bloqueio_manualEnum.PADRAO)
    indicacao_contrato_id :Mapped[Optional[int]] = mapped_field(None)
    data_assinatura :Mapped[Optional[str]] = mapped_field('')
    isentar_contrato :Mapped[Optional[Isentar_contratoEnum]] = mapped_field(Isentar_contratoEnum.NAO)
    data_ativacao :Mapped[Optional[str]] = mapped_field('')
    situacao_financeira_contrato :Mapped[Optional[str]] = mapped_field('')
    data_renovacao :Mapped[Optional[str]] = mapped_field('')
    pago_ate_data :Mapped[Optional[str]] = mapped_field('')
    status :Mapped[Optional[StatusEnum]] = mapped_field(StatusEnum.PRE_CONTRATO)
    status_internet :Mapped[Optional[Status_internetEnum]] = mapped_field(Status_internetEnum.DESATIVADO)
    status_velocidade :Mapped[Optional[Status_velocidadeEnum]] = mapped_field(Status_velocidadeEnum.NORMAL)
    tipo_produtos_plano :Mapped[Optional[str]] = mapped_field('')
    motivo_inclusao :Mapped[Optional[Motivo_inclusaoEnum]] = mapped_field(Motivo_inclusaoEnum.INSTALACAO)
    id_motivo_inclusao :Mapped[Optional[int]] = mapped_field(None)
    id_indexador_reajuste :Mapped[Optional[int]] = mapped_field(None)
    url_assinatura_digital :Mapped[Optional[str]] = mapped_field('')
    token_assinatura_digital :Mapped[Optional[str]] = mapped_field('')
    moeda :Mapped[Optional[int]] = mapped_field(None)
    comissao :Mapped[Optional[str]] = mapped_field('')
    cc_previsao :Mapped[Cc_previsaoEnum] = mapped_field(Cc_previsaoEnum.CONFIGURACAO_PADRAO_)
    tipo_cobranca :Mapped[Tipo_cobrancaEnum] = mapped_field(Tipo_cobrancaEnum.CONFIGURACAO_PADRAO)
    id_contrato_principal :Mapped[Optional[int]] = mapped_field(None)
    renovacao_automatica :Mapped[Renovacao_automaticaEnum] = mapped_field(Renovacao_automaticaEnum.SIM)
    gerar_finan_assin_digital_contrato :Mapped[Optional[Gerar_finan_assin_digital_contratoEnum]] = mapped_field(Gerar_finan_assin_digital_contratoEnum.PADRAO)
    agrupar_financeiro_contrato :Mapped[Optional[Agrupar_financeiro_contratoEnum]] = mapped_field(Agrupar_financeiro_contratoEnum.PADRAO)
    aplicar_desconto_tempo_bloqueio :Mapped[Optional[Aplicar_desconto_tempo_bloqueioEnum]] = mapped_field(Aplicar_desconto_tempo_bloqueioEnum.PADRAO)
    num_parcelas_atraso :Mapped[Optional[str]] = mapped_field('')
    contrato_recorrencia :Mapped[Optional[Contrato_recorrenciaEnum]] = mapped_field(None)
    credit_card_recorrente_bandeira_cartao :Mapped[Optional[str]] = mapped_field('')
    credit_card_recorrente_token :Mapped[Optional[str]] = mapped_field('')
    ids_contratos_recorrencia :Mapped[Optional[str]] = mapped_field('')
    status_recorrencia :Mapped[Optional[Status_recorrenciaEnum]] = mapped_field(None)
    base_geracao_tipo_doc :Mapped[Base_geracao_tipo_docEnum] = mapped_field(Base_geracao_tipo_docEnum.PADRAO)
    tipo_doc_opc :Mapped[Optional[int]] = mapped_field(None)
    tipo_doc_opc2 :Mapped[Optional[int]] = mapped_field(None)
    tipo_doc_opc3 :Mapped[Optional[int]] = mapped_field(None)
    tipo_doc_opc4 :Mapped[Optional[int]] = mapped_field(None)
    nf_info_adicionais :Mapped[Optional[str]] = mapped_field('')
    id_tipo_doc_ativ :Mapped[Optional[int]] = mapped_field(None)
    id_produto_ativ :Mapped[Optional[int]] = mapped_field(None)
    taxa_instalacao :Mapped[Optional[str]] = mapped_field('')
    id_cond_pag_ativ :Mapped[Optional[int]] = mapped_field(None)
    id_responsavel :Mapped[Optional[int]] = mapped_field(None)
    id_vendedor_ativ :Mapped[Optional[int]] = mapped_field(None)
    ativacao_numero_parcelas :Mapped[Optional[str]] = mapped_field('')
    ativacao_vencimentos :Mapped[Optional[str]] = mapped_field('')
    btn_nf_ativacao :Mapped[Optional[str]] = mapped_field('')
    ativacao_valor_parcela :Mapped[Optional[str]] = mapped_field('')
    fidelidade :Mapped[Optional[str]] = mapped_field('')
    data_expiracao :Mapped[Optional[str]] = mapped_field('')
    dica_data_expiracao :Mapped[Optional[str]] = mapped_field('')
    desconto_fidelidade :Mapped[Optional[str]] = mapped_field('')
    id_instalador :Mapped[Optional[int]] = mapped_field(None)
    taxa_improdutiva :Mapped[Optional[str]] = mapped_field('')
    venc_personalizado :Mapped[Optional[str]] = mapped_field('')
    com_entrada :Mapped[Optional[str]] = mapped_field('')
    dia_fixo_vencimento :Mapped[Optional[str]] = mapped_field('')
    tipo_condicao_pag :Mapped[Optional[str]] = mapped_field('')
    bloqueio_automatico :Mapped[Bloqueio_automaticoEnum] = mapped_field(Bloqueio_automaticoEnum.SIM)
    nao_bloquear_ate :Mapped[Optional[str]] = mapped_field('')
    aviso_atraso :Mapped[Aviso_atrasoEnum] = mapped_field(Aviso_atrasoEnum.SIM)
    nao_avisar_ate :Mapped[Optional[str]] = mapped_field('')
    desbloqueio_confianca :Mapped[Optional[Desbloqueio_confiancaEnum]] = mapped_field(Desbloqueio_confiancaEnum.PADRAO)
    desbloqueio_confianca_ativo :Mapped[Optional[Desbloqueio_confianca_ativoEnum]] = mapped_field(Desbloqueio_confianca_ativoEnum.NAO)
    restricao_auto_desbloqueio :Mapped[Optional[Restricao_auto_desbloqueioEnum]] = mapped_field(Restricao_auto_desbloqueioEnum.NAO)
    motivo_restricao_auto_desbloq :Mapped[Optional[str]] = mapped_field('')
    obs :Mapped[Optional[str]] = mapped_field('')
    nao_susp_parc_ate :Mapped[Optional[str]] = mapped_field('')
    liberacao_suspensao_parcial :Mapped[Optional[Liberacao_suspensao_parcialEnum]] = mapped_field(Liberacao_suspensao_parcialEnum.PADRAO)
    utilizando_auto_libera_susp_parc :Mapped[Optional[Utilizando_auto_libera_susp_parcEnum]] = mapped_field(Utilizando_auto_libera_susp_parcEnum.NAO)
    restricao_auto_libera_susp_parcial :Mapped[Optional[Restricao_auto_libera_susp_parcialEnum]] = mapped_field(Restricao_auto_libera_susp_parcialEnum.NAO)
    motivo_restri_auto_libera_parc :Mapped[Optional[str]] = mapped_field('')
    contrato_suspenso :Mapped[Optional[Contrato_suspensoEnum]] = mapped_field(Contrato_suspensoEnum.NAO)
    data_inicial_suspensao :Mapped[Optional[str]] = mapped_field('')
    data_final_suspensao :Mapped[Optional[str]] = mapped_field('')
    data_acesso_desativado :Mapped[Optional[str]] = mapped_field('')
    fieldset_mensagem_atencao_irreversivel :Mapped[Optional[str]] = mapped_field('')
    data_cancelamento :Mapped[Optional[str]] = mapped_field('')
    id_responsavel_cancelamento :Mapped[Optional[int]] = mapped_field(None)
    motivo_cancelamento :Mapped[Optional[int]] = mapped_field(None)
    motivo_adicional :Mapped[Optional[int]] = mapped_field(None)
    concorrente_mot_adicional :Mapped[Optional[int]] = mapped_field(None)
    obs_cancelamento :Mapped[Optional[str]] = mapped_field('')
    tempo_permanencia :Mapped[Optional[str]] = mapped_field('')
    dica_tmp :Mapped[Optional[str]] = mapped_field('')
    origem_cancelamento :Mapped[Optional[Origem_cancelamentoEnum]] = mapped_field(None)
    data_negativacao :Mapped[Optional[str]] = mapped_field('')
    id_responsavel_negativacao :Mapped[Optional[int]] = mapped_field(None)
    protocolo_negativacao :Mapped[Optional[str]] = mapped_field('')
    id_motivo_negativacao :Mapped[Optional[int]] = mapped_field(None)
    obs_negativacao :Mapped[Optional[str]] = mapped_field('')
    data_desistencia :Mapped[Optional[str]] = mapped_field('')
    id_responsavel_desistencia :Mapped[Optional[int]] = mapped_field(None)
    motivo_desistencia :Mapped[Optional[int]] = mapped_field(None)
    obs_desistencia :Mapped[Optional[str]] = mapped_field('')
    obs_contrato :Mapped[Optional[str]] = mapped_field('')
    alerta_contrato :Mapped[Optional[str]] = mapped_field('')
    imp_realizado :Mapped[Optional[Imp_realizadoEnum]] = mapped_field(Imp_realizadoEnum.SIM)
    imp_inicial :Mapped[Optional[str]] = mapped_field('')
    imp_carteira :Mapped[Optional[Imp_carteiraEnum]] = mapped_field(Imp_carteiraEnum.EM_ANDAMENTO)
    imp_importacao :Mapped[Optional[Imp_importacaoEnum]] = mapped_field(Imp_importacaoEnum.EM_ANDAMENTO)
    imp_treinamento :Mapped[Optional[Imp_treinamentoEnum]] = mapped_field(Imp_treinamentoEnum.EM_ANDAMENTO)
    imp_rede :Mapped[Optional[Imp_redeEnum]] = mapped_field(Imp_redeEnum.EM_ANDAMENTO)
    imp_bkp :Mapped[Optional[Imp_bkpEnum]] = mapped_field(Imp_bkpEnum.EM_ANDAMENTO)
    imp_obs :Mapped[Optional[str]] = mapped_field('')
    imp_final :Mapped[Optional[str]] = mapped_field('')
    imp_status :Mapped[Optional[Imp_statusEnum]] = mapped_field(Imp_statusEnum.EM_ANDAMENTO)
    imp_motivo :Mapped[Optional[str]] = mapped_field('')
    dt_ult_bloq_auto :Mapped[Optional[str]] = mapped_field('')
    dt_ult_bloq_manual :Mapped[Optional[str]] = mapped_field('')
    dt_ult_desbloq_auto :Mapped[Optional[str]] = mapped_field('')
    dt_ult_desbloq_manual :Mapped[Optional[str]] = mapped_field('')
    dt_ult_finan_atraso :Mapped[Optional[str]] = mapped_field('')
    dt_ult_des_bloq_conf :Mapped[Optional[str]] = mapped_field('')
    dt_ult_liberacao_susp_parc :Mapped[Optional[str]] = mapped_field('')
    dt_ult_ativacao :Mapped[Optional[str]] = mapped_field('')
    dt_utl_negativacao :Mapped[Optional[str]] = mapped_field('')
    dt_ult_desiste :Mapped[Optional[str]] = mapped_field('')
    data_cadastro_sistema :Mapped[Optional[str]] = mapped_field('')
    ultima_atualizacao :Mapped[Optional[str]] = mapped_field('')
    data_retomada_contrato :Mapped[Optional[str]] = mapped_field('')
    endereco_padrao_alert :Mapped[Optional[str]] = mapped_field('')
    id_condominio :Mapped[Optional[int]] = mapped_field(None)
    condominio_novo :Mapped[Optional[int]] = mapped_field(None)
    bloco :Mapped[Optional[str]] = mapped_field('')
    bloco_novo :Mapped[Optional[str]] = mapped_field('')
    apartamento :Mapped[Optional[str]] = mapped_field('')
    apartamento_novo :Mapped[Optional[str]] = mapped_field('')
    cep :Mapped[Optional[str]] = mapped_field('')
    cep_novo :Mapped[Optional[str]] = mapped_field('')
    endereco :Mapped[Optional[str]] = mapped_field('')
    endereco_novo :Mapped[Optional[str]] = mapped_field('')
    numero :Mapped[Optional[str]] = mapped_field('')
    numero_novo :Mapped[Optional[str]] = mapped_field('')
    bairro :Mapped[Optional[str]] = mapped_field('')
    bairro_novo :Mapped[Optional[str]] = mapped_field('')
    cidade :Mapped[Optional[int]] = mapped_field(None)
    cidade_novo :Mapped[Optional[int]] = mapped_field(None)
    complemento :Mapped[Optional[str]] = mapped_field('')
    complemento_novo :Mapped[Optional[str]] = mapped_field('')
    referencia :Mapped[Optional[str]] = mapped_field('')
    referencia_novo :Mapped[Optional[str]] = mapped_field('')
    latitude :Mapped[Optional[str]] = mapped_field('')
    latitude_novo :Mapped[Optional[str]] = mapped_field('')
    longitude :Mapped[Optional[str]] = mapped_field('')
    longitude_novo :Mapped[Optional[str]] = mapped_field('')
    tipo_localidade :Mapped[Optional[Tipo_localidadeEnum]] = mapped_field(Tipo_localidadeEnum.ZONA_URBANA)
    avalista_1 :Mapped[Optional[int]] = mapped_field(None)
    avalista_2 :Mapped[Optional[int]] = mapped_field(None)
    testemunha_assinatura_digital :Mapped[Optional[int]] = mapped_field(None)
    email_assinatura_digital :Mapped[Optional[str]] = mapped_field('')
    contato_assinatura_digital :Mapped[Optional[str]] = mapped_field('')
    document_photo :Mapped[Optional[Document_photoEnum]] = mapped_field(Document_photoEnum.PADRAO)
    selfie_photo :Mapped[Optional[Selfie_photoEnum]] = mapped_field(Selfie_photoEnum.PADRAO)

    @property
    def table(self) -> str:
        return "cliente_contrato"
   
    def _serialize_enum(self, value) -> str:
        """Serializa um valor de enum ou retorna string vazia se None"""
        if value is None:
            return ''
        if hasattr(value, 'value'):
            return str(value.value)
        return str(value)
    
    def to_dict(self) -> dict[str, str]:
        def serialize(value) -> str:
            if value is None:
                return ''
            raw = getattr(value, 'value', value)
            return '' if raw is None else str(raw)

        data = {
            'id': str(self.id),
            'id_cliente': str(self.id_cliente) if self.id_cliente is not None else '',
            'id_vd_contrato': str(self.id_vd_contrato) if self.id_vd_contrato is not None else '',
            'contrato': self.contrato if self.contrato is not None else '',
            'id_tipo_contrato': str(self.id_tipo_contrato) if self.id_tipo_contrato is not None else '',
            'id_modelo': str(self.id_modelo) if self.id_modelo is not None else '',
            'id_filial': str(self.id_filial) if self.id_filial is not None else '',
            'data': self.data if self.data is not None else '',
            'id_tipo_documento': str(self.id_tipo_documento) if self.id_tipo_documento is not None else '',
            'id_carteira_cobranca': str(self.id_carteira_cobranca) if self.id_carteira_cobranca is not None else '',
            'id_vendedor': str(self.id_vendedor) if self.id_vendedor is not None else '',
            'endereco_padrao_cliente': self.endereco_padrao_cliente if self.endereco_padrao_cliente is not None else '',
            'tipo': self._serialize_enum(self.tipo) if self.tipo is not None else '',
            'estrato_social_col': self._serialize_enum(self.estrato_social_col) if self.estrato_social_col is not None else '',
            'descricao_aux_plano_venda': self.descricao_aux_plano_venda if self.descricao_aux_plano_venda is not None else '',
            'assinatura_digital': self._serialize_enum(self.assinatura_digital) if self.assinatura_digital is not None else '',
            'integracao_assinatura_digital': self._serialize_enum(self.integracao_assinatura_digital) if self.integracao_assinatura_digital is not None else '',
            'liberacao_bloqueio_manual': self._serialize_enum(self.liberacao_bloqueio_manual) if self.liberacao_bloqueio_manual is not None else '',
            'indicacao_contrato_id': str(self.indicacao_contrato_id) if self.indicacao_contrato_id is not None else '',
            'data_assinatura': self.data_assinatura if self.data_assinatura is not None else '',
            'isentar_contrato': self._serialize_enum(self.isentar_contrato) if self.isentar_contrato is not None else '',
            'data_ativacao': self.data_ativacao if self.data_ativacao is not None else '',
            'situacao_financeira_contrato': self.situacao_financeira_contrato if self.situacao_financeira_contrato is not None else '',
            'data_renovacao': self.data_renovacao if self.data_renovacao is not None else '',
            'pago_ate_data': self.pago_ate_data if self.pago_ate_data is not None else '',
            'status': self._serialize_enum(self.status) if self.status is not None else '',
            'status_internet': self._serialize_enum(self.status_internet) if self.status_internet is not None else '',
            'status_velocidade': self._serialize_enum(self.status_velocidade) if self.status_velocidade is not None else '',
            'tipo_produtos_plano': self.tipo_produtos_plano if self.tipo_produtos_plano is not None else '',
            'motivo_inclusao': self._serialize_enum(self.motivo_inclusao) if self.motivo_inclusao is not None else '',
            'id_motivo_inclusao': str(self.id_motivo_inclusao) if self.id_motivo_inclusao is not None else '',
            'id_indexador_reajuste': str(self.id_indexador_reajuste) if self.id_indexador_reajuste is not None else '',
            'url_assinatura_digital': self.url_assinatura_digital if self.url_assinatura_digital is not None else '',
            'token_assinatura_digital': self.token_assinatura_digital if self.token_assinatura_digital is not None else '',
            'moeda': str(self.moeda) if self.moeda is not None else '',
            'comissao': self.comissao if self.comissao is not None else '',
            'cc_previsao': self._serialize_enum(self.cc_previsao) if self.cc_previsao is not None else '',
            'tipo_cobranca': self._serialize_enum(self.tipo_cobranca) if self.tipo_cobranca is not None else '',
            'id_contrato_principal': str(self.id_contrato_principal) if self.id_contrato_principal is not None else '',
            'renovacao_automatica': self._serialize_enum(self.renovacao_automatica) if self.renovacao_automatica is not None else '',
            'gerar_finan_assin_digital_contrato': self._serialize_enum(self.gerar_finan_assin_digital_contrato) if self.gerar_finan_assin_digital_contrato is not None else '',
            'agrupar_financeiro_contrato': self._serialize_enum(self.agrupar_financeiro_contrato) if self.agrupar_financeiro_contrato is not None else '',
            'aplicar_desconto_tempo_bloqueio': self._serialize_enum(self.aplicar_desconto_tempo_bloqueio) if self.aplicar_desconto_tempo_bloqueio is not None else '',
            'num_parcelas_atraso': self.num_parcelas_atraso if self.num_parcelas_atraso is not None else '',
            'contrato_recorrencia': self._serialize_enum(self.contrato_recorrencia) if self.contrato_recorrencia is not None else '',
            'credit_card_recorrente_bandeira_cartao': self.credit_card_recorrente_bandeira_cartao if self.credit_card_recorrente_bandeira_cartao is not None else '',
            'credit_card_recorrente_token': self.credit_card_recorrente_token if self.credit_card_recorrente_token is not None else '',
            'ids_contratos_recorrencia': self.ids_contratos_recorrencia if self.ids_contratos_recorrencia is not None else '',
            'status_recorrencia': self._serialize_enum(self.status_recorrencia) if self.status_recorrencia is not None else '',
            'base_geracao_tipo_doc': self._serialize_enum(self.base_geracao_tipo_doc) if self.base_geracao_tipo_doc is not None else '',
            'tipo_doc_opc': str(self.tipo_doc_opc) if self.tipo_doc_opc is not None else '',
            'tipo_doc_opc2': str(self.tipo_doc_opc2) if self.tipo_doc_opc2 is not None else '',
            'tipo_doc_opc3': str(self.tipo_doc_opc3) if self.tipo_doc_opc3 is not None else '',
            'tipo_doc_opc4': str(self.tipo_doc_opc4) if self.tipo_doc_opc4 is not None else '',
            'nf_info_adicionais': self.nf_info_adicionais if self.nf_info_adicionais is not None else '',
            'id_tipo_doc_ativ': str(self.id_tipo_doc_ativ) if self.id_tipo_doc_ativ is not None else '',
            'id_produto_ativ': str(self.id_produto_ativ) if self.id_produto_ativ is not None else '',
            'taxa_instalacao': self.taxa_instalacao if self.taxa_instalacao is not None else '',
            'id_cond_pag_ativ': str(self.id_cond_pag_ativ) if self.id_cond_pag_ativ is not None else '',
            'id_responsavel': str(self.id_responsavel) if self.id_responsavel is not None else '',
            'id_vendedor_ativ': str(self.id_vendedor_ativ) if self.id_vendedor_ativ is not None else '',
            'ativacao_numero_parcelas': self.ativacao_numero_parcelas if self.ativacao_numero_parcelas is not None else '',
            'ativacao_vencimentos': self.ativacao_vencimentos if self.ativacao_vencimentos is not None else '',
            'btn_nf_ativacao': self.btn_nf_ativacao if self.btn_nf_ativacao is not None else '',
            'ativacao_valor_parcela': self.ativacao_valor_parcela if self.ativacao_valor_parcela is not None else '',
            'fidelidade': self.fidelidade if self.fidelidade is not None else '',
            'data_expiracao': self.data_expiracao if self.data_expiracao is not None else '',
            'dica_data_expiracao': self.dica_data_expiracao if self.dica_data_expiracao is not None else '',
            'desconto_fidelidade': self.desconto_fidelidade if self.desconto_fidelidade is not None else '',
            'id_instalador': str(self.id_instalador) if self.id_instalador is not None else '',
            'taxa_improdutiva': self.taxa_improdutiva if self.taxa_improdutiva is not None else '',
            'venc_personalizado': self.venc_personalizado if self.venc_personalizado is not None else '',
            'com_entrada': self.com_entrada if self.com_entrada is not None else '',
            'dia_fixo_vencimento': self.dia_fixo_vencimento if self.dia_fixo_vencimento is not None else '',
            'tipo_condicao_pag': self.tipo_condicao_pag if self.tipo_condicao_pag is not None else '',
            'bloqueio_automatico': self._serialize_enum(self.bloqueio_automatico) if self.bloqueio_automatico is not None else '',
            'nao_bloquear_ate': self.nao_bloquear_ate if self.nao_bloquear_ate is not None else '',
            'aviso_atraso': self._serialize_enum(self.aviso_atraso) if self.aviso_atraso is not None else '',
            'nao_avisar_ate': self.nao_avisar_ate if self.nao_avisar_ate is not None else '',
            'desbloqueio_confianca': self._serialize_enum(self.desbloqueio_confianca) if self.desbloqueio_confianca is not None else '',
            'desbloqueio_confianca_ativo': self._serialize_enum(self.desbloqueio_confianca_ativo) if self.desbloqueio_confianca_ativo is not None else '',
            'restricao_auto_desbloqueio': self._serialize_enum(self.restricao_auto_desbloqueio) if self.restricao_auto_desbloqueio is not None else '',
            'motivo_restricao_auto_desbloq': self.motivo_restricao_auto_desbloq if self.motivo_restricao_auto_desbloq is not None else '',
            'obs': self.obs if self.obs is not None else '',
            'nao_susp_parc_ate': self.nao_susp_parc_ate if self.nao_susp_parc_ate is not None else '',
            'liberacao_suspensao_parcial': self._serialize_enum(self.liberacao_suspensao_parcial) if self.liberacao_suspensao_parcial is not None else '',
            'utilizando_auto_libera_susp_parc': self._serialize_enum(self.utilizando_auto_libera_susp_parc) if self.utilizando_auto_libera_susp_parc is not None else '',
            'restricao_auto_libera_susp_parcial': self._serialize_enum(self.restricao_auto_libera_susp_parcial) if self.restricao_auto_libera_susp_parcial is not None else '',
            'motivo_restri_auto_libera_parc': self.motivo_restri_auto_libera_parc if self.motivo_restri_auto_libera_parc is not None else '',
            'contrato_suspenso': self._serialize_enum(self.contrato_suspenso) if self.contrato_suspenso is not None else '',
            'data_inicial_suspensao': self.data_inicial_suspensao if self.data_inicial_suspensao is not None else '',
            'data_final_suspensao': self.data_final_suspensao if self.data_final_suspensao is not None else '',
            'data_acesso_desativado': self.data_acesso_desativado if self.data_acesso_desativado is not None else '',
            'fieldset_mensagem_atencao_irreversivel': self.fieldset_mensagem_atencao_irreversivel if self.fieldset_mensagem_atencao_irreversivel is not None else '',
            'data_cancelamento': self.data_cancelamento if self.data_cancelamento is not None else '',
            'id_responsavel_cancelamento': str(self.id_responsavel_cancelamento) if self.id_responsavel_cancelamento is not None else '',
            'motivo_cancelamento': str(self.motivo_cancelamento) if self.motivo_cancelamento is not None else '',
            'motivo_adicional': str(self.motivo_adicional) if self.motivo_adicional is not None else '',
            'concorrente_mot_adicional': str(self.concorrente_mot_adicional) if self.concorrente_mot_adicional is not None else '',
            'obs_cancelamento': self.obs_cancelamento if self.obs_cancelamento is not None else '',
            'tempo_permanencia': self.tempo_permanencia if self.tempo_permanencia is not None else '',
            'dica_tmp': self.dica_tmp if self.dica_tmp is not None else '',
            'origem_cancelamento': self._serialize_enum(self.origem_cancelamento) if self.origem_cancelamento is not None else '',
            'data_negativacao': self.data_negativacao if self.data_negativacao is not None else '',
            'id_responsavel_negativacao': str(self.id_responsavel_negativacao) if self.id_responsavel_negativacao is not None else '',
            'protocolo_negativacao': self.protocolo_negativacao if self.protocolo_negativacao is not None else '',
            'id_motivo_negativacao': str(self.id_motivo_negativacao) if self.id_motivo_negativacao is not None else '',
            'obs_negativacao': self.obs_negativacao if self.obs_negativacao is not None else '',
            'data_desistencia': self.data_desistencia if self.data_desistencia is not None else '',
            'id_responsavel_desistencia': str(self.id_responsavel_desistencia) if self.id_responsavel_desistencia is not None else '',
            'motivo_desistencia': str(self.motivo_desistencia) if self.motivo_desistencia is not None else '',
            'obs_desistencia': self.obs_desistencia if self.obs_desistencia is not None else '',
            'obs_contrato': self.obs_contrato if self.obs_contrato is not None else '',
            'alerta_contrato': self.alerta_contrato if self.alerta_contrato is not None else '',
            'imp_realizado': self._serialize_enum(self.imp_realizado) if self.imp_realizado is not None else '',
            'imp_inicial': self.imp_inicial if self.imp_inicial is not None else '',
            'imp_carteira': self._serialize_enum(self.imp_carteira) if self.imp_carteira is not None else '',
            'imp_importacao': self._serialize_enum(self.imp_importacao) if self.imp_importacao is not None else '',
            'imp_treinamento': self._serialize_enum(self.imp_treinamento) if self.imp_treinamento is not None else '',
            'imp_rede': self._serialize_enum(self.imp_rede) if self.imp_rede is not None else '',
            'imp_bkp': self._serialize_enum(self.imp_bkp) if self.imp_bkp is not None else '',
            'imp_obs': self.imp_obs if self.imp_obs is not None else '',
            'imp_final': self.imp_final if self.imp_final is not None else '',
            'imp_status': self._serialize_enum(self.imp_status) if self.imp_status is not None else '',
            'imp_motivo': self.imp_motivo if self.imp_motivo is not None else '',
            'dt_ult_bloq_auto': self.dt_ult_bloq_auto if self.dt_ult_bloq_auto is not None else '',
            'dt_ult_bloq_manual': self.dt_ult_bloq_manual if self.dt_ult_bloq_manual is not None else '',
            'dt_ult_desbloq_auto': self.dt_ult_desbloq_auto if self.dt_ult_desbloq_auto is not None else '',
            'dt_ult_desbloq_manual': self.dt_ult_desbloq_manual if self.dt_ult_desbloq_manual is not None else '',
            'dt_ult_finan_atraso': self.dt_ult_finan_atraso if self.dt_ult_finan_atraso is not None else '',
            'dt_ult_des_bloq_conf': self.dt_ult_des_bloq_conf if self.dt_ult_des_bloq_conf is not None else '',
            'dt_ult_liberacao_susp_parc': self.dt_ult_liberacao_susp_parc if self.dt_ult_liberacao_susp_parc is not None else '',
            'dt_ult_ativacao': self.dt_ult_ativacao if self.dt_ult_ativacao is not None else '',
            'dt_utl_negativacao': self.dt_utl_negativacao if self.dt_utl_negativacao is not None else '',
            'dt_ult_desiste': self.dt_ult_desiste if self.dt_ult_desiste is not None else '',
            'data_cadastro_sistema': self.data_cadastro_sistema if self.data_cadastro_sistema is not None else '',
            'ultima_atualizacao': self.ultima_atualizacao if self.ultima_atualizacao is not None else '',
            'data_retomada_contrato': self.data_retomada_contrato if self.data_retomada_contrato is not None else '',
            'endereco_padrao_alert': self.endereco_padrao_alert if self.endereco_padrao_alert is not None else '',
            'id_condominio': str(self.id_condominio) if self.id_condominio is not None else '',
            'condominio_novo': str(self.condominio_novo) if self.condominio_novo is not None else '',
            'bloco': self.bloco if self.bloco is not None else '',
            'bloco_novo': self.bloco_novo if self.bloco_novo is not None else '',
            'apartamento': self.apartamento if self.apartamento is not None else '',
            'apartamento_novo': self.apartamento_novo if self.apartamento_novo is not None else '',
            'cep': self.cep if self.cep is not None else '',
            'cep_novo': self.cep_novo if self.cep_novo is not None else '',
            'endereco': self.endereco if self.endereco is not None else '',
            'endereco_novo': self.endereco_novo if self.endereco_novo is not None else '',
            'numero': self.numero if self.numero is not None else '',
            'numero_novo': self.numero_novo if self.numero_novo is not None else '',
            'bairro': self.bairro if self.bairro is not None else '',
            'bairro_novo': self.bairro_novo if self.bairro_novo is not None else '',
            'cidade': str(self.cidade) if self.cidade is not None else '',
            'cidade_novo': str(self.cidade_novo) if self.cidade_novo is not None else '',
            'complemento': self.complemento if self.complemento is not None else '',
            'complemento_novo': self.complemento_novo if self.complemento_novo is not None else '',
            'referencia': self.referencia if self.referencia is not None else '',
            'referencia_novo': self.referencia_novo if self.referencia_novo is not None else '',
            'latitude': self.latitude if self.latitude is not None else '',
            'latitude_novo': self.latitude_novo if self.latitude_novo is not None else '',
            'longitude': self.longitude if self.longitude is not None else '',
            'longitude_novo': self.longitude_novo if self.longitude_novo is not None else '',
            'tipo_localidade': self._serialize_enum(self.tipo_localidade) if self.tipo_localidade is not None else '',
            'avalista_1': str(self.avalista_1) if self.avalista_1 is not None else '',
            'avalista_2': str(self.avalista_2) if self.avalista_2 is not None else '',
            'testemunha_assinatura_digital': str(self.testemunha_assinatura_digital) if self.testemunha_assinatura_digital is not None else '',
            'email_assinatura_digital': self.email_assinatura_digital if self.email_assinatura_digital is not None else '',
            'contato_assinatura_digital': self.contato_assinatura_digital if self.contato_assinatura_digital is not None else '',
            'document_photo': self._serialize_enum(self.document_photo) if self.document_photo is not None else '',
            'selfie_photo': self._serialize_enum(self.selfie_photo) if self.selfie_photo is not None else '',
        }
        return {key: serialize(value) for key, value in data.items()}


    def is_valid(self) -> bool:
        return self.id_autoincrement is not None and self.id_cliente is not None and self.id_vd_contrato is not None and self.contrato is not None and self.id_tipo_contrato is not None and self.id_modelo is not None and self.id_filial is not None and self.data is not None and self.id_tipo_documento is not None and self.id_carteira_cobranca is not None and self.id_vendedor is not None and self.endereco_padrao_cliente is not None