from __future__ import annotations
from typing import Optional
from ORM_IXC.interfaces import IModelWithId
from ORM_IXC.enums.movimentoDeProdutos import *
from ORM_IXC.statemants.maps.mapper import Mapped, field as mapped_field
from ORM_IXC.statemants.maps.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel


@MetaModels
class MovimentoDeProdutosModel(IModelWithId, BaseModel):
    id_produto :Mapped[int]
    id_unidade :Mapped[int]
    id_almox :Mapped[int]
    quantidade :Mapped[str]
    valor_unitario :Mapped[str]
    valor_total :Mapped[str]
    estoque :Mapped[str]
    tipo :Mapped[str]
    unidade_sigla :Mapped[str]
    dica_outras_despesas :Mapped[str]
    id :Mapped[Optional[int]]
    tipo_preenchimento_tributacao :Mapped[Optional[Tipo_preenchimento_tributacaoEnum]] = mapped_field(None)
    codigo_fornecedor :Mapped[Optional[int]] = mapped_field(None)
    descricao_fornecedor :Mapped[Optional[str]] = mapped_field('')
    descricao :Mapped[Optional[str]] = mapped_field('')
    label_produto_pratrimonial :Mapped[Optional[str]] = mapped_field('')
    garantia_ate :Mapped[Optional[str]] = mapped_field('')
    fieldset_utiliza_fator_conversao :Mapped[Optional[str]] = mapped_field('')
    label_info_qtde_produto_patrimonial :Mapped[Optional[str]] = mapped_field('')
    pdesconto :Mapped[Optional[str]] = mapped_field('')
    valor_frete :Mapped[Optional[str]] = mapped_field('')
    vdesconto :Mapped[Optional[str]] = mapped_field('')
    id_itens_pedido :Mapped[Optional[str]] = mapped_field('')
    id_entrada :Mapped[Optional[str]] = mapped_field('')
    id_pedido_compra :Mapped[Optional[str]] = mapped_field('')
    id_pedido_compra_itens :Mapped[Optional[str]] = mapped_field('')
    qtde_saida :Mapped[Optional[str]] = mapped_field('')
    id_inventario :Mapped[Optional[str]] = mapped_field('')
    data :Mapped[Optional[str]] = mapped_field('')
    filial_id :Mapped[Optional[str]] = mapped_field('')
    fator_conversao :Mapped[Optional[str]] = mapped_field('')
    id_negociacao :Mapped[Optional[str]] = mapped_field('')
    tipo_produto :Mapped[Optional[str]] = mapped_field('')
    id_transf_almox_item :Mapped[Optional[str]] = mapped_field('')
    id_moeda :Mapped[Optional[str]] = mapped_field('')
    id_estrutura :Mapped[Optional[str]] = mapped_field('')
    imobilizado :Mapped[Optional[str]] = mapped_field('')
    eh_importacao_xml :Mapped[Optional[str]] = mapped_field('')
    ultima_atualizacao :Mapped[Optional[str]] = mapped_field('')
    id_saida :Mapped[Optional[str]] = mapped_field('')
    origem_movimento :Mapped[Optional[str]] = mapped_field('')
    mac :Mapped[Optional[str]] = mapped_field('')
    numero_serie :Mapped[Optional[str]] = mapped_field('')
    tributacao_digitada :Mapped[Optional[str]] = mapped_field('')
    id_class_fiscal :Mapped[Optional[int]] = mapped_field(None)
    cfop :Mapped[Optional[int]] = mapped_field(None)
    ncm :Mapped[Optional[int]] = mapped_field(None)
    icms_sn_stributaria :Mapped[Optional[Icms_sn_stributariaEnum]] = mapped_field(None)
    valor_icm :Mapped[Optional[str]] = mapped_field('')
    valor_fcp :Mapped[Optional[str]] = mapped_field('')
    valor_ipi :Mapped[Optional[str]] = mapped_field('')
    iss_valor :Mapped[Optional[str]] = mapped_field('')
    valor_icms_st :Mapped[Optional[str]] = mapped_field('')
    valor_fcp_st :Mapped[Optional[str]] = mapped_field('')
    valor_outros :Mapped[Optional[str]] = mapped_field('')
    pis_retido_valor :Mapped[Optional[str]] = mapped_field('')
    cofins_retido_valor :Mapped[Optional[str]] = mapped_field('')
    csll_valor :Mapped[Optional[str]] = mapped_field('')
    irrf_valor :Mapped[Optional[str]] = mapped_field('')
    inss_valor :Mapped[Optional[str]] = mapped_field('')
    iss_valor_retido :Mapped[Optional[str]] = mapped_field('')
    forma_tributacao :Mapped[Optional[Forma_tributacaoEnum]] = mapped_field(None)
    cod_classificacao_tribut_cbs_ibs :Mapped[Optional[Cod_classificacao_tribut_cbs_ibsEnum]] = mapped_field(None)
    cod_situacao_tribut_cbs_ibs :Mapped[Optional[str]] = mapped_field('')
    cbs_ibs_base_calculo :Mapped[Optional[str]] = mapped_field('')
    reducao_aliquota :Mapped[Optional[str]] = mapped_field('')
    cbs_aliquota :Mapped[Optional[str]] = mapped_field('')
    aliquota_cbs_efetiva :Mapped[Optional[str]] = mapped_field('')
    cbs_valor :Mapped[Optional[str]] = mapped_field('')
    ibs_estadual_aliquota :Mapped[Optional[str]] = mapped_field('')
    aliquota_ibs_efetiva :Mapped[Optional[str]] = mapped_field('')
    ibs_estadual_valor :Mapped[Optional[str]] = mapped_field('')
    ibs_municipal_aliquota :Mapped[Optional[str]] = mapped_field('')
    aliquota_ibs_efetiva_munic :Mapped[Optional[str]] = mapped_field('')
    ibs_municipal_valor :Mapped[Optional[str]] = mapped_field('')
    valor_ibs :Mapped[Optional[str]] = mapped_field('')
    html :Mapped[Optional[str]] = mapped_field('')

    @property
    def table(self) -> str:
        return "movimento_produtos"

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
            'id_produto': str(self.id_produto) if self.id_produto is not None else '',
            'id_unidade': str(self.id_unidade) if self.id_unidade is not None else '',
            'id_almox': str(self.id_almox) if self.id_almox is not None else '',
            'quantidade': self._serialize_enum_and_str(self.quantidade) if self.quantidade is not None else '',
            'valor_unitario': self._serialize_enum_and_str(self.valor_unitario) if self.valor_unitario is not None else '',
            'valor_total': self._serialize_enum_and_str(self.valor_total) if self.valor_total is not None else '',
            'estoque': self._serialize_enum_and_str(self.estoque) if self.estoque is not None else '',
            'tipo': self._serialize_enum_and_str(self.tipo) if self.tipo is not None else '',
            'unidade_sigla': self._serialize_enum_and_str(self.unidade_sigla) if self.unidade_sigla is not None else '',
            'dica_outras_despesas': self._serialize_enum_and_str(self.dica_outras_despesas) if self.dica_outras_despesas is not None else '',
            'id': str(self.id) if self.id is not None else '',
            'tipo_preenchimento_tributacao': self._serialize_enum_and_str(self.tipo_preenchimento_tributacao) if self.tipo_preenchimento_tributacao is not None else '',
            'codigo_fornecedor': str(self.codigo_fornecedor) if self.codigo_fornecedor is not None else '',
            'descricao_fornecedor': self._serialize_enum_and_str(self.descricao_fornecedor) if self.descricao_fornecedor is not None else '',
            'descricao': self._serialize_enum_and_str(self.descricao) if self.descricao is not None else '',
            'label_produto_pratrimonial': self._serialize_enum_and_str(self.label_produto_pratrimonial) if self.label_produto_pratrimonial is not None else '',
            'garantia_ate': self._serialize_enum_and_str(self.garantia_ate) if self.garantia_ate is not None else '',
            'fieldset_utiliza_fator_conversao': self._serialize_enum_and_str(self.fieldset_utiliza_fator_conversao) if self.fieldset_utiliza_fator_conversao is not None else '',
            'label_info_qtde_produto_patrimonial': self._serialize_enum_and_str(self.label_info_qtde_produto_patrimonial) if self.label_info_qtde_produto_patrimonial is not None else '',
            'pdesconto': self._serialize_enum_and_str(self.pdesconto) if self.pdesconto is not None else '',
            'valor_frete': self._serialize_enum_and_str(self.valor_frete) if self.valor_frete is not None else '',
            'vdesconto': self._serialize_enum_and_str(self.vdesconto) if self.vdesconto is not None else '',
            'id_itens_pedido': self._serialize_enum_and_str(self.id_itens_pedido) if self.id_itens_pedido is not None else '',
            'id_entrada': self._serialize_enum_and_str(self.id_entrada) if self.id_entrada is not None else '',
            'id_pedido_compra': self._serialize_enum_and_str(self.id_pedido_compra) if self.id_pedido_compra is not None else '',
            'id_pedido_compra_itens': self._serialize_enum_and_str(self.id_pedido_compra_itens) if self.id_pedido_compra_itens is not None else '',
            'qtde_saida': self._serialize_enum_and_str(self.qtde_saida) if self.qtde_saida is not None else '',
            'id_inventario': self._serialize_enum_and_str(self.id_inventario) if self.id_inventario is not None else '',
            'data': self._serialize_enum_and_str(self.data) if self.data is not None else '',
            'filial_id': self._serialize_enum_and_str(self.filial_id) if self.filial_id is not None else '',
            'fator_conversao': self._serialize_enum_and_str(self.fator_conversao) if self.fator_conversao is not None else '',
            'id_negociacao': self._serialize_enum_and_str(self.id_negociacao) if self.id_negociacao is not None else '',
            'tipo_produto': self._serialize_enum_and_str(self.tipo_produto) if self.tipo_produto is not None else '',
            'id_transf_almox_item': self._serialize_enum_and_str(self.id_transf_almox_item) if self.id_transf_almox_item is not None else '',
            'id_moeda': self._serialize_enum_and_str(self.id_moeda) if self.id_moeda is not None else '',
            'id_estrutura': self._serialize_enum_and_str(self.id_estrutura) if self.id_estrutura is not None else '',
            'imobilizado': self._serialize_enum_and_str(self.imobilizado) if self.imobilizado is not None else '',
            'eh_importacao_xml': self._serialize_enum_and_str(self.eh_importacao_xml) if self.eh_importacao_xml is not None else '',
            'ultima_atualizacao': self._serialize_enum_and_str(self.ultima_atualizacao) if self.ultima_atualizacao is not None else '',
            'id_saida': self._serialize_enum_and_str(self.id_saida) if self.id_saida is not None else '',
            'origem_movimento': self._serialize_enum_and_str(self.origem_movimento) if self.origem_movimento is not None else '',
            'mac': self._serialize_enum_and_str(self.mac) if self.mac is not None else '',
            'numero_serie': self._serialize_enum_and_str(self.numero_serie) if self.numero_serie is not None else '',
            'tributacao_digitada': self._serialize_enum_and_str(self.tributacao_digitada) if self.tributacao_digitada is not None else '',
            'id_class_fiscal': str(self.id_class_fiscal) if self.id_class_fiscal is not None else '',
            'cfop': str(self.cfop) if self.cfop is not None else '',
            'ncm': str(self.ncm) if self.ncm is not None else '',
            'icms_sn_stributaria': self._serialize_enum_and_str(self.icms_sn_stributaria) if self.icms_sn_stributaria is not None else '',
            'valor_icm': self._serialize_enum_and_str(self.valor_icm) if self.valor_icm is not None else '',
            'valor_fcp': self._serialize_enum_and_str(self.valor_fcp) if self.valor_fcp is not None else '',
            'valor_ipi': self._serialize_enum_and_str(self.valor_ipi) if self.valor_ipi is not None else '',
            'iss_valor': self._serialize_enum_and_str(self.iss_valor) if self.iss_valor is not None else '',
            'valor_icms_st': self._serialize_enum_and_str(self.valor_icms_st) if self.valor_icms_st is not None else '',
            'valor_fcp_st': self._serialize_enum_and_str(self.valor_fcp_st) if self.valor_fcp_st is not None else '',
            'valor_outros': self._serialize_enum_and_str(self.valor_outros) if self.valor_outros is not None else '',
            'pis_retido_valor': self._serialize_enum_and_str(self.pis_retido_valor) if self.pis_retido_valor is not None else '',
            'cofins_retido_valor': self._serialize_enum_and_str(self.cofins_retido_valor) if self.cofins_retido_valor is not None else '',
            'csll_valor': self._serialize_enum_and_str(self.csll_valor) if self.csll_valor is not None else '',
            'irrf_valor': self._serialize_enum_and_str(self.irrf_valor) if self.irrf_valor is not None else '',
            'inss_valor': self._serialize_enum_and_str(self.inss_valor) if self.inss_valor is not None else '',
            'iss_valor_retido': self._serialize_enum_and_str(self.iss_valor_retido) if self.iss_valor_retido is not None else '',
            'forma_tributacao': self._serialize_enum_and_str(self.forma_tributacao) if self.forma_tributacao is not None else '',
            'cod_classificacao_tribut_cbs_ibs': self._serialize_enum_and_str(self.cod_classificacao_tribut_cbs_ibs) if self.cod_classificacao_tribut_cbs_ibs is not None else '',
            'cod_situacao_tribut_cbs_ibs': self._serialize_enum_and_str(self.cod_situacao_tribut_cbs_ibs) if self.cod_situacao_tribut_cbs_ibs is not None else '',
            'cbs_ibs_base_calculo': self._serialize_enum_and_str(self.cbs_ibs_base_calculo) if self.cbs_ibs_base_calculo is not None else '',
            'reducao_aliquota': self._serialize_enum_and_str(self.reducao_aliquota) if self.reducao_aliquota is not None else '',
            'cbs_aliquota': self._serialize_enum_and_str(self.cbs_aliquota) if self.cbs_aliquota is not None else '',
            'aliquota_cbs_efetiva': self._serialize_enum_and_str(self.aliquota_cbs_efetiva) if self.aliquota_cbs_efetiva is not None else '',
            'cbs_valor': self._serialize_enum_and_str(self.cbs_valor) if self.cbs_valor is not None else '',
            'ibs_estadual_aliquota': self._serialize_enum_and_str(self.ibs_estadual_aliquota) if self.ibs_estadual_aliquota is not None else '',
            'aliquota_ibs_efetiva': self._serialize_enum_and_str(self.aliquota_ibs_efetiva) if self.aliquota_ibs_efetiva is not None else '',
            'ibs_estadual_valor': self._serialize_enum_and_str(self.ibs_estadual_valor) if self.ibs_estadual_valor is not None else '',
            'ibs_municipal_aliquota': self._serialize_enum_and_str(self.ibs_municipal_aliquota) if self.ibs_municipal_aliquota is not None else '',
            'aliquota_ibs_efetiva_munic': self._serialize_enum_and_str(self.aliquota_ibs_efetiva_munic) if self.aliquota_ibs_efetiva_munic is not None else '',
            'ibs_municipal_valor': self._serialize_enum_and_str(self.ibs_municipal_valor) if self.ibs_municipal_valor is not None else '',
            'valor_ibs': self._serialize_enum_and_str(self.valor_ibs) if self.valor_ibs is not None else '',
            'html': self._serialize_enum_and_str(self.html) if self.html is not None else '',
        }
        return {key: serialize(value) for key, value in data.items()}

    def is_valid(self) -> bool:
        return self.id_produto is not None and self.id_unidade is not None and self.id_almox is not None and self.quantidade is not None and self.valor_unitario is not None and self.valor_total is not None and self.estoque is not None and self.tipo is not None and self.unidade_sigla is not None and self.dica_outras_despesas is not None
