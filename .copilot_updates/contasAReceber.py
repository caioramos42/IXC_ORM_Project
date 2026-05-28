from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from ORM_IXC.enums.contasAReceber import *
from ORM_IXC.interfaces import IModel, IModelWithId
from ORM_IXC.statemants.classBase import Field
from ORM_IXC.statemants.mapper import Mapped
from ORM_IXC.statemants.metaManager import MetaModels
from ORM_IXC.models.defaultModel import BaseModel

@MetaModels
class ContasAReceberModel(IModelWithId, BaseModel):
    id: int
    id_cliente: int
    id_conta: int
    filial_id: int
    data_emissao: str
    data_vencimento: str
    valor: str
    tipo_recebimento: Tipo_recebimentoEnum
    id_conta_class_finan_a: Mapped[Optional[int]] = Field("id_conta_class_finan_a", int, None)
    agencia_sequencial: Mapped[Optional[str]] = Field("agencia_sequencial", str, '')
    documento: Mapped[Optional[str]] = Field("documento", str, '')
    previsao: Mapped[PrevisaoEnum] = Field("previsao", PrevisaoEnum, PrevisaoEnum.COMPETENCIA_)
    id_carteira_cobranca: Mapped[Optional[int]] = Field("id_carteira_cobranca", int, None)
    obs: Mapped[Optional[str]] = Field("obs", str, '')
    data_inicial: Mapped[Optional[str]] = Field("data_inicial", str, '')
    data_final: Mapped[Optional[str]] = Field("data_final", str, '')
    status: Mapped[Optional[StatusEnum]] = Field("status", StatusEnum, StatusEnum.A_RECEBER)
    id_saida: Mapped[Optional[str]] = Field("id_saida", str, '')
    liberado: Mapped[Optional[str]] = Field("liberado", str, '')
    nn_boleto: Mapped[Optional[str]] = Field("nn_boleto", str, '')
    gateway_link: Mapped[Optional[str]] = Field("gateway_link", str, '')
    gerencianet_token: Mapped[Optional[str]] = Field("gerencianet_token", str, '')
    tipo_conta: Mapped[Optional[str]] = Field("tipo_conta", str, '')
    id_cobranca: Mapped[Optional[str]] = Field("id_cobranca", str, '')
    status_cobranca: Mapped[Optional[str]] = Field("status_cobranca", str, '')
    id_nota_gerada: Mapped[Optional[str]] = Field("id_nota_gerada", str, '')
    id_im_imovel: Mapped[Optional[str]] = Field("id_im_imovel", str, '')
    impresso: Mapped[Optional[ImpressoEnum]] = Field("impresso", ImpressoEnum, ImpressoEnum.NAO)
    arquivo_remessa_baixado: Mapped[Optional[Arquivo_remessa_baixadoEnum]] = Field("arquivo_remessa_baixado", Arquivo_remessa_baixadoEnum, None)
    duplicata: Mapped[Optional[str]] = Field("duplicata", str, '')
    id_sip: Mapped[Optional[str]] = Field("id_sip", str, '')
    tipo_renegociacao: Mapped[Optional[str]] = Field("tipo_renegociacao", str, '')
    id_renegociacao: Mapped[Optional[str]] = Field("id_renegociacao", str, '')
    id_renegociacao_novo: Mapped[Optional[str]] = Field("id_renegociacao_novo", str, '')
    boleto: Mapped[Optional[str]] = Field("boleto", str, '')
    forma_recebimento: Mapped[Optional[Forma_recebimentoEnum]] = Field("forma_recebimento", Forma_recebimentoEnum, Forma_recebimentoEnum.RECEBIDO_DE_FORMA_MANUAL)
    credito_data: Mapped[Optional[str]] = Field("credito_data", str, '')
    baixa_data: Mapped[Optional[str]] = Field("baixa_data", str, '')
    baixa_id_operador: Mapped[Optional[str]] = Field("baixa_id_operador", str, '')
    cancelamento_id_operador: Mapped[Optional[str]] = Field("cancelamento_id_operador", str, '')
    numero_parcela_recorrente: Mapped[Optional[str]] = Field("numero_parcela_recorrente", str, '')
    nparcela: Mapped[Optional[str]] = Field("nparcela", str, '')
    id_contrato_principal: Mapped[Optional[str]] = Field("id_contrato_principal", str, '')
    previsao_conta_receita: Mapped[Optional[str]] = Field("previsao_conta_receita", str, '')
    tipo_cobranca: Mapped[Optional[Tipo_cobrancaEnum]] = Field("tipo_cobranca", Tipo_cobrancaEnum, None)
    parcela_proporcional: Mapped[Optional[str]] = Field("parcela_proporcional", str, '')
    tipo_pagamento_cartao: Mapped[Optional[str]] = Field("tipo_pagamento_cartao", str, '')
    titulo_protestado: Mapped[Optional[Titulo_protestadoEnum]] = Field("titulo_protestado", Titulo_protestadoEnum, Titulo_protestadoEnum.NAO)
    desconto_condicional_valor: Mapped[Optional[str]] = Field("desconto_condicional_valor", str, '')
    validade_desconto_condicional: Mapped[Optional[str]] = Field("validade_desconto_condicional", str, '')
    id_nota_gerada_opc2: Mapped[Optional[str]] = Field("id_nota_gerada_opc2", str, '')
    id_nota_gerada_opc3: Mapped[Optional[str]] = Field("id_nota_gerada_opc3", str, '')
    id_nota_gerada_opc4: Mapped[Optional[str]] = Field("id_nota_gerada_opc4", str, '')
    id_lote_geracao_financeiro_fatura: Mapped[Optional[str]] = Field("id_lote_geracao_financeiro_fatura", str, '')
    titulo_renegociado: Mapped[Optional[Titulo_renegociadoEnum]] = Field("titulo_renegociado", Titulo_renegociadoEnum, None)
    id_cobranca_regua: Mapped[Optional[str]] = Field("id_cobranca_regua", str, '')
    id_lote_cobranca_regua: Mapped[Optional[str]] = Field("id_lote_cobranca_regua", str, '')
    etapa_envio_regua: Mapped[Optional[Etapa_envio_reguaEnum]] = Field("etapa_envio_regua", Etapa_envio_reguaEnum, None)
    status_cobranca_regua: Mapped[Optional[Status_cobranca_reguaEnum]] = Field("status_cobranca_regua", Status_cobranca_reguaEnum, None)
    ids_contratos_origem: Mapped[Optional[str]] = Field("ids_contratos_origem", str, '')
    em_cobranca: Mapped[Optional[Em_cobrancaEnum]] = Field("em_cobranca", Em_cobrancaEnum, None)
    valor_aberto: Mapped[Optional[str]] = Field("valor_aberto", str, '')
    valor_recebido: Mapped[Optional[str]] = Field("valor_recebido", str, '')
    pagamento_valor: Mapped[Optional[str]] = Field("pagamento_valor", str, '')
    valor_juros: Mapped[Optional[str]] = Field("valor_juros", str, '')
    valor_multas: Mapped[Optional[str]] = Field("valor_multas", str, '')
    pagamento_data: Mapped[Optional[str]] = Field("pagamento_data", str, '')
    valor_cancelado: Mapped[Optional[str]] = Field("valor_cancelado", str, '')
    data_cancelamento: Mapped[Optional[str]] = Field("data_cancelamento", str, '')
    origem_importacao: Mapped[Optional[str]] = Field("origem_importacao", str, '')
    titulo_importado: Mapped[Optional[Titulo_importadoEnum]] = Field("titulo_importado", Titulo_importadoEnum, Titulo_importadoEnum.NAO)
    aguardando_confirmacao_pagamento: Mapped[Optional[Aguardando_confirmacao_pagamentoEnum]] = Field("aguardando_confirmacao_pagamento", Aguardando_confirmacao_pagamentoEnum, Aguardando_confirmacao_pagamentoEnum.NAO)
    parcelado_cartao: Mapped[Optional[Parcelado_cartaoEnum]] = Field("parcelado_cartao", Parcelado_cartaoEnum, Parcelado_cartaoEnum.NAO)
    bandeira_pagamento: Mapped[Optional[str]] = Field("bandeira_pagamento", str, '')
    recebido_via_pix: Mapped[Optional[Recebido_via_pixEnum]] = Field("recebido_via_pix", Recebido_via_pixEnum, Recebido_via_pixEnum.NAO)
    recebido_por_recorrencia: Mapped[Optional[Recebido_por_recorrenciaEnum]] = Field("recebido_por_recorrencia", Recebido_por_recorrenciaEnum, Recebido_por_recorrenciaEnum.NAO)
    estornado: Mapped[Optional[EstornadoEnum]] = Field("estornado", EstornadoEnum, None)
    conta_recebimento: Mapped[Optional[int]] = Field("conta_recebimento", int, None)
    id_remessa: Mapped[Optional[str]] = Field("id_remessa", str, '')
    linha_digitavel: Mapped[Optional[str]] = Field("linha_digitavel", str, '')
    id_remessa_alteracao: Mapped[Optional[str]] = Field("id_remessa_alteracao", str, '')
    motivo_alteracao: Mapped[Optional[Motivo_alteracaoEnum]] = Field("motivo_alteracao", Motivo_alteracaoEnum, None)
    pix_txid: Mapped[Optional[str]] = Field("pix_txid", str, '')
    tipo_cobranca_pix: Mapped[Optional[Tipo_cobranca_pixEnum]] = Field("tipo_cobranca_pix", Tipo_cobranca_pixEnum, None)
    pix_txid_recorrente: Mapped[Optional[str]] = Field("pix_txid_recorrente", str, '')
    pix_status_recorrente: Mapped[Optional[Pix_status_recorrenteEnum]] = Field("pix_status_recorrente", Pix_status_recorrenteEnum, None)
    tentativa_pix_recorrente: Mapped[Optional[str]] = Field("tentativa_pix_recorrente", str, '')
    data_prevista_tentativa_pix_recorrente: Mapped[Optional[str]] = Field("data_prevista_tentativa_pix_recorrente", str, '')
    libera_periodo: Mapped[Optional[Libera_periodoEnum]] = Field("libera_periodo", Libera_periodoEnum, Libera_periodoEnum.NAO)
    id_mot_cancelamento: Mapped[Optional[int]] = Field("id_mot_cancelamento", int, None)
    id_contrato: Mapped[Optional[int]] = Field("id_contrato", int, None)
    id_contrato_avulso: Mapped[Optional[int]] = Field("id_contrato_avulso", int, None)
    ultima_atualizacao: Mapped[Optional[str]] = Field("ultima_atualizacao", str, '')
    botoes_classe_finan: Mapped[Optional[str]] = Field("botoes_classe_finan", str, '')
    id_conta_class_finan: Mapped[Optional[int]] = Field("id_conta_class_finan", int, None)
    valor_class_finan: Mapped[Optional[str]] = Field("valor_class_finan", str, '')
    grid_classe_finan: Mapped[Optional[str]] = Field("grid_classe_finan", str, '')
    json_class_finan: Mapped[Optional[str]] = Field("json_class_finan", str, '')
    id_nf_gerada: Mapped[Optional[int]] = Field("id_nf_gerada", int, None)
    id_nf_opcional2: Mapped[Optional[int]] = Field("id_nf_opcional2", int, None)
    id_nf_opcional3: Mapped[Optional[int]] = Field("id_nf_opcional3", int, None)
    id_nf_opcional4: Mapped[Optional[int]] = Field("id_nf_opcional4", int, None)

    @property
    def table(self) -> str:
        return "fn_areceber"
    
    def to_dict(self) -> dict:
        def serialize(value) -> str:
            if value is None:
                return ''
            raw = getattr(value, 'value', value)
            return '' if raw is None else str(raw)

        data = {
            'id': str(self.id),
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
        return {key: serialize(value) for key, value in data.items()}

    def is_valid(self) -> bool:
        return self.id_autoincrement is not None and self.id_cliente is not None and self.id_conta is not None and self.filial_id is not None and self.data_emissao is not None and self.data_vencimento is not None and self.valor is not None and self.tipo_recebimento is not None
