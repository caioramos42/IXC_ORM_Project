from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from ORM_IXC.enums.atendimento import *
from ORM_IXC.statemants.mapper import Mapped, field as mapped_field
from ORM_IXC.interfaces import IModel, IModelWithId
from ORM_IXC.statemants.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel

@MetaModels
class AtendimentoModel(IModelWithId, BaseModel):
    id: Mapped[Optional[int]]
    titulo: Mapped[str]
    id_ticket_setor: Mapped[int]
    menssagem: Mapped[str]
    tipo: Mapped[TipoEnum] = mapped_field(TipoEnum.CLIENTE)
    id_estrutura: Mapped[Optional[int]] = mapped_field(None)
    protocolo: Mapped[Optional[str]] = mapped_field('')
    id_circuito: Mapped[Optional[int]] = mapped_field(None)
    id_cliente: Mapped[Optional[int]] = mapped_field(None)
    id_login: Mapped[Optional[int]] = mapped_field(None)
    id_contrato: Mapped[Optional[int]] = mapped_field(None)
    id_filial: Mapped[Optional[int]] = mapped_field(None)
    id_assunto: Mapped[Optional[int]] = mapped_field(None)
    origem_endereco: Mapped[Optional[Origem_enderecoEnum]] = mapped_field(Origem_enderecoEnum.MANUAL)
    origem_endereco_estrutura: Mapped[Optional[Origem_endereco_estruturaEnum]] = mapped_field(Origem_endereco_estruturaEnum.ESTRUTURA)
    endereco: Mapped[Optional[str]] = mapped_field('')
    latitude: Mapped[Optional[str]] = mapped_field('')
    longitude: Mapped[Optional[str]] = mapped_field('')
    id_wfl_processo: Mapped[Optional[int]] = mapped_field(None)
    id_responsavel_tecnico: Mapped[Optional[int]] = mapped_field(None)
    data_criacao: Mapped[Optional[str]] = mapped_field('')
    data_ultima_alteracao: Mapped[Optional[str]] = mapped_field('')
    prioridade: Mapped[PrioridadeEnum] = mapped_field(PrioridadeEnum.NORMAL)
    data_reservada: Mapped[Optional[str]] = mapped_field('')
    melhor_horario_reserva: Mapped[Optional[Melhor_horario_reservaEnum]] = mapped_field(Melhor_horario_reservaEnum.QUALQUER)
    id_ticket_origem: Mapped[Optional[Id_ticket_origemEnum]] = mapped_field(Id_ticket_origemEnum.INTERNA)
    id_usuarios: Mapped[Optional[int]] = mapped_field(None)
    id_resposta: Mapped[Optional[int]] = mapped_field(None)
    interacao_pendente: Mapped[Optional[Interacao_pendenteEnum]] = mapped_field(Interacao_pendenteEnum.NENHUMA)
    su_status: Mapped[Su_statusEnum] = mapped_field(Su_statusEnum.NOVO)
    id_evento_status_processo: Mapped[Optional[int]] = mapped_field(None)
    id_canal_atendimento: Mapped[Optional[int]] = mapped_field(None)
    status: Mapped[Optional[str]] = mapped_field('')
    mensagens_nao_lida_cli: Mapped[Optional[str]] = mapped_field('')
    mensagens_nao_lida_sup: Mapped[Optional[str]] = mapped_field('')
    token: Mapped[Optional[str]] = mapped_field('')
    finalizar_atendimento: Mapped[Optional[str]] = mapped_field('')
    id_su_diagnostico: Mapped[Optional[int]] = mapped_field(None)
    status_sla: Mapped[Optional[str]] = mapped_field('')
    origem_cadastro: Mapped[Optional[str]] = mapped_field('')
    updated_user: Mapped[Optional[str]] = mapped_field('')
    ultima_atualizacao: Mapped[Optional[str]] = mapped_field('')
    cliente_fone: Mapped[Optional[str]] = mapped_field('')
    cliente_telefone_comercial: Mapped[Optional[str]] = mapped_field('')
    cliente_id_operadora_celular: Mapped[Optional[str]] = mapped_field('')
    cliente_telefone_celular: Mapped[Optional[str]] = mapped_field('')
    cliente_whatsapp: Mapped[Optional[str]] = mapped_field('')
    cliente_ramal: Mapped[Optional[str]] = mapped_field('')
    cliente_email: Mapped[Optional[str]] = mapped_field('')
    cliente_contato: Mapped[Optional[str]] = mapped_field('')
    cliente_website: Mapped[Optional[str]] = mapped_field('')
    cliente_skype: Mapped[Optional[str]] = mapped_field('')
    cliente_facebook: Mapped[Optional[str]] = mapped_field('')
    atualizar_cliente: Mapped[Optional[str]] = mapped_field('')
    latitude_cli: Mapped[Optional[str]] = mapped_field('')
    longitude_cli: Mapped[Optional[str]] = mapped_field('')
    atualizar_login: Mapped[Optional[str]] = mapped_field('')
    latitude_login: Mapped[Optional[str]] = mapped_field('')
    longitude_login: Mapped[Optional[str]] = mapped_field('')

    @property
    def table(self) -> str:
        return "su_ticket"
    
    def _serialize_enum(self, value) -> str:
        """Serializa um valor de enum ou retorna string vazia se None"""
        if value is None:
            return ''
        if hasattr(value, 'value'):
            return str(value.value)
        return str(value)  
    
    def to_dict(self) -> dict:
        return {
            'id': str(self.id),
            'titulo': self.titulo if self.titulo is not None else '',
            'id_ticket_setor': str(self.id_ticket_setor) if self.id_ticket_setor is not None else '',
            'menssagem': self.menssagem if self.menssagem is not None else '',
            'tipo': self._serialize_enum(self.tipo) if self.tipo is not None else '',
            'id_estrutura': str(self.id_estrutura) if self.id_estrutura is not None else '',
            'protocolo': self.protocolo if self.protocolo is not None else '',
            'id_circuito': str(self.id_circuito) if self.id_circuito is not None else '',
            'id_cliente': str(self.id_cliente) if self.id_cliente is not None else '',
            'id_login': str(self.id_login) if self.id_login is not None else '',
            'id_contrato': str(self.id_contrato) if self.id_contrato is not None else '',
            'id_filial': str(self.id_filial) if self.id_filial is not None else '',
            'id_assunto': str(self.id_assunto) if self.id_assunto is not None else '',
            'origem_endereco': self._serialize_enum(self.origem_endereco) if self.origem_endereco is not None else '',
            'origem_endereco_estrutura': self._serialize_enum(self.origem_endereco_estrutura) if self.origem_endereco_estrutura is not None else '',
            'endereco': self.endereco if self.endereco is not None else '',
            'latitude': self.latitude if self.latitude is not None else '',
            'longitude': self.longitude if self.longitude is not None else '',
            'id_wfl_processo': str(self.id_wfl_processo) if self.id_wfl_processo is not None else '',
            'id_responsavel_tecnico': str(self.id_responsavel_tecnico) if self.id_responsavel_tecnico is not None else '',
            'data_criacao': self.data_criacao if self.data_criacao is not None else '',
            'data_ultima_alteracao': self.data_ultima_alteracao if self.data_ultima_alteracao is not None else '',
            'prioridade': self._serialize_enum(self.prioridade) if self.prioridade is not None else '',
            'data_reservada': self.data_reservada if self.data_reservada is not None else '',
            'melhor_horario_reserva': self._serialize_enum(self.melhor_horario_reserva) if self.melhor_horario_reserva is not None else '',
            'id_ticket_origem': self._serialize_enum(self.id_ticket_origem) if self.id_ticket_origem is not None else '',
            'id_usuarios': str(self.id_usuarios) if self.id_usuarios is not None else '',
            'id_resposta': str(self.id_resposta) if self.id_resposta is not None else '',
            'interacao_pendente': self._serialize_enum(self.interacao_pendente) if self.interacao_pendente is not None else '',
            'su_status': self._serialize_enum(self.su_status) if self.su_status is not None else '',
            'id_evento_status_processo': str(self.id_evento_status_processo) if self.id_evento_status_processo is not None else '',
            'id_canal_atendimento': str(self.id_canal_atendimento) if self.id_canal_atendimento is not None else '',
            'status': self.status if self.status is not None else '',
            'mensagens_nao_lida_cli': self.mensagens_nao_lida_cli if self.mensagens_nao_lida_cli is not None else '',
            'mensagens_nao_lida_sup': self.mensagens_nao_lida_sup if self.mensagens_nao_lida_sup is not None else '',
            'token': self.token if self.token is not None else '',
            'finalizar_atendimento': self.finalizar_atendimento if self.finalizar_atendimento is not None else '',
            'id_su_diagnostico': str(self.id_su_diagnostico) if self.id_su_diagnostico is not None else '',
            'status_sla': self.status_sla if self.status_sla is not None else '',
            'origem_cadastro': self.origem_cadastro if self.origem_cadastro is not None else '',
            'updated_user': self.updated_user if self.updated_user is not None else '',
            'ultima_atualizacao': self.ultima_atualizacao if self.ultima_atualizacao is not None else '',
            'cliente_fone': self.cliente_fone if self.cliente_fone is not None else '',
            'cliente_telefone_comercial': self.cliente_telefone_comercial if self.cliente_telefone_comercial is not None else '',
            'cliente_id_operadora_celular': self.cliente_id_operadora_celular if self.cliente_id_operadora_celular is not None else '',
            'cliente_telefone_celular': self.cliente_telefone_celular if self.cliente_telefone_celular is not None else '',
            'cliente_whatsapp': self.cliente_whatsapp if self.cliente_whatsapp is not None else '',
            'cliente_ramal': self.cliente_ramal if self.cliente_ramal is not None else '',
            'cliente_email': self.cliente_email if self.cliente_email is not None else '',
            'cliente_contato': self.cliente_contato if self.cliente_contato is not None else '',
            'cliente_website': self.cliente_website if self.cliente_website is not None else '',
            'cliente_skype': self.cliente_skype if self.cliente_skype is not None else '',
            'cliente_facebook': self.cliente_facebook if self.cliente_facebook is not None else '',
            'atualizar_cliente': self.atualizar_cliente if self.atualizar_cliente is not None else '',
            'latitude_cli': self.latitude_cli if self.latitude_cli is not None else '',
            'longitude_cli': self.longitude_cli if self.longitude_cli is not None else '',
            'atualizar_login': self.atualizar_login if self.atualizar_login is not None else '',
            'latitude_login': self.latitude_login if self.latitude_login is not None else '',
            'longitude_login': self.longitude_login if self.longitude_login is not None else '',
        }

    def is_valid(self) -> bool:
        return self.id is not None and self.titulo is not None and self.id_ticket_setor is not None and self.menssagem is not None

    def __repr__(self) -> str:
        return f"Atendimento(id={self.id!r}, titulo={self.titulo!r}, id_ticket_setor={self.id_ticket_setor!r}, menssagem={self.menssagem!r})"
