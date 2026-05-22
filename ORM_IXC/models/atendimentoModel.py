from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from ORM_IXC.enums.atendimento import *

from ORM_IXC.interfaces import IModel, IModelWithId

@dataclass(kw_only=True)
class AtendimentoModel(IModelWithId):
    id_autoincrement: int
    titulo: str
    id_ticket_setor: int
    menssagem: str
    tipo: TipoEnum = TipoEnum.CLIENTE
    id_estrutura: Optional[int] = None
    protocolo: Optional[str] = ''
    id_circuito: Optional[int] = None
    id_cliente: Optional[int] = None
    id_login: Optional[int] = None
    id_contrato: Optional[int] = None
    id_filial: Optional[int] = None
    id_assunto: Optional[int] = None
    origem_endereco: Optional[Origem_enderecoEnum] = Origem_enderecoEnum.MANUAL
    origem_endereco_estrutura: Optional[Origem_endereco_estruturaEnum] = Origem_endereco_estruturaEnum.ESTRUTURA
    endereco: Optional[str] = ''
    latitude: Optional[str] = ''
    longitude: Optional[str] = ''
    id_wfl_processo: Optional[int] = None
    id_responsavel_tecnico: Optional[int] = None
    data_criacao: Optional[str] = ''
    data_ultima_alteracao: Optional[str] = ''
    prioridade: PrioridadeEnum = PrioridadeEnum.NORMAL
    data_reservada: Optional[str] = ''
    melhor_horario_reserva: Optional[Melhor_horario_reservaEnum] = Melhor_horario_reservaEnum.QUALQUER
    id_ticket_origem: Optional[Id_ticket_origemEnum] = Id_ticket_origemEnum.INTERNA
    id_usuarios: Optional[int] = None
    id_resposta: Optional[int] = None
    interacao_pendente: Optional[Interacao_pendenteEnum] = Interacao_pendenteEnum.NENHUMA
    su_status: Su_statusEnum = Su_statusEnum.NOVO
    id_evento_status_processo: Optional[int] = None
    id_canal_atendimento: Optional[int] = None
    status: Optional[str] = ''
    mensagens_nao_lida_cli: Optional[str] = ''
    mensagens_nao_lida_sup: Optional[str] = ''
    token: Optional[str] = ''
    finalizar_atendimento: Optional[str] = ''
    id_su_diagnostico: Optional[int] = None
    status_sla: Optional[str] = ''
    origem_cadastro: Optional[str] = ''
    updated_user: Optional[str] = ''
    ultima_atualizacao: Optional[str] = ''
    cliente_fone: Optional[str] = ''
    cliente_telefone_comercial: Optional[str] = ''
    cliente_id_operadora_celular: Optional[str] = ''
    cliente_telefone_celular: Optional[str] = ''
    cliente_whatsapp: Optional[str] = ''
    cliente_ramal: Optional[str] = ''
    cliente_email: Optional[str] = ''
    cliente_contato: Optional[str] = ''
    cliente_website: Optional[str] = ''
    cliente_skype: Optional[str] = ''
    cliente_facebook: Optional[str] = ''
    atualizar_cliente: Optional[str] = ''
    latitude_cli: Optional[str] = ''
    longitude_cli: Optional[str] = ''
    atualizar_login: Optional[str] = ''
    latitude_login: Optional[str] = ''
    longitude_login: Optional[str] = ''
    
    @property
    def id(self) -> str:
        return str(self.id_autoincrement)

    @property
    def table(self) -> str:
        return "su_ticket"
    def to_dict(self) -> dict:
        return {
            'id_autoincrement': str(self.id_autoincrement),
            'titulo': self.titulo if self.titulo is not None else '',
            'id_ticket_setor': str(self.id_ticket_setor) if self.id_ticket_setor is not None else '',
            'menssagem': self.menssagem if self.menssagem is not None else '',
            'tipo': self.tipo.value if self.tipo is not None else '',
            'id_estrutura': str(self.id_estrutura) if self.id_estrutura is not None else '',
            'protocolo': self.protocolo if self.protocolo is not None else '',
            'id_circuito': str(self.id_circuito) if self.id_circuito is not None else '',
            'id_cliente': str(self.id_cliente) if self.id_cliente is not None else '',
            'id_login': str(self.id_login) if self.id_login is not None else '',
            'id_contrato': str(self.id_contrato) if self.id_contrato is not None else '',
            'id_filial': str(self.id_filial) if self.id_filial is not None else '',
            'id_assunto': str(self.id_assunto) if self.id_assunto is not None else '',
            'origem_endereco': self.origem_endereco.value if self.origem_endereco is not None else '',
            'origem_endereco_estrutura': self.origem_endereco_estrutura.value if self.origem_endereco_estrutura is not None else '',
            'endereco': self.endereco if self.endereco is not None else '',
            'latitude': self.latitude if self.latitude is not None else '',
            'longitude': self.longitude if self.longitude is not None else '',
            'id_wfl_processo': str(self.id_wfl_processo) if self.id_wfl_processo is not None else '',
            'id_responsavel_tecnico': str(self.id_responsavel_tecnico) if self.id_responsavel_tecnico is not None else '',
            'data_criacao': self.data_criacao if self.data_criacao is not None else '',
            'data_ultima_alteracao': self.data_ultima_alteracao if self.data_ultima_alteracao is not None else '',
            'prioridade': self.prioridade.value if self.prioridade is not None else '',
            'data_reservada': self.data_reservada if self.data_reservada is not None else '',
            'melhor_horario_reserva': self.melhor_horario_reserva.value if self.melhor_horario_reserva is not None else '',
            'id_ticket_origem': self.id_ticket_origem.value if self.id_ticket_origem is not None else '',
            'id_usuarios': str(self.id_usuarios) if self.id_usuarios is not None else '',
            'id_resposta': str(self.id_resposta) if self.id_resposta is not None else '',
            'interacao_pendente': self.interacao_pendente.value if self.interacao_pendente is not None else '',
            'su_status': self.su_status.value if self.su_status is not None else '',
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
        return self.id_autoincrement is not None and self.titulo is not None and self.id_ticket_setor is not None and self.menssagem is not None

    def __repr__(self) -> str:
        return f"Atendimento(id_autoincrement={self.id_autoincrement!r}, titulo={self.titulo!r}, id_ticket_setor={self.id_ticket_setor!r}, menssagem={self.menssagem!r})"

    #------------------------------ CONVERSOR DTO ------------------------------#
    def dto_convert(self, data: dict[str, str]) -> IModel:
        return AtendimentoModel(
            id_autoincrement=int(data.get('id_autoincrement', 0)),
            titulo=data.get('titulo', ''),
            id_ticket_setor=int(data['id_ticket_setor']),
            menssagem=data.get('menssagem', ''),
            tipo=TipoEnum(data['tipo']),
            id_estrutura=int(data['id_estrutura']) if data.get('id_estrutura') else None,
            protocolo=data.get('protocolo', ''),
            id_circuito=int(data['id_circuito']) if data.get('id_circuito') else None,
            id_cliente=int(data['id_cliente']) if data.get('id_cliente') else None,
            id_login=int(data['id_login']) if data.get('id_login') else None,
            id_contrato=int(data['id_contrato']) if data.get('id_contrato') else None,
            id_filial=int(data['id_filial']) if data.get('id_filial') else None,
            id_assunto=int(data['id_assunto']) if data.get('id_assunto') else None,
            origem_endereco=Origem_enderecoEnum(data['origem_endereco']) if data.get('origem_endereco') else None,
            origem_endereco_estrutura=Origem_endereco_estruturaEnum(data['origem_endereco_estrutura']) if data.get('origem_endereco_estrutura') else None,
            endereco=data.get('endereco', ''),
            latitude=data.get('latitude', ''),
            longitude=data.get('longitude', ''),
            id_wfl_processo=int(data['id_wfl_processo']) if data.get('id_wfl_processo') else None,
            id_responsavel_tecnico=int(data['id_responsavel_tecnico']) if data.get('id_responsavel_tecnico') else None,
            data_criacao=data.get('data_criacao', ''),
            data_ultima_alteracao=data.get('data_ultima_alteracao', ''),
            prioridade=PrioridadeEnum(data['prioridade']),
            data_reservada=data.get('data_reservada', ''),
            melhor_horario_reserva=Melhor_horario_reservaEnum(data['melhor_horario_reserva']) if data.get('melhor_horario_reserva') else None,
            id_ticket_origem=Id_ticket_origemEnum(data['id_ticket_origem']) if data.get('id_ticket_origem') else None,
            id_usuarios=int(data['id_usuarios']) if data.get('id_usuarios') else None,
            id_resposta=int(data['id_resposta']) if data.get('id_resposta') else None,
            interacao_pendente=Interacao_pendenteEnum(data['interacao_pendente']) if data.get('interacao_pendente') else None,
            su_status=Su_statusEnum(data['su_status']),
            id_evento_status_processo=int(data['id_evento_status_processo']) if data.get('id_evento_status_processo') else None,
            id_canal_atendimento=int(data['id_canal_atendimento']) if data.get('id_canal_atendimento') else None,
            status=data.get('status', ''),
            mensagens_nao_lida_cli=data.get('mensagens_nao_lida_cli', ''),
            mensagens_nao_lida_sup=data.get('mensagens_nao_lida_sup', ''),
            token=data.get('token', ''),
            finalizar_atendimento=data.get('finalizar_atendimento', ''),
            id_su_diagnostico=int(data['id_su_diagnostico']) if data.get('id_su_diagnostico') else None,
            status_sla=data.get('status_sla', ''),
            origem_cadastro=data.get('origem_cadastro', ''),
            updated_user=data.get('updated_user', ''),
            ultima_atualizacao=data.get('ultima_atualizacao', ''),
            cliente_fone=data.get('cliente_fone', ''),
            cliente_telefone_comercial=data.get('cliente_telefone_comercial', ''),
            cliente_id_operadora_celular=data.get('cliente_id_operadora_celular', ''),
            cliente_telefone_celular=data.get('cliente_telefone_celular', ''),
            cliente_whatsapp=data.get('cliente_whatsapp', ''),
            cliente_ramal=data.get('cliente_ramal', ''),
            cliente_email=data.get('cliente_email', ''),
            cliente_contato=data.get('cliente_contato', ''),
            cliente_website=data.get('cliente_website', ''),
            cliente_skype=data.get('cliente_skype', ''),
            cliente_facebook=data.get('cliente_facebook', ''),
            atualizar_cliente=data.get('atualizar_cliente', ''),
            latitude_cli=data.get('latitude_cli', ''),
            longitude_cli=data.get('longitude_cli', ''),
            atualizar_login=data.get('atualizar_login', ''),
            latitude_login=data.get('latitude_login', ''),
            longitude_login=data.get('longitude_login', ''),
        )
