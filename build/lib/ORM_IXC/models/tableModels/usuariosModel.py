from __future__ import annotations
from typing import Optional
from ORM_IXC.interfaces import IModelWithId
from ORM_IXC.enums.usuarios import *
from ORM_IXC.statemants.maps.mapper import Mapped, field as mapped_field
from ORM_IXC.statemants.maps.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel


@MetaModels
class UsuariosModel(IModelWithId, BaseModel):
    id_grupo :Mapped[int] = mapped_field('')
    nome :Mapped[str] = mapped_field('')
    email :Mapped[str] = mapped_field('')
    senha :Mapped[str] = mapped_field('')
    tipo_acesso :Mapped[Tipo_acessoEnum] = mapped_field('')
    scheme :Mapped[SchemeEnum] = mapped_field('')
    language :Mapped[LanguageEnum] = mapped_field('')
    recebimentos_dia_atual :Mapped[Recebimentos_dia_atualEnum] = mapped_field('')
    pagamentos_dia_atual :Mapped[Pagamentos_dia_atualEnum] = mapped_field('')
    lancamentos_dia_atual :Mapped[Lancamentos_dia_atualEnum] = mapped_field('')
    desc_parc_atraso :Mapped[Desc_parc_atrasoEnum] = mapped_field('')
    filtra_colaborador_quadro_kanban :Mapped[str] = mapped_field('')
    id :Mapped[Optional[int]] = mapped_field('')
    tipo_alcada :Mapped[Optional[str]] = mapped_field('')
    status :Mapped[Optional[StatusEnum]] = mapped_field(None)
    fieldset_user_group_inactive :Mapped[Optional[str]] = mapped_field('')
    template :Mapped[Optional[TemplateEnum]] = mapped_field(None)
    funcionario :Mapped[Optional[int]] = mapped_field(None)
    dica_colaborador :Mapped[Optional[str]] = mapped_field('')
    imagem :Mapped[Optional[str]] = mapped_field(None)
    dica_imagem :Mapped[Optional[str]] = mapped_field('')
    acesso_webservice :Mapped[Optional[str]] = mapped_field('')
    acesso_token :Mapped[Optional[str]] = mapped_field('')
    user_callcenter :Mapped[Optional[str]] = mapped_field('')
    callcenter :Mapped[Optional[CallcenterEnum]] = mapped_field(None)
    alter_passwd_date :Mapped[Optional[str]] = mapped_field('')
    caixa_fn_receber :Mapped[Optional[int]] = mapped_field(None)
    id_caixa :Mapped[Optional[str]] = mapped_field('')
    vendedor_padrao :Mapped[Optional[int]] = mapped_field(None)
    filtrar_plano_venda_filial_contrato :Mapped[Optional[Filtrar_plano_venda_filial_contratoEnum]] = mapped_field(None)
    permitir_alterar_versao_chaves :Mapped[Optional[Permitir_alterar_versao_chavesEnum]] = mapped_field(None)
    desc_max_recebimento :Mapped[Optional[str]] = mapped_field('')
    desc_max_monetario :Mapped[Optional[str]] = mapped_field('')
    desc_max_venda :Mapped[Optional[str]] = mapped_field('')
    desc_max_renegociacao :Mapped[Optional[str]] = mapped_field('')
    permite_alterar_comunicacao_fn_apagar :Mapped[Optional[Permite_alterar_comunicacao_fn_apagarEnum]] = mapped_field(None)
    filtra_departamento_ticket :Mapped[Optional[Filtra_departamento_ticketEnum]] = mapped_field(None)
    filtra_funcionario_ticket :Mapped[Optional[Filtra_funcionario_ticketEnum]] = mapped_field(None)
    mostrar_ticket_sem_funcionario :Mapped[Optional[Mostrar_ticket_sem_funcionarioEnum]] = mapped_field(None)
    filtra_setor :Mapped[Optional[Filtra_setorEnum]] = mapped_field(None)
    filtra_funcionario :Mapped[Optional[Filtra_funcionarioEnum]] = mapped_field(None)
    mostrar_os_sem_funcionario :Mapped[Optional[Mostrar_os_sem_funcionarioEnum]] = mapped_field(None)
    inmap_filtra_vendedor :Mapped[Optional[str]] = mapped_field('')
    dica_filtra_responsavel :Mapped[Optional[str]] = mapped_field('')
    crm_filtra_vendedor :Mapped[Optional[str]] = mapped_field('')
    administrador_kanban :Mapped[Optional[Administrador_kanbanEnum]] = mapped_field(None)
    enviar_monitoramento_host :Mapped[Optional[str]] = mapped_field('')
    enviar_notificacao_backup :Mapped[Optional[str]] = mapped_field('')
    permite_inutilizar_patrimonio :Mapped[Optional[Permite_inutilizar_patrimonioEnum]] = mapped_field(None)
    permite_ver_diferenca :Mapped[Optional[Permite_ver_diferencaEnum]] = mapped_field(None)

    @property
    def table(self) -> str:
        return "usuarios"

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
            'id_grupo': str(self.id_grupo) if self.id_grupo is not None else '',
            'nome': self._serialize_enum_and_str(self.nome) if self.nome is not None else '',
            'email': self._serialize_enum_and_str(self.email) if self.email is not None else '',
            'senha': self._serialize_enum_and_str(self.senha) if self.senha is not None else '',
            'tipo_acesso': self._serialize_enum_and_str(self.tipo_acesso) if self.tipo_acesso is not None else '',
            'scheme': self._serialize_enum_and_str(self.scheme) if self.scheme is not None else '',
            'language': self._serialize_enum_and_str(self.language) if self.language is not None else '',
            'recebimentos_dia_atual': self._serialize_enum_and_str(self.recebimentos_dia_atual) if self.recebimentos_dia_atual is not None else '',
            'pagamentos_dia_atual': self._serialize_enum_and_str(self.pagamentos_dia_atual) if self.pagamentos_dia_atual is not None else '',
            'lancamentos_dia_atual': self._serialize_enum_and_str(self.lancamentos_dia_atual) if self.lancamentos_dia_atual is not None else '',
            'desc_parc_atraso': self._serialize_enum_and_str(self.desc_parc_atraso) if self.desc_parc_atraso is not None else '',
            'filtra_colaborador_quadro_kanban': self._serialize_enum_and_str(self.filtra_colaborador_quadro_kanban) if self.filtra_colaborador_quadro_kanban is not None else '',
            'id': str(self.id) if self.id is not None else '',
            'tipo_alcada': self._serialize_enum_and_str(self.tipo_alcada) if self.tipo_alcada is not None else '',
            'status': self._serialize_enum_and_str(self.status) if self.status is not None else '',
            'fieldset_user_group_inactive': self._serialize_enum_and_str(self.fieldset_user_group_inactive) if self.fieldset_user_group_inactive is not None else '',
            'template': self._serialize_enum_and_str(self.template) if self.template is not None else '',
            'funcionario': str(self.funcionario) if self.funcionario is not None else '',
            'dica_colaborador': self._serialize_enum_and_str(self.dica_colaborador) if self.dica_colaborador is not None else '',
            'imagem': self._serialize_enum_and_str(self.imagem) if self.imagem is not None else '',
            'dica_imagem': self._serialize_enum_and_str(self.dica_imagem) if self.dica_imagem is not None else '',
            'acesso_webservice': self._serialize_enum_and_str(self.acesso_webservice) if self.acesso_webservice is not None else '',
            'acesso_token': self._serialize_enum_and_str(self.acesso_token) if self.acesso_token is not None else '',
            'user_callcenter': self._serialize_enum_and_str(self.user_callcenter) if self.user_callcenter is not None else '',
            'callcenter': self._serialize_enum_and_str(self.callcenter) if self.callcenter is not None else '',
            'alter_passwd_date': self._serialize_enum_and_str(self.alter_passwd_date) if self.alter_passwd_date is not None else '',
            'caixa_fn_receber': str(self.caixa_fn_receber) if self.caixa_fn_receber is not None else '',
            'id_caixa': self._serialize_enum_and_str(self.id_caixa) if self.id_caixa is not None else '',
            'vendedor_padrao': str(self.vendedor_padrao) if self.vendedor_padrao is not None else '',
            'filtrar_plano_venda_filial_contrato': self._serialize_enum_and_str(self.filtrar_plano_venda_filial_contrato) if self.filtrar_plano_venda_filial_contrato is not None else '',
            'permitir_alterar_versao_chaves': self._serialize_enum_and_str(self.permitir_alterar_versao_chaves) if self.permitir_alterar_versao_chaves is not None else '',
            'desc_max_recebimento': self._serialize_enum_and_str(self.desc_max_recebimento) if self.desc_max_recebimento is not None else '',
            'desc_max_monetario': self._serialize_enum_and_str(self.desc_max_monetario) if self.desc_max_monetario is not None else '',
            'desc_max_venda': self._serialize_enum_and_str(self.desc_max_venda) if self.desc_max_venda is not None else '',
            'desc_max_renegociacao': self._serialize_enum_and_str(self.desc_max_renegociacao) if self.desc_max_renegociacao is not None else '',
            'permite_alterar_comunicacao_fn_apagar': self._serialize_enum_and_str(self.permite_alterar_comunicacao_fn_apagar) if self.permite_alterar_comunicacao_fn_apagar is not None else '',
            'filtra_departamento_ticket': self._serialize_enum_and_str(self.filtra_departamento_ticket) if self.filtra_departamento_ticket is not None else '',
            'filtra_funcionario_ticket': self._serialize_enum_and_str(self.filtra_funcionario_ticket) if self.filtra_funcionario_ticket is not None else '',
            'mostrar_ticket_sem_funcionario': self._serialize_enum_and_str(self.mostrar_ticket_sem_funcionario) if self.mostrar_ticket_sem_funcionario is not None else '',
            'filtra_setor': self._serialize_enum_and_str(self.filtra_setor) if self.filtra_setor is not None else '',
            'filtra_funcionario': self._serialize_enum_and_str(self.filtra_funcionario) if self.filtra_funcionario is not None else '',
            'mostrar_os_sem_funcionario': self._serialize_enum_and_str(self.mostrar_os_sem_funcionario) if self.mostrar_os_sem_funcionario is not None else '',
            'inmap_filtra_vendedor': self._serialize_enum_and_str(self.inmap_filtra_vendedor) if self.inmap_filtra_vendedor is not None else '',
            'dica_filtra_responsavel': self._serialize_enum_and_str(self.dica_filtra_responsavel) if self.dica_filtra_responsavel is not None else '',
            'crm_filtra_vendedor': self._serialize_enum_and_str(self.crm_filtra_vendedor) if self.crm_filtra_vendedor is not None else '',
            'administrador_kanban': self._serialize_enum_and_str(self.administrador_kanban) if self.administrador_kanban is not None else '',
            'enviar_monitoramento_host': self._serialize_enum_and_str(self.enviar_monitoramento_host) if self.enviar_monitoramento_host is not None else '',
            'enviar_notificacao_backup': self._serialize_enum_and_str(self.enviar_notificacao_backup) if self.enviar_notificacao_backup is not None else '',
            'permite_inutilizar_patrimonio': self._serialize_enum_and_str(self.permite_inutilizar_patrimonio) if self.permite_inutilizar_patrimonio is not None else '',
            'permite_ver_diferenca': self._serialize_enum_and_str(self.permite_ver_diferenca) if self.permite_ver_diferenca is not None else '',
        }
        return {key: serialize(value) for key, value in data.items()}

    def is_valid(self) -> bool:
        return self.id_grupo is not None and self.nome is not None and self.email is not None and self.senha is not None and self.tipo_acesso is not None and self.scheme is not None and self.language is not None and self.recebimentos_dia_atual is not None and self.pagamentos_dia_atual is not None and self.lancamentos_dia_atual is not None and self.desc_parc_atraso is not None and self.filtra_colaborador_quadro_kanban is not None
