from __future__ import annotations
from typing import Optional
from ORM_IXC.interfaces import IModelWithId
from ORM_IXC.enums.planosPorContrato import *
from ORM_IXC.statemants.maps.mapper import Mapped, field as mapped_field
from ORM_IXC.statemants.maps.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel


@MetaModels
class PlanosPorContratoModel(IModelWithId, BaseModel):
    tipo :Mapped[TipoEnum]
    qtde :Mapped[str]
    valor_unit :Mapped[str]
    fixar_ip :Mapped[Fixar_ipEnum]
    id :Mapped[Optional[int]]
    id_produto :Mapped[Optional[int]] = mapped_field(None)
    id_plano :Mapped[Optional[int]] = mapped_field(None)
    descricao :Mapped[Optional[str]] = mapped_field('')
    obs :Mapped[Optional[str]] = mapped_field('')
    valor_ate_vencimento :Mapped[Optional[str]] = mapped_field('')
    tipo_desconto :Mapped[Optional[Tipo_descontoEnum]] = mapped_field(None)
    repetir :Mapped[Optional[RepetirEnum]] = mapped_field(None)
    qtde_repeticoes_desconto_produto :Mapped[Optional[str]] = mapped_field('')
    valor_desconto_produto :Mapped[Optional[str]] = mapped_field('')
    desconto_percentual :Mapped[Optional[str]] = mapped_field('')
    ultima_atualizacao :Mapped[Optional[str]] = mapped_field('')
    descricao_plano_valor_1 :Mapped[Optional[str]] = mapped_field('')
    descricao_plano_valor_2 :Mapped[Optional[str]] = mapped_field('')
    id_tipo_documento :Mapped[Optional[int]] = mapped_field(None)
    id_contrato :Mapped[Optional[str]] = mapped_field('')
    id_vd_contrato :Mapped[Optional[str]] = mapped_field('')
    limite_pacote :Mapped[Optional[str]] = mapped_field('')
    valor_adicional_pacote :Mapped[Optional[str]] = mapped_field('')

    @property
    def table(self) -> str:
        return "vd_contratos_produtos"

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
            'qtde': self._serialize_enum_and_str(self.qtde) if self.qtde is not None else '',
            'valor_unit': self._serialize_enum_and_str(self.valor_unit) if self.valor_unit is not None else '',
            'fixar_ip': self._serialize_enum_and_str(self.fixar_ip) if self.fixar_ip is not None else '',
            'id': str(self.id) if self.id is not None else '',
            'id_produto': str(self.id_produto) if self.id_produto is not None else '',
            'id_plano': str(self.id_plano) if self.id_plano is not None else '',
            'descricao': self._serialize_enum_and_str(self.descricao) if self.descricao is not None else '',
            'obs': self._serialize_enum_and_str(self.obs) if self.obs is not None else '',
            'valor_ate_vencimento': self._serialize_enum_and_str(self.valor_ate_vencimento) if self.valor_ate_vencimento is not None else '',
            'tipo_desconto': self._serialize_enum_and_str(self.tipo_desconto) if self.tipo_desconto is not None else '',
            'repetir': self._serialize_enum_and_str(self.repetir) if self.repetir is not None else '',
            'qtde_repeticoes_desconto_produto': self._serialize_enum_and_str(self.qtde_repeticoes_desconto_produto) if self.qtde_repeticoes_desconto_produto is not None else '',
            'valor_desconto_produto': self._serialize_enum_and_str(self.valor_desconto_produto) if self.valor_desconto_produto is not None else '',
            'desconto_percentual': self._serialize_enum_and_str(self.desconto_percentual) if self.desconto_percentual is not None else '',
            'ultima_atualizacao': self._serialize_enum_and_str(self.ultima_atualizacao) if self.ultima_atualizacao is not None else '',
            'descricao_plano_valor_1': self._serialize_enum_and_str(self.descricao_plano_valor_1) if self.descricao_plano_valor_1 is not None else '',
            'descricao_plano_valor_2': self._serialize_enum_and_str(self.descricao_plano_valor_2) if self.descricao_plano_valor_2 is not None else '',
            'id_tipo_documento': str(self.id_tipo_documento) if self.id_tipo_documento is not None else '',
            'id_contrato': self._serialize_enum_and_str(self.id_contrato) if self.id_contrato is not None else '',
            'id_vd_contrato': self._serialize_enum_and_str(self.id_vd_contrato) if self.id_vd_contrato is not None else '',
            'limite_pacote': self._serialize_enum_and_str(self.limite_pacote) if self.limite_pacote is not None else '',
            'valor_adicional_pacote': self._serialize_enum_and_str(self.valor_adicional_pacote) if self.valor_adicional_pacote is not None else '',
        }
        return {key: serialize(value) for key, value in data.items()}

    def is_valid(self) -> bool:
        return self.tipo is not None and self.qtde is not None and self.valor_unit is not None and self.fixar_ip is not None
