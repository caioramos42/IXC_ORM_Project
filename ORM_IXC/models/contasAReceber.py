from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from ORM_IXC.enums.contasAReceber import *
from ORM_IXC.interfaces import IModel, IModelWithId

@dataclass(kw_only=True)
class ContasAReceberModel(IModelWithId):
    id_autoincrement: int
    id_cliente: int
    id_conta: int
    filial_id: int
    data_emissao: str
    data_vencimento: str
    valor: str
    tipo_recebimento: Tipo_recebimentoEnum
    id_conta_class_finan_a: Optional[int] = None
    agencia_sequencial: Optional[str] = ''
    documento: Optional[str] = ''
    previsao: PrevisaoEnum = PrevisaoEnum.COMPETENCIA_
    id_carteira_cobranca: Optional[int] = None
    obs: Optional[str] = ''
    data_inicial: Optional[str] = ''
    data_final: Optional[str] = ''
    status: Optional[StatusEnum] = StatusEnum.A_RECEBER
    id_saida: Optional[str] = ''
    liberado: Optional[str] = ''
    nn_boleto: Optional[str] = ''
    gateway_link: Optional[str] = ''
    gerencianet_token: Optional[str] = ''
    tipo_conta: Optional[str] = ''
    id_cobranca: Optional[str] = ''
    status_cobranca: Optional[str] = ''
    id_nota_gerada: Optional[str] = ''
    id_im_imovel: Optional[str] = ''
    impresso: Optional[ImpressoEnum] = ImpressoEnum.NAO
    arquivo_remessa_baixado: Optional[Arquivo_remessa_baixadoEnum] = None
    duplicata: Optional[str] = ''
    id_sip: Optional[str] = ''
    tipo_renegociacao: Optional[str] = ''
    id_renegociacao: Optional[str] = ''
    id_renegociacao_novo: Optional[str] = ''
    boleto: Optional[str] = ''
    forma_recebimento: Optional[Forma_recebimentoEnum] = Forma_recebimentoEnum.RECEBIDO_DE_FORMA_MANUAL
    credito_data: Optional[str] = ''
    baixa_data: Optional[str] = ''
    baixa_id_operador: Optional[str] = ''
    cancelamento_id_operador: Optional[str] = ''
    numero_parcela_recorrente: Optional[str] = ''
    nparcela: Optional[str] = ''
    id_contrato_principal: Optional[str] = ''
    previsao_conta_receita: Optional[str] = ''
    tipo_cobranca: Optional[Tipo_cobrancaEnum] = None
    parcela_proporcional: Optional[str] = ''
    tipo_pagamento_cartao: Optional[str] = ''
    titulo_protestado: Optional[Titulo_protestadoEnum] = Titulo_protestadoEnum.NAO
    desconto_condicional_valor: Optional[str] = ''
    validade_desconto_condicional: Optional[str] = ''
    id_nota_gerada_opc2: Optional[str] = ''
    id_nota_gerada_opc3: Optional[str] = ''
    id_nota_gerada_opc4: Optional[str] = ''
    id_lote_geracao_financeiro_fatura: Optional[str] = ''
    titulo_renegociado: Optional[Titulo_renegociadoEnum] = None
    id_cobranca_regua: Optional[str] = ''
    id_lote_cobranca_regua: Optional[str] = ''
    etapa_envio_regua: Optional[Etapa_envio_reguaEnum] = None
    status_cobranca_regua: Optional[Status_cobranca_reguaEnum] = None
    ids_contratos_origem: Optional[str] = ''
    em_cobranca: Optional[Em_cobrancaEnum] = None
    valor_aberto: Optional[str] = ''
    valor_recebido: Optional[str] = ''
    pagamento_valor: Optional[str] = ''
    valor_juros: Optional[str] = ''
    valor_multas: Optional[str] = ''
    pagamento_data: Optional[str] = ''
    valor_cancelado: Optional[str] = ''
    data_cancelamento: Optional[str] = ''
    origem_importacao: Optional[str] = ''
    titulo_importado: Optional[Titulo_importadoEnum] = Titulo_importadoEnum.NAO
    aguardando_confirmacao_pagamento: Optional[Aguardando_confirmacao_pagamentoEnum] = Aguardando_confirmacao_pagamentoEnum.NAO
    parcelado_cartao: Optional[Parcelado_cartaoEnum] = Parcelado_cartaoEnum.NAO
    bandeira_pagamento: Optional[str] = ''
    recebido_via_pix: Optional[Recebido_via_pixEnum] = Recebido_via_pixEnum.NAO
    recebido_por_recorrencia: Optional[Recebido_por_recorrenciaEnum] = Recebido_por_recorrenciaEnum.NAO
    estornado: Optional[EstornadoEnum] = None
    conta_recebimento: Optional[int] = None
    id_remessa: Optional[str] = ''
    linha_digitavel: Optional[str] = ''
    id_remessa_alteracao: Optional[str] = ''
    motivo_alteracao: Optional[Motivo_alteracaoEnum] = None
    pix_txid: Optional[str] = ''
    tipo_cobranca_pix: Optional[Tipo_cobranca_pixEnum] = None
    pix_txid_recorrente: Optional[str] = ''
    pix_status_recorrente: Optional[Pix_status_recorrenteEnum] = None
    tentativa_pix_recorrente: Optional[str] = ''
    data_prevista_tentativa_pix_recorrente: Optional[str] = ''
    libera_periodo: Optional[Libera_periodoEnum] = Libera_periodoEnum.NAO
    id_mot_cancelamento: Optional[int] = None
    id_contrato: Optional[int] = None
    id_contrato_avulso: Optional[int] = None
    ultima_atualizacao: Optional[str] = ''
    botoes_classe_finan: Optional[str] = ''
    id_conta_class_finan: Optional[int] = None
    valor_class_finan: Optional[str] = ''
    grid_classe_finan: Optional[str] = ''
    json_class_finan: Optional[str] = ''
    id_nf_gerada: Optional[int] = None
    id_nf_opcional2: Optional[int] = None
    id_nf_opcional3: Optional[int] = None
    id_nf_opcional4: Optional[int] = None
    
    @property
    def id(self) -> str:
        return str(self.id_autoincrement)

    @property
    def table(self) -> str:
        return "fn_areceber"
    
    def to_dict(self) -> dict:
        return {
            'id_autoincrement': str(self.id_autoincrement),
            'id_cliente': str(self.id_cliente) if self.id_cliente is not None else '',
            'id_conta': str(self.id_conta) if self.id_conta is not None else '',
            'filial_id': str(self.filial_id) if self.filial_id is not None else '',
            'data_emissao': self.data_emissao if self.data_emissao is not None else '',
            'data_vencimento': self.data_vencimento if self.data_vencimento is not None else '',
            'valor': self.valor if self.valor is not None else '',
            'tipo_recebimento': self.tipo_recebimento.value if self.tipo_recebimento is not None else '',
            'id_conta_class_finan_a': str(self.id_conta_class_finan_a) if self.id_conta_class_finan_a is not None else '',
            'agencia_sequencial': self.agencia_sequencial if self.agencia_sequencial is not None else '',
            'documento': self.documento if self.documento is not None else '',
            'previsao': self.previsao.value if self.previsao is not None else '',
            'id_carteira_cobranca': str(self.id_carteira_cobranca) if self.id_carteira_cobranca is not None else '',
            'obs': self.obs if self.obs is not None else '',
            'data_inicial': self.data_inicial if self.data_inicial is not None else '',
            'data_final': self.data_final if self.data_final is not None else '',
            'status': self.status.value if self.status is not None else '',
            'id_saida': self.id_saida if self.id_saida is not None else '',
            'liberado': self.liberado if self.liberado is not None else '',
            'nn_boleto': self.nn_boleto if self.nn_boleto is not None else '',
            'gateway_link': self.gateway_link if self.gateway_link is not None else '',
            'gerencianet_token': self.gerencianet_token if self.gerencianet_token is not None else '',
            'tipo_conta': self.tipo_conta if self.tipo_conta is not None else '',
            'id_cobranca': self.id_cobranca if self.id_cobranca is not None else '',
            'status_cobranca': self.status_cobranca if self.status_cobranca is not None else '',
            'id_nota_gerada': self.id_nota_gerada if self.id_nota_gerada is not None else '',
            'id_im_imovel': self.id_im_imovel if self.id_im_imovel is not None else '',
            'impresso': self.impresso.value if self.impresso is not None else '',
            'arquivo_remessa_baixado': self.arquivo_remessa_baixado.value if self.arquivo_remessa_baixado is not None else '',
            'duplicata': self.duplicata if self.duplicata is not None else '',
            'id_sip': self.id_sip if self.id_sip is not None else '',
            'tipo_renegociacao': self.tipo_renegociacao if self.tipo_renegociacao is not None else '',
            'id_renegociacao': self.id_renegociacao if self.id_renegociacao is not None else '',
            'id_renegociacao_novo': self.id_renegociacao_novo if self.id_renegociacao_novo is not None else '',
            'boleto': self.boleto if self.boleto is not None else '',
            'forma_recebimento': self.forma_recebimento.value if self.forma_recebimento is not None else '',
            'credito_data': self.credito_data if self.credito_data is not None else '',
            'baixa_data': self.baixa_data if self.baixa_data is not None else '',
            'baixa_id_operador': self.baixa_id_operador if self.baixa_id_operador is not None else '',
            'cancelamento_id_operador': self.cancelamento_id_operador if self.cancelamento_id_operador is not None else '',
            'numero_parcela_recorrente': self.numero_parcela_recorrente if self.numero_parcela_recorrente is not None else '',
            'nparcela': self.nparcela if self.nparcela is not None else '',
            'id_contrato_principal': self.id_contrato_principal if self.id_contrato_principal is not None else '',
            'previsao_conta_receita': self.previsao_conta_receita if self.previsao_conta_receita is not None else '',
            'tipo_cobranca': self.tipo_cobranca.value if self.tipo_cobranca is not None else '',
            'parcela_proporcional': self.parcela_proporcional if self.parcela_proporcional is not None else '',
            'tipo_pagamento_cartao': self.tipo_pagamento_cartao if self.tipo_pagamento_cartao is not None else '',
            'titulo_protestado': self.titulo_protestado.value if self.titulo_protestado is not None else '',
            'desconto_condicional_valor': self.desconto_condicional_valor if self.desconto_condicional_valor is not None else '',
            'validade_desconto_condicional': self.validade_desconto_condicional if self.validade_desconto_condicional is not None else '',
            'id_nota_gerada_opc2': self.id_nota_gerada_opc2 if self.id_nota_gerada_opc2 is not None else '',
            'id_nota_gerada_opc3': self.id_nota_gerada_opc3 if self.id_nota_gerada_opc3 is not None else '',
            'id_nota_gerada_opc4': self.id_nota_gerada_opc4 if self.id_nota_gerada_opc4 is not None else '',
            'id_lote_geracao_financeiro_fatura': self.id_lote_geracao_financeiro_fatura if self.id_lote_geracao_financeiro_fatura is not None else '',
            'titulo_renegociado': self.titulo_renegociado.value if self.titulo_renegociado is not None else '',
            'id_cobranca_regua': self.id_cobranca_regua if self.id_cobranca_regua is not None else '',
            'id_lote_cobranca_regua': self.id_lote_cobranca_regua if self.id_lote_cobranca_regua is not None else '',
            'etapa_envio_regua': self.etapa_envio_regua.value if self.etapa_envio_regua is not None else '',
            'status_cobranca_regua': self.status_cobranca_regua.value if self.status_cobranca_regua is not None else '',
            'ids_contratos_origem': self.ids_contratos_origem if self.ids_contratos_origem is not None else '',
            'em_cobranca': self.em_cobranca.value if self.em_cobranca is not None else '',
            'valor_aberto': self.valor_aberto if self.valor_aberto is not None else '',
            'valor_recebido': self.valor_recebido if self.valor_recebido is not None else '',
            'pagamento_valor': self.pagamento_valor if self.pagamento_valor is not None else '',
            'valor_juros': self.valor_juros if self.valor_juros is not None else '',
            'valor_multas': self.valor_multas if self.valor_multas is not None else '',
            'pagamento_data': self.pagamento_data if self.pagamento_data is not None else '',
            'valor_cancelado': self.valor_cancelado if self.valor_cancelado is not None else '',
            'data_cancelamento': self.data_cancelamento if self.data_cancelamento is not None else '',
            'origem_importacao': self.origem_importacao if self.origem_importacao is not None else '',
            'titulo_importado': self.titulo_importado.value if self.titulo_importado is not None else '',
            'aguardando_confirmacao_pagamento': self.aguardando_confirmacao_pagamento.value if self.aguardando_confirmacao_pagamento is not None else '',
            'parcelado_cartao': self.parcelado_cartao.value if self.parcelado_cartao is not None else '',
            'bandeira_pagamento': self.bandeira_pagamento if self.bandeira_pagamento is not None else '',
            'recebido_via_pix': self.recebido_via_pix.value if self.recebido_via_pix is not None else '',
            'recebido_por_recorrencia': self.recebido_por_recorrencia.value if self.recebido_por_recorrencia is not None else '',
            'estornado': self.estornado.value if self.estornado is not None else '',
            'conta_recebimento': str(self.conta_recebimento) if self.conta_recebimento is not None else '',
            'id_remessa': self.id_remessa if self.id_remessa is not None else '',
            'linha_digitavel': self.linha_digitavel if self.linha_digitavel is not None else '',
            'id_remessa_alteracao': self.id_remessa_alteracao if self.id_remessa_alteracao is not None else '',
            'motivo_alteracao': self.motivo_alteracao.value if self.motivo_alteracao is not None else '',
            'pix_txid': self.pix_txid if self.pix_txid is not None else '',
            'tipo_cobranca_pix': self.tipo_cobranca_pix.value if self.tipo_cobranca_pix is not None else '',
            'pix_txid_recorrente': self.pix_txid_recorrente if self.pix_txid_recorrente is not None else '',
            'pix_status_recorrente': self.pix_status_recorrente.value if self.pix_status_recorrente is not None else '',
            'tentativa_pix_recorrente': self.tentativa_pix_recorrente if self.tentativa_pix_recorrente is not None else '',
            'data_prevista_tentativa_pix_recorrente': self.data_prevista_tentativa_pix_recorrente if self.data_prevista_tentativa_pix_recorrente is not None else '',
            'libera_periodo': self.libera_periodo.value if self.libera_periodo is not None else '',
            'id_mot_cancelamento': str(self.id_mot_cancelamento) if self.id_mot_cancelamento is not None else '',
            'id_contrato': str(self.id_contrato) if self.id_contrato is not None else '',
            'id_contrato_avulso': str(self.id_contrato_avulso) if self.id_contrato_avulso is not None else '',
            'ultima_atualizacao': self.ultima_atualizacao if self.ultima_atualizacao is not None else '',
            'botoes_classe_finan': self.botoes_classe_finan if self.botoes_classe_finan is not None else '',
            'id_conta_class_finan': str(self.id_conta_class_finan) if self.id_conta_class_finan is not None else '',
            'valor_class_finan': self.valor_class_finan if self.valor_class_finan is not None else '',
            'grid_classe_finan': self.grid_classe_finan if self.grid_classe_finan is not None else '',
            'json_class_finan': self.json_class_finan if self.json_class_finan is not None else '',
            'id_nf_gerada': str(self.id_nf_gerada) if self.id_nf_gerada is not None else '',
            'id_nf_opcional2': str(self.id_nf_opcional2) if self.id_nf_opcional2 is not None else '',
            'id_nf_opcional3': str(self.id_nf_opcional3) if self.id_nf_opcional3 is not None else '',
            'id_nf_opcional4': str(self.id_nf_opcional4) if self.id_nf_opcional4 is not None else '',
        }

    def is_valid(self) -> bool:
        return self.id_autoincrement is not None and self.id_cliente is not None and self.id_conta is not None and self.filial_id is not None and self.data_emissao is not None and self.data_vencimento is not None and self.valor is not None and self.tipo_recebimento is not None

    def __repr__(self) -> str:
        return f"ContasAReceber(id_autoincrement={self.id_autoincrement!r}, id_cliente={self.id_cliente!r}, id_conta={self.id_conta!r}, filial_id={self.filial_id!r}, data_emissao={self.data_emissao!r}, data_vencimento={self.data_vencimento!r}, valor={self.valor!r}, tipo_recebimento={self.tipo_recebimento!r})"

    #------------------------------ CONVERSOR DTO ------------------------------#
    def dto_convert(self, data: dict[str, str]) -> IModel:
        return ContasAReceberModel(
            id_autoincrement=int(data.get('id_autoincrement', 0)),
            id_cliente=int(data['id_cliente']),
            id_conta=int(data['id_conta']),
            filial_id=int(data['filial_id']),
            data_emissao=data.get('data_emissao', ''),
            data_vencimento=data.get('data_vencimento', ''),
            valor=data.get('valor', ''),
            tipo_recebimento=Tipo_recebimentoEnum(data['tipo_recebimento']),
            id_conta_class_finan_a=int(data['id_conta_class_finan_a']) if data.get('id_conta_class_finan_a') else None,
            agencia_sequencial=data.get('agencia_sequencial', ''),
            documento=data.get('documento', ''),
            previsao=PrevisaoEnum(data['previsao']),
            id_carteira_cobranca=int(data['id_carteira_cobranca']) if data.get('id_carteira_cobranca') else None,
            obs=data.get('obs', ''),
            data_inicial=data.get('data_inicial', ''),
            data_final=data.get('data_final', ''),
            status=StatusEnum(data['status']) if data.get('status') else None,
            id_saida=data.get('id_saida', ''),
            liberado=data.get('liberado', ''),
            nn_boleto=data.get('nn_boleto', ''),
            gateway_link=data.get('gateway_link', ''),
            gerencianet_token=data.get('gerencianet_token', ''),
            tipo_conta=data.get('tipo_conta', ''),
            id_cobranca=data.get('id_cobranca', ''),
            status_cobranca=data.get('status_cobranca', ''),
            id_nota_gerada=data.get('id_nota_gerada', ''),
            id_im_imovel=data.get('id_im_imovel', ''),
            impresso=ImpressoEnum(data['impresso']) if data.get('impresso') else None,
            arquivo_remessa_baixado=Arquivo_remessa_baixadoEnum(data['arquivo_remessa_baixado']) if data.get('arquivo_remessa_baixado') else None,
            duplicata=data.get('duplicata', ''),
            id_sip=data.get('id_sip', ''),
            tipo_renegociacao=data.get('tipo_renegociacao', ''),
            id_renegociacao=data.get('id_renegociacao', ''),
            id_renegociacao_novo=data.get('id_renegociacao_novo', ''),
            boleto=data.get('boleto', ''),
            forma_recebimento=Forma_recebimentoEnum(data['forma_recebimento']) if data.get('forma_recebimento') else None,
            credito_data=data.get('credito_data', ''),
            baixa_data=data.get('baixa_data', ''),
            baixa_id_operador=data.get('baixa_id_operador', ''),
            cancelamento_id_operador=data.get('cancelamento_id_operador', ''),
            numero_parcela_recorrente=data.get('numero_parcela_recorrente', ''),
            nparcela=data.get('nparcela', ''),
            id_contrato_principal=data.get('id_contrato_principal', ''),
            previsao_conta_receita=data.get('previsao_conta_receita', ''),
            tipo_cobranca=Tipo_cobrancaEnum(data['tipo_cobranca']) if data.get('tipo_cobranca') else None,
            parcela_proporcional=data.get('parcela_proporcional', ''),
            tipo_pagamento_cartao=data.get('tipo_pagamento_cartao', ''),
            titulo_protestado=Titulo_protestadoEnum(data['titulo_protestado']) if data.get('titulo_protestado') else None,
            desconto_condicional_valor=data.get('desconto_condicional_valor', ''),
            validade_desconto_condicional=data.get('validade_desconto_condicional', ''),
            id_nota_gerada_opc2=data.get('id_nota_gerada_opc2', ''),
            id_nota_gerada_opc3=data.get('id_nota_gerada_opc3', ''),
            id_nota_gerada_opc4=data.get('id_nota_gerada_opc4', ''),
            id_lote_geracao_financeiro_fatura=data.get('id_lote_geracao_financeiro_fatura', ''),
            titulo_renegociado=Titulo_renegociadoEnum(data['titulo_renegociado']) if data.get('titulo_renegociado') else None,
            id_cobranca_regua=data.get('id_cobranca_regua', ''),
            id_lote_cobranca_regua=data.get('id_lote_cobranca_regua', ''),
            etapa_envio_regua=Etapa_envio_reguaEnum(data['etapa_envio_regua']) if data.get('etapa_envio_regua') else None,
            status_cobranca_regua=Status_cobranca_reguaEnum(data['status_cobranca_regua']) if data.get('status_cobranca_regua') else None,
            ids_contratos_origem=data.get('ids_contratos_origem', ''),
            em_cobranca=Em_cobrancaEnum(data['em_cobranca']) if data.get('em_cobranca') else None,
            valor_aberto=data.get('valor_aberto', ''),
            valor_recebido=data.get('valor_recebido', ''),
            pagamento_valor=data.get('pagamento_valor', ''),
            valor_juros=data.get('valor_juros', ''),
            valor_multas=data.get('valor_multas', ''),
            pagamento_data=data.get('pagamento_data', ''),
            valor_cancelado=data.get('valor_cancelado', ''),
            data_cancelamento=data.get('data_cancelamento', ''),
            origem_importacao=data.get('origem_importacao', ''),
            titulo_importado=Titulo_importadoEnum(data['titulo_importado']) if data.get('titulo_importado') else None,
            aguardando_confirmacao_pagamento=Aguardando_confirmacao_pagamentoEnum(data['aguardando_confirmacao_pagamento']) if data.get('aguardando_confirmacao_pagamento') else None,
            parcelado_cartao=Parcelado_cartaoEnum(data['parcelado_cartao']) if data.get('parcelado_cartao') else None,
            bandeira_pagamento=data.get('bandeira_pagamento', ''),
            recebido_via_pix=Recebido_via_pixEnum(data['recebido_via_pix']) if data.get('recebido_via_pix') else None,
            recebido_por_recorrencia=Recebido_por_recorrenciaEnum(data['recebido_por_recorrencia']) if data.get('recebido_por_recorrencia') else None,
            estornado=EstornadoEnum(data['estornado']) if data.get('estornado') else None,
            conta_recebimento=int(data['conta_recebimento']) if data.get('conta_recebimento') else None,
            id_remessa=data.get('id_remessa', ''),
            linha_digitavel=data.get('linha_digitavel', ''),
            id_remessa_alteracao=data.get('id_remessa_alteracao', ''),
            motivo_alteracao=Motivo_alteracaoEnum(data['motivo_alteracao']) if data.get('motivo_alteracao') else None,
            pix_txid=data.get('pix_txid', ''),
            tipo_cobranca_pix=Tipo_cobranca_pixEnum(data['tipo_cobranca_pix']) if data.get('tipo_cobranca_pix') else None,
            pix_txid_recorrente=data.get('pix_txid_recorrente', ''),
            pix_status_recorrente=Pix_status_recorrenteEnum(data['pix_status_recorrente']) if data.get('pix_status_recorrente') else None,
            tentativa_pix_recorrente=data.get('tentativa_pix_recorrente', ''),
            data_prevista_tentativa_pix_recorrente=data.get('data_prevista_tentativa_pix_recorrente', ''),
            libera_periodo=Libera_periodoEnum(data['libera_periodo']) if data.get('libera_periodo') else None,
            id_mot_cancelamento=int(data['id_mot_cancelamento']) if data.get('id_mot_cancelamento') else None,
            id_contrato=int(data['id_contrato']) if data.get('id_contrato') else None,
            id_contrato_avulso=int(data['id_contrato_avulso']) if data.get('id_contrato_avulso') else None,
            ultima_atualizacao=data.get('ultima_atualizacao', ''),
            botoes_classe_finan=data.get('botoes_classe_finan', ''),
            id_conta_class_finan=int(data['id_conta_class_finan']) if data.get('id_conta_class_finan') else None,
            valor_class_finan=data.get('valor_class_finan', ''),
            grid_classe_finan=data.get('grid_classe_finan', ''),
            json_class_finan=data.get('json_class_finan', ''),
            id_nf_gerada=int(data['id_nf_gerada']) if data.get('id_nf_gerada') else None,
            id_nf_opcional2=int(data['id_nf_opcional2']) if data.get('id_nf_opcional2') else None,
            id_nf_opcional3=int(data['id_nf_opcional3']) if data.get('id_nf_opcional3') else None,
            id_nf_opcional4=int(data['id_nf_opcional4']) if data.get('id_nf_opcional4') else None,
        )
