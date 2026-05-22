from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from ORM_IXC.interfaces import IModel, IModelWithId
from ORM_IXC.enums.contratoDoCliente import * 

@dataclass(kw_only=True)
class ContratoDoClienteModel(IModelWithId):
    id_autoincrement: int
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
    tipo: TipoEnum = TipoEnum.INTERNET
    estrato_social_col: Optional[Estrato_social_colEnum] = None
    descricao_aux_plano_venda: Optional[str] = ''
    assinatura_digital: Optional[Assinatura_digitalEnum] = Assinatura_digitalEnum.PADRAO
    integracao_assinatura_digital: Optional[Integracao_assinatura_digitalEnum] = Integracao_assinatura_digitalEnum.PADRAO
    liberacao_bloqueio_manual: Optional[Liberacao_bloqueio_manualEnum] = Liberacao_bloqueio_manualEnum.PADRAO
    indicacao_contrato_id: Optional[int] = None
    data_assinatura: Optional[str] = ''
    isentar_contrato: Optional[Isentar_contratoEnum] = Isentar_contratoEnum.NAO
    data_ativacao: Optional[str] = ''
    situacao_financeira_contrato: Optional[str] = ''
    data_renovacao: Optional[str] = ''
    pago_ate_data: Optional[str] = ''
    status: Optional[StatusEnum] = StatusEnum.PRE_CONTRATO
    status_internet: Optional[Status_internetEnum] = Status_internetEnum.DESATIVADO
    status_velocidade: Optional[Status_velocidadeEnum] = Status_velocidadeEnum.NORMAL
    tipo_produtos_plano: Optional[str] = ''
    motivo_inclusao: Optional[Motivo_inclusaoEnum] = Motivo_inclusaoEnum.INSTALACAO
    id_motivo_inclusao: Optional[int] = None
    id_indexador_reajuste: Optional[int] = None
    url_assinatura_digital: Optional[str] = ''
    token_assinatura_digital: Optional[str] = ''
    moeda: Optional[int] = None
    comissao: Optional[str] = ''
    cc_previsao: Cc_previsaoEnum = Cc_previsaoEnum.CONFIGURACAO_PADRAO_
    tipo_cobranca: Tipo_cobrancaEnum = Tipo_cobrancaEnum.CONFIGURACAO_PADRAO
    id_contrato_principal: Optional[int] = None
    renovacao_automatica: Renovacao_automaticaEnum = Renovacao_automaticaEnum.SIM
    gerar_finan_assin_digital_contrato: Optional[Gerar_finan_assin_digital_contratoEnum] = Gerar_finan_assin_digital_contratoEnum.PADRAO
    agrupar_financeiro_contrato: Optional[Agrupar_financeiro_contratoEnum] = Agrupar_financeiro_contratoEnum.PADRAO
    aplicar_desconto_tempo_bloqueio: Optional[Aplicar_desconto_tempo_bloqueioEnum] = Aplicar_desconto_tempo_bloqueioEnum.PADRAO
    num_parcelas_atraso: Optional[str] = ''
    contrato_recorrencia: Optional[Contrato_recorrenciaEnum] = None
    credit_card_recorrente_bandeira_cartao: Optional[str] = ''
    credit_card_recorrente_token: Optional[str] = ''
    ids_contratos_recorrencia: Optional[str] = ''
    status_recorrencia: Optional[Status_recorrenciaEnum] = None
    base_geracao_tipo_doc: Base_geracao_tipo_docEnum = Base_geracao_tipo_docEnum.PADRAO
    tipo_doc_opc: Optional[int] = None
    tipo_doc_opc2: Optional[int] = None
    tipo_doc_opc3: Optional[int] = None
    tipo_doc_opc4: Optional[int] = None
    nf_info_adicionais: Optional[str] = ''
    id_tipo_doc_ativ: Optional[int] = None
    id_produto_ativ: Optional[int] = None
    taxa_instalacao: Optional[str] = ''
    id_cond_pag_ativ: Optional[int] = None
    id_responsavel: Optional[int] = None
    id_vendedor_ativ: Optional[int] = None
    ativacao_numero_parcelas: Optional[str] = ''
    ativacao_vencimentos: Optional[str] = ''
    btn_nf_ativacao: Optional[str] = ''
    ativacao_valor_parcela: Optional[str] = ''
    fidelidade: Optional[str] = ''
    data_expiracao: Optional[str] = ''
    dica_data_expiracao: Optional[str] = ''
    desconto_fidelidade: Optional[str] = ''
    id_instalador: Optional[int] = None
    taxa_improdutiva: Optional[str] = ''
    venc_personalizado: Optional[str] = ''
    com_entrada: Optional[str] = ''
    dia_fixo_vencimento: Optional[str] = ''
    tipo_condicao_pag: Optional[str] = ''
    bloqueio_automatico: Bloqueio_automaticoEnum = Bloqueio_automaticoEnum.SIM
    nao_bloquear_ate: Optional[str] = ''
    aviso_atraso: Aviso_atrasoEnum = Aviso_atrasoEnum.SIM
    nao_avisar_ate: Optional[str] = ''
    desbloqueio_confianca: Optional[Desbloqueio_confiancaEnum] = Desbloqueio_confiancaEnum.PADRAO
    desbloqueio_confianca_ativo: Optional[Desbloqueio_confianca_ativoEnum] = Desbloqueio_confianca_ativoEnum.NAO
    restricao_auto_desbloqueio: Optional[Restricao_auto_desbloqueioEnum] = Restricao_auto_desbloqueioEnum.NAO
    motivo_restricao_auto_desbloq: Optional[str] = ''
    obs: Optional[str] = ''
    nao_susp_parc_ate: Optional[str] = ''
    liberacao_suspensao_parcial: Optional[Liberacao_suspensao_parcialEnum] = Liberacao_suspensao_parcialEnum.PADRAO
    utilizando_auto_libera_susp_parc: Optional[Utilizando_auto_libera_susp_parcEnum] = Utilizando_auto_libera_susp_parcEnum.NAO
    restricao_auto_libera_susp_parcial: Optional[Restricao_auto_libera_susp_parcialEnum] = Restricao_auto_libera_susp_parcialEnum.NAO
    motivo_restri_auto_libera_parc: Optional[str] = ''
    contrato_suspenso: Optional[Contrato_suspensoEnum] = Contrato_suspensoEnum.NAO
    data_inicial_suspensao: Optional[str] = ''
    data_final_suspensao: Optional[str] = ''
    data_acesso_desativado: Optional[str] = ''
    fieldset_mensagem_atencao_irreversivel: Optional[str] = ''
    data_cancelamento: Optional[str] = ''
    id_responsavel_cancelamento: Optional[int] = None
    motivo_cancelamento: Optional[int] = None
    motivo_adicional: Optional[int] = None
    concorrente_mot_adicional: Optional[int] = None
    obs_cancelamento: Optional[str] = ''
    tempo_permanencia: Optional[str] = ''
    dica_tmp: Optional[str] = ''
    origem_cancelamento: Optional[Origem_cancelamentoEnum] = None
    data_negativacao: Optional[str] = ''
    id_responsavel_negativacao: Optional[int] = None
    protocolo_negativacao: Optional[str] = ''
    id_motivo_negativacao: Optional[int] = None
    obs_negativacao: Optional[str] = ''
    data_desistencia: Optional[str] = ''
    id_responsavel_desistencia: Optional[int] = None
    motivo_desistencia: Optional[int] = None
    obs_desistencia: Optional[str] = ''
    obs_contrato: Optional[str] = ''
    alerta_contrato: Optional[str] = ''
    imp_realizado: Optional[Imp_realizadoEnum] = Imp_realizadoEnum.SIM
    imp_inicial: Optional[str] = ''
    imp_carteira: Optional[Imp_carteiraEnum] = Imp_carteiraEnum.EM_ANDAMENTO
    imp_importacao: Optional[Imp_importacaoEnum] = Imp_importacaoEnum.EM_ANDAMENTO
    imp_treinamento: Optional[Imp_treinamentoEnum] = Imp_treinamentoEnum.EM_ANDAMENTO
    imp_rede: Optional[Imp_redeEnum] = Imp_redeEnum.EM_ANDAMENTO
    imp_bkp: Optional[Imp_bkpEnum] = Imp_bkpEnum.EM_ANDAMENTO
    imp_obs: Optional[str] = ''
    imp_final: Optional[str] = ''
    imp_status: Optional[Imp_statusEnum] = Imp_statusEnum.EM_ANDAMENTO
    imp_motivo: Optional[str] = ''
    dt_ult_bloq_auto: Optional[str] = ''
    dt_ult_bloq_manual: Optional[str] = ''
    dt_ult_desbloq_auto: Optional[str] = ''
    dt_ult_desbloq_manual: Optional[str] = ''
    dt_ult_finan_atraso: Optional[str] = ''
    dt_ult_des_bloq_conf: Optional[str] = ''
    dt_ult_liberacao_susp_parc: Optional[str] = ''
    dt_ult_ativacao: Optional[str] = ''
    dt_utl_negativacao: Optional[str] = ''
    dt_ult_desiste: Optional[str] = ''
    data_cadastro_sistema: Optional[str] = ''
    ultima_atualizacao: Optional[str] = ''
    data_retomada_contrato: Optional[str] = ''
    endereco_padrao_alert: Optional[str] = ''
    id_condominio: Optional[int] = None
    condominio_novo: Optional[int] = None
    bloco: Optional[str] = ''
    bloco_novo: Optional[str] = ''
    apartamento: Optional[str] = ''
    apartamento_novo: Optional[str] = ''
    cep: Optional[str] = ''
    cep_novo: Optional[str] = ''
    endereco: Optional[str] = ''
    endereco_novo: Optional[str] = ''
    numero: Optional[str] = ''
    numero_novo: Optional[str] = ''
    bairro: Optional[str] = ''
    bairro_novo: Optional[str] = ''
    cidade: Optional[int] = None
    cidade_novo: Optional[int] = None
    complemento: Optional[str] = ''
    complemento_novo: Optional[str] = ''
    referencia: Optional[str] = ''
    referencia_novo: Optional[str] = ''
    latitude: Optional[str] = ''
    latitude_novo: Optional[str] = ''
    longitude: Optional[str] = ''
    longitude_novo: Optional[str] = ''
    tipo_localidade: Optional[Tipo_localidadeEnum] = Tipo_localidadeEnum.ZONA_URBANA
    avalista_1: Optional[int] = None
    avalista_2: Optional[int] = None
    testemunha_assinatura_digital: Optional[int] = None
    email_assinatura_digital: Optional[str] = ''
    contato_assinatura_digital: Optional[str] = ''
    document_photo: Optional[Document_photoEnum] = Document_photoEnum.PADRAO
    selfie_photo: Optional[Selfie_photoEnum] = Selfie_photoEnum.PADRAO
    
    @property
    def id(self) -> str:
        return str(self.id_autoincrement)

    @property
    def table(self) -> str:
        return "cliente_contrato"
    
    def to_dict(self) -> dict:
        return {
            'id_autoincrement': str(self.id_autoincrement),
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

    def is_valid(self) -> bool:
        return self.id_autoincrement is not None and self.id_cliente is not None and self.id_vd_contrato is not None and self.contrato is not None and self.id_tipo_contrato is not None and self.id_modelo is not None and self.id_filial is not None and self.data is not None and self.id_tipo_documento is not None and self.id_carteira_cobranca is not None and self.id_vendedor is not None and self.endereco_padrao_cliente is not None

    def __repr__(self) -> str:
        return f"ContratoDoCliente(id_autoincrement={self.id_autoincrement!r}, id_cliente={self.id_cliente!r}, id_vd_contrato={self.id_vd_contrato!r}, contrato={self.contrato!r}, id_tipo_contrato={self.id_tipo_contrato!r}, id_modelo={self.id_modelo!r}, id_filial={self.id_filial!r}, data={self.data!r}, id_tipo_documento={self.id_tipo_documento!r}, id_carteira_cobranca={self.id_carteira_cobranca!r}, id_vendedor={self.id_vendedor!r}, endereco_padrao_cliente={self.endereco_padrao_cliente!r})"

    #------------------------------ CONVERSOR DTO ------------------------------#
    def dto_convert(self, data: dict[str, str]) -> IModel:
        return ContratoDoClienteModel(
            id_autoincrement=int(data.get('id_autoincrement', 0)),
            id_cliente=int(data['id_cliente']),
            id_vd_contrato=int(data['id_vd_contrato']),
            contrato=data.get('contrato', ''),
            id_tipo_contrato=int(data['id_tipo_contrato']),
            id_modelo=int(data['id_modelo']),
            id_filial=int(data['id_filial']),
            data=data.get('data', ''),
            id_tipo_documento=int(data['id_tipo_documento']),
            id_carteira_cobranca=int(data['id_carteira_cobranca']),
            id_vendedor=int(data['id_vendedor']),
            endereco_padrao_cliente=data.get('endereco_padrao_cliente', ''),
            tipo=TipoEnum(data['tipo']),
            estrato_social_col=Estrato_social_colEnum(data['estrato_social_col']) if data.get('estrato_social_col') else None,
            descricao_aux_plano_venda=data.get('descricao_aux_plano_venda', ''),
            assinatura_digital=Assinatura_digitalEnum(data['assinatura_digital']) if data.get('assinatura_digital') else None,
            integracao_assinatura_digital=Integracao_assinatura_digitalEnum(data['integracao_assinatura_digital']) if data.get('integracao_assinatura_digital') else None,
            liberacao_bloqueio_manual=Liberacao_bloqueio_manualEnum(data['liberacao_bloqueio_manual']) if data.get('liberacao_bloqueio_manual') else None,
            indicacao_contrato_id=int(data['indicacao_contrato_id']) if data.get('indicacao_contrato_id') else None,
            data_assinatura=data.get('data_assinatura', ''),
            isentar_contrato=Isentar_contratoEnum(data['isentar_contrato']) if data.get('isentar_contrato') else None,
            data_ativacao=data.get('data_ativacao', ''),
            situacao_financeira_contrato=data.get('situacao_financeira_contrato', ''),
            data_renovacao=data.get('data_renovacao', ''),
            pago_ate_data=data.get('pago_ate_data', ''),
            status=StatusEnum(data['status']) if data.get('status') else None,
            status_internet=Status_internetEnum(data['status_internet']) if data.get('status_internet') else None,
            status_velocidade=Status_velocidadeEnum(data['status_velocidade']) if data.get('status_velocidade') else None,
            tipo_produtos_plano=data.get('tipo_produtos_plano', ''),
            motivo_inclusao=Motivo_inclusaoEnum(data['motivo_inclusao']) if data.get('motivo_inclusao') else None,
            id_motivo_inclusao=int(data['id_motivo_inclusao']) if data.get('id_motivo_inclusao') else None,
            id_indexador_reajuste=int(data['id_indexador_reajuste']) if data.get('id_indexador_reajuste') else None,
            url_assinatura_digital=data.get('url_assinatura_digital', ''),
            token_assinatura_digital=data.get('token_assinatura_digital', ''),
            moeda=int(data['moeda']) if data.get('moeda') else None,
            comissao=data.get('comissao', ''),
            cc_previsao=Cc_previsaoEnum(data['cc_previsao']),
            tipo_cobranca=Tipo_cobrancaEnum(data['tipo_cobranca']),
            id_contrato_principal=int(data['id_contrato_principal']) if data.get('id_contrato_principal') else None,
            renovacao_automatica=Renovacao_automaticaEnum(data['renovacao_automatica']),
            gerar_finan_assin_digital_contrato=Gerar_finan_assin_digital_contratoEnum(data['gerar_finan_assin_digital_contrato']) if data.get('gerar_finan_assin_digital_contrato') else None,
            agrupar_financeiro_contrato=Agrupar_financeiro_contratoEnum(data['agrupar_financeiro_contrato']) if data.get('agrupar_financeiro_contrato') else None,
            aplicar_desconto_tempo_bloqueio=Aplicar_desconto_tempo_bloqueioEnum(data['aplicar_desconto_tempo_bloqueio']) if data.get('aplicar_desconto_tempo_bloqueio') else None,
            num_parcelas_atraso=data.get('num_parcelas_atraso', ''),
            contrato_recorrencia=Contrato_recorrenciaEnum(data['contrato_recorrencia']) if data.get('contrato_recorrencia') else None,
            credit_card_recorrente_bandeira_cartao=data.get('credit_card_recorrente_bandeira_cartao', ''),
            credit_card_recorrente_token=data.get('credit_card_recorrente_token', ''),
            ids_contratos_recorrencia=data.get('ids_contratos_recorrencia', ''),
            status_recorrencia=Status_recorrenciaEnum(data['status_recorrencia']) if data.get('status_recorrencia') else None,
            base_geracao_tipo_doc=Base_geracao_tipo_docEnum(data['base_geracao_tipo_doc']),
            tipo_doc_opc=int(data['tipo_doc_opc']) if data.get('tipo_doc_opc') else None,
            tipo_doc_opc2=int(data['tipo_doc_opc2']) if data.get('tipo_doc_opc2') else None,
            tipo_doc_opc3=int(data['tipo_doc_opc3']) if data.get('tipo_doc_opc3') else None,
            tipo_doc_opc4=int(data['tipo_doc_opc4']) if data.get('tipo_doc_opc4') else None,
            nf_info_adicionais=data.get('nf_info_adicionais', ''),
            id_tipo_doc_ativ=int(data['id_tipo_doc_ativ']) if data.get('id_tipo_doc_ativ') else None,
            id_produto_ativ=int(data['id_produto_ativ']) if data.get('id_produto_ativ') else None,
            taxa_instalacao=data.get('taxa_instalacao', ''),
            id_cond_pag_ativ=int(data['id_cond_pag_ativ']) if data.get('id_cond_pag_ativ') else None,
            id_responsavel=int(data['id_responsavel']) if data.get('id_responsavel') else None,
            id_vendedor_ativ=int(data['id_vendedor_ativ']) if data.get('id_vendedor_ativ') else None,
            ativacao_numero_parcelas=data.get('ativacao_numero_parcelas', ''),
            ativacao_vencimentos=data.get('ativacao_vencimentos', ''),
            btn_nf_ativacao=data.get('btn_nf_ativacao', ''),
            ativacao_valor_parcela=data.get('ativacao_valor_parcela', ''),
            fidelidade=data.get('fidelidade', ''),
            data_expiracao=data.get('data_expiracao', ''),
            dica_data_expiracao=data.get('dica_data_expiracao', ''),
            desconto_fidelidade=data.get('desconto_fidelidade', ''),
            id_instalador=int(data['id_instalador']) if data.get('id_instalador') else None,
            taxa_improdutiva=data.get('taxa_improdutiva', ''),
            venc_personalizado=data.get('venc_personalizado', ''),
            com_entrada=data.get('com_entrada', ''),
            dia_fixo_vencimento=data.get('dia_fixo_vencimento', ''),
            tipo_condicao_pag=data.get('tipo_condicao_pag', ''),
            bloqueio_automatico=Bloqueio_automaticoEnum(data['bloqueio_automatico']),
            nao_bloquear_ate=data.get('nao_bloquear_ate', ''),
            aviso_atraso=Aviso_atrasoEnum(data['aviso_atraso']),
            nao_avisar_ate=data.get('nao_avisar_ate', ''),
            desbloqueio_confianca=Desbloqueio_confiancaEnum(data['desbloqueio_confianca']) if data.get('desbloqueio_confianca') else None,
            desbloqueio_confianca_ativo=Desbloqueio_confianca_ativoEnum(data['desbloqueio_confianca_ativo']) if data.get('desbloqueio_confianca_ativo') else None,
            restricao_auto_desbloqueio=Restricao_auto_desbloqueioEnum(data['restricao_auto_desbloqueio']) if data.get('restricao_auto_desbloqueio') else None,
            motivo_restricao_auto_desbloq=data.get('motivo_restricao_auto_desbloq', ''),
            obs=data.get('obs', ''),
            nao_susp_parc_ate=data.get('nao_susp_parc_ate', ''),
            liberacao_suspensao_parcial=Liberacao_suspensao_parcialEnum(data['liberacao_suspensao_parcial']) if data.get('liberacao_suspensao_parcial') else None,
            utilizando_auto_libera_susp_parc=Utilizando_auto_libera_susp_parcEnum(data['utilizando_auto_libera_susp_parc']) if data.get('utilizando_auto_libera_susp_parc') else None,
            restricao_auto_libera_susp_parcial=Restricao_auto_libera_susp_parcialEnum(data['restricao_auto_libera_susp_parcial']) if data.get('restricao_auto_libera_susp_parcial') else None,
            motivo_restri_auto_libera_parc=data.get('motivo_restri_auto_libera_parc', ''),
            contrato_suspenso=Contrato_suspensoEnum(data['contrato_suspenso']) if data.get('contrato_suspenso') else None,
            data_inicial_suspensao=data.get('data_inicial_suspensao', ''),
            data_final_suspensao=data.get('data_final_suspensao', ''),
            data_acesso_desativado=data.get('data_acesso_desativado', ''),
            fieldset_mensagem_atencao_irreversivel=data.get('fieldset_mensagem_atencao_irreversivel', ''),
            data_cancelamento=data.get('data_cancelamento', ''),
            id_responsavel_cancelamento=int(data['id_responsavel_cancelamento']) if data.get('id_responsavel_cancelamento') else None,
            motivo_cancelamento=int(data['motivo_cancelamento']) if data.get('motivo_cancelamento') else None,
            motivo_adicional=int(data['motivo_adicional']) if data.get('motivo_adicional') else None,
            concorrente_mot_adicional=int(data['concorrente_mot_adicional']) if data.get('concorrente_mot_adicional') else None,
            obs_cancelamento=data.get('obs_cancelamento', ''),
            tempo_permanencia=data.get('tempo_permanencia', ''),
            dica_tmp=data.get('dica_tmp', ''),
            origem_cancelamento=Origem_cancelamentoEnum(data['origem_cancelamento']) if data.get('origem_cancelamento') else None,
            data_negativacao=data.get('data_negativacao', ''),
            id_responsavel_negativacao=int(data['id_responsavel_negativacao']) if data.get('id_responsavel_negativacao') else None,
            protocolo_negativacao=data.get('protocolo_negativacao', ''),
            id_motivo_negativacao=int(data['id_motivo_negativacao']) if data.get('id_motivo_negativacao') else None,
            obs_negativacao=data.get('obs_negativacao', ''),
            data_desistencia=data.get('data_desistencia', ''),
            id_responsavel_desistencia=int(data['id_responsavel_desistencia']) if data.get('id_responsavel_desistencia') else None,
            motivo_desistencia=int(data['motivo_desistencia']) if data.get('motivo_desistencia') else None,
            obs_desistencia=data.get('obs_desistencia', ''),
            obs_contrato=data.get('obs_contrato', ''),
            alerta_contrato=data.get('alerta_contrato', ''),
            imp_realizado=Imp_realizadoEnum(data['imp_realizado']) if data.get('imp_realizado') else None,
            imp_inicial=data.get('imp_inicial', ''),
            imp_carteira=Imp_carteiraEnum(data['imp_carteira']) if data.get('imp_carteira') else None,
            imp_importacao=Imp_importacaoEnum(data['imp_importacao']) if data.get('imp_importacao') else None,
            imp_treinamento=Imp_treinamentoEnum(data['imp_treinamento']) if data.get('imp_treinamento') else None,
            imp_rede=Imp_redeEnum(data['imp_rede']) if data.get('imp_rede') else None,
            imp_bkp=Imp_bkpEnum(data['imp_bkp']) if data.get('imp_bkp') else None,
            imp_obs=data.get('imp_obs', ''),
            imp_final=data.get('imp_final', ''),
            imp_status=Imp_statusEnum(data['imp_status']) if data.get('imp_status') else None,
            imp_motivo=data.get('imp_motivo', ''),
            dt_ult_bloq_auto=data.get('dt_ult_bloq_auto', ''),
            dt_ult_bloq_manual=data.get('dt_ult_bloq_manual', ''),
            dt_ult_desbloq_auto=data.get('dt_ult_desbloq_auto', ''),
            dt_ult_desbloq_manual=data.get('dt_ult_desbloq_manual', ''),
            dt_ult_finan_atraso=data.get('dt_ult_finan_atraso', ''),
            dt_ult_des_bloq_conf=data.get('dt_ult_des_bloq_conf', ''),
            dt_ult_liberacao_susp_parc=data.get('dt_ult_liberacao_susp_parc', ''),
            dt_ult_ativacao=data.get('dt_ult_ativacao', ''),
            dt_utl_negativacao=data.get('dt_utl_negativacao', ''),
            dt_ult_desiste=data.get('dt_ult_desiste', ''),
            data_cadastro_sistema=data.get('data_cadastro_sistema', ''),
            ultima_atualizacao=data.get('ultima_atualizacao', ''),
            data_retomada_contrato=data.get('data_retomada_contrato', ''),
            endereco_padrao_alert=data.get('endereco_padrao_alert', ''),
            id_condominio=int(data['id_condominio']) if data.get('id_condominio') else None,
            condominio_novo=int(data['condominio_novo']) if data.get('condominio_novo') else None,
            bloco=data.get('bloco', ''),
            bloco_novo=data.get('bloco_novo', ''),
            apartamento=data.get('apartamento', ''),
            apartamento_novo=data.get('apartamento_novo', ''),
            cep=data.get('cep', ''),
            cep_novo=data.get('cep_novo', ''),
            endereco=data.get('endereco', ''),
            endereco_novo=data.get('endereco_novo', ''),
            numero=data.get('numero', ''),
            numero_novo=data.get('numero_novo', ''),
            bairro=data.get('bairro', ''),
            bairro_novo=data.get('bairro_novo', ''),
            cidade=int(data['cidade']) if data.get('cidade') else None,
            cidade_novo=int(data['cidade_novo']) if data.get('cidade_novo') else None,
            complemento=data.get('complemento', ''),
            complemento_novo=data.get('complemento_novo', ''),
            referencia=data.get('referencia', ''),
            referencia_novo=data.get('referencia_novo', ''),
            latitude=data.get('latitude', ''),
            latitude_novo=data.get('latitude_novo', ''),
            longitude=data.get('longitude', ''),
            longitude_novo=data.get('longitude_novo', ''),
            tipo_localidade=Tipo_localidadeEnum(data['tipo_localidade']) if data.get('tipo_localidade') else None,
            avalista_1=int(data['avalista_1']) if data.get('avalista_1') else None,
            avalista_2=int(data['avalista_2']) if data.get('avalista_2') else None,
            testemunha_assinatura_digital=int(data['testemunha_assinatura_digital']) if data.get('testemunha_assinatura_digital') else None,
            email_assinatura_digital=data.get('email_assinatura_digital', ''),
            contato_assinatura_digital=data.get('contato_assinatura_digital', ''),
            document_photo=Document_photoEnum(data['document_photo']) if data.get('document_photo') else None,
            selfie_photo=Selfie_photoEnum(data['selfie_photo']) if data.get('selfie_photo') else None,
        )
