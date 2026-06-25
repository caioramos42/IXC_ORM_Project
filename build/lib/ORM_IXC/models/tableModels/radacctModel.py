from __future__ import annotations
from typing import Optional
from ORM_IXC.interfaces import IModelWithId
from ORM_IXC.statemants.maps.mapper import Mapped, field as mapped_field
from ORM_IXC.statemants.maps.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel


@MetaModels
class RadacctModel(IModelWithId, BaseModel):
    radacctid :Mapped[str]
    acctsessionid :Mapped[str]
    acctuniqueid :Mapped[str]
    username :Mapped[str]
    groupname :Mapped[str]
    nasipaddress :Mapped[str]
    calledstationid :Mapped[str]
    callingstationid :Mapped[str]
    acctterminatecause :Mapped[str]
    framedipaddress :Mapped[str]
    acctstartdelay :Mapped[str]
    acctstopdelay :Mapped[str]
    realm :Mapped[Optional[str]] = mapped_field('')
    nasipv6address :Mapped[Optional[str]] = mapped_field('')
    nasportid :Mapped[Optional[str]] = mapped_field('')
    nasporttype :Mapped[Optional[str]] = mapped_field('')
    acctstarttime :Mapped[Optional[str]] = mapped_field('')
    acctstoptime :Mapped[Optional[str]] = mapped_field('')
    acctsessiontime :Mapped[Optional[str]] = mapped_field('')
    acctauthentic :Mapped[Optional[str]] = mapped_field('')
    connectinfo_start :Mapped[Optional[str]] = mapped_field('')
    connectinfo_stop :Mapped[Optional[str]] = mapped_field('')
    acctinputoctets :Mapped[Optional[str]] = mapped_field('')
    acctoutputoctets :Mapped[Optional[str]] = mapped_field('')
    servicetype :Mapped[Optional[str]] = mapped_field('')
    framedprotocol :Mapped[Optional[str]] = mapped_field('')
    xascendsessionsvrkey :Mapped[Optional[str]] = mapped_field('')
    acctupdatetime :Mapped[Optional[str]] = mapped_field('')
    acctinterval :Mapped[Optional[str]] = mapped_field('')
    framedipv6prefix :Mapped[Optional[str]] = mapped_field('')
    delegatedipv6prefix :Mapped[Optional[str]] = mapped_field('')

    @property
    def table(self) -> str:
        return "radacct"

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
            'radacctid': self._serialize_enum_and_str(self.radacctid) if self.radacctid is not None else '',
            'acctsessionid': self._serialize_enum_and_str(self.acctsessionid) if self.acctsessionid is not None else '',
            'acctuniqueid': self._serialize_enum_and_str(self.acctuniqueid) if self.acctuniqueid is not None else '',
            'username': self._serialize_enum_and_str(self.username) if self.username is not None else '',
            'groupname': self._serialize_enum_and_str(self.groupname) if self.groupname is not None else '',
            'nasipaddress': self._serialize_enum_and_str(self.nasipaddress) if self.nasipaddress is not None else '',
            'calledstationid': self._serialize_enum_and_str(self.calledstationid) if self.calledstationid is not None else '',
            'callingstationid': self._serialize_enum_and_str(self.callingstationid) if self.callingstationid is not None else '',
            'acctterminatecause': self._serialize_enum_and_str(self.acctterminatecause) if self.acctterminatecause is not None else '',
            'framedipaddress': self._serialize_enum_and_str(self.framedipaddress) if self.framedipaddress is not None else '',
            'acctstartdelay': self._serialize_enum_and_str(self.acctstartdelay) if self.acctstartdelay is not None else '',
            'acctstopdelay': self._serialize_enum_and_str(self.acctstopdelay) if self.acctstopdelay is not None else '',
            'realm': self._serialize_enum_and_str(self.realm) if self.realm is not None else '',
            'nasipv6address': self._serialize_enum_and_str(self.nasipv6address) if self.nasipv6address is not None else '',
            'nasportid': self._serialize_enum_and_str(self.nasportid) if self.nasportid is not None else '',
            'nasporttype': self._serialize_enum_and_str(self.nasporttype) if self.nasporttype is not None else '',
            'acctstarttime': self._serialize_enum_and_str(self.acctstarttime) if self.acctstarttime is not None else '',
            'acctstoptime': self._serialize_enum_and_str(self.acctstoptime) if self.acctstoptime is not None else '',
            'acctsessiontime': self._serialize_enum_and_str(self.acctsessiontime) if self.acctsessiontime is not None else '',
            'acctauthentic': self._serialize_enum_and_str(self.acctauthentic) if self.acctauthentic is not None else '',
            'connectinfo_start': self._serialize_enum_and_str(self.connectinfo_start) if self.connectinfo_start is not None else '',
            'connectinfo_stop': self._serialize_enum_and_str(self.connectinfo_stop) if self.connectinfo_stop is not None else '',
            'acctinputoctets': self._serialize_enum_and_str(self.acctinputoctets) if self.acctinputoctets is not None else '',
            'acctoutputoctets': self._serialize_enum_and_str(self.acctoutputoctets) if self.acctoutputoctets is not None else '',
            'servicetype': self._serialize_enum_and_str(self.servicetype) if self.servicetype is not None else '',
            'framedprotocol': self._serialize_enum_and_str(self.framedprotocol) if self.framedprotocol is not None else '',
            'xascendsessionsvrkey': self._serialize_enum_and_str(self.xascendsessionsvrkey) if self.xascendsessionsvrkey is not None else '',
            'acctupdatetime': self._serialize_enum_and_str(self.acctupdatetime) if self.acctupdatetime is not None else '',
            'acctinterval': self._serialize_enum_and_str(self.acctinterval) if self.acctinterval is not None else '',
            'framedipv6prefix': self._serialize_enum_and_str(self.framedipv6prefix) if self.framedipv6prefix is not None else '',
            'delegatedipv6prefix': self._serialize_enum_and_str(self.delegatedipv6prefix) if self.delegatedipv6prefix is not None else '',
        }
        return {key: serialize(value) for key, value in data.items()}

    def is_valid(self) -> bool:
        return self.radacctid is not None and self.acctsessionid is not None and self.acctuniqueid is not None and self.username is not None and self.groupname is not None and self.nasipaddress is not None and self.calledstationid is not None and self.callingstationid is not None and self.acctterminatecause is not None and self.framedipaddress is not None and self.acctstartdelay is not None and self.acctstopdelay is not None
