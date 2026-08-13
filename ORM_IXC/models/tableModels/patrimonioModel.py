from __future__ import annotations
from typing import Optional
from ORM_IXC.interfaces import IModelWithId
from ORM_IXC.enums.patrimonio import *
from ORM_IXC.statemants.maps.mapper import Mapped, field as mapped_field
from ORM_IXC.statemants.maps.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel

@MetaModels
class PatrimonioModel(IModelWithId, BaseModel):
    serial :Mapped[str]= mapped_field('')
    id_filial :Mapped[int]= mapped_field('')
    id_produto :Mapped[int]= mapped_field('')
    descricao :Mapped[str]= mapped_field('')
    data_aquisicao :Mapped[str]= mapped_field('')
    id :Mapped[Optional[int]]= mapped_field('')
    id_fornecedor :Mapped[Optional[int]] = mapped_field(None)
    id_mac :Mapped[Optional[str]] = mapped_field('')
    serial_fornecedor :Mapped[Optional[str]] = mapped_field('')
    garantia_ate :Mapped[Optional[str]] = mapped_field('')
    id_almoxarifado :Mapped[Optional[int]] = mapped_field(None)
    numero_nf :Mapped[Optional[str]] = mapped_field('')
    valor_bem :Mapped[Optional[str]] = mapped_field('')
    departamento_id :Mapped[Optional[int]] = mapped_field(None)
    responsavel_id :Mapped[Optional[int]] = mapped_field(None)
    valor_residual :Mapped[Optional[str]] = mapped_field('')
    id_contrato_comodato :Mapped[Optional[int]] = mapped_field(None)
    id_cliente_comodato :Mapped[Optional[int]] = mapped_field(None)
    situacao :Mapped[SituacaoEnum] = mapped_field(SituacaoEnum.DISPONIVEL)
    estado :Mapped[EstadoEnum] = mapped_field(EstadoEnum.BOM)
    id_movimento_produto :Mapped[Optional[str]] = mapped_field('')
    em_laboratorio :Mapped[Optional[Em_laboratorioEnum]] = mapped_field(Em_laboratorioEnum.NAO)
    aguardando_instalacao :Mapped[Optional[Aguardando_instalacaoEnum]] = mapped_field(Aguardando_instalacaoEnum.NAO)
    validacao_form_patrimonio :Mapped[Optional[str]] = mapped_field('')
    dica_aba_indisponivel :Mapped[Optional[str]] = mapped_field('')
    finalidade_indisponivel :Mapped[Optional[Finalidade_indisponivelEnum]] = mapped_field(None)
    id_finalidade :Mapped[Optional[str]] = mapped_field('')
    data_movimentacao_indisponivel :Mapped[Optional[str]] = mapped_field('')
    cod_patrimonio :Mapped[Optional[str]] = mapped_field('')
    nro_patrimonio :Mapped[Optional[str]] = mapped_field('')
    descricao_indisponivel :Mapped[Optional[str]] = mapped_field('')
    id_pedido_os :Mapped[Optional[str]] = mapped_field('')

    @property
    def table(self) -> str:
        return "patrimonio"

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
            'serial': self._serialize_enum_and_str(self.serial) if self.serial is not None else '',
            'id_filial': str(self.id_filial) if self.id_filial is not None else '',
            'id_produto': str(self.id_produto) if self.id_produto is not None else '',
            'descricao': self._serialize_enum_and_str(self.descricao) if self.descricao is not None else '',
            'data_aquisicao': self._serialize_enum_and_str(self.data_aquisicao) if self.data_aquisicao is not None else '',
            'id': str(self.id) if self.id is not None else '',
            'id_fornecedor': str(self.id_fornecedor) if self.id_fornecedor is not None else '',
            'id_mac': self._serialize_enum_and_str(self.id_mac) if self.id_mac is not None else '',
            'serial_fornecedor': self._serialize_enum_and_str(self.serial_fornecedor) if self.serial_fornecedor is not None else '',
            'garantia_ate': self._serialize_enum_and_str(self.garantia_ate) if self.garantia_ate is not None else '',
            'id_almoxarifado': str(self.id_almoxarifado) if self.id_almoxarifado is not None else '',
            'numero_nf': self._serialize_enum_and_str(self.numero_nf) if self.numero_nf is not None else '',
            'valor_bem': self._serialize_enum_and_str(self.valor_bem) if self.valor_bem is not None else '',
            'departamento_id': str(self.departamento_id) if self.departamento_id is not None else '',
            'responsavel_id': str(self.responsavel_id) if self.responsavel_id is not None else '',
            'valor_residual': self._serialize_enum_and_str(self.valor_residual) if self.valor_residual is not None else '',
            'id_contrato_comodato': str(self.id_contrato_comodato) if self.id_contrato_comodato is not None else '',
            'id_cliente_comodato': str(self.id_cliente_comodato) if self.id_cliente_comodato is not None else '',
            'situacao': self._serialize_enum_and_str(self.situacao) if self.situacao is not None else '',
            'estado': self._serialize_enum_and_str(self.estado) if self.estado is not None else '',
            'id_movimento_produto': self._serialize_enum_and_str(self.id_movimento_produto) if self.id_movimento_produto is not None else '',
            'em_laboratorio': self._serialize_enum_and_str(self.em_laboratorio) if self.em_laboratorio is not None else '',
            'aguardando_instalacao': self._serialize_enum_and_str(self.aguardando_instalacao) if self.aguardando_instalacao is not None else '',
            'validacao_form_patrimonio': self._serialize_enum_and_str(self.validacao_form_patrimonio) if self.validacao_form_patrimonio is not None else '',
            'dica_aba_indisponivel': self._serialize_enum_and_str(self.dica_aba_indisponivel) if self.dica_aba_indisponivel is not None else '',
            'finalidade_indisponivel': self._serialize_enum_and_str(self.finalidade_indisponivel) if self.finalidade_indisponivel is not None else '',
            'id_finalidade': self._serialize_enum_and_str(self.id_finalidade) if self.id_finalidade is not None else '',
            'data_movimentacao_indisponivel': self._serialize_enum_and_str(self.data_movimentacao_indisponivel) if self.data_movimentacao_indisponivel is not None else '',
            'cod_patrimonio': self._serialize_enum_and_str(self.cod_patrimonio) if self.cod_patrimonio is not None else '',
            'nro_patrimonio': self._serialize_enum_and_str(self.nro_patrimonio) if self.nro_patrimonio is not None else '',
            'descricao_indisponivel': self._serialize_enum_and_str(self.descricao_indisponivel) if self.descricao_indisponivel is not None else '',
            'id_pedido_os': self._serialize_enum_and_str(self.id_pedido_os) if self.id_pedido_os is not None else '',
        }
        return {key: serialize(value) for key, value in data.items()}

    def is_valid(self) -> bool:
        return self.serial is not None and self.id_filial is not None and self.id_produto is not None and self.descricao is not None and self.data_aquisicao is not None
