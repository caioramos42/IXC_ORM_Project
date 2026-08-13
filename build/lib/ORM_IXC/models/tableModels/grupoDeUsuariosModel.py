from __future__ import annotations
from typing import Optional
from ORM_IXC.interfaces import IModelWithId
from ORM_IXC.enums.grupoDeUsuarios import *
from ORM_IXC.statemants.maps.mapper import Mapped, field as mapped_field
from ORM_IXC.statemants.maps.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel


@MetaModels
class GrupoDeUsuariosModel(IModelWithId, BaseModel):
    grupo :Mapped[str]
    redes :Mapped[str]
    permissao_tipo :Mapped[Permissao_tipoEnum]
    permissao_bt_form :Mapped[Permissao_bt_formEnum]
    permissao_campo_form :Mapped[Permissao_campo_formEnum]
    poermissao_bt_grid :Mapped[str]
    id :Mapped[Optional[int]]
    tipo_alcada :Mapped[Optional[str]] = mapped_field('')
    descricao :Mapped[Optional[str]] = mapped_field('')
    ativo :Mapped[Optional[AtivoEnum]] = mapped_field(None)
    campo_dica_inativar_grupo :Mapped[Optional[str]] = mapped_field('')
    enable_totp_group :Mapped[Optional[Enable_totp_groupEnum]] = mapped_field(None)
    fieldset_tfa_grupo :Mapped[Optional[str]] = mapped_field('')
    horarios :Mapped[Optional[str]] = mapped_field('')
    filtrar_filiais :Mapped[Optional[str]] = mapped_field('')
    filtra_grid_filial :Mapped[Optional[str]] = mapped_field('')
    fiberdocs_filtro_filial :Mapped[Optional[str]] = mapped_field('')
    filtrar_requisicao_material :Mapped[Optional[str]] = mapped_field('')
    filtrar_transferencia_material_confirmacao :Mapped[Optional[str]] = mapped_field('')
    filtrar_grid_os_cliente :Mapped[Optional[str]] = mapped_field('')
    exporta_xls :Mapped[Optional[str]] = mapped_field('')
    permite_atualizar :Mapped[Optional[Permite_atualizarEnum]] = mapped_field(None)
    permite_chamar_suporte :Mapped[Optional[str]] = mapped_field('')
    permite_alteracao_data_base_grupo :Mapped[Optional[str]] = mapped_field('')
    visualizar_auditoria :Mapped[Optional[str]] = mapped_field('')
    habilitar_barra_pesquisa :Mapped[Optional[str]] = mapped_field('')
    permite_listar_caixas :Mapped[Optional[str]] = mapped_field('')
    acesso_upvoty_ixc :Mapped[Optional[Acesso_upvoty_ixcEnum]] = mapped_field(None)
    expire_password :Mapped[Optional[Expire_passwordEnum]] = mapped_field(None)
    expire_password_days :Mapped[Optional[str]] = mapped_field('')
    tempo_limite_sessao_minutos :Mapped[Optional[Tempo_limite_sessao_minutosEnum]] = mapped_field(None)
    retrospectiva :Mapped[Optional[str]] = mapped_field('')
    visualizar_retro :Mapped[Optional[str]] = mapped_field('')
    permissao_retrospectiva :Mapped[Optional[str]] = mapped_field('')
    dica_usuarios :Mapped[Optional[str]] = mapped_field('')
    acesso_querybuilder :Mapped[Optional[Acesso_querybuilderEnum]] = mapped_field(None)
    visualizar_visoes_querybuilder :Mapped[Optional[str]] = mapped_field('')
    acesso_avancado_querybuilder :Mapped[Optional[Acesso_avancado_querybuilderEnum]] = mapped_field(None)
    dashboard_padrao :Mapped[Optional[Dashboard_padraoEnum]] = mapped_field(None)
    dash_principal :Mapped[Optional[Dash_principalEnum]] = mapped_field(None)
    dash_contratos :Mapped[Optional[Dash_contratosEnum]] = mapped_field(None)
    dash_cobrancas :Mapped[Optional[Dash_cobrancasEnum]] = mapped_field(None)
    dash_financeiro :Mapped[Optional[Dash_financeiroEnum]] = mapped_field(None)
    dash_contas_a_receber :Mapped[Optional[Dash_contas_a_receberEnum]] = mapped_field(None)
    dash_contas_a_pagar :Mapped[Optional[Dash_contas_a_pagarEnum]] = mapped_field(None)
    dash_cliente_chave :Mapped[Optional[Dash_cliente_chaveEnum]] = mapped_field(None)
    dash_acessos :Mapped[Optional[Dash_acessosEnum]] = mapped_field(None)
    dash_atendimento :Mapped[Optional[Dash_atendimentoEnum]] = mapped_field(None)
    dash_ordem_servico :Mapped[Optional[Dash_ordem_servicoEnum]] = mapped_field(None)
    dash_ordem_servico_user :Mapped[Optional[Dash_ordem_servico_userEnum]] = mapped_field(None)
    dash_crm :Mapped[Optional[Dash_crmEnum]] = mapped_field(None)
    dash_crm_pessoa_fisica :Mapped[Optional[Dash_crm_pessoa_fisicaEnum]] = mapped_field(None)
    dash_crm_corporativo :Mapped[Optional[Dash_crm_corporativoEnum]] = mapped_field(None)
    dash_crm_user :Mapped[Optional[Dash_crm_userEnum]] = mapped_field(None)
    dash_negociacoes :Mapped[Optional[Dash_negociacoesEnum]] = mapped_field(None)
    dash_serverinfo :Mapped[Optional[Dash_serverinfoEnum]] = mapped_field(None)
    dash_radius :Mapped[Optional[Dash_radiusEnum]] = mapped_field(None)
    dash_monitoramento_fibra :Mapped[Optional[Dash_monitoramento_fibraEnum]] = mapped_field(None)
    dash_faturas :Mapped[Optional[Dash_faturasEnum]] = mapped_field(None)

    @property
    def table(self) -> str:
        return "usuarios_grupo"

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
            'grupo': self._serialize_enum_and_str(self.grupo) if self.grupo is not None else '',
            'redes': self._serialize_enum_and_str(self.redes) if self.redes is not None else '',
            'permissao_tipo': self._serialize_enum_and_str(self.permissao_tipo) if self.permissao_tipo is not None else '',
            'permissao_bt_form': self._serialize_enum_and_str(self.permissao_bt_form) if self.permissao_bt_form is not None else '',
            'permissao_campo_form': self._serialize_enum_and_str(self.permissao_campo_form) if self.permissao_campo_form is not None else '',
            'poermissao_bt_grid': self._serialize_enum_and_str(self.poermissao_bt_grid) if self.poermissao_bt_grid is not None else '',
            'id': str(self.id) if self.id is not None else '',
            'tipo_alcada': self._serialize_enum_and_str(self.tipo_alcada) if self.tipo_alcada is not None else '',
            'descricao': self._serialize_enum_and_str(self.descricao) if self.descricao is not None else '',
            'ativo': self._serialize_enum_and_str(self.ativo) if self.ativo is not None else '',
            'campo_dica_inativar_grupo': self._serialize_enum_and_str(self.campo_dica_inativar_grupo) if self.campo_dica_inativar_grupo is not None else '',
            'enable_totp_group': self._serialize_enum_and_str(self.enable_totp_group) if self.enable_totp_group is not None else '',
            'fieldset_tfa_grupo': self._serialize_enum_and_str(self.fieldset_tfa_grupo) if self.fieldset_tfa_grupo is not None else '',
            'horarios': self._serialize_enum_and_str(self.horarios) if self.horarios is not None else '',
            'filtrar_filiais': self._serialize_enum_and_str(self.filtrar_filiais) if self.filtrar_filiais is not None else '',
            'filtra_grid_filial': self._serialize_enum_and_str(self.filtra_grid_filial) if self.filtra_grid_filial is not None else '',
            'fiberdocs_filtro_filial': self._serialize_enum_and_str(self.fiberdocs_filtro_filial) if self.fiberdocs_filtro_filial is not None else '',
            'filtrar_requisicao_material': self._serialize_enum_and_str(self.filtrar_requisicao_material) if self.filtrar_requisicao_material is not None else '',
            'filtrar_transferencia_material_confirmacao': self._serialize_enum_and_str(self.filtrar_transferencia_material_confirmacao) if self.filtrar_transferencia_material_confirmacao is not None else '',
            'filtrar_grid_os_cliente': self._serialize_enum_and_str(self.filtrar_grid_os_cliente) if self.filtrar_grid_os_cliente is not None else '',
            'exporta_xls': self._serialize_enum_and_str(self.exporta_xls) if self.exporta_xls is not None else '',
            'permite_atualizar': self._serialize_enum_and_str(self.permite_atualizar) if self.permite_atualizar is not None else '',
            'permite_chamar_suporte': self._serialize_enum_and_str(self.permite_chamar_suporte) if self.permite_chamar_suporte is not None else '',
            'permite_alteracao_data_base_grupo': self._serialize_enum_and_str(self.permite_alteracao_data_base_grupo) if self.permite_alteracao_data_base_grupo is not None else '',
            'visualizar_auditoria': self._serialize_enum_and_str(self.visualizar_auditoria) if self.visualizar_auditoria is not None else '',
            'habilitar_barra_pesquisa': self._serialize_enum_and_str(self.habilitar_barra_pesquisa) if self.habilitar_barra_pesquisa is not None else '',
            'permite_listar_caixas': self._serialize_enum_and_str(self.permite_listar_caixas) if self.permite_listar_caixas is not None else '',
            'acesso_upvoty_ixc': self._serialize_enum_and_str(self.acesso_upvoty_ixc) if self.acesso_upvoty_ixc is not None else '',
            'expire_password': self._serialize_enum_and_str(self.expire_password) if self.expire_password is not None else '',
            'expire_password_days': self._serialize_enum_and_str(self.expire_password_days) if self.expire_password_days is not None else '',
            'tempo_limite_sessao_minutos': self._serialize_enum_and_str(self.tempo_limite_sessao_minutos) if self.tempo_limite_sessao_minutos is not None else '',
            'retrospectiva': self._serialize_enum_and_str(self.retrospectiva) if self.retrospectiva is not None else '',
            'visualizar_retro': self._serialize_enum_and_str(self.visualizar_retro) if self.visualizar_retro is not None else '',
            'permissao_retrospectiva': self._serialize_enum_and_str(self.permissao_retrospectiva) if self.permissao_retrospectiva is not None else '',
            'dica_usuarios': self._serialize_enum_and_str(self.dica_usuarios) if self.dica_usuarios is not None else '',
            'acesso_querybuilder': self._serialize_enum_and_str(self.acesso_querybuilder) if self.acesso_querybuilder is not None else '',
            'visualizar_visoes_querybuilder': self._serialize_enum_and_str(self.visualizar_visoes_querybuilder) if self.visualizar_visoes_querybuilder is not None else '',
            'acesso_avancado_querybuilder': self._serialize_enum_and_str(self.acesso_avancado_querybuilder) if self.acesso_avancado_querybuilder is not None else '',
            'dashboard_padrao': self._serialize_enum_and_str(self.dashboard_padrao) if self.dashboard_padrao is not None else '',
            'dash_principal': self._serialize_enum_and_str(self.dash_principal) if self.dash_principal is not None else '',
            'dash_contratos': self._serialize_enum_and_str(self.dash_contratos) if self.dash_contratos is not None else '',
            'dash_cobrancas': self._serialize_enum_and_str(self.dash_cobrancas) if self.dash_cobrancas is not None else '',
            'dash_financeiro': self._serialize_enum_and_str(self.dash_financeiro) if self.dash_financeiro is not None else '',
            'dash_contas_a_receber': self._serialize_enum_and_str(self.dash_contas_a_receber) if self.dash_contas_a_receber is not None else '',
            'dash_contas_a_pagar': self._serialize_enum_and_str(self.dash_contas_a_pagar) if self.dash_contas_a_pagar is not None else '',
            'dash_cliente_chave': self._serialize_enum_and_str(self.dash_cliente_chave) if self.dash_cliente_chave is not None else '',
            'dash_acessos': self._serialize_enum_and_str(self.dash_acessos) if self.dash_acessos is not None else '',
            'dash_atendimento': self._serialize_enum_and_str(self.dash_atendimento) if self.dash_atendimento is not None else '',
            'dash_ordem_servico': self._serialize_enum_and_str(self.dash_ordem_servico) if self.dash_ordem_servico is not None else '',
            'dash_ordem_servico_user': self._serialize_enum_and_str(self.dash_ordem_servico_user) if self.dash_ordem_servico_user is not None else '',
            'dash_crm': self._serialize_enum_and_str(self.dash_crm) if self.dash_crm is not None else '',
            'dash_crm_pessoa_fisica': self._serialize_enum_and_str(self.dash_crm_pessoa_fisica) if self.dash_crm_pessoa_fisica is not None else '',
            'dash_crm_corporativo': self._serialize_enum_and_str(self.dash_crm_corporativo) if self.dash_crm_corporativo is not None else '',
            'dash_crm_user': self._serialize_enum_and_str(self.dash_crm_user) if self.dash_crm_user is not None else '',
            'dash_negociacoes': self._serialize_enum_and_str(self.dash_negociacoes) if self.dash_negociacoes is not None else '',
            'dash_serverinfo': self._serialize_enum_and_str(self.dash_serverinfo) if self.dash_serverinfo is not None else '',
            'dash_radius': self._serialize_enum_and_str(self.dash_radius) if self.dash_radius is not None else '',
            'dash_monitoramento_fibra': self._serialize_enum_and_str(self.dash_monitoramento_fibra) if self.dash_monitoramento_fibra is not None else '',
            'dash_faturas': self._serialize_enum_and_str(self.dash_faturas) if self.dash_faturas is not None else '',
        }
        return {key: serialize(value) for key, value in data.items()}

    def is_valid(self) -> bool:
        return self.grupo is not None and self.redes is not None and self.permissao_tipo is not None and self.permissao_bt_form is not None and self.permissao_campo_form is not None and self.poermissao_bt_grid is not None
