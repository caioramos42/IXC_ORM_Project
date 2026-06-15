from __future__ import annotations
from typing import Optional
from ORM_IXC.interfaces import IModelWithId
from ORM_IXC.enums.tipoDeCobrancaDoContrato import *
from ORM_IXC.statemants.maps.mapper import Mapped, field as mapped_field
from ORM_IXC.statemants.maps.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel


@MetaModels
class TipoDeCobrancaDoContratoModel(IModelWithId, BaseModel):
    tipo_contrato :Mapped[str]
    tipo_pagamento :Mapped[Tipo_pagamentoEnum]
    id_condicoes_pagamento :Mapped[int]
    avisar_dias :Mapped[str]
    bloquear_dias :Mapped[str]
    qtd_periodos :Mapped[str]
    id :Mapped[Optional[int]]
    ativo :Mapped[Optional[AtivoEnum]] = mapped_field(AtivoEnum.SIM)
    pagamento_antecipado :Mapped[Optional[Pagamento_antecipadoEnum]] = mapped_field(Pagamento_antecipadoEnum.NAO)
    base_periodo_prestacao :Mapped[Base_periodo_prestacaoEnum] = mapped_field(Base_periodo_prestacaoEnum.DATA_VENCIMENTO)
    bloqueio_renegociado_n_dias :Mapped[Optional[str]] = mapped_field('')
    fieldset_dica :Mapped[Optional[str]] = mapped_field('')
    periodo :Mapped[PeriodoEnum] = mapped_field(PeriodoEnum.MES)
    ordem :Mapped[Optional[str]] = mapped_field('')
    ultima_atualizacao :Mapped[Optional[str]] = mapped_field('')
    parcela_cobrar_proporcional :Mapped[Optional[Parcela_cobrar_proporcionalEnum]] = mapped_field(Parcela_cobrar_proporcionalEnum.PRIMEIRA_PARCELA)
    dias_proporcional_cob_mes :Mapped[Optional[str]] = mapped_field('')
    parcelas_cob_adicional :Mapped[Optional[str]] = mapped_field('')
    max_titulos_abertos_gerar_contrato :Mapped[Optional[str]] = mapped_field('')
    dias_carencia_pre :Mapped[Optional[str]] = mapped_field('')

    @property
    def table(self) -> str:
        return "tipodecobrançadocontrato"

    def _serialize_enum(self, value) -> str:
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
            'tipo_contrato': self.tipo_contrato if self.tipo_contrato is not None else '',
            'tipo_pagamento': self._serialize_enum(self.tipo_pagamento) if self.tipo_pagamento is not None else '',
            'id_condicoes_pagamento': str(self.id_condicoes_pagamento) if self.id_condicoes_pagamento is not None else '',
            'avisar_dias': self.avisar_dias if self.avisar_dias is not None else '',
            'bloquear_dias': self.bloquear_dias if self.bloquear_dias is not None else '',
            'qtd_periodos': self.qtd_periodos if self.qtd_periodos is not None else '',
            'id': str(self.id) if self.id is not None else '',
            'ativo': self._serialize_enum(self.ativo) if self.ativo is not None else '',
            'pagamento_antecipado': self._serialize_enum(self.pagamento_antecipado) if self.pagamento_antecipado is not None else '',
            'base_periodo_prestacao': self._serialize_enum(self.base_periodo_prestacao) if self.base_periodo_prestacao is not None else '',
            'bloqueio_renegociado_n_dias': self.bloqueio_renegociado_n_dias if self.bloqueio_renegociado_n_dias is not None else '',
            'fieldset_dica': self.fieldset_dica if self.fieldset_dica is not None else '',
            'periodo': self._serialize_enum(self.periodo) if self.periodo is not None else '',
            'ordem': self.ordem if self.ordem is not None else '',
            'ultima_atualizacao': self.ultima_atualizacao if self.ultima_atualizacao is not None else '',
            'parcela_cobrar_proporcional': self._serialize_enum(self.parcela_cobrar_proporcional) if self.parcela_cobrar_proporcional is not None else '',
            'dias_proporcional_cob_mes': self.dias_proporcional_cob_mes if self.dias_proporcional_cob_mes is not None else '',
            'parcelas_cob_adicional': self.parcelas_cob_adicional if self.parcelas_cob_adicional is not None else '',
            'max_titulos_abertos_gerar_contrato': self.max_titulos_abertos_gerar_contrato if self.max_titulos_abertos_gerar_contrato is not None else '',
            'dias_carencia_pre': self.dias_carencia_pre if self.dias_carencia_pre is not None else '',
        }
        return {key: serialize(value) for key, value in data.items()}

    def is_valid(self) -> bool:
        return self.tipo_contrato is not None and self.tipo_pagamento is not None and self.id_condicoes_pagamento is not None and self.avisar_dias is not None and self.bloquear_dias is not None and self.qtd_periodos is not None
