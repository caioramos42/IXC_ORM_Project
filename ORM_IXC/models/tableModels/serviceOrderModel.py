from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, override
from ORM_IXC.interfaces.IModel import IModel, IModelWithId
from ORM_IXC.enums.serviceOrder import *
from ORM_IXC.statemants.classBase import Field
from ORM_IXC.statemants.mapper import Mapped, field as mapped_field
from ORM_IXC.statemants.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel

@MetaModels
class ServiceOrderModel(IModelWithId, BaseModel):
    id: Mapped[Optional[int]] = mapped_field(0)
    id_assunto: Mapped[int] = mapped_field(0)
    id_filial: Mapped[int] = mapped_field(0)
    setor: Mapped[int] = mapped_field(0)
    id_atendente: Mapped[str] = mapped_field('')
    tipo: Mapped[Optional[TipoEnum]] = mapped_field(default=TipoEnum.CLIENTE)
    id_ticket: Mapped[Optional[int]] = mapped_field(default=None)
    protocolo: Mapped[Optional[str]] = mapped_field(default='')
    dica_assinatura_digital: Mapped[Optional[str]] = mapped_field(default= '')
    id_cliente: Mapped[Optional[int]] = mapped_field(None)
    id_estrutura: Mapped[Optional[int]] = mapped_field(None)
    id_login: Mapped[Optional[int]] = mapped_field(None)
    id_contrato_kit: Mapped[Optional[int]] = mapped_field(None)
    origem_endereco: Mapped[Origem_enderecoEnum] = mapped_field(Origem_enderecoEnum.MANUAL)
    origem_endereco_estrutura: Mapped[Optional[Origem_endereco_estruturaEnum]] = mapped_field(Origem_endereco_estruturaEnum.ESTRUTURA)
    latitude: Mapped[Optional[str]] = mapped_field('')
    longitude: Mapped[Optional[str]] = mapped_field('')
    status_conexao: Mapped[Optional[Status_conexaoEnum]] = mapped_field(None)
    prioridade: Mapped[PrioridadeEnum] = mapped_field(PrioridadeEnum.NORMAL)
    melhor_horario_agenda: Mapped[Optional[Melhor_horario_agendaEnum]] = mapped_field(Melhor_horario_agendaEnum.QUALQUER)
    id_tecnico: Mapped[Optional[int]] = mapped_field(None)
    mensagem: Mapped[Optional[str]] = mapped_field('')
    id_receber: Mapped[Optional[str]] = mapped_field('')
    idx: Mapped[Optional[str]] = mapped_field('')
    status_pesquisa_satisfacao: Mapped[Optional[Status_pesquisa_satisfacaoEnum]] = mapped_field(None)
    status: Mapped[StatusEnum] = mapped_field(StatusEnum.ABERTA)
    habilita_assinatura_cliente: Mapped[Optional[str]] = mapped_field('')
    status_assinatura: Mapped[Optional[Status_assinaturaEnum]] = mapped_field(Status_assinaturaEnum.PENDENTE)
    gera_comissao: Mapped[Optional[Gera_comissaoEnum]] = mapped_field(Gera_comissaoEnum.SIM)
    liberado: Mapped[Optional[LiberadoEnum]] = mapped_field(LiberadoEnum.SIM)
    impresso: Mapped[Optional[ImpressoEnum]] = mapped_field(ImpressoEnum.NAO)
    preview: Mapped[Optional[str]] = mapped_field('')
    id_wfl_param_os: Mapped[Optional[str]] = mapped_field('')
    id_wfl_tarefa: Mapped[Optional[str]] = mapped_field('')
    id_su_diagnostico: Mapped[Optional[int]] = mapped_field(None)
    regiao_manutencao: Mapped[Optional[str]] = mapped_field('')
    origem_cadastro: Mapped[Optional[Origem_cadastroEnum]] = mapped_field(Origem_cadastroEnum.P)
    origem_change_endereco: Mapped[Optional[str]] = mapped_field('')
    status_sla: Mapped[Optional[str]] = mapped_field('')
    ultima_atualizacao: Mapped[Optional[str]] = mapped_field('')
    ids_login_regiao_manutencao: Mapped[Optional[str]] = mapped_field('')
    origem_os_aberta: Mapped[Optional[Origem_os_abertaEnum]] = mapped_field(None)
    id_cidade: Mapped[Optional[int]] = mapped_field(None)
    bairro: Mapped[Optional[str]] = mapped_field('')
    endereco: Mapped[Optional[str]] = mapped_field('')
    complemento: Mapped[Optional[str]] = mapped_field('')
    referencia: Mapped[Optional[str]] = mapped_field('')
    id_condominio: Mapped[Optional[int]] = mapped_field(None)
    bloco: Mapped[Optional[str]] = mapped_field('')
    apartamento: Mapped[Optional[str]] = mapped_field('')
    data_abertura: Mapped[Optional[str]] = mapped_field('')
    data_inicio: Mapped[Optional[str]] = mapped_field('')
    data_hora_analise: Mapped[Optional[str]] = mapped_field('')
    data_agenda: Mapped[Optional[str]] = mapped_field('')
    data_agenda_final: Mapped[Optional[str]] = mapped_field('')
    data_hora_encaminhado: Mapped[Optional[str]] = mapped_field('')
    data_hora_assumido: Mapped[Optional[str]] = mapped_field('')
    data_hora_execucao: Mapped[Optional[str]] = mapped_field('')
    data_final: Mapped[Optional[str]] = mapped_field('')
    data_fechamento: Mapped[Optional[str]] = mapped_field('')
    data_prazo_limite: Mapped[Optional[str]] = mapped_field('')
    data_reservada: Mapped[Optional[str]] = mapped_field('')
    data_reagendar: Mapped[Optional[str]] = mapped_field('')
    data_prev_final: Mapped[Optional[str]] = mapped_field('')
    mensagem_resposta: Mapped[Optional[str]] = mapped_field('')
    justificativa_sla_atrasado: Mapped[Optional[str]] = mapped_field('')
    valor_total: Mapped[Optional[str]] = mapped_field('')
    valor_outras_despesas: Mapped[Optional[str]] = mapped_field('')
    valor_unit_comissao: Mapped[Optional[str]] = mapped_field('')
    valor_total_comissao: Mapped[Optional[str]] = mapped_field('')
  
    @property
    def table(self) -> str:
        return "su_oss_chamado"

    def to_dict(self) -> dict[str, str]:
        def serialize(value) -> str:
            if value is None:
                return ''
            raw = getattr(value, 'value', value)
            return '' if raw is None else str(raw)

        data = {
            'id': str(self.id),
            'id_assunto': str(self.id_assunto) if self.id_assunto is not None else '',
            'id_filial': str(self.id_filial) if self.id_filial is not None else '',
            'setor': str(self.setor) if self.setor is not None else '',
            'id_atendente': self.id_atendente if self.id_atendente is not None else '',
            'tipo': self.tipo.value if self.tipo is not None else '',
            'id_ticket': str(self.id_ticket) if self.id_ticket is not None else '',
            'protocolo': self.protocolo if self.protocolo is not None else '',
            'dica_assinatura_digital': self.dica_assinatura_digital if self.dica_assinatura_digital is not None else '',
            'id_cliente': str(self.id_cliente) if self.id_cliente is not None else '',
            'id_estrutura': str(self.id_estrutura) if self.id_estrutura is not None else '',
            'id_login': str(self.id_login) if self.id_login is not None else '',
            'id_contrato_kit': str(self.id_contrato_kit) if self.id_contrato_kit is not None else '',
            'origem_endereco': self.origem_endereco.value if self.origem_endereco is not None else '',
            'origem_endereco_estrutura': self.origem_endereco_estrutura.value if self.origem_endereco_estrutura is not None else '',
            'latitude': self.latitude if self.latitude is not None else '',
            'longitude': self.longitude if self.longitude is not None else '',
            'status_conexao': self.status_conexao.value if self.status_conexao is not None else '',
            'prioridade': self.prioridade.value if self.prioridade is not None else '',
            'melhor_horario_agenda': self.melhor_horario_agenda.value if self.melhor_horario_agenda is not None else '',
            'id_tecnico': str(self.id_tecnico) if self.id_tecnico is not None else '',
            'mensagem': self.mensagem if self.mensagem is not None else '',
            'id_receber': self.id_receber if self.id_receber is not None else '',
            'idx': self.idx if self.idx is not None else '',
            'status_pesquisa_satisfacao': self.status_pesquisa_satisfacao.value if self.status_pesquisa_satisfacao is not None else '',
            'status': self.status.value if self.status is not None else '',
            'habilita_assinatura_cliente': self.habilita_assinatura_cliente if self.habilita_assinatura_cliente is not None else '',
            'status_assinatura': self.status_assinatura.value if self.status_assinatura is not None else '',
            'gera_comissao': self.gera_comissao.value if self.gera_comissao is not None else '',
            'liberado': self.liberado.value if self.liberado is not None else '',
            'impresso': self.impresso.value if self.impresso is not None else '',
            'preview': self.preview if self.preview is not None else '',
            'id_wfl_param_os': self.id_wfl_param_os if self.id_wfl_param_os is not None else '',
            'id_wfl_tarefa': self.id_wfl_tarefa if self.id_wfl_tarefa is not None else '',
            'id_su_diagnostico': str(self.id_su_diagnostico) if self.id_su_diagnostico is not None else '',
            'regiao_manutencao': self.regiao_manutencao if self.regiao_manutencao is not None else '',
            'origem_cadastro': self.origem_cadastro.value if self.origem_cadastro is not None else '',
            'origem_change_endereco': self.origem_change_endereco if self.origem_change_endereco is not None else '',
            'status_sla': self.status_sla if self.status_sla is not None else '',
            'ultima_atualizacao': self.ultima_atualizacao if self.ultima_atualizacao is not None else '',
            'ids_login_regiao_manutencao': self.ids_login_regiao_manutencao if self.ids_login_regiao_manutencao is not None else '',
            'origem_os_aberta': self.origem_os_aberta.value if self.origem_os_aberta is not None else '',
            'id_cidade': str(self.id_cidade) if self.id_cidade is not None else '',
            'bairro': self.bairro if self.bairro is not None else '',
            'endereco': self.endereco if self.endereco is not None else '',
            'complemento': self.complemento if self.complemento is not None else '',
            'referencia': self.referencia if self.referencia is not None else '',
            'id_condominio': str(self.id_condominio) if self.id_condominio is not None else '',
            'bloco': self.bloco if self.bloco is not None else '',
            'apartamento': self.apartamento if self.apartamento is not None else '',
            'data_abertura': self.data_abertura if self.data_abertura is not None else '',
            'data_inicio': self.data_inicio if self.data_inicio is not None else '',
            'data_hora_analise': self.data_hora_analise if self.data_hora_analise is not None else '',
            'data_agenda': self.data_agenda if self.data_agenda is not None else '',
            'data_agenda_final': self.data_agenda_final if self.data_agenda_final is not None else '',
            'data_hora_encaminhado': self.data_hora_encaminhado if self.data_hora_encaminhado is not None else '',
            'data_hora_assumido': self.data_hora_assumido if self.data_hora_assumido is not None else '',
            'data_hora_execucao': self.data_hora_execucao if self.data_hora_execucao is not None else '',
            'data_final': self.data_final if self.data_final is not None else '',
            'data_fechamento': self.data_fechamento if self.data_fechamento is not None else '',
            'data_prazo_limite': self.data_prazo_limite if self.data_prazo_limite is not None else '',
            'data_reservada': self.data_reservada if self.data_reservada is not None else '',
            'data_reagendar': self.data_reagendar if self.data_reagendar is not None else '',
            'data_prev_final': self.data_prev_final if self.data_prev_final is not None else '',
            'mensagem_resposta': self.mensagem_resposta if self.mensagem_resposta is not None else '',
            'justificativa_sla_atrasado': self.justificativa_sla_atrasado if self.justificativa_sla_atrasado is not None else '',
            'valor_total': self.valor_total if self.valor_total is not None else '',
            'valor_outras_despesas': self.valor_outras_despesas if self.valor_outras_despesas is not None else '',
            'valor_unit_comissao': self.valor_unit_comissao if self.valor_unit_comissao is not None else '',
            'valor_total_comissao': self.valor_total_comissao if self.valor_total_comissao is not None else '',
        }
        return {key: serialize(value) for key, value in data.items()}

    def is_valid(self) -> bool:
        return self.id is not None and self.id_assunto is not None and self.id_filial is not None and self.setor is not None and self.id_atendente is not None

    @classmethod
    def dto_convert(cls_: object, data: dict[str, str]):
        raise NotImplementedError