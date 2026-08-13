from __future__ import annotations
from typing import Optional
from ORM_IXC.interfaces import IModelWithId
from ORM_IXC.enums.cidade import *
from ORM_IXC.statemants.maps.mapper import Mapped, field as mapped_field
from ORM_IXC.statemants.maps.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel


@MetaModels
class CidadeModel(IModelWithId, BaseModel):
    origem :Mapped[OrigemEnum]
    nome :Mapped[str]
    uf :Mapped[int]
    cod_ibge :Mapped[str]
    id :Mapped[Optional[int]]
    regiao :Mapped[Optional[str]] = mapped_field('')
    cod_siafi :Mapped[Optional[str]] = mapped_field('')
    cod_cidade_nfse_forquilhinha_sc :Mapped[Optional[str]] = mapped_field('')
    codigo :Mapped[Optional[str]] = mapped_field('')

    @property
    def table(self) -> str:
        return "cidade"

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
            'origem': self._serialize_enum_and_str(self.origem) if self.origem is not None else '',
            'nome': self._serialize_enum_and_str(self.nome) if self.nome is not None else '',
            'uf': str(self.uf) if self.uf is not None else '',
            'cod_ibge': self._serialize_enum_and_str(self.cod_ibge) if self.cod_ibge is not None else '',
            'id': str(self.id) if self.id is not None else '',
            'regiao': self._serialize_enum_and_str(self.regiao) if self.regiao is not None else '',
            'cod_siafi': self._serialize_enum_and_str(self.cod_siafi) if self.cod_siafi is not None else '',
            'cod_cidade_nfse_forquilhinha_sc': self._serialize_enum_and_str(self.cod_cidade_nfse_forquilhinha_sc) if self.cod_cidade_nfse_forquilhinha_sc is not None else '',
            'codigo': self._serialize_enum_and_str(self.codigo) if self.codigo is not None else '',
        }
        return {key: serialize(value) for key, value in data.items()}

    def is_valid(self) -> bool:
        return self.origem is not None and self.nome is not None and self.uf is not None and self.cod_ibge is not None
