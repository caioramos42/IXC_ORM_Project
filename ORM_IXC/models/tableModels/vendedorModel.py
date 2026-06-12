from __future__ import annotations
from typing import Optional
from ORM_IXC.interfaces.IModel import IModelWithId
from ORM_IXC.enums.vendedor import *
from ORM_IXC.statemants.maps.mapper import Mapped, field as mapped_field
from ORM_IXC.statemants.maps.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel

@MetaModels
class VendedorModel(IModelWithId, BaseModel):
    id: Mapped[Optional[int]]
    nome :Mapped[str]
    comissao :Mapped[str]
    id_cidade :Mapped[int]
    comissao_perc_recebimento :Mapped[Optional[str]] = mapped_field('')
    comissao_v :Mapped[Optional[str]] = mapped_field('')
    endereco :Mapped[Optional[str]] = mapped_field('')
    bairro :Mapped[Optional[str]] = mapped_field('')
    telefone :Mapped[Optional[str]] = mapped_field('')
    celular :Mapped[Optional[str]] = mapped_field('')
    cnpj_cpf :Mapped[Optional[str]] = mapped_field('')
    ie_rg :Mapped[Optional[str]] = mapped_field('')
    email :Mapped[Optional[str]] = mapped_field('')
    pipe_id_usuario :Mapped[Optional[str]] = mapped_field('')
    status :Mapped[StatusEnum] = mapped_field(StatusEnum.ATIVO)
    ultima_atualizacao :Mapped[Optional[str]] = mapped_field('')
    cor_no_mapa :Mapped[Optional[str]] = mapped_field('')

    @property
    def table(self) -> str:
        return "vendedor"

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
            'id': str(self.id) if self.id is not None else '',
            'nome': self.nome if self.nome is not None else '',
            'comissao': self.comissao if self.comissao is not None else '',
            'id_cidade': str(self.id_cidade) if self.id_cidade is not None else '',
            'comissao_perc_recebimento': self.comissao_perc_recebimento if self.comissao_perc_recebimento is not None else '',
            'comissao_v': self.comissao_v if self.comissao_v is not None else '',
            'endereco': self.endereco if self.endereco is not None else '',
            'bairro': self.bairro if self.bairro is not None else '',
            'telefone': self.telefone if self.telefone is not None else '',
            'celular': self.celular if self.celular is not None else '',
            'cnpj_cpf': self.cnpj_cpf if self.cnpj_cpf is not None else '',
            'ie_rg': self.ie_rg if self.ie_rg is not None else '',
            'email': self.email if self.email is not None else '',
            'pipe_id_usuario': self.pipe_id_usuario if self.pipe_id_usuario is not None else '',
            'status': self._serialize_enum(self.status) if self.status is not None else '',
            'ultima_atualizacao': self.ultima_atualizacao if self.ultima_atualizacao is not None else '',
            'cor_no_mapa': self.cor_no_mapa if self.cor_no_mapa is not None else '',
        }
        return {key: serialize(value) for key, value in data.items()}

    def is_valid(self) -> bool:
        return self.id is not None and self.nome is not None and self.comissao is not None and self.id_cidade is not None
    
    @classmethod
    def dto_convert(cls_: object, data: dict[str, str]):
        raise NotImplementedError
