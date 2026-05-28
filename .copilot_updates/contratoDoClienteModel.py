from __future__ import annotations
from dataclasses import  dataclass, field
from typing import Optional
from ORM_IXC.interfaces import IModel, IModelWithId
from ORM_IXC.enums.contratoDoCliente import *
from ORM_IXC.statemants.classBase import Field
from ORM_IXC.statemants.metaManager import MetaModels
from ORM_IXC.models.defaultModel import BaseModel

@MetaModels
class ContratoDoClienteModel(IModelWithId, BaseModel):
    id: int
    id_cliente: int
    id_vd_contrato: int
    contrato: str
    id_tipo_contrato: int
    id_modelo: int
    id_filial: int
    data: str
    id_tipo_documento: int
    id_carteira_cobranca: int
    id_vendedor: int
    endereco_padrao_cliente: str
    tipo: Mapped[TipoEnum] = Field("tipo", TipoEnum, TipoEnum.INTERNET)
    estrato_social_col: Mapped[Optional[Estrato_social_colEnum]] = Field("estrato_social_col", Estrato_social_colEnum, None)
    descricao_aux_plano_venda: Mapped[Optional[str]] = Field("descricao_aux_plano_venda", str, '')
    assinatura_digital: Mapped[Optional[Assinatura_digitalEnum]] = Field("assinatura_digital", Assinatura_digitalEnum, Assinatura_digitalEnum.PADRAO)
    integracao_assinatura_digital: Mapped[Optional[Integracao_assinatura_digitalEnum]] = Field("integracao_assinatura_digital", Integracao_assinatura_digitalEnum, Integracao_assinatura_digitalEnum.PADRAO)
    liberacao_bloqueio_manual: Mapped[Optional[Liberacao_bloqueio_manualEnum]] = Field("liberacao_bloqueio_manual", Liberacao_bloqueio_manualEnum, Liberacao_bloqueio_manualEnum.PADRAO)
    indicacao_contrato_id: Mapped[Optional[int]] = Field("indicacao_contrato_id", int, None)
    data_assinatura: Mapped[Optional[str]] = Field("data_assinatura", str, '')
    isentar_contrato: Mapped[Optional[Isentar_contratoEnum]] = Field("isentar_contrato", Isentar_contratoEnum, Isentar_contratoEnum.NAO)
    data_ativacao: Mapped[Optional[str]] = Field("data_ativacao", str, '')
    situacao_financeira_contrato: Mapped[Optional[str]] = Field("situacao_financeira_contrato", str, '')
    data_renovacao: Mapped[Optional[str]] = Field("data_renovacao", str, '')
    pago_ate_data: Mapped[Optional[str]] = Field("pago_ate_data", str, '')
    status: Mapped[Optional[StatusEnum]] = Field("status", StatusEnum, StatusEnum.PRE_CONTRATO)
    status_internet: Mapped[Optional[Status_internetEnum]] = Field("status_internet", Status_internetEnum, Status_internetEnum.DESATIVADO)
    status_velocidade: Mapped[Optional[Status_velocidadeEnum]] = Field("status_velocidade", Status_velocidadeEnum, Status_velocidadeEnum.NORMAL)
    tipo_produtos_plano: Mapped[Optional[str]] = Field("tipo_produtos_plano", str, '')
    motivo_inclusao: Mapped[Optional[Motivo_inclusaoEnum]] = Field("motivo_inclusao", Motivo_inclusaoEnum, Motivo_inclusaoEnum.INSTALACAO)
    id_motivo_inclusao: Mapped[Optional[int]] = Field("id_motivo_inclusao", int, None)
    id_indexador_reajuste: Mapped[Optional[int]] = Field("id_indexador_reajuste", int, None)
    url_assinatura_digital: Mapped[Optional[str]] = Field("url_assinatura_digital", str, '')
    token_assinatura_digital: Mapped[Optional[str]] = Field("token_assinatura_digital", str, '')
    moeda: Mapped[Optional[int]] = Field("moeda", int, None)
    comissao: Mapped[Optional[str]] = Field("comissao", str, '')
    cc_previsao: Mapped[Cc_previsaoEnum] = Field("cc_previsao", Cc_previsaoEnum, Cc_previsaoEnum.CONFIGURACAO_PADRAO_)
    tipo_cobranca: Mapped[Tipo_cobrancaEnum] = Field("tipo_cobranca", Tipo_cobrancaEnum, Tipo_cobrancaEnum.CONFIGURACAO_PADRAO)
    id_contrato_principal: Mapped[Optional[int]] = Field("id_contrato_principal", int, None)
    renovacao_automatica: Mapped[Renovacao_automaticaEnum] = Field("renovacao_automatica", Renovacao_automaticaEnum, Renovacao_automaticaEnum.SIM)
    gerar_finan_assin_digital_contrato: Mapped[Optional[Gerar_finan_assin_digital_contratoEnum]] = Field("gerar_finan_assin_digital_contrato", Gerar_finan_assin_digital_contratoEnum, Gerar_finan_assin_digital_contratoEnum.PADRAO)
    agrupar_financeiro_contrato: Mapped[Optional[Agrupar_financeiro_contratoEnum]] = Field("agrupar_financeiro_contrato", Agrupar_financeiro_contratoEnum, Agrupar_financeiro_contratoEnum.PADRAO)
    aplicar_desconto_tempo_bloqueio: Mapped[Optional[Aplicar_desconto_tempo_bloqueioEnum]] = Field("aplicar_desconto_tempo_bloqueio", Aplicar_desconto_tempo_bloqueioEnum, Aplicar_desconto_tempo_bloqueioEnum.PADRAO)
    num_parcelas_atraso: Mapped[Optional[str]] = Field("num_parcelas_atraso", str, '')
    contrato_recorrencia: Mapped[Optional[Contrato_recorrenciaEnum]] = Field("contrato_recorrencia", Contrato_recorrenciaEnum, None)
    credit_card_recorrente_bandeira_cartao: Mapped[Optional[str]] = Field("credit_card_recorrente_bandeira_cartao", str, '')
    credit_card_recorrente_token: Mapped[Optional[str]] = Field("credit_card_recorrente_token", str, '')
    ids_contratos_recorrencia: Mapped[Optional[str]] = Field("ids_contratos_recorrencia", str, '')
    status_recorrencia: Mapped[Optional[Status_recorrenciaEnum]] = Field("status_recorrencia", Status_recorrenciaEnum, None)
    base_geracao_tipo_doc: Mapped[Base_geracao_tipo_docEnum] = Field("base_geracao_tipo_doc", Base_geracao_tipo_docEnum, Base_geracao_tipo_docEnum.PADRAO)
    tipo_doc_opc: Mapped[Optional[int]] = Field("tipo_doc_opc", int, None)
    tipo_doc_opc2: Mapped[Optional[int]] = Field("tipo_doc_opc2", int, None)
    tipo_doc_opc3: Mapped[Optional[int]] = Field("tipo_doc_opc3", int, None)
    tipo_doc_opc4: Mapped[Optional[int]] = Field("tipo_doc_opc4", int, None)
    nf_info_adicionais: Mapped[Optional[str]] = Field("nf_info_adicionais", str, '')
    id_tipo_doc_ativ: Mapped[Optional[int]] = Field("id_tipo_doc_ativ", int, None)
    id_produto_ativ: Mapped[Optional[int]] = Field("id_produto_ativ", int, None)
    taxa_instalacao: Mapped[Optional[str]] = Field("taxa_instalacao", str, '')
    id_cond_pag_ativ: Mapped[Optional[int]] = Field("id_cond_pag_ativ", int, None)
    id_responsavel: Mapped[Optional[int]] = Field("id_responsavel", int, None)
    id_vendedor_ativ: Mapped[Optional[int]] = Field("id_vendedor_ativ", int, None)
    ativacao_numero_parcelas: Mapped[Optional[str]] = Field("ativacao_numero_parcelas", str, '')
    ativacao_vencimentos: Mapped[Optional[str]] = Field("ativacao_vencimentos", str, '')
    btn_nf_ativacao: Mapped[Optional[str]] = Field("btn_nf_ativacao", str, '')
    ativacao_valor_parcela: Mapped[Optional[str]] = Field("ativacao_valor_parcela", str, '')
    fidelidade: Mapped[Optional[str]] = Field("fidelidade", str, '')
    data_expiracao: Mapped[Optional[str]] = Field("data_expiracao", str, '')
    dica_data_expiracao: Mapped[Optional[str]] = Field("dica_data_expiracao", str, '')
    desconto_fidelidade: Mapped[Optional[str]] = Field("desconto_fidelidade", str, '')
    id_instalador: Mapped[Optional[int]] = Field("id_instalador", int, None)
    taxa_improdutiva: Mapped[Optional[str]] = Field("taxa_improdutiva", str, '')
    venc_personalizado: Mapped[Optional[str]] = Field("venc_personalizado", str, '')
    com_entrada: Mapped[Optional[str]] = Field("com_entrada", str, '')
    dia_fixo_vencimento: Mapped[Optional[str]] = Field("dia_fixo_vencimento", str, '')
    tipo_condicao_pag: Mapped[Optional[str]] = Field("tipo_condicao_pag", str, '')
    bloqueio_automatico: Mapped[Bloqueio_automaticoEnum] = Field("bloqueio_automatico", Bloqueio_automaticoEnum, Bloqueio_automaticoEnum.SIM)
    nao_bloquear_ate: Mapped[Optional[str]] = Field("nao_bloquear_ate", str, '')
    aviso_atraso: Mapped[Aviso_atrasoEnum] = Field("aviso_atraso", Aviso_atrasoEnum, Aviso_atrasoEnum.SIM)
    nao_avisar_ate: Mapped[Optional[str]] = Field("nao_avisar_ate", str, '')
    desbloqueio_confianca: Mapped[Optional[Desbloqueio_confiancaEnum]] = Field("desbloqueio_confianca", Desbloqueio_confiancaEnum, Desbloqueio_confiancaEnum.PADRAO)
    desbloqueio_confianca_ativo: Mapped[Optional[Desbloqueio_confianca_ativoEnum]] = Field("desbloqueio_confianca_ativo", Desbloqueio_confianca_ativoEnum, Desbloqueio_confianca_ativoEnum.NAO)
    restricao_auto_desbloqueio: Mapped[Optional[Restricao_auto_desbloqueioEnum]] = Field("restricao_auto_desbloqueio", Restricao_auto_desbloqueioEnum, Restricao_auto_desbloqueioEnum.NAO)
    motivo_restricao_auto_desbloq: Mapped[Optional[str]] = Field("motivo_restricao_auto_desbloq", str, '')
    obs: Mapped[Optional[str]] = Field("obs", str, '')
    nao_susp_parc_ate: Mapped[Optional[str]] = Field("nao_susp_parc_ate", str, '')
    liberacao_suspensao_parcial: Mapped[Optional[Liberacao_suspensao_parcialEnum]] = Field("liberacao_suspensao_parcial", Liberacao_suspensao_parcialEnum, Liberacao_suspensao_parcialEnum.PADRAO)
    utilizando_auto_libera_susp_parc: Mapped[Optional[Utilizando_auto_libera_susp_parcEnum]] = Field("utilizando_auto_libera_susp_parc", Utilizando_auto_libera_susp_parcEnum, Utilizando_auto_libera_susp_parcEnum.NAO)
    restricao_auto_libera_susp_parcial: Mapped[Optional[Restricao_auto_libera_susp_parcialEnum]] = Field("restricao_auto_libera_susp_parcial", Restricao_auto_libera_susp_parcialEnum, Restricao_auto_libera_susp_parcialEnum.NAO)
    motivo_restri_auto_libera_parc: Mapped[Optional[str]] = Field("motivo_restri_auto_libera_parc", str, '')
    contrato_suspenso: Mapped[Optional[Contrato_suspensoEnum]] = Field("contrato_suspenso", Contrato_suspensoEnum, Contrato_suspensoEnum.NAO)
    data_inicial_suspensao: Mapped[Optional[str]] = Field("data_inicial_suspensao", str, '')
    data_final_suspensao: Mapped[Optional[str]] = Field("data_final_suspensao", str, '')
    data_acesso_desativado: Mapped[Optional[str]] = Field("data_acesso_desativado", str, '')
    fieldset_mensagem_atencao_irreversivel: Mapped[Optional[str]] = Field("fieldset_mensagem_atencao_irreversivel", str, '')
    data_cancelamento: Mapped[Optional[str]] = Field("data_cancelamento", str, '')
    id_responsavel_cancelamento: Mapped[Optional[int]] = Field("id_responsavel_cancelamento", int, None)
    motivo_cancelamento: Mapped[Optional[int]] = Field("motivo_cancelamento", int, None)
    motivo_adicional: Mapped[Optional[int]] = Field("motivo_adicional", int, None)
    concorrente_mot_adicional: Mapped[Optional[int]] = Field("concorrente_mot_adicional", int, None)
    obs_cancelamento: Mapped[Optional[str]] = Field("obs_cancelamento", str, '')
    tempo_permanencia: Mapped[Optional[str]] = Field("tempo_permanencia", str, '')
    dica_tmp: Mapped[Optional[str]] = Field("dica_tmp", str, '')
    origem_cancelamento: Mapped[Optional[Origem_cancelamentoEnum]] = Field("origem_cancelamento", Origem_cancelamentoEnum, None)
    data_negativacao: Mapped[Optional[str]] = Field("data_negativacao", str, '')
    id_responsavel_negativacao: Mapped[Optional[int]] = Field("id_responsavel_negativacao", int, None)
    protocolo_negativacao: Mapped[Optional[str]] = Field("protocolo_negativacao", str, '')
    id_motivo_negativacao: Mapped[Optional[int]] = Field("id_motivo_negativacao", int, None)
    obs_negativacao: Mapped[Optional[str]] = Field("obs_negativacao", str, '')
    data_desistencia: Mapped[Optional[str]] = Field("data_desistencia", str, '')
    id_responsavel_desistencia: Mapped[Optional[int]] = Field("id_responsavel_desistencia", int, None)
    motivo_desistencia: Mapped[Optional[int]] = Field("motivo_desistencia", int, None)
    obs_desistencia: Mapped[Optional[str]] = Field("obs_desistencia", str, '')
    obs_contrato: Mapped[Optional[str]] = Field("obs_contrato", str, '')
    alerta_contrato: Mapped[Optional[str]] = Field("alerta_contrato", str, '')
    imp_realizado: Mapped[Optional[Imp_realizadoEnum]] = Field("imp_realizado", Imp_realizadoEnum, Imp_realizadoEnum.SIM)
    imp_inicial: Mapped[Optional[str]] = Field("imp_inicial", str, '')
    imp_carteira: Mapped[Optional[Imp_carteiraEnum]] = Field("imp_carteira", Imp_carteiraEnum, Imp_carteiraEnum.EM_ANDAMENTO)
    imp_importacao: Mapped[Optional[Imp_importacaoEnum]] = Field("imp_importacao", Imp_importacaoEnum, Imp_importacaoEnum.EM_ANDAMENTO)
    imp_treinamento: Mapped[Optional[Imp_treinamentoEnum]] = Field("imp_treinamento", Imp_treinamentoEnum, Imp_treinamentoEnum.EM_ANDAMENTO)
    imp_rede: Mapped[Optional[Imp_redeEnum]] = Field("imp_rede", Imp_redeEnum, Imp_redeEnum.EM_ANDAMENTO)
    imp_bkp: Mapped[Optional[Imp_bkpEnum]] = Field("imp_bkp", Imp_bkpEnum, Imp_bkpEnum.EM_ANDAMENTO)
    imp_obs: Mapped[Optional[str]] = Field("imp_obs", str, '')
    imp_final: Mapped[Optional[str]] = Field("imp_final", str, '')
    imp_status: Mapped[Optional[Imp_statusEnum]] = Field("imp_status", Imp_statusEnum, Imp_statusEnum.EM_ANDAMENTO)
    imp_motivo: Mapped[Optional[str]] = Field("imp_motivo", str, '')
    dt_ult_bloq_auto: Mapped[Optional[str]] = Field("dt_ult_bloq_auto", str, '')
    dt_ult_bloq_manual: Mapped[Optional[str]] = Field("dt_ult_bloq_manual", str, '')
    dt_ult_desbloq_auto: Mapped[Optional[str]] = Field("dt_ult_desbloq_auto", str, '')
    dt_ult_desbloq_manual: Mapped[Optional[str]] = Field("dt_ult_desbloq_manual", str, '')
    dt_ult_finan_atraso: Mapped[Optional[str]] = Field("dt_ult_finan_atraso", str, '')
    dt_ult_des_bloq_conf: Mapped[Optional[str]] = Field("dt_ult_des_bloq_conf", str, '')
    dt_ult_liberacao_susp_parc: Mapped[Optional[str]] = Field("dt_ult_liberacao_susp_parc", str, '')
    dt_ult_ativacao: Mapped[Optional[str]] = Field("dt_ult_ativacao", str, '')
    dt_utl_negativacao: Mapped[Optional[str]] = Field("dt_utl_negativacao", str, '')
    dt_ult_desiste: Mapped[Optional[str]] = Field("dt_ult_desiste", str, '')
    data_cadastro_sistema: Mapped[Optional[str]] = Field("data_cadastro_sistema", str, '')
    ultima_atualizacao: Mapped[Optional[str]] = Field("ultima_atualizacao", str, '')
    data_retomada_contrato: Mapped[Optional[str]] = Field("data_retomada_contrato", str, '')
    endereco_padrao_alert: Mapped[Optional[str]] = Field("endereco_padrao_alert", str, '')
    id_condominio: Mapped[Optional[int]] = Field("id_condominio", int, None)
    condominio_novo: Mapped[Optional[int]] = Field("condominio_novo", int, None)
    bloco: Mapped[Optional[str]] = Field("bloco", str, '')
    bloco_novo: Mapped[Optional[str]] = Field("bloco_novo", str, '')
    apartamento: Mapped[Optional[str]] = Field("apartamento", str, '')
    apartamento_novo: Mapped[Optional[str]] = Field("apartamento_novo", str, '')
    cep: Mapped[Optional[str]] = Field("cep", str, '')
    cep_novo: Mapped[Optional[str]] = Field("cep_novo", str, '')
    endereco: Mapped[Optional[str]] = Field("endereco", str, '')
    endereco_novo: Mapped[Optional[str]] = Field("endereco_novo", str, '')
    numero: Mapped[Optional[str]] = Field("numero", str, '')
    numero_novo: Mapped[Optional[str]] = Field("numero_novo", str, '')
    bairro: Mapped[Optional[str]] = Field("bairro", str, '')
    bairro_novo: Mapped[Optional[str]] = Field("bairro_novo", str, '')
    cidade: Mapped[Optional[int]] = Field("cidade", int, None)
    cidade_novo: Mapped[Optional[int]] = Field("cidade_novo", int, None)
    complemento: Mapped[Optional[str]] = Field("complemento", str, '')
    complemento_novo: Mapped[Optional[str]] = Field("complemento_novo", str, '')
    referencia: Mapped[Optional[str]] = Field("referencia", str, '')
    referencia_novo: Mapped[Optional[str]] = Field("referencia_novo", str, '')
    latitude: Mapped[Optional[str]] = Field("latitude", str, '')
    latitude_novo: Mapped[Optional[str]] = Field("latitude_novo", str, '')
    longitude: Mapped[Optional[str]] = Field("longitude", str, '')
    longitude_novo: Mapped[Optional[str]] = Field("longitude_novo", str, '')
    tipo_localidade: Mapped[Optional[Tipo_localidadeEnum]] = Field("tipo_localidade", Tipo_localidadeEnum, Tipo_localidadeEnum.ZONA_URBANA)
    avalista_1: Mapped[Optional[int]] = Field("avalista_1", int, None)
    avalista_2: Mapped[Optional[int]] = Field("avalista_2", int, None)
    testemunha_assinatura_digital: Mapped[Optional[int]] = Field("testemunha_assinatura_digital", int, None)
    email_assinatura_digital: Mapped[Optional[str]] = Field("email_assinatura_digital", str, '')
    contato_assinatura_digital: Mapped[Optional[str]] = Field("contato_assinatura_digital", str, '')
    document_photo: Mapped[Optional[Document_photoEnum]] = Field("document_photo", Document_photoEnum, Document_photoEnum.PADRAO)
    selfie_photo: Mapped[Optional[Selfie_photoEnum]] = Field("selfie_photo", Selfie_photoEnum, Selfie_photoEnum.PADRAO)

    @property
    def table(self) -> str:
        return "cliente_contrato"
    
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
            'tipo': self.tipo.value if self.tipo is not None else '',
            'estrato_social_col': self.estrato_social_col.value if self.estrato_social_col is not None else '',
            'descricao_aux_plano_venda': self.descricao_aux_plano_venda if self.descricao_aux_plano_venda is not None else '',
            'assinatura_digital': self.assinatura_digital.value if self.assinatura_digital is not None else '',
            'integracao_assinatura_digital': self.integracao_assinatura_digital.value if self.integracao_assinatura_digital is not None else '',
            'liberacao_bloqueio_manual': self.liberacao_bloqueio_manual.value if self.liberacao_bloqueio_manual is not None else '',
            'indicacao_contrato_id': str(self.indicacao_contrato_id) if self.indicacao_contrato_id is not None else '',
            'data_assinatura': self.data_assinatura if self.data_assinatura is not None else '',
            'isentar_contrato': self.isentar_contrato.value if self.isentar_contrato is not None else '',
            'data_ativacao': self.data_ativacao if self.data_ativacao is not None else '',
            'situacao_financeira_contrato': self.situacao_financeira_contrato if self.situacao_financeira_contrato is not None else '',
            'data_renovacao': self.data_renovacao if self.data_renovacao is not None else '',
            'pago_ate_data': self.pago_ate_data if self.pago_ate_data is not None else '',
            'status': self.status.value if self.status is not None else '',
            'status_internet': self.status_internet.value if self.status_internet is not None else '',
            'status_velocidade': self.status_velocidade.value if self.status_velocidade is not None else '',
            'tipo_produtos_plano': self.tipo_produtos_plano if self.tipo_produtos_plano is not None else '',
            'motivo_inclusao': self.motivo_inclusao.value if self.motivo_inclusao is not None else '',
            'id_motivo_inclusao': str(self.id_motivo_inclusao) if self.id_motivo_inclusao is not None else '',
            'id_indexador_reajuste': str(self.id_indexador_reajuste) if self.id_indexador_reajuste is not None else '',
            'url_assinatura_digital': self.url_assinatura_digital if self.url_assinatura_digital is not None else '',
            'token_assinatura_digital': self.token_assinatura_digital if self.token_assinatura_digital is not None else '',
            'moeda': str(self.moeda) if self.moeda is not None else '',
            'comissao': self.comissao if self.comissao is not None else '',
            'cc_previsao': self.cc_previsao.value if self.cc_previsao is not None else '',
            'tipo_cobranca': self.tipo_cobranca.value if self.tipo_cobranca is not None else '',
            'id_contrato_principal': str(self.id_contrato_principal) if self.id_contrato_principal is not None else '',
            'renovacao_automatica': self.renovacao_automatica.value if self.renovacao_automatica is not None else '',
            'gerar_finan_assin_digital_contrato': self.gerar_finan_assin_digital_contrato.value if self.gerar_finan_assin_digital_contrato is not None else '',
            'agrupar_financeiro_contrato': self.agrupar_financeiro_contrato.value if self.agrupar_financeiro_contrato is not None else '',
            'aplicar_desconto_tempo_bloqueio': self.aplicar_desconto_tempo_bloqueio.value if self.aplicar_desconto_tempo_bloqueio is not None else '',
            'num_parcelas_atraso': self.num_parcelas_atraso if self.num_parcelas_atraso is not None else '',
            'contrato_recorrencia': self.contrato_recorrencia.value if self.contrato_recorrencia is not None else '',
            'credit_card_recorrente_bandeira_cartao': self.credit_card_recorrente_bandeira_cartao if self.credit_card_recorrente_bandeira_cartao is not None else '',
            'credit_card_recorrente_token': self.credit_card_recorrente_token if self.credit_card_recorrente_token is not None else '',
            'ids_contratos_recorrencia': self.ids_contratos_recorrencia if self.ids_contratos_recorrencia is not None else '',
            'status_recorrencia': self.status_recorrencia.value if self.status_recorrencia is not None else '',
            'base_geracao_tipo_doc': self.base_geracao_tipo_doc.value if self.base_geracao_tipo_doc is not None else '',
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
            'bloqueio_automatico': self.bloqueio_automatico.value if self.bloqueio_automatico is not None else '',
            'nao_bloquear_ate': self.nao_bloquear_ate if self.nao_bloquear_ate is not None else '',
            'aviso_atraso': self.aviso_atraso.value if self.aviso_atraso is not None else '',
            'nao_avisar_ate': self.nao_avisar_ate if self.nao_avisar_ate is not None else '',
            'desbloqueio_confianca': self.desbloqueio_confianca.value if self.desbloqueio_confianca is not None else '',
            'desbloqueio_confianca_ativo': self.desbloqueio_confianca_ativo.value if self.desbloqueio_confianca_ativo is not None else '',
            'restricao_auto_desbloqueio': self.restricao_auto_desbloqueio.value if self.restricao_auto_desbloqueio is not None else '',
            'motivo_restricao_auto_desbloq': self.motivo_restricao_auto_desbloq if self.motivo_restricao_auto_desbloq is not None else '',
            'obs': self.obs if self.obs is not None else '',
            'nao_susp_parc_ate': self.nao_susp_parc_ate if self.nao_susp_parc_ate is not None else '',
            'liberacao_suspensao_parcial': self.liberacao_suspensao_parcial.value if self.liberacao_suspensao_parcial is not None else '',
            'utilizando_auto_libera_susp_parc': self.utilizando_auto_libera_susp_parc.value if self.utilizando_auto_libera_susp_parc is not None else '',
            'restricao_auto_libera_susp_parcial': self.restricao_auto_libera_susp_parcial.value if self.restricao_auto_libera_susp_parcial is not None else '',
            'motivo_restri_auto_libera_parc': self.motivo_restri_auto_libera_parc if self.motivo_restri_auto_libera_parc is not None else '',
            'contrato_suspenso': self.contrato_suspenso.value if self.contrato_suspenso is not None else '',
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
            'origem_cancelamento': self.origem_cancelamento.value if self.origem_cancelamento is not None else '',
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
            'imp_realizado': self.imp_realizado.value if self.imp_realizado is not None else '',
            'imp_inicial': self.imp_inicial if self.imp_inicial is not None else '',
            'imp_carteira': self.imp_carteira.value if self.imp_carteira is not None else '',
            'imp_importacao': self.imp_importacao.value if self.imp_importacao is not None else '',
            'imp_treinamento': self.imp_treinamento.value if self.imp_treinamento is not None else '',
            'imp_rede': self.imp_rede.value if self.imp_rede is not None else '',
            'imp_bkp': self.imp_bkp.value if self.imp_bkp is not None else '',
            'imp_obs': self.imp_obs if self.imp_obs is not None else '',
            'imp_final': self.imp_final if self.imp_final is not None else '',
            'imp_status': self.imp_status.value if self.imp_status is not None else '',
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
            'tipo_localidade': self.tipo_localidade.value if self.tipo_localidade is not None else '',
            'avalista_1': str(self.avalista_1) if self.avalista_1 is not None else '',
            'avalista_2': str(self.avalista_2) if self.avalista_2 is not None else '',
            'testemunha_assinatura_digital': str(self.testemunha_assinatura_digital) if self.testemunha_assinatura_digital is not None else '',
            'email_assinatura_digital': self.email_assinatura_digital if self.email_assinatura_digital is not None else '',
            'contato_assinatura_digital': self.contato_assinatura_digital if self.contato_assinatura_digital is not None else '',
            'document_photo': self.document_photo.value if self.document_photo is not None else '',
            'selfie_photo': self.selfie_photo.value if self.selfie_photo is not None else '',
        }
        return {key: serialize(value) for key, value in data.items()}


    def is_valid(self) -> bool:
        return self.id_autoincrement is not None and self.id_cliente is not None and self.id_vd_contrato is not None and self.contrato is not None and self.id_tipo_contrato is not None and self.id_modelo is not None and self.id_filial is not None and self.data is not None and self.id_tipo_documento is not None and self.id_carteira_cobranca is not None and self.id_vendedor is not None and self.endereco_padrao_cliente is not None
