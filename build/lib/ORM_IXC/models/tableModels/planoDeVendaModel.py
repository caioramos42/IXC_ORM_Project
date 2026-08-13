from __future__ import annotations
from typing import Optional
from ORM_IXC.interfaces import IModelWithId
from ORM_IXC.enums.planoDeVenda import *
from ORM_IXC.statemants.maps.mapper import Mapped, field as mapped_field
from ORM_IXC.statemants.maps.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel


@MetaModels
class PlanoDeVendaModel(IModelWithId, BaseModel):
    tipo :Mapped[TipoEnum]
    tipo_pessoa :Mapped[Tipo_pessoaEnum]
    nome :Mapped[str]
    id :Mapped[Optional[int]]
    descricao :Mapped[Optional[str]] = mapped_field('')
    moeda :Mapped[Optional[int]] = mapped_field(None)
    id_tipo_documento :Mapped[Optional[int]] = mapped_field(None)
    id_modelo :Mapped[Optional[int]] = mapped_field(None)
    id_carteira_cobranca :Mapped[Optional[int]] = mapped_field(None)
    id_vendedor :Mapped[Optional[int]] = mapped_field(None)
    id_filial :Mapped[Optional[int]] = mapped_field(None)
    comissao :Mapped[Optional[str]] = mapped_field('')
    valor_contrato :Mapped[Optional[str]] = mapped_field('')
    limitar_n_logins :Mapped[Optional[str]] = mapped_field('')
    logins_simultaneos :Mapped[Optional[str]] = mapped_field('')
    Ativo :Mapped[Optional[AtivoEnum]] = mapped_field(None)
    base_geracao_por_tipo_doc :Mapped[Optional[Base_geracao_por_tipo_docEnum]] = mapped_field(None)
    tipo_doc_opc :Mapped[Optional[int]] = mapped_field(None)
    tipo_doc_opc2 :Mapped[Optional[int]] = mapped_field(None)
    tipo_doc_opc3 :Mapped[Optional[int]] = mapped_field(None)
    tipo_doc_opc4 :Mapped[Optional[int]] = mapped_field(None)
    ultima_atualizacao :Mapped[Optional[str]] = mapped_field('')
    tel_franquia_segundos :Mapped[Optional[str]] = mapped_field('')
    tel_franquia_prefix :Mapped[Optional[str]] = mapped_field('')
    id_cidade :Mapped[Optional[int]] = mapped_field(None)
    id_tipo_doc_ativ :Mapped[Optional[int]] = mapped_field(None)
    id_produto_ativ :Mapped[Optional[int]] = mapped_field(None)
    id_cond_pag_ativ :Mapped[Optional[int]] = mapped_field(None)
    id_vendedor_ativ :Mapped[Optional[int]] = mapped_field(None)
    fidelidade :Mapped[Optional[str]] = mapped_field('')
    utilizar_desconto_ate_vencimento :Mapped[Optional[Utilizar_desconto_ate_vencimentoEnum]] = mapped_field(None)
    utilizar_desconto_por_repeticao :Mapped[Optional[Utilizar_desconto_por_repeticaoEnum]] = mapped_field(None)
    utilizar_desconto_no_produto_plano :Mapped[Optional[Utilizar_desconto_no_produto_planoEnum]] = mapped_field(None)
    qtde_repeticoes_desconto :Mapped[Optional[str]] = mapped_field('')
    id_produto_ate_vencimento :Mapped[Optional[int]] = mapped_field(None)
    id_produto_contrato_vinc :Mapped[Optional[int]] = mapped_field(None)
    valor_desconto :Mapped[Optional[str]] = mapped_field('')

    @property
    def table(self) -> str:
        return "vd_contratos"

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
            'tipo': self._serialize_enum_and_str(self.tipo) if self.tipo is not None else '',
            'tipo_pessoa': self._serialize_enum_and_str(self.tipo_pessoa) if self.tipo_pessoa is not None else '',
            'nome': self._serialize_enum_and_str(self.nome) if self.nome is not None else '',
            'id': str(self.id) if self.id is not None else '',
            'descricao': self._serialize_enum_and_str(self.descricao) if self.descricao is not None else '',
            'moeda': str(self.moeda) if self.moeda is not None else '',
            'id_tipo_documento': str(self.id_tipo_documento) if self.id_tipo_documento is not None else '',
            'id_modelo': str(self.id_modelo) if self.id_modelo is not None else '',
            'id_carteira_cobranca': str(self.id_carteira_cobranca) if self.id_carteira_cobranca is not None else '',
            'id_vendedor': str(self.id_vendedor) if self.id_vendedor is not None else '',
            'id_filial': str(self.id_filial) if self.id_filial is not None else '',
            'comissao': self._serialize_enum_and_str(self.comissao) if self.comissao is not None else '',
            'valor_contrato': self._serialize_enum_and_str(self.valor_contrato) if self.valor_contrato is not None else '',
            'limitar_n_logins': self._serialize_enum_and_str(self.limitar_n_logins) if self.limitar_n_logins is not None else '',
            'logins_simultaneos': self._serialize_enum_and_str(self.logins_simultaneos) if self.logins_simultaneos is not None else '',
            'Ativo': self._serialize_enum_and_str(self.Ativo) if self.Ativo is not None else '',
            'base_geracao_por_tipo_doc': self._serialize_enum_and_str(self.base_geracao_por_tipo_doc) if self.base_geracao_por_tipo_doc is not None else '',
            'tipo_doc_opc': str(self.tipo_doc_opc) if self.tipo_doc_opc is not None else '',
            'tipo_doc_opc2': str(self.tipo_doc_opc2) if self.tipo_doc_opc2 is not None else '',
            'tipo_doc_opc3': str(self.tipo_doc_opc3) if self.tipo_doc_opc3 is not None else '',
            'tipo_doc_opc4': str(self.tipo_doc_opc4) if self.tipo_doc_opc4 is not None else '',
            'ultima_atualizacao': self._serialize_enum_and_str(self.ultima_atualizacao) if self.ultima_atualizacao is not None else '',
            'tel_franquia_segundos': self._serialize_enum_and_str(self.tel_franquia_segundos) if self.tel_franquia_segundos is not None else '',
            'tel_franquia_prefix': self._serialize_enum_and_str(self.tel_franquia_prefix) if self.tel_franquia_prefix is not None else '',
            'id_cidade': str(self.id_cidade) if self.id_cidade is not None else '',
            'id_tipo_doc_ativ': str(self.id_tipo_doc_ativ) if self.id_tipo_doc_ativ is not None else '',
            'id_produto_ativ': str(self.id_produto_ativ) if self.id_produto_ativ is not None else '',
            'id_cond_pag_ativ': str(self.id_cond_pag_ativ) if self.id_cond_pag_ativ is not None else '',
            'id_vendedor_ativ': str(self.id_vendedor_ativ) if self.id_vendedor_ativ is not None else '',
            'fidelidade': self._serialize_enum_and_str(self.fidelidade) if self.fidelidade is not None else '',
            'utilizar_desconto_ate_vencimento': self._serialize_enum_and_str(self.utilizar_desconto_ate_vencimento) if self.utilizar_desconto_ate_vencimento is not None else '',
            'utilizar_desconto_por_repeticao': self._serialize_enum_and_str(self.utilizar_desconto_por_repeticao) if self.utilizar_desconto_por_repeticao is not None else '',
            'utilizar_desconto_no_produto_plano': self._serialize_enum_and_str(self.utilizar_desconto_no_produto_plano) if self.utilizar_desconto_no_produto_plano is not None else '',
            'qtde_repeticoes_desconto': self._serialize_enum_and_str(self.qtde_repeticoes_desconto) if self.qtde_repeticoes_desconto is not None else '',
            'id_produto_ate_vencimento': str(self.id_produto_ate_vencimento) if self.id_produto_ate_vencimento is not None else '',
            'id_produto_contrato_vinc': str(self.id_produto_contrato_vinc) if self.id_produto_contrato_vinc is not None else '',
            'valor_desconto': self._serialize_enum_and_str(self.valor_desconto) if self.valor_desconto is not None else '',
        }
        return {key: serialize(value) for key, value in data.items()}

    def is_valid(self) -> bool:
        return self.tipo is not None and self.tipo_pessoa is not None and self.nome is not None
