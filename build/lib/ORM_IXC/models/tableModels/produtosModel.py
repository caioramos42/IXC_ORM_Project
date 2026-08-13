from __future__ import annotations
from typing import Optional
from ORM_IXC.interfaces import IModelWithId
from ORM_IXC.enums.produtos import *
from ORM_IXC.statemants.maps.mapper import Mapped, field as mapped_field
from ORM_IXC.statemants.maps.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel


@MetaModels
class ProdutosModel(IModelWithId, BaseModel):
    ativo :Mapped[AtivoEnum]
    descricao :Mapped[str]
    tipo :Mapped[TipoEnum]
    controla_estoque :Mapped[Controla_estoqueEnum]
    movimentacao :Mapped[MovimentacaoEnum]
    id_sub_grupo :Mapped[int]
    unidade :Mapped[int]
    preco_base :Mapped[str]
    aceita_valor :Mapped[str]
    icms_issqn :Mapped[Icms_issqnEnum]
    id :Mapped[Optional[int]]
    descricao_alt :Mapped[Optional[str]] = mapped_field('')
    dica_servico_controla_estoque :Mapped[Optional[str]] = mapped_field('')
    dica_patrimonio_controla_estoque :Mapped[Optional[str]] = mapped_field('')
    subgrupo_tipo :Mapped[Optional[str]] = mapped_field('')
    valor :Mapped[Optional[str]] = mapped_field('')
    valor_custo :Mapped[Optional[str]] = mapped_field('')
    custo_medio :Mapped[Optional[str]] = mapped_field('')
    custo_medio_total :Mapped[Optional[str]] = mapped_field('')
    obs :Mapped[Optional[str]] = mapped_field('')
    saldo :Mapped[Optional[str]] = mapped_field('')
    id_tabela_fipe :Mapped[Optional[int]] = mapped_field(None)
    codigo_tecido :Mapped[Optional[str]] = mapped_field('')
    qtde_min :Mapped[Optional[str]] = mapped_field('')
    qtde_max :Mapped[Optional[str]] = mapped_field('')
    vencimento_garantia :Mapped[Optional[str]] = mapped_field('')
    id_categoria_patrimonio :Mapped[Optional[str]] = mapped_field('')
    margem_lucro :Mapped[Optional[str]] = mapped_field('')
    pcomissao :Mapped[Optional[str]] = mapped_field('')
    codigo :Mapped[Optional[str]] = mapped_field('')
    codigo_barras :Mapped[Optional[str]] = mapped_field('')
    ultima_atualizacao :Mapped[Optional[str]] = mapped_field('')
    codigo_externo_produto_col :Mapped[Optional[str]] = mapped_field('')
    descricao_produto_col :Mapped[Optional[str]] = mapped_field('')
    tp_transacao_pry :Mapped[Optional[Tp_transacao_pryEnum]] = mapped_field(None)
    excecao_tributacao_nfcom :Mapped[Optional[Excecao_tributacao_nfcomEnum]] = mapped_field(None)
    id_class_fiscal :Mapped[Optional[int]] = mapped_field(None)
    id_class_fiscal_entrada :Mapped[Optional[int]] = mapped_field(None)
    ncm :Mapped[Optional[int]] = mapped_field(None)
    id_produtos_ncm_cest :Mapped[Optional[int]] = mapped_field(None)
    cod_servico :Mapped[Optional[int]] = mapped_field(None)
    cod_classificacao_servico :Mapped[Optional[Cod_classificacao_servicoEnum]] = mapped_field(None)
    cnpj_op_longa_distancia :Mapped[Optional[str]] = mapped_field('')
    identificacao_item_sped :Mapped[Optional[Identificacao_item_spedEnum]] = mapped_field(None)
    id_conta_estoque :Mapped[Optional[int]] = mapped_field(None)
    id_conta_despesa :Mapped[Optional[int]] = mapped_field(None)
    id_conta_receita :Mapped[Optional[int]] = mapped_field(None)
    id_conta_comodato :Mapped[Optional[int]] = mapped_field(None)
    centro_custo_regra_criterio :Mapped[Optional[Centro_custo_regra_criterioEnum]] = mapped_field(None)
    id_centro_custo_rel_centro_custo_categoria_padrao :Mapped[Optional[int]] = mapped_field(None)
    id_centro_custo_criterio_rateio :Mapped[Optional[int]] = mapped_field(None)
    id_centro_resultado_rel_centro_custo_categoria_padrao :Mapped[Optional[int]] = mapped_field(None)
    vICMSSTRet :Mapped[Optional[str]] = mapped_field('')
    iss_natureza_operacao :Mapped[Optional[Iss_natureza_operacaoEnum]] = mapped_field(None)
    controle_impressao_etiqueta :Mapped[Optional[Controle_impressao_etiquetaEnum]] = mapped_field(None)
    id_tipo_documento_servico :Mapped[Optional[int]] = mapped_field(None)
    id_tipo_documento_servico_pj :Mapped[Optional[int]] = mapped_field(None)
    id_fr_faturamento_classificacoes :Mapped[Optional[int]] = mapped_field(None)
    imagem :Mapped[Optional[str]] = mapped_field('')
    qtde_tecido_base :Mapped[Optional[str]] = mapped_field('')
    qtde_tecido_almofadas :Mapped[Optional[str]] = mapped_field('')
    pesob :Mapped[Optional[str]] = mapped_field('')
    pesol :Mapped[Optional[str]] = mapped_field('')
    altura :Mapped[Optional[str]] = mapped_field('')
    largura :Mapped[Optional[str]] = mapped_field('')
    profundidade :Mapped[Optional[str]] = mapped_field('')
    ecommerce :Mapped[Optional[EcommerceEnum]] = mapped_field(None)
    ecommerce_pg_inicial :Mapped[Optional[Ecommerce_pg_inicialEnum]] = mapped_field(None)
    mostra_valor_ecommerce :Mapped[Optional[Mostra_valor_ecommerceEnum]] = mapped_field(None)
    tipo_ecommerce :Mapped[Optional[Tipo_ecommerceEnum]] = mapped_field(None)
    ecommerce_prioridade :Mapped[Optional[str]] = mapped_field('')
    valor_prefixo :Mapped[Optional[str]] = mapped_field('')
    valor_sufixo :Mapped[Optional[str]] = mapped_field('')
    descricao_completa :Mapped[Optional[str]] = mapped_field('')
    id_sva_integracao :Mapped[Optional[int]] = mapped_field(None)
    id_sva_pacote :Mapped[Optional[str]] = mapped_field('')
    id_sva_pacote_adicional :Mapped[Optional[str]] = mapped_field('')
    plataforma :Mapped[Optional[PlataformaEnum]] = mapped_field(None)
    tv_id_plataforma :Mapped[Optional[str]] = mapped_field('')
    tv_LineUp :Mapped[Optional[str]] = mapped_field('')
    tv_data_inicial :Mapped[Optional[str]] = mapped_field('')
    tv_data_final :Mapped[Optional[str]] = mapped_field('')
    id_integracao_tv :Mapped[Optional[int]] = mapped_field(None)
    tv_id_pacote_servicos :Mapped[Optional[int]] = mapped_field(None)
    tv_id_pacote_servicos_watch :Mapped[Optional[str]] = mapped_field('')
    descricao_pacote_watch :Mapped[Optional[str]] = mapped_field('')
    total_tickets_watch :Mapped[Optional[str]] = mapped_field('')
    tv_id_pacotes :Mapped[Optional[str]] = mapped_field('')
    tv_id_pacote_temporario :Mapped[Optional[str]] = mapped_field('')
    tv_dias_expiracao_pacote_temporario :Mapped[Optional[str]] = mapped_field('')
    tv_mus_produtos_disponiveis :Mapped[Optional[str]] = mapped_field('')
    produto_playhub :Mapped[Optional[Produto_playhubEnum]] = mapped_field(None)
    tariff_plan :Mapped[Optional[str]] = mapped_field('')
    tv_dtvgo_produtos_disponiveis :Mapped[Optional[str]] = mapped_field('')
    tv_id_pacotes_adicionais :Mapped[Optional[str]] = mapped_field('')
    id_integracao_iot :Mapped[Optional[int]] = mapped_field(None)
    id_produto_iot :Mapped[Optional[str]] = mapped_field('')
    tipo_produto_integracao :Mapped[Optional[Tipo_produto_integracaoEnum]] = mapped_field(None)
    id_assinatura_integracao :Mapped[Optional[int]] = mapped_field(None)
    plataforma_integracao :Mapped[Optional[Plataforma_integracaoEnum]] = mapped_field(None)
    checkbox1 :Mapped[Optional[str]] = mapped_field('')
    checkbox2 :Mapped[Optional[str]] = mapped_field('')
    checkbox3 :Mapped[Optional[str]] = mapped_field('')
    checkbox4 :Mapped[Optional[str]] = mapped_field('')
    checkbox5 :Mapped[Optional[str]] = mapped_field('')
    checkbox6 :Mapped[Optional[str]] = mapped_field('')
    checkbox7 :Mapped[Optional[str]] = mapped_field('')
    checkbox8 :Mapped[Optional[str]] = mapped_field('')
    checkbox9 :Mapped[Optional[str]] = mapped_field('')
    checkbox10 :Mapped[Optional[str]] = mapped_field('')
    checkbox11 :Mapped[Optional[str]] = mapped_field('')
    checkbox12 :Mapped[Optional[str]] = mapped_field('')
    checkbox13 :Mapped[Optional[str]] = mapped_field('')
    checkbox14 :Mapped[Optional[str]] = mapped_field('')
    checkbox15 :Mapped[Optional[str]] = mapped_field('')
    checkbox16 :Mapped[Optional[str]] = mapped_field('')
    checkbox17 :Mapped[Optional[str]] = mapped_field('')
    checkbox18 :Mapped[Optional[str]] = mapped_field('')
    checkbox19 :Mapped[Optional[str]] = mapped_field('')
    checkbox20 :Mapped[Optional[str]] = mapped_field('')
    checkbox21 :Mapped[Optional[str]] = mapped_field('')
    checkbox22 :Mapped[Optional[str]] = mapped_field('')
    checkbox23 :Mapped[Optional[str]] = mapped_field('')
    checkbox24 :Mapped[Optional[str]] = mapped_field('')
    checkbox25 :Mapped[Optional[str]] = mapped_field('')
    checkbox26 :Mapped[Optional[str]] = mapped_field('')
    checkbox27 :Mapped[Optional[str]] = mapped_field('')
    checkbox28 :Mapped[Optional[str]] = mapped_field('')
    checkbox29 :Mapped[Optional[str]] = mapped_field('')
    checkbox30 :Mapped[Optional[str]] = mapped_field('')
    checkbox31 :Mapped[Optional[str]] = mapped_field('')
    checkbox32 :Mapped[Optional[str]] = mapped_field('')
    checkbox33 :Mapped[Optional[str]] = mapped_field('')
    checkbox34 :Mapped[Optional[str]] = mapped_field('')
    checkbox35 :Mapped[Optional[str]] = mapped_field('')
    checkbox36 :Mapped[Optional[str]] = mapped_field('')
    checkbox37 :Mapped[Optional[str]] = mapped_field('')
    checkbox38 :Mapped[Optional[str]] = mapped_field('')
    checkbox39 :Mapped[Optional[str]] = mapped_field('')
    checkbox40 :Mapped[Optional[str]] = mapped_field('')
    chassi :Mapped[Optional[str]] = mapped_field('')
    renavan :Mapped[Optional[str]] = mapped_field('')
    km :Mapped[Optional[str]] = mapped_field('')
    veiculo_cor :Mapped[Optional[Veiculo_corEnum]] = mapped_field(None)
    cambio :Mapped[Optional[CambioEnum]] = mapped_field(None)
    qtdportas :Mapped[Optional[QtdportasEnum]] = mapped_field(None)
    veiculo_combustivel :Mapped[Optional[Veiculo_combustivelEnum]] = mapped_field(None)
    integrador :Mapped[Optional[int]] = mapped_field(None)
    limite_pacote :Mapped[Optional[str]] = mapped_field('')
    valor_adicional_pacote :Mapped[Optional[str]] = mapped_field('')

    @property
    def table(self) -> str:
        return "produtos"

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
            'descricao': self._serialize_enum_and_str(self.descricao) if self.descricao is not None else '',
            'tipo': self._serialize_enum_and_str(self.tipo) if self.tipo is not None else '',
            'controla_estoque': self._serialize_enum_and_str(self.controla_estoque) if self.controla_estoque is not None else '',
            'movimentacao': self._serialize_enum_and_str(self.movimentacao) if self.movimentacao is not None else '',
            'id_sub_grupo': str(self.id_sub_grupo) if self.id_sub_grupo is not None else '',
            'unidade': str(self.unidade) if self.unidade is not None else '',
            'preco_base': self._serialize_enum_and_str(self.preco_base) if self.preco_base is not None else '',
            'aceita_valor': self._serialize_enum_and_str(self.aceita_valor) if self.aceita_valor is not None else '',
            'icms_issqn': self._serialize_enum_and_str(self.icms_issqn) if self.icms_issqn is not None else '',
            'id': str(self.id) if self.id is not None else '',
            'descricao_alt': self._serialize_enum_and_str(self.descricao_alt) if self.descricao_alt is not None else '',
            'dica_servico_controla_estoque': self._serialize_enum_and_str(self.dica_servico_controla_estoque) if self.dica_servico_controla_estoque is not None else '',
            'dica_patrimonio_controla_estoque': self._serialize_enum_and_str(self.dica_patrimonio_controla_estoque) if self.dica_patrimonio_controla_estoque is not None else '',
            'subgrupo_tipo': self._serialize_enum_and_str(self.subgrupo_tipo) if self.subgrupo_tipo is not None else '',
            'valor': self._serialize_enum_and_str(self.valor) if self.valor is not None else '',
            'valor_custo': self._serialize_enum_and_str(self.valor_custo) if self.valor_custo is not None else '',
            'custo_medio': self._serialize_enum_and_str(self.custo_medio) if self.custo_medio is not None else '',
            'custo_medio_total': self._serialize_enum_and_str(self.custo_medio_total) if self.custo_medio_total is not None else '',
            'obs': self._serialize_enum_and_str(self.obs) if self.obs is not None else '',
            'saldo': self._serialize_enum_and_str(self.saldo) if self.saldo is not None else '',
            'id_tabela_fipe': str(self.id_tabela_fipe) if self.id_tabela_fipe is not None else '',
            'codigo_tecido': self._serialize_enum_and_str(self.codigo_tecido) if self.codigo_tecido is not None else '',
            'qtde_min': self._serialize_enum_and_str(self.qtde_min) if self.qtde_min is not None else '',
            'qtde_max': self._serialize_enum_and_str(self.qtde_max) if self.qtde_max is not None else '',
            'vencimento_garantia': self._serialize_enum_and_str(self.vencimento_garantia) if self.vencimento_garantia is not None else '',
            'id_categoria_patrimonio': self._serialize_enum_and_str(self.id_categoria_patrimonio) if self.id_categoria_patrimonio is not None else '',
            'margem_lucro': self._serialize_enum_and_str(self.margem_lucro) if self.margem_lucro is not None else '',
            'pcomissao': self._serialize_enum_and_str(self.pcomissao) if self.pcomissao is not None else '',
            'codigo': self._serialize_enum_and_str(self.codigo) if self.codigo is not None else '',
            'codigo_barras': self._serialize_enum_and_str(self.codigo_barras) if self.codigo_barras is not None else '',
            'ultima_atualizacao': self._serialize_enum_and_str(self.ultima_atualizacao) if self.ultima_atualizacao is not None else '',
            'codigo_externo_produto_col': self._serialize_enum_and_str(self.codigo_externo_produto_col) if self.codigo_externo_produto_col is not None else '',
            'descricao_produto_col': self._serialize_enum_and_str(self.descricao_produto_col) if self.descricao_produto_col is not None else '',
            'tp_transacao_pry': self._serialize_enum_and_str(self.tp_transacao_pry) if self.tp_transacao_pry is not None else '',
            'excecao_tributacao_nfcom': self._serialize_enum_and_str(self.excecao_tributacao_nfcom) if self.excecao_tributacao_nfcom is not None else '',
            'id_class_fiscal': str(self.id_class_fiscal) if self.id_class_fiscal is not None else '',
            'id_class_fiscal_entrada': str(self.id_class_fiscal_entrada) if self.id_class_fiscal_entrada is not None else '',
            'ncm': str(self.ncm) if self.ncm is not None else '',
            'id_produtos_ncm_cest': str(self.id_produtos_ncm_cest) if self.id_produtos_ncm_cest is not None else '',
            'cod_servico': str(self.cod_servico) if self.cod_servico is not None else '',
            'cod_classificacao_servico': self._serialize_enum_and_str(self.cod_classificacao_servico) if self.cod_classificacao_servico is not None else '',
            'cnpj_op_longa_distancia': self._serialize_enum_and_str(self.cnpj_op_longa_distancia) if self.cnpj_op_longa_distancia is not None else '',
            'identificacao_item_sped': self._serialize_enum_and_str(self.identificacao_item_sped) if self.identificacao_item_sped is not None else '',
            'id_conta_estoque': str(self.id_conta_estoque) if self.id_conta_estoque is not None else '',
            'id_conta_despesa': str(self.id_conta_despesa) if self.id_conta_despesa is not None else '',
            'id_conta_receita': str(self.id_conta_receita) if self.id_conta_receita is not None else '',
            'id_conta_comodato': str(self.id_conta_comodato) if self.id_conta_comodato is not None else '',
            'centro_custo_regra_criterio': self._serialize_enum_and_str(self.centro_custo_regra_criterio) if self.centro_custo_regra_criterio is not None else '',
            'id_centro_custo_rel_centro_custo_categoria_padrao': str(self.id_centro_custo_rel_centro_custo_categoria_padrao) if self.id_centro_custo_rel_centro_custo_categoria_padrao is not None else '',
            'id_centro_custo_criterio_rateio': str(self.id_centro_custo_criterio_rateio) if self.id_centro_custo_criterio_rateio is not None else '',
            'id_centro_resultado_rel_centro_custo_categoria_padrao': str(self.id_centro_resultado_rel_centro_custo_categoria_padrao) if self.id_centro_resultado_rel_centro_custo_categoria_padrao is not None else '',
            'vICMSSTRet': self._serialize_enum_and_str(self.vICMSSTRet) if self.vICMSSTRet is not None else '',
            'iss_natureza_operacao': self._serialize_enum_and_str(self.iss_natureza_operacao) if self.iss_natureza_operacao is not None else '',
            'controle_impressao_etiqueta': self._serialize_enum_and_str(self.controle_impressao_etiqueta) if self.controle_impressao_etiqueta is not None else '',
            'id_tipo_documento_servico': str(self.id_tipo_documento_servico) if self.id_tipo_documento_servico is not None else '',
            'id_tipo_documento_servico_pj': str(self.id_tipo_documento_servico_pj) if self.id_tipo_documento_servico_pj is not None else '',
            'id_fr_faturamento_classificacoes': str(self.id_fr_faturamento_classificacoes) if self.id_fr_faturamento_classificacoes is not None else '',
            'imagem': self._serialize_enum_and_str(self.imagem) if self.imagem is not None else '',
            'qtde_tecido_base': self._serialize_enum_and_str(self.qtde_tecido_base) if self.qtde_tecido_base is not None else '',
            'qtde_tecido_almofadas': self._serialize_enum_and_str(self.qtde_tecido_almofadas) if self.qtde_tecido_almofadas is not None else '',
            'pesob': self._serialize_enum_and_str(self.pesob) if self.pesob is not None else '',
            'pesol': self._serialize_enum_and_str(self.pesol) if self.pesol is not None else '',
            'altura': self._serialize_enum_and_str(self.altura) if self.altura is not None else '',
            'largura': self._serialize_enum_and_str(self.largura) if self.largura is not None else '',
            'profundidade': self._serialize_enum_and_str(self.profundidade) if self.profundidade is not None else '',
            'ecommerce': self._serialize_enum_and_str(self.ecommerce) if self.ecommerce is not None else '',
            'ecommerce_pg_inicial': self._serialize_enum_and_str(self.ecommerce_pg_inicial) if self.ecommerce_pg_inicial is not None else '',
            'mostra_valor_ecommerce': self._serialize_enum_and_str(self.mostra_valor_ecommerce) if self.mostra_valor_ecommerce is not None else '',
            'tipo_ecommerce': self._serialize_enum_and_str(self.tipo_ecommerce) if self.tipo_ecommerce is not None else '',
            'ecommerce_prioridade': self._serialize_enum_and_str(self.ecommerce_prioridade) if self.ecommerce_prioridade is not None else '',
            'valor_prefixo': self._serialize_enum_and_str(self.valor_prefixo) if self.valor_prefixo is not None else '',
            'valor_sufixo': self._serialize_enum_and_str(self.valor_sufixo) if self.valor_sufixo is not None else '',
            'descricao_completa': self._serialize_enum_and_str(self.descricao_completa) if self.descricao_completa is not None else '',
            'id_sva_integracao': str(self.id_sva_integracao) if self.id_sva_integracao is not None else '',
            'id_sva_pacote': self._serialize_enum_and_str(self.id_sva_pacote) if self.id_sva_pacote is not None else '',
            'id_sva_pacote_adicional': self._serialize_enum_and_str(self.id_sva_pacote_adicional) if self.id_sva_pacote_adicional is not None else '',
            'plataforma': self._serialize_enum_and_str(self.plataforma) if self.plataforma is not None else '',
            'tv_id_plataforma': self._serialize_enum_and_str(self.tv_id_plataforma) if self.tv_id_plataforma is not None else '',
            'tv_LineUp': self._serialize_enum_and_str(self.tv_LineUp) if self.tv_LineUp is not None else '',
            'tv_data_inicial': self._serialize_enum_and_str(self.tv_data_inicial) if self.tv_data_inicial is not None else '',
            'tv_data_final': self._serialize_enum_and_str(self.tv_data_final) if self.tv_data_final is not None else '',
            'id_integracao_tv': str(self.id_integracao_tv) if self.id_integracao_tv is not None else '',
            'tv_id_pacote_servicos': str(self.tv_id_pacote_servicos) if self.tv_id_pacote_servicos is not None else '',
            'tv_id_pacote_servicos_watch': self._serialize_enum_and_str(self.tv_id_pacote_servicos_watch) if self.tv_id_pacote_servicos_watch is not None else '',
            'descricao_pacote_watch': self._serialize_enum_and_str(self.descricao_pacote_watch) if self.descricao_pacote_watch is not None else '',
            'total_tickets_watch': self._serialize_enum_and_str(self.total_tickets_watch) if self.total_tickets_watch is not None else '',
            'tv_id_pacotes': self._serialize_enum_and_str(self.tv_id_pacotes) if self.tv_id_pacotes is not None else '',
            'tv_id_pacote_temporario': self._serialize_enum_and_str(self.tv_id_pacote_temporario) if self.tv_id_pacote_temporario is not None else '',
            'tv_dias_expiracao_pacote_temporario': self._serialize_enum_and_str(self.tv_dias_expiracao_pacote_temporario) if self.tv_dias_expiracao_pacote_temporario is not None else '',
            'tv_mus_produtos_disponiveis': self._serialize_enum_and_str(self.tv_mus_produtos_disponiveis) if self.tv_mus_produtos_disponiveis is not None else '',
            'produto_playhub': self._serialize_enum_and_str(self.produto_playhub) if self.produto_playhub is not None else '',
            'tariff_plan': self._serialize_enum_and_str(self.tariff_plan) if self.tariff_plan is not None else '',
            'tv_dtvgo_produtos_disponiveis': self._serialize_enum_and_str(self.tv_dtvgo_produtos_disponiveis) if self.tv_dtvgo_produtos_disponiveis is not None else '',
            'tv_id_pacotes_adicionais': self._serialize_enum_and_str(self.tv_id_pacotes_adicionais) if self.tv_id_pacotes_adicionais is not None else '',
            'id_integracao_iot': str(self.id_integracao_iot) if self.id_integracao_iot is not None else '',
            'id_produto_iot': self._serialize_enum_and_str(self.id_produto_iot) if self.id_produto_iot is not None else '',
            'tipo_produto_integracao': self._serialize_enum_and_str(self.tipo_produto_integracao) if self.tipo_produto_integracao is not None else '',
            'id_assinatura_integracao': str(self.id_assinatura_integracao) if self.id_assinatura_integracao is not None else '',
            'plataforma_integracao': self._serialize_enum_and_str(self.plataforma_integracao) if self.plataforma_integracao is not None else '',
            'checkbox1': self._serialize_enum_and_str(self.checkbox1) if self.checkbox1 is not None else '',
            'checkbox2': self._serialize_enum_and_str(self.checkbox2) if self.checkbox2 is not None else '',
            'checkbox3': self._serialize_enum_and_str(self.checkbox3) if self.checkbox3 is not None else '',
            'checkbox4': self._serialize_enum_and_str(self.checkbox4) if self.checkbox4 is not None else '',
            'checkbox5': self._serialize_enum_and_str(self.checkbox5) if self.checkbox5 is not None else '',
            'checkbox6': self._serialize_enum_and_str(self.checkbox6) if self.checkbox6 is not None else '',
            'checkbox7': self._serialize_enum_and_str(self.checkbox7) if self.checkbox7 is not None else '',
            'checkbox8': self._serialize_enum_and_str(self.checkbox8) if self.checkbox8 is not None else '',
            'checkbox9': self._serialize_enum_and_str(self.checkbox9) if self.checkbox9 is not None else '',
            'checkbox10': self._serialize_enum_and_str(self.checkbox10) if self.checkbox10 is not None else '',
            'checkbox11': self._serialize_enum_and_str(self.checkbox11) if self.checkbox11 is not None else '',
            'checkbox12': self._serialize_enum_and_str(self.checkbox12) if self.checkbox12 is not None else '',
            'checkbox13': self._serialize_enum_and_str(self.checkbox13) if self.checkbox13 is not None else '',
            'checkbox14': self._serialize_enum_and_str(self.checkbox14) if self.checkbox14 is not None else '',
            'checkbox15': self._serialize_enum_and_str(self.checkbox15) if self.checkbox15 is not None else '',
            'checkbox16': self._serialize_enum_and_str(self.checkbox16) if self.checkbox16 is not None else '',
            'checkbox17': self._serialize_enum_and_str(self.checkbox17) if self.checkbox17 is not None else '',
            'checkbox18': self._serialize_enum_and_str(self.checkbox18) if self.checkbox18 is not None else '',
            'checkbox19': self._serialize_enum_and_str(self.checkbox19) if self.checkbox19 is not None else '',
            'checkbox20': self._serialize_enum_and_str(self.checkbox20) if self.checkbox20 is not None else '',
            'checkbox21': self._serialize_enum_and_str(self.checkbox21) if self.checkbox21 is not None else '',
            'checkbox22': self._serialize_enum_and_str(self.checkbox22) if self.checkbox22 is not None else '',
            'checkbox23': self._serialize_enum_and_str(self.checkbox23) if self.checkbox23 is not None else '',
            'checkbox24': self._serialize_enum_and_str(self.checkbox24) if self.checkbox24 is not None else '',
            'checkbox25': self._serialize_enum_and_str(self.checkbox25) if self.checkbox25 is not None else '',
            'checkbox26': self._serialize_enum_and_str(self.checkbox26) if self.checkbox26 is not None else '',
            'checkbox27': self._serialize_enum_and_str(self.checkbox27) if self.checkbox27 is not None else '',
            'checkbox28': self._serialize_enum_and_str(self.checkbox28) if self.checkbox28 is not None else '',
            'checkbox29': self._serialize_enum_and_str(self.checkbox29) if self.checkbox29 is not None else '',
            'checkbox30': self._serialize_enum_and_str(self.checkbox30) if self.checkbox30 is not None else '',
            'checkbox31': self._serialize_enum_and_str(self.checkbox31) if self.checkbox31 is not None else '',
            'checkbox32': self._serialize_enum_and_str(self.checkbox32) if self.checkbox32 is not None else '',
            'checkbox33': self._serialize_enum_and_str(self.checkbox33) if self.checkbox33 is not None else '',
            'checkbox34': self._serialize_enum_and_str(self.checkbox34) if self.checkbox34 is not None else '',
            'checkbox35': self._serialize_enum_and_str(self.checkbox35) if self.checkbox35 is not None else '',
            'checkbox36': self._serialize_enum_and_str(self.checkbox36) if self.checkbox36 is not None else '',
            'checkbox37': self._serialize_enum_and_str(self.checkbox37) if self.checkbox37 is not None else '',
            'checkbox38': self._serialize_enum_and_str(self.checkbox38) if self.checkbox38 is not None else '',
            'checkbox39': self._serialize_enum_and_str(self.checkbox39) if self.checkbox39 is not None else '',
            'checkbox40': self._serialize_enum_and_str(self.checkbox40) if self.checkbox40 is not None else '',
            'chassi': self._serialize_enum_and_str(self.chassi) if self.chassi is not None else '',
            'renavan': self._serialize_enum_and_str(self.renavan) if self.renavan is not None else '',
            'km': self._serialize_enum_and_str(self.km) if self.km is not None else '',
            'veiculo_cor': self._serialize_enum_and_str(self.veiculo_cor) if self.veiculo_cor is not None else '',
            'cambio': self._serialize_enum_and_str(self.cambio) if self.cambio is not None else '',
            'qtdportas': self._serialize_enum_and_str(self.qtdportas) if self.qtdportas is not None else '',
            'veiculo_combustivel': self._serialize_enum_and_str(self.veiculo_combustivel) if self.veiculo_combustivel is not None else '',
            'integrador': str(self.integrador) if self.integrador is not None else '',
            'limite_pacote': self._serialize_enum_and_str(self.limite_pacote) if self.limite_pacote is not None else '',
            'valor_adicional_pacote': self._serialize_enum_and_str(self.valor_adicional_pacote) if self.valor_adicional_pacote is not None else '',
        }
        return {key: serialize(value) for key, value in data.items()}

    def is_valid(self) -> bool:
        return self.ativo is not None and self.descricao is not None and self.tipo is not None and self.controla_estoque is not None and self.movimentacao is not None and self.id_sub_grupo is not None and self.unidade is not None and self.preco_base is not None and self.aceita_valor is not None and self.icms_issqn is not None
