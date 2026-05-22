from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from ORM_IXC.interfaces.IModel import IModel, IModelWithId
from ORM_IXC.enums.serviceOrder import *

@dataclass(kw_only=True)
class ServiceOrderModel(IModelWithId):
    id_autoincrement: int
    id_assunto: int
    id_filial: int
    setor: int
    id_atendente: str
    tipo: Optional[TipoEnum] = TipoEnum.CLIENTE
    id_ticket: Optional[int] = None
    protocolo: Optional[str] = ''
    dica_assinatura_digital: Optional[str] = ''
    id_cliente: Optional[int] = None
    id_estrutura: Optional[int] = None
    id_login: Optional[int] = None
    id_contrato_kit: Optional[int] = None
    origem_endereco: Origem_enderecoEnum = Origem_enderecoEnum.MANUAL
    origem_endereco_estrutura: Optional[Origem_endereco_estruturaEnum] = Origem_endereco_estruturaEnum.ESTRUTURA
    latitude: Optional[str] = ''
    longitude: Optional[str] = ''
    status_conexao: Optional[Status_conexaoEnum] = None
    prioridade: PrioridadeEnum = PrioridadeEnum.NORMAL
    melhor_horario_agenda: Optional[Melhor_horario_agendaEnum] = Melhor_horario_agendaEnum.QUALQUER
    id_tecnico: Optional[int] = None
    mensagem: Optional[str] = ''
    id_receber: Optional[str] = ''
    idx: Optional[str] = ''
    status_pesquisa_satisfacao: Optional[Status_pesquisa_satisfacaoEnum] = None
    status: StatusEnum = StatusEnum.ABERTA
    habilita_assinatura_cliente: Optional[str] = ''
    status_assinatura: Optional[Status_assinaturaEnum] = Status_assinaturaEnum.PENDENTE
    gera_comissao: Optional[Gera_comissaoEnum] = Gera_comissaoEnum.SIM
    liberado: Optional[LiberadoEnum] = LiberadoEnum.SIM
    impresso: Optional[ImpressoEnum] = ImpressoEnum.NAO
    preview: Optional[str] = ''
    id_wfl_param_os: Optional[str] = ''
    id_wfl_tarefa: Optional[str] = ''
    id_su_diagnostico: Optional[int] = None
    regiao_manutencao: Optional[str] = ''
    origem_cadastro: Optional[Origem_cadastroEnum] = Origem_cadastroEnum.P
    origem_change_endereco: Optional[str] = ''
    status_sla: Optional[str] = ''
    ultima_atualizacao: Optional[str] = ''
    ids_login_regiao_manutencao: Optional[str] = ''
    origem_os_aberta: Optional[Origem_os_abertaEnum] = None
    id_cidade: Optional[int] = None
    bairro: Optional[str] = ''
    endereco: Optional[str] = ''
    complemento: Optional[str] = ''
    referencia: Optional[str] = ''
    id_condominio: Optional[int] = None
    bloco: Optional[str] = ''
    apartamento: Optional[str] = ''
    data_abertura: Optional[str] = ''
    data_inicio: Optional[str] = ''
    data_hora_analise: Optional[str] = ''
    data_agenda: Optional[str] = ''
    data_agenda_final: Optional[str] = ''
    data_hora_encaminhado: Optional[str] = ''
    data_hora_assumido: Optional[str] = ''
    data_hora_execucao: Optional[str] = ''
    data_final: Optional[str] = ''
    data_fechamento: Optional[str] = ''
    data_prazo_limite: Optional[str] = ''
    data_reservada: Optional[str] = ''
    data_reagendar: Optional[str] = ''
    data_prev_final: Optional[str] = ''
    mensagem_resposta: Optional[str] = ''
    justificativa_sla_atrasado: Optional[str] = ''
    valor_total: Optional[str] = ''
    valor_outras_despesas: Optional[str] = ''
    valor_unit_comissao: Optional[str] = ''
    valor_total_comissao: Optional[str] = ''

    @property
    def id(self) -> str:
        return str(self.id_autoincrement)
  
    @property
    def table(self) -> str:
        return "su_oss_chamado"

    def to_dict(self) -> dict[str, str]:
        return {
            'id_autoincrement': str(self.id_autoincrement),
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

    def is_valid(self) -> bool:
        return self.id_autoincrement is not None and self.id_assunto is not None and self.id_filial is not None and self.setor is not None and self.id_atendente is not None

    #def __repr__(self) -> str:
        #return f"OrdemDeServiço(id_autoincrement={self.id_autoincrement!r}, id_assunto={self.id_assunto!r}, id_filial={self.id_filial!r}, setor={self.setor!r}, id_atendente={self.id_atendente!r})"

#------------------------------ CONVERSOR DTO ------------------------------#
    def dto_convert(self, data: dict[str, str]) -> IModel:
        return ServiceOrderModel(
            id_autoincrement=int(data.get('id_autoincrement', 0)),
            id_assunto=int(data['id_assunto']),
            id_filial=int(data['id_filial']),
            setor=int(data['setor']),
            id_atendente=data.get('id_atendente', ''),
            tipo=TipoEnum(data['tipo']) if data.get('tipo') else None,
            id_ticket=int(data['id_ticket']) if data.get('id_ticket') else None,
            protocolo=data.get('protocolo', ''),
            dica_assinatura_digital=data.get('dica_assinatura_digital', ''),
            id_cliente=int(data['id_cliente']) if data.get('id_cliente') else None,
            id_estrutura=int(data['id_estrutura']) if data.get('id_estrutura') else None,
            id_login=int(data['id_login']) if data.get('id_login') else None,
            id_contrato_kit=int(data['id_contrato_kit']) if data.get('id_contrato_kit') else None,
            origem_endereco=Origem_enderecoEnum(data['origem_endereco']),
            origem_endereco_estrutura=Origem_endereco_estruturaEnum(data['origem_endereco_estrutura']) if data.get('origem_endereco_estrutura') else None,
            latitude=data.get('latitude', ''),
            longitude=data.get('longitude', ''),
            status_conexao=Status_conexaoEnum(data['status_conexao']) if data.get('status_conexao') else None,
            prioridade=PrioridadeEnum(data['prioridade']),
            melhor_horario_agenda=Melhor_horario_agendaEnum(data['melhor_horario_agenda']) if data.get('melhor_horario_agenda') else None,
            id_tecnico=int(data['id_tecnico']) if data.get('id_tecnico') else None,
            mensagem=data.get('mensagem', ''),
            id_receber=data.get('id_receber', ''),
            idx=data.get('idx', ''),
            status_pesquisa_satisfacao=Status_pesquisa_satisfacaoEnum(data['status_pesquisa_satisfacao']) if data.get('status_pesquisa_satisfacao') else None,
            status=StatusEnum(data['status']),
            habilita_assinatura_cliente=data.get('habilita_assinatura_cliente', ''),
            status_assinatura=Status_assinaturaEnum(data['status_assinatura']) if data.get('status_assinatura') else None,
            gera_comissao=Gera_comissaoEnum(data['gera_comissao']) if data.get('gera_comissao') else None,
            liberado=LiberadoEnum(data['liberado']) if data.get('liberado') else None,
            impresso=ImpressoEnum(data['impresso']) if data.get('impresso') else None,
            preview=data.get('preview', ''),
            id_wfl_param_os=data.get('id_wfl_param_os', ''),
            id_wfl_tarefa=data.get('id_wfl_tarefa', ''),
            id_su_diagnostico=int(data['id_su_diagnostico']) if data.get('id_su_diagnostico') else None,
            regiao_manutencao=data.get('regiao_manutencao', ''),
            origem_cadastro=Origem_cadastroEnum(data['origem_cadastro']) if data.get('origem_cadastro') else None,
            origem_change_endereco=data.get('origem_change_endereco', ''),
            status_sla=data.get('status_sla', ''),
            ultima_atualizacao=data.get('ultima_atualizacao', ''),
            ids_login_regiao_manutencao=data.get('ids_login_regiao_manutencao', ''),
            origem_os_aberta=Origem_os_abertaEnum(data['origem_os_aberta']) if data.get('origem_os_aberta') else None,
            id_cidade=int(data['id_cidade']) if data.get('id_cidade') else None,
            bairro=data.get('bairro', ''),
            endereco=data.get('endereco', ''),
            complemento=data.get('complemento', ''),
            referencia=data.get('referencia', ''),
            id_condominio=int(data['id_condominio']) if data.get('id_condominio') else None,
            bloco=data.get('bloco', ''),
            apartamento=data.get('apartamento', ''),
            data_abertura=data.get('data_abertura', ''),
            data_inicio=data.get('data_inicio', ''),
            data_hora_analise=data.get('data_hora_analise', ''),
            data_agenda=data.get('data_agenda', ''),
            data_agenda_final=data.get('data_agenda_final', ''),
            data_hora_encaminhado=data.get('data_hora_encaminhado', ''),
            data_hora_assumido=data.get('data_hora_assumido', ''),
            data_hora_execucao=data.get('data_hora_execucao', ''),
            data_final=data.get('data_final', ''),
            data_fechamento=data.get('data_fechamento', ''),
            data_prazo_limite=data.get('data_prazo_limite', ''),
            data_reservada=data.get('data_reservada', ''),
            data_reagendar=data.get('data_reagendar', ''),
            data_prev_final=data.get('data_prev_final', ''),
            mensagem_resposta=data.get('mensagem_resposta', ''),
            justificativa_sla_atrasado=data.get('justificativa_sla_atrasado', ''),
            valor_total=data.get('valor_total', ''),
            valor_outras_despesas=data.get('valor_outras_despesas', ''),
            valor_unit_comissao=data.get('valor_unit_comissao', ''),
            valor_total_comissao=data.get('valor_total_comissao', ''),
        )
