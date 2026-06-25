from __future__ import annotations
from typing import Optional
from ORM_IXC.interfaces.IModel import IModelWithId
from ORM_IXC.enums.tipoDocumento import *
from ORM_IXC.statemants.maps.mapper import Mapped, field as mapped_field
from ORM_IXC.statemants.maps.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel


@MetaModels
class TipoDocumentoModel(IModelWithId, BaseModel):
    codigo :Mapped[str]
    tipo_documento :Mapped[str]
    tipo :Mapped[TipoEnum]
    gera_finan :Mapped[Gera_finanEnum]
    gera_contab :Mapped[Gera_contabEnum]
    gera_fiscal :Mapped[Gera_fiscalEnum]
    gera_estoque :Mapped[Gera_estoqueEnum]
    regime_tributario :Mapped[Regime_tributarioEnum]
    nf_importacao :Mapped[Nf_importacaoEnum]
    mask_entrada_quantidade :Mapped[str]
    mask_entrada_valor_unit :Mapped[str]
    tipo_rateio_frete :Mapped[Tipo_rateio_freteEnum]
    mask_saida_quantidade :Mapped[str]
    mask_saida_valor_unit :Mapped[str]
    gera_servicos :Mapped[Gera_servicosEnum]
    financeiro_liberado :Mapped[Financeiro_liberadoEnum]
    dica_ajusta_patrimonio :Mapped[str]
    dica_imposto_retido :Mapped[str]
    id :Mapped[Optional[int]]
    modelo_impressao_nota :Mapped[Optional[int]] = mapped_field(None)
    endereco_padrao_alert :Mapped[Optional[str]] = mapped_field('')
    id_filial :Mapped[Optional[int]] = mapped_field(None)
    ultima_atualizacao :Mapped[Optional[str]] = mapped_field('')
    isento_iva_col :Mapped[Optional[Isento_iva_colEnum]] = mapped_field(None)
    tipo_tributacao :Mapped[Optional[Tipo_tributacaoEnum]] = mapped_field(None)
    modelo_nf :Mapped[Optional[str]] = mapped_field('')
    serie_nf :Mapped[Optional[str]] = mapped_field('')
    finalidade_nfe_tipo_doc :Mapped[Optional[Finalidade_nfe_tipo_docEnum]] = mapped_field(None)
    tp_nota_debito :Mapped[Optional[Tp_nota_debitoEnum]] = mapped_field(None)
    tp_nota_credito :Mapped[Optional[Tp_nota_creditoEnum]] = mapped_field(None)
    natureza_dentro_estado :Mapped[Optional[int]] = mapped_field(None)
    natureza_fora_estado :Mapped[Optional[int]] = mapped_field(None)
    indPres :Mapped[Optional[IndPresEnum]] = mapped_field(None)
    exibir_tributos_csll_irrf :Mapped[Optional[Exibir_tributos_csll_irrfEnum]] = mapped_field(None)
    impostometro :Mapped[Optional[ImpostometroEnum]] = mapped_field(None)
    descricao_produto_nf :Mapped[Optional[Descricao_produto_nfEnum]] = mapped_field(None)
    desc_prod_arq_fiscais :Mapped[Optional[Desc_prod_arq_fiscaisEnum]] = mapped_field(None)
    gerar_produtos_valor_zerado :Mapped[Optional[Gerar_produtos_valor_zeradoEnum]] = mapped_field(None)
    converter_tributacao_entrada_xml :Mapped[Optional[Converter_tributacao_entrada_xmlEnum]] = mapped_field(None)
    soma_frete_base_calc :Mapped[Optional[Soma_frete_base_calcEnum]] = mapped_field(None)
    soma_voutros_base_calc :Mapped[Optional[Soma_voutros_base_calcEnum]] = mapped_field(None)
    soma_frete_base_calc_pis_cofins :Mapped[Optional[Soma_frete_base_calc_pis_cofinsEnum]] = mapped_field(None)
    soma_voutros_base_calc_pis_cofins :Mapped[Optional[Soma_voutros_base_calc_pis_cofinsEnum]] = mapped_field(None)
    nat_bc_cred :Mapped[Optional[Nat_bc_credEnum]] = mapped_field(None)
    gera_servicos_nf :Mapped[Optional[Gera_servicos_nfEnum]] = mapped_field(None)
    gera_internet :Mapped[Optional[Gera_internetEnum]] = mapped_field(None)
    gera_mercadoria :Mapped[Optional[Gera_mercadoriaEnum]] = mapped_field(None)
    gera_telefonia :Mapped[Optional[Gera_telefoniaEnum]] = mapped_field(None)
    gera_sva :Mapped[Optional[Gera_svaEnum]] = mapped_field(None)
    gera_smp :Mapped[Optional[Gera_smpEnum]] = mapped_field(None)
    gera_tv :Mapped[Optional[Gera_tvEnum]] = mapped_field(None)
    gera_fcem_sped :Mapped[Optional[Gera_fcem_spedEnum]] = mapped_field(None)
    alterar_descricao_nf :Mapped[Optional[Alterar_descricao_nfEnum]] = mapped_field(None)
    natureza_operacao :Mapped[Optional[str]] = mapped_field('')
    nf_complementar_tp_doc :Mapped[Optional[str]] = mapped_field('')
    nf_complementar_comodato_saida :Mapped[Optional[str]] = mapped_field('')
    nf_complementar_comodato_entrada :Mapped[Optional[str]] = mapped_field('')
    dica_nota_complementar_comodato_mov :Mapped[Optional[str]] = mapped_field('')
    modelo_impressao_nota_col :Mapped[Optional[str]] = mapped_field('')
    descricao_modelo_impressao :Mapped[Optional[str]] = mapped_field('')
    numero_automatico_fatura_siigo_col :Mapped[Optional[Numero_automatico_fatura_siigo_colEnum]] = mapped_field(None)
    atualiza_custo_medio :Mapped[Optional[Atualiza_custo_medioEnum]] = mapped_field(None)
    emite_nfe_entrada :Mapped[Optional[Emite_nfe_entradaEnum]] = mapped_field(None)
    id_almox_padrao :Mapped[Optional[int]] = mapped_field(None)
    controle_estoque :Mapped[Optional[Controle_estoqueEnum]] = mapped_field(None)
    ajusta_patrimonio :Mapped[Optional[Ajusta_patrimonioEnum]] = mapped_field(None)
    ir_desconta_pis_retido_total :Mapped[Optional[str]] = mapped_field('')
    ir_desconta_cofins_retido_total :Mapped[Optional[str]] = mapped_field('')
    ir_desconta_csll_retido_total :Mapped[Optional[str]] = mapped_field('')
    ir_desconta_irrf_retido_total :Mapped[Optional[str]] = mapped_field('')
    ir_desconta_inss_retido_total :Mapped[Optional[str]] = mapped_field('')
    ir_desconta_iss_retido_total :Mapped[Optional[str]] = mapped_field('')
    cst_pis_tipo_doc :Mapped[Optional[Cst_pis_tipo_docEnum]] = mapped_field(None)
    aliquota_pis_tipo_doc :Mapped[Optional[str]] = mapped_field('')
    cst_cofins_tipo_doc :Mapped[Optional[Cst_cofins_tipo_docEnum]] = mapped_field(None)
    aliquota_cofins_tipo_doc :Mapped[Optional[str]] = mapped_field('')
    id_cnf_grade_ctb :Mapped[Optional[int]] = mapped_field(None)
    id_cnf_grade_ctb_cancelamento :Mapped[Optional[int]] = mapped_field(None)
    regime_contabilizacao :Mapped[Optional[Regime_contabilizacaoEnum]] = mapped_field(None)
    codigo_classificacao_sped :Mapped[Optional[Codigo_classificacao_spedEnum]] = mapped_field(None)
    tipo_receita_sped :Mapped[Optional[Tipo_receita_spedEnum]] = mapped_field(None)
    grupo_tensao_energia :Mapped[Optional[Grupo_tensao_energiaEnum]] = mapped_field(None)
    tipo_ligacao_energia :Mapped[Optional[Tipo_ligacao_energiaEnum]] = mapped_field(None)
    codigo_consumo_energia :Mapped[Optional[Codigo_consumo_energiaEnum]] = mapped_field(None)

    @property
    def table(self) -> str:
        return "tipo_documento"

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
            'codigo': self._serialize_enum_and_str(self.codigo) if self.codigo is not None else '',
            'tipo_documento': self._serialize_enum_and_str(self.tipo_documento) if self.tipo_documento is not None else '',
            'tipo': self._serialize_enum_and_str(self.tipo) if self.tipo is not None else '',
            'gera_finan': self._serialize_enum_and_str(self.gera_finan) if self.gera_finan is not None else '',
            'gera_contab': self._serialize_enum_and_str(self.gera_contab) if self.gera_contab is not None else '',
            'gera_fiscal': self._serialize_enum_and_str(self.gera_fiscal) if self.gera_fiscal is not None else '',
            'gera_estoque': self._serialize_enum_and_str(self.gera_estoque) if self.gera_estoque is not None else '',
            'regime_tributario': self._serialize_enum_and_str(self.regime_tributario) if self.regime_tributario is not None else '',
            'nf_importacao': self._serialize_enum_and_str(self.nf_importacao) if self.nf_importacao is not None else '',
            'mask_entrada_quantidade': self._serialize_enum_and_str(self.mask_entrada_quantidade) if self.mask_entrada_quantidade is not None else '',
            'mask_entrada_valor_unit': self._serialize_enum_and_str(self.mask_entrada_valor_unit) if self.mask_entrada_valor_unit is not None else '',
            'tipo_rateio_frete': self._serialize_enum_and_str(self.tipo_rateio_frete) if self.tipo_rateio_frete is not None else '',
            'mask_saida_quantidade': self._serialize_enum_and_str(self.mask_saida_quantidade) if self.mask_saida_quantidade is not None else '',
            'mask_saida_valor_unit': self._serialize_enum_and_str(self.mask_saida_valor_unit) if self.mask_saida_valor_unit is not None else '',
            'gera_servicos': self._serialize_enum_and_str(self.gera_servicos) if self.gera_servicos is not None else '',
            'financeiro_liberado': self._serialize_enum_and_str(self.financeiro_liberado) if self.financeiro_liberado is not None else '',
            'dica_ajusta_patrimonio': self._serialize_enum_and_str(self.dica_ajusta_patrimonio) if self.dica_ajusta_patrimonio is not None else '',
            'dica_imposto_retido': self._serialize_enum_and_str(self.dica_imposto_retido) if self.dica_imposto_retido is not None else '',
            'id': str(self.id) if self.id is not None else '',
            'modelo_impressao_nota': str(self.modelo_impressao_nota) if self.modelo_impressao_nota is not None else '',
            'endereco_padrao_alert': self._serialize_enum_and_str(self.endereco_padrao_alert) if self.endereco_padrao_alert is not None else '',
            'id_filial': str(self.id_filial) if self.id_filial is not None else '',
            'ultima_atualizacao': self._serialize_enum_and_str(self.ultima_atualizacao) if self.ultima_atualizacao is not None else '',
            'isento_iva_col': self._serialize_enum_and_str(self.isento_iva_col) if self.isento_iva_col is not None else '',
            'tipo_tributacao': self._serialize_enum_and_str(self.tipo_tributacao) if self.tipo_tributacao is not None else '',
            'modelo_nf': self._serialize_enum_and_str(self.modelo_nf) if self.modelo_nf is not None else '',
            'serie_nf': self._serialize_enum_and_str(self.serie_nf) if self.serie_nf is not None else '',
            'finalidade_nfe_tipo_doc': self._serialize_enum_and_str(self.finalidade_nfe_tipo_doc) if self.finalidade_nfe_tipo_doc is not None else '',
            'tp_nota_debito': self._serialize_enum_and_str(self.tp_nota_debito) if self.tp_nota_debito is not None else '',
            'tp_nota_credito': self._serialize_enum_and_str(self.tp_nota_credito) if self.tp_nota_credito is not None else '',
            'natureza_dentro_estado': str(self.natureza_dentro_estado) if self.natureza_dentro_estado is not None else '',
            'natureza_fora_estado': str(self.natureza_fora_estado) if self.natureza_fora_estado is not None else '',
            'indPres': self._serialize_enum_and_str(self.indPres) if self.indPres is not None else '',
            'exibir_tributos_csll_irrf': self._serialize_enum_and_str(self.exibir_tributos_csll_irrf) if self.exibir_tributos_csll_irrf is not None else '',
            'impostometro': self._serialize_enum_and_str(self.impostometro) if self.impostometro is not None else '',
            'descricao_produto_nf': self._serialize_enum_and_str(self.descricao_produto_nf) if self.descricao_produto_nf is not None else '',
            'desc_prod_arq_fiscais': self._serialize_enum_and_str(self.desc_prod_arq_fiscais) if self.desc_prod_arq_fiscais is not None else '',
            'gerar_produtos_valor_zerado': self._serialize_enum_and_str(self.gerar_produtos_valor_zerado) if self.gerar_produtos_valor_zerado is not None else '',
            'converter_tributacao_entrada_xml': self._serialize_enum_and_str(self.converter_tributacao_entrada_xml) if self.converter_tributacao_entrada_xml is not None else '',
            'soma_frete_base_calc': self._serialize_enum_and_str(self.soma_frete_base_calc) if self.soma_frete_base_calc is not None else '',
            'soma_voutros_base_calc': self._serialize_enum_and_str(self.soma_voutros_base_calc) if self.soma_voutros_base_calc is not None else '',
            'soma_frete_base_calc_pis_cofins': self._serialize_enum_and_str(self.soma_frete_base_calc_pis_cofins) if self.soma_frete_base_calc_pis_cofins is not None else '',
            'soma_voutros_base_calc_pis_cofins': self._serialize_enum_and_str(self.soma_voutros_base_calc_pis_cofins) if self.soma_voutros_base_calc_pis_cofins is not None else '',
            'nat_bc_cred': self._serialize_enum_and_str(self.nat_bc_cred) if self.nat_bc_cred is not None else '',
            'gera_servicos_nf': self._serialize_enum_and_str(self.gera_servicos_nf) if self.gera_servicos_nf is not None else '',
            'gera_internet': self._serialize_enum_and_str(self.gera_internet) if self.gera_internet is not None else '',
            'gera_mercadoria': self._serialize_enum_and_str(self.gera_mercadoria) if self.gera_mercadoria is not None else '',
            'gera_telefonia': self._serialize_enum_and_str(self.gera_telefonia) if self.gera_telefonia is not None else '',
            'gera_sva': self._serialize_enum_and_str(self.gera_sva) if self.gera_sva is not None else '',
            'gera_smp': self._serialize_enum_and_str(self.gera_smp) if self.gera_smp is not None else '',
            'gera_tv': self._serialize_enum_and_str(self.gera_tv) if self.gera_tv is not None else '',
            'gera_fcem_sped': self._serialize_enum_and_str(self.gera_fcem_sped) if self.gera_fcem_sped is not None else '',
            'alterar_descricao_nf': self._serialize_enum_and_str(self.alterar_descricao_nf) if self.alterar_descricao_nf is not None else '',
            'natureza_operacao': self._serialize_enum_and_str(self.natureza_operacao) if self.natureza_operacao is not None else '',
            'nf_complementar_tp_doc': self._serialize_enum_and_str(self.nf_complementar_tp_doc) if self.nf_complementar_tp_doc is not None else '',
            'nf_complementar_comodato_saida': self._serialize_enum_and_str(self.nf_complementar_comodato_saida) if self.nf_complementar_comodato_saida is not None else '',
            'nf_complementar_comodato_entrada': self._serialize_enum_and_str(self.nf_complementar_comodato_entrada) if self.nf_complementar_comodato_entrada is not None else '',
            'dica_nota_complementar_comodato_mov': self._serialize_enum_and_str(self.dica_nota_complementar_comodato_mov) if self.dica_nota_complementar_comodato_mov is not None else '',
            'modelo_impressao_nota_col': self._serialize_enum_and_str(self.modelo_impressao_nota_col) if self.modelo_impressao_nota_col is not None else '',
            'descricao_modelo_impressao': self._serialize_enum_and_str(self.descricao_modelo_impressao) if self.descricao_modelo_impressao is not None else '',
            'numero_automatico_fatura_siigo_col': self._serialize_enum_and_str(self.numero_automatico_fatura_siigo_col) if self.numero_automatico_fatura_siigo_col is not None else '',
            'atualiza_custo_medio': self._serialize_enum_and_str(self.atualiza_custo_medio) if self.atualiza_custo_medio is not None else '',
            'emite_nfe_entrada': self._serialize_enum_and_str(self.emite_nfe_entrada) if self.emite_nfe_entrada is not None else '',
            'id_almox_padrao': str(self.id_almox_padrao) if self.id_almox_padrao is not None else '',
            'controle_estoque': self._serialize_enum_and_str(self.controle_estoque) if self.controle_estoque is not None else '',
            'ajusta_patrimonio': self._serialize_enum_and_str(self.ajusta_patrimonio) if self.ajusta_patrimonio is not None else '',
            'ir_desconta_pis_retido_total': self._serialize_enum_and_str(self.ir_desconta_pis_retido_total) if self.ir_desconta_pis_retido_total is not None else '',
            'ir_desconta_cofins_retido_total': self._serialize_enum_and_str(self.ir_desconta_cofins_retido_total) if self.ir_desconta_cofins_retido_total is not None else '',
            'ir_desconta_csll_retido_total': self._serialize_enum_and_str(self.ir_desconta_csll_retido_total) if self.ir_desconta_csll_retido_total is not None else '',
            'ir_desconta_irrf_retido_total': self._serialize_enum_and_str(self.ir_desconta_irrf_retido_total) if self.ir_desconta_irrf_retido_total is not None else '',
            'ir_desconta_inss_retido_total': self._serialize_enum_and_str(self.ir_desconta_inss_retido_total) if self.ir_desconta_inss_retido_total is not None else '',
            'ir_desconta_iss_retido_total': self._serialize_enum_and_str(self.ir_desconta_iss_retido_total) if self.ir_desconta_iss_retido_total is not None else '',
            'cst_pis_tipo_doc': self._serialize_enum_and_str(self.cst_pis_tipo_doc) if self.cst_pis_tipo_doc is not None else '',
            'aliquota_pis_tipo_doc': self._serialize_enum_and_str(self.aliquota_pis_tipo_doc) if self.aliquota_pis_tipo_doc is not None else '',
            'cst_cofins_tipo_doc': self._serialize_enum_and_str(self.cst_cofins_tipo_doc) if self.cst_cofins_tipo_doc is not None else '',
            'aliquota_cofins_tipo_doc': self._serialize_enum_and_str(self.aliquota_cofins_tipo_doc) if self.aliquota_cofins_tipo_doc is not None else '',
            'id_cnf_grade_ctb': str(self.id_cnf_grade_ctb) if self.id_cnf_grade_ctb is not None else '',
            'id_cnf_grade_ctb_cancelamento': str(self.id_cnf_grade_ctb_cancelamento) if self.id_cnf_grade_ctb_cancelamento is not None else '',
            'regime_contabilizacao': self._serialize_enum_and_str(self.regime_contabilizacao) if self.regime_contabilizacao is not None else '',
            'codigo_classificacao_sped': self._serialize_enum_and_str(self.codigo_classificacao_sped) if self.codigo_classificacao_sped is not None else '',
            'tipo_receita_sped': self._serialize_enum_and_str(self.tipo_receita_sped) if self.tipo_receita_sped is not None else '',
            'grupo_tensao_energia': self._serialize_enum_and_str(self.grupo_tensao_energia) if self.grupo_tensao_energia is not None else '',
            'tipo_ligacao_energia': self._serialize_enum_and_str(self.tipo_ligacao_energia) if self.tipo_ligacao_energia is not None else '',
            'codigo_consumo_energia': self._serialize_enum_and_str(self.codigo_consumo_energia) if self.codigo_consumo_energia is not None else '',
        }
        return {key: serialize(value) for key, value in data.items()}

    def is_valid(self) -> bool:
        return self.codigo is not None and self.tipo_documento is not None and self.tipo is not None and self.gera_finan is not None and self.gera_contab is not None and self.gera_fiscal is not None and self.gera_estoque is not None and self.regime_tributario is not None and self.nf_importacao is not None and self.mask_entrada_quantidade is not None and self.mask_entrada_valor_unit is not None and self.tipo_rateio_frete is not None and self.mask_saida_quantidade is not None and self.mask_saida_valor_unit is not None and self.gera_servicos is not None and self.financeiro_liberado is not None and self.dica_ajusta_patrimonio is not None and self.dica_imposto_retido is not None
