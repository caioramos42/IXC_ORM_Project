# from dataclasses import dataclass
# from ORM_IXC.enums.serviceOrder import *

# @dataclass
# class ServiceOrderModel:
# 	id_autoincrement: int
# 	protocolo: str = ''
# 	id_assunto: int
# 	dica_assinatura_digital: str = ''
# 	id_cliente: int | None
# 	id_estrutura: int | None
# 	id_filial: int
# 	id_login: int | None
# 	id_contrato_kit: int | None
# 	origem_endereco: Origem_enderecoEnum = Origem_enderecoEnum.MANUAL
# 	origem_endereco_estrutura: Origem_endereco_estruturaEnum | None = Origem_endereco_estruturaEnum.ESTRUTURA
# 	latitude: str = ''
# 	longitude: str = ''
# 	status_conexao: Status_conexaoEnum | None
# 	prioridade: PrioridadeEnum = PrioridadeEnum.NORMAL
# 	melhor_horario_agenda: Melhor_horario_agendaEnum | None = Melhor_horario_agendaEnum.QUALQUER
# 	setor: int
# 	id_tecnico: int | None
# 	mensagem: str = ''
# 	id_receber: str = ''
# 	idx: str = ''
# 	status_pesquisa_satisfacao: Status_pesquisa_satisfacaoEnum | None
# 	status: StatusEnum = StatusEnum.ABERTA
# 	habilita_assinatura_cliente: str = ''
# 	status_assinatura: Status_assinaturaEnum | None = Status_assinaturaEnum.PENDENTE
# 	gera_comissao: Gera_comissaoEnum | None = Gera_comissaoEnum.SIM
# 	liberado: LiberadoEnum | None = LiberadoEnum.SIM
# 	id_atendente: str
# 	impresso: ImpressoEnum | None = ImpressoEnum.NAO
# 	preview: str = ''
# 	id_wfl_param_os: str = ''
# 	id_wfl_tarefa: str = ''
# 	id_su_diagnostico: int | None
# 	regiao_manutencao: str = ''
# 	origem_cadastro: Origem_cadastroEnum | None = Origem_cadastroEnum.P
# 	origem_change_endereco: str = ''
# 	status_sla: str = ''
# 	ultima_atualizacao: str = ''
# 	ids_login_regiao_manutencao: str = ''
# 	origem_os_aberta: Origem_os_abertaEnum | None
# 	id_cidade: int | None
# 	bairro: str = ''
# 	endereco: str = ''
# 	complemento: str = ''
# 	referencia: str = ''
# 	id_condominio: int | None
# 	bloco: str = ''
# 	apartamento: str = ''
# 	data_abertura: str = ''
# 	data_inicio: str = ''
# 	data_hora_analise: str = ''
# 	data_agenda: str = ''
# 	data_agenda_final: str = ''
# 	data_hora_encaminhado: str = ''
# 	data_hora_assumido: str = ''
# 	data_hora_execucao: str = ''
# 	data_final: str = ''
# 	data_fechamento: str = ''
# 	data_prazo_limite: str = ''
# 	data_reservada: str = ''
# 	data_reagendar: str = ''
# 	data_prev_final: str = ''
# 	mensagem_resposta: str = ''
# 	justificativa_sla_atrasado: str = ''
# 	valor_total: str = ''
# 	valor_outras_despesas: str = ''
# 	valor_unit_comissao: str = ''
# 	valor_total_comissao: str = ''
 
# 	def to_dict(self):
#  		return{
# 			'id_autoincrement': str(self.id_autoincrement),
# 			'tipo': self.tipo.value if self.tipo is not None else '',
# 			'id_ticket': str(self.id_ticket) if self.id_ticket is not None else '',
# 			'protocolo': self.protocolo,
# 			'id_assunto': str(self.id_assunto) if self.id_assunto is not None else '',
# 			'dica_assinatura_digital': self.dica_assinatura_digital,
# 			'id_cliente': str(self.id_cliente) if self.id_cliente is not None else '',
# 			'id_estrutura': str(self.id_estrutura) if self.id_estrutura is not None else '',
# 			'id_filial': str(self.id_filial) if self.id_filial is not None else '',
# 			'id_login': str(self.id_login) if self.id_login is not None else '',
# 			'id_contrato_kit': str(self.id_contrato_kit) if self.id_contrato_kit is not None else '',
# 			'origem_endereco': self.origem_endereco.value if self.origem_endereco is not None else '',
# 			'origem_endereco_estrutura': self.origem_endereco_estrutura.value if self.origem_endereco_estrutura is not None else '',
# 			'latitude': self.latitude,
# 			'longitude': self.longitude,
# 			'status_conexao': self.status_conexao.value if self.status_conexao is not None else '',
# 			'prioridade': self.prioridade.value if self.prioridade is not None else '',
# 			'melhor_horario_agenda': self.melhor_horario_agenda.value if self.melhor_horario_agenda is not None else '',
# 			'setor': str(self.setor) if self.setor is not None else '',
# 			'id_tecnico': str(self.id_tecnico) if self.id_tecnico is not None else '',
# 			'mensagem': self.mensagem,
# 			'id_receber': self.id_receber,
# 			'idx': self.idx,
# 			'status_pesquisa_satisfacao': self.status_pesquisa_satisfacao.value if self.status_pesquisa_satisfacao is not None else '',
# 			'status': self.status.value if self.status is not None else '',
# 			'habilita_assinatura_cliente': self.habilita_assinatura_cliente,
# 			'status_assinatura': self.status_assinatura.value if self.status_assinatura is not None else '',
# 			'gera_comissao': self.gera_comissao.value if self.gera_comissao is not None else '',
# 			'liberado': self.liberado.value if self.liberado is not None else '',
# 			'id_atendente': self.id_atendente,
# 			'impresso': self.impresso.value if self.impresso is not None else '',
# 			'preview': self.preview,
# 			'id_wfl_param_os': self.id_wfl_param_os,
# 			'id_wfl_tarefa': self.id_wfl_tarefa,
# 			'id_su_diagnostico': str(self.id_su_diagnostico) if self.id_su_diagnostico is not None else '',
# 			'regiao_manutencao': self.regiao_manutencao,
# 			'origem_cadastro': self.origem_cadastro.value if self.origem_cadastro is not None else '',
# 			'origem_change_endereco': self.origem_change_endereco,
# 			'status_sla': self.status_sla,
# 			'ultima_atualizacao': self.ultima_atualizacao,
# 			'ids_login_regiao_manutencao': self.ids_login_regiao_manutencao,
# 			'origem_os_aberta': self.origem_os_aberta.value if self.origem_os_aberta is not None else '',
# 			'id_cidade': str(self.id_cidade) if self.id_cidade is not None else '',
# 			'bairro': self.bairro,
# 			'endereco': self.endereco,
# 			'complemento': self.complemento,
# 			'referencia': self.referencia,
# 			'id_condominio': str(self.id_condominio) if self.id_condominio is not None else '',
# 			'bloco': self.bloco,
# 			'apartamento': self.apartamento,
# 			'data_abertura': self.data_abertura,
# 			'data_inicio': self.data_inicio,
# 			'data_hora_analise': self.data_hora_analise,
# 			'data_agenda': self.data_agenda,
# 			'data_agenda_final': self.data_agenda_final,
# 			'data_hora_encaminhado': self.data_hora_encaminhado,
# 			'data_hora_assumido': self.data_hora_assumido,
# 			'data_hora_execucao': self.data_hora_execucao,
# 			'data_final': self.data_final,
# 			'data_fechamento': self.data_fechamento,
# 			'data_prazo_limite': self.data_prazo_limite,
# 			'data_reservada': self.data_reservada,
# 			'data_reagendar': self.data_reagendar,
# 			'data_prev_final': self.data_prev_final,
# 			'mensagem_resposta': self.mensagem_resposta,
# 			'justificativa_sla_atrasado': self.justificativa_sla_atrasado,
# 			'valor_total': self.valor_total,
# 			'valor_outras_despesas': self.valor_outras_despesas,
# 			'valor_unit_comissao': self.valor_unit_comissao,
# 			'valor_total_comissao': self.valor_total_comissao,
# 		}
# def dtoConvert(data: dict) -> ServiceOrderModel:
# 	return ServiceOrderModel(
# 		id_autoincrement=int(data.get('id_autoincrement', 0)),
# 		tipo=TipoEnum(data.get('tipo')) if data.get('tipo') else None,
# 		id_ticket=int(data.get('id_ticket')) if data.get('id_ticket') else None,
# 		protocolo=data.get('protocolo', ''),
# 		id_assunto=int(data.get('id_assunto')) if data.get('id_assunto') else None,
# 		dica_assinatura_digital=data.get('dica_assinatura_digital', ''),
# 		id_cliente=int(data.get('id_cliente')) if data.get('id_cliente') else None,
# 		id_estrutura=int(data.get('id_estrutura')) if data.get('id_estrutura') else None,
# 		id_filial=int(data.get('id_filial')) if data.get('id_filial') else None,
# 		id_login=int(data.get('id_login')) if data.get('id_login') else None,
# 		id_contrato_kit=int(data.get('id_contrato_kit')) if data.get('id_contrato_kit') else None,
# 		origem_endereco=Origem_enderecoEnum(data.get('origem_endereco')) if data.get('origem_endereco') else None,
# 		origem_endereco_estrutura=Origem_endereco_estruturaEnum(data.get('origem_endereco_estrutura')) if data.get('origem_endereco_estrutura') else None,
# 		latitude=data.get('latitude', ''),
# 		longitude=data.get('longitude', ''),
# 		status_conexao=Status_conexaoEnum(data.get('status_conexao')) if data.get('status_conexao') else None,
# 		prioridade=PrioridadeEnum(data.get('prioridade')) if data.get('prioridade') else None,
# 		melhor_horario_agenda=Melhor_horario_agendaEnum(data.get('melhor_horario_agenda')) if data.get('melhor_horario_agenda') else None,
# 		setor=int(data.get('setor')) if data.get('setor') else None,
# 		id_tecnico=int(data.get('id_tecnico')) if data.get('id_tecnico') else None,
# 		mensagem=data.get('mensagem', ''),
# 		id_receber=data.get('id_receber', ''),
# 		idx=data.get('idx', ''),
# 		status_pesquisa_satisfacao=Status_pesquisa_satisfacaoEnum(data.get('status_pesquisa_satisfacao')) if data.get('status_pesquisa_satisfacao') else None,
# 		status=StatusEnum(data.get('status')) if data.get('status') else None,
# 		habilita_assinatura_cliente=data.get('habilita_assinatura_cliente', ''),
# 		status_assinatura=Status_assinaturaEnum(data.get('status_assinatura')) if data.get('status_assinatura') else None,
# 		gera_comissao=Gera_comissaoEnum(data.get('gera_comissao')) if data.get('gera_comissao') else None,
# 		liberado=LiberadoEnum(data.get('liberado')) if data.get('liberado') else None,
# 		id_atendente=data.get('id_atendente', ''),
# 		impresso=ImpressoEnum(data.get('impresso')) if data.get('impresso') else None,
# 		preview=data.get('preview', ''),
# 		id_wfl_param_os=data.get('id_wfl_param_os', ''),
# 		id_wfl_tarefa=data.get('id_wfl_tarefa', ''),
# 		id_su_diagnostico=int(data.get('id_su_diagnostico')) if data.get('id_su_diagnostico') else None,
# 		regiao_manutencao=data.get('regiao_manutencao', ''),
# 		origem_cadastro=Origem_cadastroEnum(data.get('origem_cadastro')) if data.get('origem_cadastro') else None,
# 		origem_change_endereco=data.get('origem_change_endereco', ''),
# 		status_sla=data.get('status_sla', ''),
# 		ultima_atualizacao=data.get('ultima_atualizacao', ''),
# 		ids_login_regiao_manutencao=data.get('ids_login_regiao_manutencao', ''),
# 		origem_os_aberta=Origem_os_abertaEnum(data.get('origem_os_aberta')) if data.get('origem_os_aberta') else None,
# 		id_cidade=int(data.get('id_cidade')) if data.get('id_cidade') else None,
# 		bairro=data.get('bairro', ''),
# 		endereco=data.get('endereco', ''),
# 		complemento=data.get('complemento', ''),
# 		referencia=data.get('referencia', ''),
# 		id_condominio=int(data.get('id_condominio')) if data.get('id_condominio') else None,
# 		bloco=data.get('bloco', ''),
# 		apartamento=data.get('apartamento', ''),
# 		data_abertura=data.get('data_abertura', ''),
# 		data_inicio=data.get('data_inicio', ''),
# 		data_hora_analise=data.get('data_hora_analise', ''),
# 		data_agenda=data.get('data_agenda', ''),
# 		data_agenda_final=data.get('data_agenda_final', ''),
# 		data_hora_encaminhado=data.get('data_hora_encaminhado', ''),
# 		data_hora_assumido=data.get('data_hora_assumido', ''),
# 		data_hora_execucao=data.get('data_hora_execucao', ''),
# 		data_final=data.get('data_final', ''),
# 		data_fechamento=data.get('data_fechamento', ''),
# 		data_prazo_limite=data.get('data_prazo_limite', ''),
# 		data_reservada=data.get('data_reservada', ''),
# 		data_reagendar=data.get('data_reagendar', ''),
# 		data_prev_final=data.get('data_prev_final', ''),
# 		mensagem_resposta=data.get('mensagem_resposta', ''),
# 		justificativa_sla_atrasado=data.get('justificativa_sla_atrasado', ''),
# 		valor_total=data.get('valor_total', ''),
# 		valor_outras_despesas=data.get('valor_outras_despesas', ''),
# 		valor_unit_comissao=data.get('valor_unit_comissao', ''),
# 		valor_total_comissao=data.get('valor_total_comissao', '')
# 	)

