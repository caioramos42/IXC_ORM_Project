from __future__ import annotations
from typing import Optional
from ORM_IXC.interfaces import IModelWithId
from ORM_IXC.enums.veiculos import *
from ORM_IXC.statemants.maps.mapper import Mapped, field as mapped_field
from ORM_IXC.statemants.maps.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel


@MetaModels
class VeiculosModel(IModelWithId, BaseModel):
    uf_veiculo :Mapped[int]
    descricao :Mapped[str]
    renavam :Mapped[str]
    placa :Mapped[str]
    id :Mapped[Optional[int]]
    status :Mapped[Optional[StatusEnum]] = mapped_field(None)
    id_filial :Mapped[Optional[int]] = mapped_field(None)
    condutor_principal :Mapped[Optional[int]] = mapped_field(None)
    placa_tipo :Mapped[Optional[Placa_tipoEnum]] = mapped_field(None)
    placa_anterior :Mapped[Optional[str]] = mapped_field('')
    ano_fabricacao :Mapped[Optional[str]] = mapped_field('')
    ano_modelo :Mapped[Optional[str]] = mapped_field('')
    numero_crv :Mapped[Optional[str]] = mapped_field('')
    cor :Mapped[Optional[str]] = mapped_field('')
    chassi :Mapped[Optional[str]] = mapped_field('')
    categoria_veiculo :Mapped[Optional[Categoria_veiculoEnum]] = mapped_field(None)
    caminhao_qtde_eixos :Mapped[Optional[Caminhao_qtde_eixosEnum]] = mapped_field(None)
    combustivel_tipo :Mapped[Optional[Combustivel_tipoEnum]] = mapped_field(None)
    tipo_rodado :Mapped[Optional[Tipo_rodadoEnum]] = mapped_field(None)
    tipo_carroceria :Mapped[Optional[Tipo_carroceriaEnum]] = mapped_field(None)
    tara :Mapped[Optional[str]] = mapped_field('')
    capacidade_kg :Mapped[Optional[str]] = mapped_field('')
    capacidade_m3 :Mapped[Optional[str]] = mapped_field('')
    data_aquisicao :Mapped[Optional[str]] = mapped_field('')
    data_venda :Mapped[Optional[str]] = mapped_field('')
    centro_custo_regra_rateio :Mapped[Optional[Centro_custo_regra_rateioEnum]] = mapped_field(None)
    id_centro_custo_categoria_filtro :Mapped[Optional[int]] = mapped_field(None)
    id_centro_custo_criterio_rateio :Mapped[Optional[int]] = mapped_field(None)
    id_centro_custo_rel_centro_custo_categoria_padrao :Mapped[Optional[int]] = mapped_field(None)
    oleo :Mapped[Optional[str]] = mapped_field('')
    data_ultima_troca_oleo :Mapped[Optional[str]] = mapped_field('')
    data_proxima_troca_oleo :Mapped[Optional[str]] = mapped_field('')
    aviso_troca_oleo_dias_antes :Mapped[Optional[str]] = mapped_field('')
    intervalo_dias_entre_revisoes :Mapped[Optional[str]] = mapped_field('')
    data_revisao :Mapped[Optional[str]] = mapped_field('')
    data_proxima_revisao :Mapped[Optional[str]] = mapped_field('')
    aviso_revisao_dias_antes :Mapped[Optional[str]] = mapped_field('')
    observacao :Mapped[Optional[str]] = mapped_field('')
    fieldset_distancia :Mapped[Optional[str]] = mapped_field('')
    hodometro :Mapped[Optional[str]] = mapped_field('')
    reastreador :Mapped[Optional[str]] = mapped_field('')
    status_veiculos :Mapped[Optional[Status_veiculosEnum]] = mapped_field(None)

    @property
    def table(self) -> str:
        return "veiculos"

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
            'uf_veiculo': str(self.uf_veiculo) if self.uf_veiculo is not None else '',
            'descricao': self._serialize_enum_and_str(self.descricao) if self.descricao is not None else '',
            'renavam': self._serialize_enum_and_str(self.renavam) if self.renavam is not None else '',
            'placa': self._serialize_enum_and_str(self.placa) if self.placa is not None else '',
            'id': str(self.id) if self.id is not None else '',
            'status': self._serialize_enum_and_str(self.status) if self.status is not None else '',
            'id_filial': str(self.id_filial) if self.id_filial is not None else '',
            'condutor_principal': str(self.condutor_principal) if self.condutor_principal is not None else '',
            'placa_tipo': self._serialize_enum_and_str(self.placa_tipo) if self.placa_tipo is not None else '',
            'placa_anterior': self._serialize_enum_and_str(self.placa_anterior) if self.placa_anterior is not None else '',
            'ano_fabricacao': self._serialize_enum_and_str(self.ano_fabricacao) if self.ano_fabricacao is not None else '',
            'ano_modelo': self._serialize_enum_and_str(self.ano_modelo) if self.ano_modelo is not None else '',
            'numero_crv': self._serialize_enum_and_str(self.numero_crv) if self.numero_crv is not None else '',
            'cor': self._serialize_enum_and_str(self.cor) if self.cor is not None else '',
            'chassi': self._serialize_enum_and_str(self.chassi) if self.chassi is not None else '',
            'categoria_veiculo': self._serialize_enum_and_str(self.categoria_veiculo) if self.categoria_veiculo is not None else '',
            'caminhao_qtde_eixos': self._serialize_enum_and_str(self.caminhao_qtde_eixos) if self.caminhao_qtde_eixos is not None else '',
            'combustivel_tipo': self._serialize_enum_and_str(self.combustivel_tipo) if self.combustivel_tipo is not None else '',
            'tipo_rodado': self._serialize_enum_and_str(self.tipo_rodado) if self.tipo_rodado is not None else '',
            'tipo_carroceria': self._serialize_enum_and_str(self.tipo_carroceria) if self.tipo_carroceria is not None else '',
            'tara': self._serialize_enum_and_str(self.tara) if self.tara is not None else '',
            'capacidade_kg': self._serialize_enum_and_str(self.capacidade_kg) if self.capacidade_kg is not None else '',
            'capacidade_m3': self._serialize_enum_and_str(self.capacidade_m3) if self.capacidade_m3 is not None else '',
            'data_aquisicao': self._serialize_enum_and_str(self.data_aquisicao) if self.data_aquisicao is not None else '',
            'data_venda': self._serialize_enum_and_str(self.data_venda) if self.data_venda is not None else '',
            'centro_custo_regra_rateio': self._serialize_enum_and_str(self.centro_custo_regra_rateio) if self.centro_custo_regra_rateio is not None else '',
            'id_centro_custo_categoria_filtro': str(self.id_centro_custo_categoria_filtro) if self.id_centro_custo_categoria_filtro is not None else '',
            'id_centro_custo_criterio_rateio': str(self.id_centro_custo_criterio_rateio) if self.id_centro_custo_criterio_rateio is not None else '',
            'id_centro_custo_rel_centro_custo_categoria_padrao': str(self.id_centro_custo_rel_centro_custo_categoria_padrao) if self.id_centro_custo_rel_centro_custo_categoria_padrao is not None else '',
            'oleo': self._serialize_enum_and_str(self.oleo) if self.oleo is not None else '',
            'data_ultima_troca_oleo': self._serialize_enum_and_str(self.data_ultima_troca_oleo) if self.data_ultima_troca_oleo is not None else '',
            'data_proxima_troca_oleo': self._serialize_enum_and_str(self.data_proxima_troca_oleo) if self.data_proxima_troca_oleo is not None else '',
            'aviso_troca_oleo_dias_antes': self._serialize_enum_and_str(self.aviso_troca_oleo_dias_antes) if self.aviso_troca_oleo_dias_antes is not None else '',
            'intervalo_dias_entre_revisoes': self._serialize_enum_and_str(self.intervalo_dias_entre_revisoes) if self.intervalo_dias_entre_revisoes is not None else '',
            'data_revisao': self._serialize_enum_and_str(self.data_revisao) if self.data_revisao is not None else '',
            'data_proxima_revisao': self._serialize_enum_and_str(self.data_proxima_revisao) if self.data_proxima_revisao is not None else '',
            'aviso_revisao_dias_antes': self._serialize_enum_and_str(self.aviso_revisao_dias_antes) if self.aviso_revisao_dias_antes is not None else '',
            'observacao': self._serialize_enum_and_str(self.observacao) if self.observacao is not None else '',
            'fieldset_distancia': self._serialize_enum_and_str(self.fieldset_distancia) if self.fieldset_distancia is not None else '',
            'hodometro': self._serialize_enum_and_str(self.hodometro) if self.hodometro is not None else '',
            'reastreador': self._serialize_enum_and_str(self.reastreador) if self.reastreador is not None else '',
            'status_veiculos': self._serialize_enum_and_str(self.status_veiculos) if self.status_veiculos is not None else '',
        }
        return {key: serialize(value) for key, value in data.items()}

    def is_valid(self) -> bool:
        return self.uf_veiculo is not None and self.descricao is not None and self.renavam is not None and self.placa is not None
