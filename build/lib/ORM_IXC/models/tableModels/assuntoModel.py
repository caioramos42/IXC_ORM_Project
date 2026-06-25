from __future__ import annotations
from typing import Optional
from ORM_IXC.interfaces import IModelWithId
from ORM_IXC.enums.assunto import *
from ORM_IXC.statemants.maps.mapper import Mapped, field as mapped_field
from ORM_IXC.statemants.maps.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel


@MetaModels
class AssuntoModel(IModelWithId, BaseModel):
    ativo :Mapped[AtivoEnum]
    assunto :Mapped[str]
    tipo_comissao :Mapped[Tipo_comissaoEnum]
    considerar_sla :Mapped[Considerar_slaEnum]
    metas_horas_abertura_ticket :Mapped[str]
    id :Mapped[Optional[int]]
    tipo :Mapped[Optional[TipoEnum]] = mapped_field(None)
    finalidade :Mapped[Optional[FinalidadeEnum]] = mapped_field(None)
    endereco_padrao :Mapped[Optional[Endereco_padraoEnum]] = mapped_field(None)
    mostra_hotsite :Mapped[Optional[Mostra_hotsiteEnum]] = mapped_field(None)
    cor_marcador :Mapped[Optional[str]] = mapped_field('')
    dicacampocoragenda :Mapped[Optional[str]] = mapped_field('')
    prioridade_padrao :Mapped[Optional[Prioridade_padraoEnum]] = mapped_field(None)
    contrato_obrigatorio :Mapped[Optional[Contrato_obrigatorioEnum]] = mapped_field(None)
    login_obrigatorio :Mapped[Optional[Login_obrigatorioEnum]] = mapped_field(None)
    dicaloginobrigatorio :Mapped[Optional[str]] = mapped_field('')
    card_data_reservada :Mapped[Optional[Card_data_reservadaEnum]] = mapped_field(None)
    obrigar_processo_atendimento :Mapped[Optional[Obrigar_processo_atendimentoEnum]] = mapped_field(None)
    obrigar_preenchimento_canal_atendimento :Mapped[Optional[Obrigar_preenchimento_canal_atendimentoEnum]] = mapped_field(None)
    obrigatorio_status_complementar :Mapped[Optional[Obrigatorio_status_complementarEnum]] = mapped_field(None)
    id_resposta_padrao :Mapped[Optional[int]] = mapped_field(None)
    id_processo :Mapped[Optional[int]] = mapped_field(None)
    ultima_atualizacao :Mapped[Optional[str]] = mapped_field('')
    layout_impressao :Mapped[Optional[Layout_impressaoEnum]] = mapped_field(None)
    imprimir_prod_serv :Mapped[Optional[str]] = mapped_field('')
    numero_de_vias :Mapped[Optional[str]] = mapped_field('')
    su_oss_modelo_impressao :Mapped[Optional[int]] = mapped_field(None)
    modelo_email :Mapped[Optional[int]] = mapped_field(None)
    habilita_assinatura_cliente :Mapped[Optional[Habilita_assinatura_clienteEnum]] = mapped_field(None)
    fieldset_habilita_assinatura_cliente :Mapped[Optional[str]] = mapped_field('')
    integracao_assinatura_digital :Mapped[Optional[Integracao_assinatura_digitalEnum]] = mapped_field(None)
    dica_assinatura_digital :Mapped[Optional[str]] = mapped_field('')
    permite_abrir_cliente_atraso :Mapped[Optional[Permite_abrir_cliente_atrasoEnum]] = mapped_field(None)
    validar_choque_horarios_agendamento_os :Mapped[Optional[Validar_choque_horarios_agendamento_osEnum]] = mapped_field(None)
    setor_su_oss_chamado :Mapped[Optional[int]] = mapped_field(None)
    descricao :Mapped[Optional[str]] = mapped_field('')
    exige_fotos_finalizacao_os :Mapped[Optional[Exige_fotos_finalizacao_osEnum]] = mapped_field(None)
    quantidade_fotos_finalizacao_os :Mapped[Optional[str]] = mapped_field('')
    exige_comodato_finalizar_os :Mapped[Optional[Exige_comodato_finalizar_osEnum]] = mapped_field(None)
    quantidade_equipamentos :Mapped[Optional[str]] = mapped_field('')
    exige_produto_finalizar_os :Mapped[Optional[Exige_produto_finalizar_osEnum]] = mapped_field(None)
    quantidade_produtos :Mapped[Optional[str]] = mapped_field('')
    diagnostico_obrigatorio_finalizacao_os :Mapped[Optional[Diagnostico_obrigatorio_finalizacao_osEnum]] = mapped_field(None)
    localizacao_obrigatoria_cliente_finalizacao_os :Mapped[Optional[Localizacao_obrigatoria_cliente_finalizacao_osEnum]] = mapped_field(None)
    localizacao_obrigatoria_login_finalizacao_os :Mapped[Optional[Localizacao_obrigatoria_login_finalizacao_osEnum]] = mapped_field(None)
    id_resposta_padrao_finalizacao :Mapped[Optional[int]] = mapped_field(None)
    fat_somente_finalizada :Mapped[Optional[Fat_somente_finalizadaEnum]] = mapped_field(None)
    id_vendedor_faturamento :Mapped[Optional[int]] = mapped_field(None)
    id_tipo_doc_comodato :Mapped[Optional[int]] = mapped_field(None)
    id_tipo_doc_pedido :Mapped[Optional[int]] = mapped_field(None)
    id_cond_pag_produto :Mapped[Optional[int]] = mapped_field(None)
    id_tipo_doc_servico :Mapped[Optional[int]] = mapped_field(None)
    id_cond_pag_servico :Mapped[Optional[int]] = mapped_field(None)
    id_tipo_doc_patrimonio_venda :Mapped[Optional[int]] = mapped_field(None)
    id_cond_pag_patrimonio_venda :Mapped[Optional[int]] = mapped_field(None)
    dicagerarpedidoos :Mapped[Optional[str]] = mapped_field('')
    equipe_obrigatoria_finalizacao_os :Mapped[Optional[Equipe_obrigatoria_finalizacao_osEnum]] = mapped_field(None)
    valor_comissao :Mapped[Optional[str]] = mapped_field('')
    tipo_cobranca :Mapped[Optional[str]] = mapped_field('')
    id_oss_kit :Mapped[Optional[str]] = mapped_field('')
    horario_tempo_assunto :Mapped[Optional[str]] = mapped_field('')
    formato_endereco :Mapped[Optional[str]] = mapped_field('')
    sla_apenas_dias_uteis :Mapped[Optional[Sla_apenas_dias_uteisEnum]] = mapped_field(None)
    meta_horas_abertura :Mapped[Optional[str]] = mapped_field('')
    meta_horas_agendamento :Mapped[Optional[str]] = mapped_field('')
    wiz_comodato :Mapped[Optional[Wiz_comodatoEnum]] = mapped_field(None)
    wiz_produtos :Mapped[Optional[Wiz_produtosEnum]] = mapped_field(None)
    wiz_mensalidade :Mapped[Optional[Wiz_mensalidadeEnum]] = mapped_field(None)
    wiz_autorizar_ONU :Mapped[Optional[Wiz_autorizar_ONUEnum]] = mapped_field(None)
    wiz_localizacao :Mapped[Optional[Wiz_localizacaoEnum]] = mapped_field(None)
    wiz_arquivos :Mapped[Optional[Wiz_arquivosEnum]] = mapped_field(None)
    wiz_resumo_os :Mapped[Optional[Wiz_resumo_osEnum]] = mapped_field(None)
    wiz_servico :Mapped[Optional[Wiz_servicoEnum]] = mapped_field(None)
    dicamostraabaswizard :Mapped[Optional[str]] = mapped_field('')
    wiz_assinatura_obrig :Mapped[Optional[str]] = mapped_field('')
    fieldset_wiz_assinatura_obrig :Mapped[Optional[str]] = mapped_field('')
    habilitar_mini_projeto :Mapped[Optional[str]] = mapped_field('')
    mesclar_mini_projetos_ao_finalizar_os :Mapped[Optional[str]] = mapped_field('')
    mostrar_no_service :Mapped[Optional[Mostrar_no_serviceEnum]] = mapped_field(None)
    conceder_desconto_login_regiao_manutencao :Mapped[Optional[Conceder_desconto_login_regiao_manutencaoEnum]] = mapped_field(None)
    service_mobile_max_parc_adic_serv :Mapped[Optional[str]] = mapped_field('')
    id_checklist :Mapped[Optional[int]] = mapped_field(None)
    id_feedback :Mapped[Optional[int]] = mapped_field(None)
    mostrar_checklist_analise_risco :Mapped[Optional[Mostrar_checklist_analise_riscoEnum]] = mapped_field(None)
    id_questionario_analise_risco :Mapped[Optional[int]] = mapped_field(None)
    msg_regiao_manutencao :Mapped[Optional[str]] = mapped_field('')
    dicacorabaassunto :Mapped[Optional[str]] = mapped_field('')
    wiz_service_mobile_adicionais :Mapped[Optional[Wiz_service_mobile_adicionaisEnum]] = mapped_field(None)
    wiz_service_mobile_onu :Mapped[Optional[Wiz_service_mobile_onuEnum]] = mapped_field(None)
    wiz_service_mobile_config_dispositivo :Mapped[Optional[Wiz_service_mobile_config_dispositivoEnum]] = mapped_field(None)
    wiz_service_mobile_loc :Mapped[Optional[Wiz_service_mobile_locEnum]] = mapped_field(None)
    wiz_service_mobile_anexos :Mapped[Optional[Wiz_service_mobile_anexosEnum]] = mapped_field(None)
    wiz_service_mobile_checklist :Mapped[Optional[Wiz_service_mobile_checklistEnum]] = mapped_field(None)
    wiz_service_mobile_enviar_sms_deslocamento :Mapped[Optional[Wiz_service_mobile_enviar_sms_deslocamentoEnum]] = mapped_field(None)
    id_sms_deslocamento :Mapped[Optional[int]] = mapped_field(None)
    id_msg_omnichannel_deslocamento :Mapped[Optional[int]] = mapped_field(None)

    @property
    def table(self) -> str:
        return "su_oss_assunto"

    def _serialize_enum_and_str(self, value) -> str:
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
            'ativo': self._serialize_enum_and_str(self.ativo) if self.ativo is not None else '',
            'assunto': self._serialize_enum_and_str(self.assunto) if self.assunto is not None else '',
            'tipo_comissao': self._serialize_enum_and_str(self.tipo_comissao) if self.tipo_comissao is not None else '',
            'considerar_sla': self._serialize_enum_and_str(self.considerar_sla) if self.considerar_sla is not None else '',
            'metas_horas_abertura_ticket': self._serialize_enum_and_str(self.metas_horas_abertura_ticket) if self.metas_horas_abertura_ticket is not None else '',
            'id': str(self.id) if self.id is not None else '',
            'tipo': self._serialize_enum_and_str(self.tipo) if self.tipo is not None else '',
            'finalidade': self._serialize_enum_and_str(self.finalidade) if self.finalidade is not None else '',
            'endereco_padrao': self._serialize_enum_and_str(self.endereco_padrao) if self.endereco_padrao is not None else '',
            'mostra_hotsite': self._serialize_enum_and_str(self.mostra_hotsite) if self.mostra_hotsite is not None else '',
            'cor_marcador': self._serialize_enum_and_str(self.cor_marcador) if self.cor_marcador is not None else '',
            'dicacampocoragenda': self._serialize_enum_and_str(self.dicacampocoragenda) if self.dicacampocoragenda is not None else '',
            'prioridade_padrao': self._serialize_enum_and_str(self.prioridade_padrao) if self.prioridade_padrao is not None else '',
            'contrato_obrigatorio': self._serialize_enum_and_str(self.contrato_obrigatorio) if self.contrato_obrigatorio is not None else '',
            'login_obrigatorio': self._serialize_enum_and_str(self.login_obrigatorio) if self.login_obrigatorio is not None else '',
            'dicaloginobrigatorio': self._serialize_enum_and_str(self.dicaloginobrigatorio) if self.dicaloginobrigatorio is not None else '',
            'card_data_reservada': self._serialize_enum_and_str(self.card_data_reservada) if self.card_data_reservada is not None else '',
            'obrigar_processo_atendimento': self._serialize_enum_and_str(self.obrigar_processo_atendimento) if self.obrigar_processo_atendimento is not None else '',
            'obrigar_preenchimento_canal_atendimento': self._serialize_enum_and_str(self.obrigar_preenchimento_canal_atendimento) if self.obrigar_preenchimento_canal_atendimento is not None else '',
            'obrigatorio_status_complementar': self._serialize_enum_and_str(self.obrigatorio_status_complementar) if self.obrigatorio_status_complementar is not None else '',
            'id_resposta_padrao': str(self.id_resposta_padrao) if self.id_resposta_padrao is not None else '',
            'id_processo': str(self.id_processo) if self.id_processo is not None else '',
            'ultima_atualizacao': self._serialize_enum_and_str(self.ultima_atualizacao) if self.ultima_atualizacao is not None else '',
            'layout_impressao': self._serialize_enum_and_str(self.layout_impressao) if self.layout_impressao is not None else '',
            'imprimir_prod_serv': self._serialize_enum_and_str(self.imprimir_prod_serv) if self.imprimir_prod_serv is not None else '',
            'numero_de_vias': self._serialize_enum_and_str(self.numero_de_vias) if self.numero_de_vias is not None else '',
            'su_oss_modelo_impressao': str(self.su_oss_modelo_impressao) if self.su_oss_modelo_impressao is not None else '',
            'modelo_email': str(self.modelo_email) if self.modelo_email is not None else '',
            'habilita_assinatura_cliente': self._serialize_enum_and_str(self.habilita_assinatura_cliente) if self.habilita_assinatura_cliente is not None else '',
            'fieldset_habilita_assinatura_cliente': self._serialize_enum_and_str(self.fieldset_habilita_assinatura_cliente) if self.fieldset_habilita_assinatura_cliente is not None else '',
            'integracao_assinatura_digital': self._serialize_enum_and_str(self.integracao_assinatura_digital) if self.integracao_assinatura_digital is not None else '',
            'dica_assinatura_digital': self._serialize_enum_and_str(self.dica_assinatura_digital) if self.dica_assinatura_digital is not None else '',
            'permite_abrir_cliente_atraso': self._serialize_enum_and_str(self.permite_abrir_cliente_atraso) if self.permite_abrir_cliente_atraso is not None else '',
            'validar_choque_horarios_agendamento_os': self._serialize_enum_and_str(self.validar_choque_horarios_agendamento_os) if self.validar_choque_horarios_agendamento_os is not None else '',
            'setor_su_oss_chamado': str(self.setor_su_oss_chamado) if self.setor_su_oss_chamado is not None else '',
            'descricao': self._serialize_enum_and_str(self.descricao) if self.descricao is not None else '',
            'exige_fotos_finalizacao_os': self._serialize_enum_and_str(self.exige_fotos_finalizacao_os) if self.exige_fotos_finalizacao_os is not None else '',
            'quantidade_fotos_finalizacao_os': self._serialize_enum_and_str(self.quantidade_fotos_finalizacao_os) if self.quantidade_fotos_finalizacao_os is not None else '',
            'exige_comodato_finalizar_os': self._serialize_enum_and_str(self.exige_comodato_finalizar_os) if self.exige_comodato_finalizar_os is not None else '',
            'quantidade_equipamentos': self._serialize_enum_and_str(self.quantidade_equipamentos) if self.quantidade_equipamentos is not None else '',
            'exige_produto_finalizar_os': self._serialize_enum_and_str(self.exige_produto_finalizar_os) if self.exige_produto_finalizar_os is not None else '',
            'quantidade_produtos': self._serialize_enum_and_str(self.quantidade_produtos) if self.quantidade_produtos is not None else '',
            'diagnostico_obrigatorio_finalizacao_os': self._serialize_enum_and_str(self.diagnostico_obrigatorio_finalizacao_os) if self.diagnostico_obrigatorio_finalizacao_os is not None else '',
            'localizacao_obrigatoria_cliente_finalizacao_os': self._serialize_enum_and_str(self.localizacao_obrigatoria_cliente_finalizacao_os) if self.localizacao_obrigatoria_cliente_finalizacao_os is not None else '',
            'localizacao_obrigatoria_login_finalizacao_os': self._serialize_enum_and_str(self.localizacao_obrigatoria_login_finalizacao_os) if self.localizacao_obrigatoria_login_finalizacao_os is not None else '',
            'id_resposta_padrao_finalizacao': str(self.id_resposta_padrao_finalizacao) if self.id_resposta_padrao_finalizacao is not None else '',
            'fat_somente_finalizada': self._serialize_enum_and_str(self.fat_somente_finalizada) if self.fat_somente_finalizada is not None else '',
            'id_vendedor_faturamento': str(self.id_vendedor_faturamento) if self.id_vendedor_faturamento is not None else '',
            'id_tipo_doc_comodato': str(self.id_tipo_doc_comodato) if self.id_tipo_doc_comodato is not None else '',
            'id_tipo_doc_pedido': str(self.id_tipo_doc_pedido) if self.id_tipo_doc_pedido is not None else '',
            'id_cond_pag_produto': str(self.id_cond_pag_produto) if self.id_cond_pag_produto is not None else '',
            'id_tipo_doc_servico': str(self.id_tipo_doc_servico) if self.id_tipo_doc_servico is not None else '',
            'id_cond_pag_servico': str(self.id_cond_pag_servico) if self.id_cond_pag_servico is not None else '',
            'id_tipo_doc_patrimonio_venda': str(self.id_tipo_doc_patrimonio_venda) if self.id_tipo_doc_patrimonio_venda is not None else '',
            'id_cond_pag_patrimonio_venda': str(self.id_cond_pag_patrimonio_venda) if self.id_cond_pag_patrimonio_venda is not None else '',
            'dicagerarpedidoos': self._serialize_enum_and_str(self.dicagerarpedidoos) if self.dicagerarpedidoos is not None else '',
            'equipe_obrigatoria_finalizacao_os': self._serialize_enum_and_str(self.equipe_obrigatoria_finalizacao_os) if self.equipe_obrigatoria_finalizacao_os is not None else '',
            'valor_comissao': self._serialize_enum_and_str(self.valor_comissao) if self.valor_comissao is not None else '',
            'tipo_cobranca': self._serialize_enum_and_str(self.tipo_cobranca) if self.tipo_cobranca is not None else '',
            'id_oss_kit': self._serialize_enum_and_str(self.id_oss_kit) if self.id_oss_kit is not None else '',
            'horario_tempo_assunto': self._serialize_enum_and_str(self.horario_tempo_assunto) if self.horario_tempo_assunto is not None else '',
            'formato_endereco': self._serialize_enum_and_str(self.formato_endereco) if self.formato_endereco is not None else '',
            'sla_apenas_dias_uteis': self._serialize_enum_and_str(self.sla_apenas_dias_uteis) if self.sla_apenas_dias_uteis is not None else '',
            'meta_horas_abertura': self._serialize_enum_and_str(self.meta_horas_abertura) if self.meta_horas_abertura is not None else '',
            'meta_horas_agendamento': self._serialize_enum_and_str(self.meta_horas_agendamento) if self.meta_horas_agendamento is not None else '',
            'wiz_comodato': self._serialize_enum_and_str(self.wiz_comodato) if self.wiz_comodato is not None else '',
            'wiz_produtos': self._serialize_enum_and_str(self.wiz_produtos) if self.wiz_produtos is not None else '',
            'wiz_mensalidade': self._serialize_enum_and_str(self.wiz_mensalidade) if self.wiz_mensalidade is not None else '',
            'wiz_autorizar_ONU': self._serialize_enum_and_str(self.wiz_autorizar_ONU) if self.wiz_autorizar_ONU is not None else '',
            'wiz_localizacao': self._serialize_enum_and_str(self.wiz_localizacao) if self.wiz_localizacao is not None else '',
            'wiz_arquivos': self._serialize_enum_and_str(self.wiz_arquivos) if self.wiz_arquivos is not None else '',
            'wiz_resumo_os': self._serialize_enum_and_str(self.wiz_resumo_os) if self.wiz_resumo_os is not None else '',
            'wiz_servico': self._serialize_enum_and_str(self.wiz_servico) if self.wiz_servico is not None else '',
            'dicamostraabaswizard': self._serialize_enum_and_str(self.dicamostraabaswizard) if self.dicamostraabaswizard is not None else '',
            'wiz_assinatura_obrig': self._serialize_enum_and_str(self.wiz_assinatura_obrig) if self.wiz_assinatura_obrig is not None else '',
            'fieldset_wiz_assinatura_obrig': self._serialize_enum_and_str(self.fieldset_wiz_assinatura_obrig) if self.fieldset_wiz_assinatura_obrig is not None else '',
            'habilitar_mini_projeto': self._serialize_enum_and_str(self.habilitar_mini_projeto) if self.habilitar_mini_projeto is not None else '',
            'mesclar_mini_projetos_ao_finalizar_os': self._serialize_enum_and_str(self.mesclar_mini_projetos_ao_finalizar_os) if self.mesclar_mini_projetos_ao_finalizar_os is not None else '',
            'mostrar_no_service': self._serialize_enum_and_str(self.mostrar_no_service) if self.mostrar_no_service is not None else '',
            'conceder_desconto_login_regiao_manutencao': self._serialize_enum_and_str(self.conceder_desconto_login_regiao_manutencao) if self.conceder_desconto_login_regiao_manutencao is not None else '',
            'service_mobile_max_parc_adic_serv': self._serialize_enum_and_str(self.service_mobile_max_parc_adic_serv) if self.service_mobile_max_parc_adic_serv is not None else '',
            'id_checklist': str(self.id_checklist) if self.id_checklist is not None else '',
            'id_feedback': str(self.id_feedback) if self.id_feedback is not None else '',
            'mostrar_checklist_analise_risco': self._serialize_enum_and_str(self.mostrar_checklist_analise_risco) if self.mostrar_checklist_analise_risco is not None else '',
            'id_questionario_analise_risco': str(self.id_questionario_analise_risco) if self.id_questionario_analise_risco is not None else '',
            'msg_regiao_manutencao': self._serialize_enum_and_str(self.msg_regiao_manutencao) if self.msg_regiao_manutencao is not None else '',
            'dicacorabaassunto': self._serialize_enum_and_str(self.dicacorabaassunto) if self.dicacorabaassunto is not None else '',
            'wiz_service_mobile_adicionais': self._serialize_enum_and_str(self.wiz_service_mobile_adicionais) if self.wiz_service_mobile_adicionais is not None else '',
            'wiz_service_mobile_onu': self._serialize_enum_and_str(self.wiz_service_mobile_onu) if self.wiz_service_mobile_onu is not None else '',
            'wiz_service_mobile_config_dispositivo': self._serialize_enum_and_str(self.wiz_service_mobile_config_dispositivo) if self.wiz_service_mobile_config_dispositivo is not None else '',
            'wiz_service_mobile_loc': self._serialize_enum_and_str(self.wiz_service_mobile_loc) if self.wiz_service_mobile_loc is not None else '',
            'wiz_service_mobile_anexos': self._serialize_enum_and_str(self.wiz_service_mobile_anexos) if self.wiz_service_mobile_anexos is not None else '',
            'wiz_service_mobile_checklist': self._serialize_enum_and_str(self.wiz_service_mobile_checklist) if self.wiz_service_mobile_checklist is not None else '',
            'wiz_service_mobile_enviar_sms_deslocamento': self._serialize_enum_and_str(self.wiz_service_mobile_enviar_sms_deslocamento) if self.wiz_service_mobile_enviar_sms_deslocamento is not None else '',
            'id_sms_deslocamento': str(self.id_sms_deslocamento) if self.id_sms_deslocamento is not None else '',
            'id_msg_omnichannel_deslocamento': str(self.id_msg_omnichannel_deslocamento) if self.id_msg_omnichannel_deslocamento is not None else '',
        }
        return {key: serialize(value) for key, value in data.items()}

    def is_valid(self) -> bool:
        return self.ativo is not None and self.assunto is not None and self.tipo_comissao is not None and self.considerar_sla is not None and self.metas_horas_abertura_ticket is not None
