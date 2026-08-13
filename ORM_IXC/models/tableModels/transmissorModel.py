from __future__ import annotations
from typing import Optional
from ORM_IXC.interfaces import IModelWithId
from ORM_IXC.enums.transmissor import *
from ORM_IXC.statemants.maps.mapper import Mapped, field as mapped_field
from ORM_IXC.statemants.maps.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel


@MetaModels
class TransmissorModel(IModelWithId, BaseModel):
    id :Mapped[Optional[int]]
    descricao :Mapped[str]
    id_pop :Mapped[int]
    ip :Mapped[str]
    login :Mapped[str]
    senha :Mapped[str]
    login_hw :Mapped[Optional[str]] = mapped_field('')
    senha_hw :Mapped[Optional[str]] = mapped_field('')
    fabricante_modelo :Mapped[Fabricante_modeloEnum] = mapped_field(Fabricante_modeloEnum.RADIO_MIKROTIK)
    perfil_fibra_padrao :Mapped[Optional[int]] = mapped_field(None)
    porta_ssh :Mapped[Optional[str]] = mapped_field('')
    porta_telnet :Mapped[Optional[str]] = mapped_field('')
    httpd_port :Mapped[Optional[str]] = mapped_field('')
    id_prov_snmp :Mapped[Optional[int]] = mapped_field(None)
    porta_api :Mapped[Optional[str]] = mapped_field('')
    timeout :Mapped[Optional[str]] = mapped_field('')
    ativo :Mapped[AtivoEnum] = mapped_field(AtivoEnum.SIM)
    cor_mapa :Mapped[Optional[str]] = mapped_field('')
    id_padrao_cores :Mapped[Optional[int]] = mapped_field(None)
    ip_anm :Mapped[Optional[str]] = mapped_field('')
    login_anm :Mapped[Optional[str]] = mapped_field('')
    senha_anm :Mapped[Optional[str]] = mapped_field(None)
    porta_telnet_tl1 :Mapped[Optional[str]] = mapped_field('')
    gabinete :Mapped[Optional[str]] = mapped_field('')
    subrack :Mapped[Optional[str]] = mapped_field('')
    usa_smart :Mapped[Optional[str]] = mapped_field('')
    id_servidor_unms :Mapped[Optional[int]] = mapped_field(None)
    id_olt_unms :Mapped[Optional[str]] = mapped_field('')
    id_olt_conscius :Mapped[Optional[str]] = mapped_field('')
    id_olt_externo :Mapped[Optional[str]] = mapped_field('')
    conexoes_ulltima_data :Mapped[Optional[str]] = mapped_field('')
    conexoes_ultima :Mapped[Optional[str]] = mapped_field('')
    fwversion :Mapped[Optional[str]] = mapped_field('')
    uptime :Mapped[Optional[str]] = mapped_field('')
    time :Mapped[Optional[str]] = mapped_field('')
    modelo :Mapped[Optional[str]] = mapped_field('')
    cpu_load :Mapped[Optional[str]] = mapped_field('')
    total_memory :Mapped[Optional[str]] = mapped_field('')
    free_memory :Mapped[Optional[str]] = mapped_field('')
    temperatura :Mapped[Optional[str]] = mapped_field('')
    voltagem :Mapped[Optional[str]] = mapped_field('')
    current_firmware :Mapped[Optional[str]] = mapped_field('')
    upgrade_firmware :Mapped[Optional[str]] = mapped_field('')
    id_olt :Mapped[Optional[str]] = mapped_field('')
    autosave :Mapped[Optional[str]] = mapped_field('')
    speed_lan :Mapped[Optional[str]] = mapped_field('')
    speed_wlan :Mapped[Optional[str]] = mapped_field('')
    rxrate :Mapped[Optional[str]] = mapped_field('')
    txrate :Mapped[Optional[str]] = mapped_field('')
    usa_vpn :Mapped[Usa_vpnEnum] = mapped_field(Usa_vpnEnum.NAO)
    busca_potencia :Mapped[Busca_potenciaEnum] = mapped_field(Busca_potenciaEnum.NAO)
    perfil_neutro_bridge :Mapped[Optional[int]] = mapped_field(None)
    perfil_neutro_router :Mapped[Optional[int]] = mapped_field(None)
    id_pv_grupo_backup :Mapped[Optional[int]] = mapped_field(None)
    operador_neutro :Mapped[Optional[int]] = mapped_field(None)

    @property
    def table(self) -> str:
        return "radpop_radio"

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
            'descricao': self._serialize_enum_and_str(self.descricao) if self.descricao is not None else '',
            'id_pop': str(self.id_pop) if self.id_pop is not None else '',
            'ip': self._serialize_enum_and_str(self.ip) if self.ip is not None else '',
            'login': self._serialize_enum_and_str(self.login) if self.login is not None else '',
            'senha': self._serialize_enum_and_str(self.senha) if self.senha is not None else '',
            'login_hw': self._serialize_enum_and_str(self.login_hw) if self.login_hw is not None else '',
            'senha_hw': self._serialize_enum_and_str(self.senha_hw) if self.senha_hw is not None else '',
            'id': str(self.id) if self.id is not None else '',
            'fabricante_modelo': self._serialize_enum_and_str(self.fabricante_modelo) if self.fabricante_modelo is not None else '',
            'perfil_fibra_padrao': str(self.perfil_fibra_padrao) if self.perfil_fibra_padrao is not None else '',
            'porta_ssh': self._serialize_enum_and_str(self.porta_ssh) if self.porta_ssh is not None else '',
            'porta_telnet': self._serialize_enum_and_str(self.porta_telnet) if self.porta_telnet is not None else '',
            'httpd_port': self._serialize_enum_and_str(self.httpd_port) if self.httpd_port is not None else '',
            'id_prov_snmp': str(self.id_prov_snmp) if self.id_prov_snmp is not None else '',
            'porta_api': self._serialize_enum_and_str(self.porta_api) if self.porta_api is not None else '',
            'timeout': self._serialize_enum_and_str(self.timeout) if self.timeout is not None else '',
            'ativo': self._serialize_enum_and_str(self.ativo) if self.ativo is not None else '',
            'cor_mapa': self._serialize_enum_and_str(self.cor_mapa) if self.cor_mapa is not None else '',
            'id_padrao_cores': str(self.id_padrao_cores) if self.id_padrao_cores is not None else '',
            'ip_anm': self._serialize_enum_and_str(self.ip_anm) if self.ip_anm is not None else '',
            'login_anm': self._serialize_enum_and_str(self.login_anm) if self.login_anm is not None else '',
            'senha_anm': self._serialize_enum_and_str(self.senha_anm) if self.senha_anm is not None else '',
            'porta_telnet_tl1': self._serialize_enum_and_str(self.porta_telnet_tl1) if self.porta_telnet_tl1 is not None else '',
            'gabinete': self._serialize_enum_and_str(self.gabinete) if self.gabinete is not None else '',
            'subrack': self._serialize_enum_and_str(self.subrack) if self.subrack is not None else '',
            'usa_smart': self._serialize_enum_and_str(self.usa_smart) if self.usa_smart is not None else '',
            'id_servidor_unms': str(self.id_servidor_unms) if self.id_servidor_unms is not None else '',
            'id_olt_unms': self._serialize_enum_and_str(self.id_olt_unms) if self.id_olt_unms is not None else '',
            'id_olt_conscius': self._serialize_enum_and_str(self.id_olt_conscius) if self.id_olt_conscius is not None else '',
            'id_olt_externo': self._serialize_enum_and_str(self.id_olt_externo) if self.id_olt_externo is not None else '',
            'conexoes_ulltima_data': self._serialize_enum_and_str(self.conexoes_ulltima_data) if self.conexoes_ulltima_data is not None else '',
            'conexoes_ultima': self._serialize_enum_and_str(self.conexoes_ultima) if self.conexoes_ultima is not None else '',
            'fwversion': self._serialize_enum_and_str(self.fwversion) if self.fwversion is not None else '',
            'uptime': self._serialize_enum_and_str(self.uptime) if self.uptime is not None else '',
            'time': self._serialize_enum_and_str(self.time) if self.time is not None else '',
            'modelo': self._serialize_enum_and_str(self.modelo) if self.modelo is not None else '',
            'cpu_load': self._serialize_enum_and_str(self.cpu_load) if self.cpu_load is not None else '',
            'total_memory': self._serialize_enum_and_str(self.total_memory) if self.total_memory is not None else '',
            'free_memory': self._serialize_enum_and_str(self.free_memory) if self.free_memory is not None else '',
            'temperatura': self._serialize_enum_and_str(self.temperatura) if self.temperatura is not None else '',
            'voltagem': self._serialize_enum_and_str(self.voltagem) if self.voltagem is not None else '',
            'current_firmware': self._serialize_enum_and_str(self.current_firmware) if self.current_firmware is not None else '',
            'upgrade_firmware': self._serialize_enum_and_str(self.upgrade_firmware) if self.upgrade_firmware is not None else '',
            'id_olt': self._serialize_enum_and_str(self.id_olt) if self.id_olt is not None else '',
            'autosave': self._serialize_enum_and_str(self.autosave) if self.autosave is not None else '',
            'speed_lan': self._serialize_enum_and_str(self.speed_lan) if self.speed_lan is not None else '',
            'speed_wlan': self._serialize_enum_and_str(self.speed_wlan) if self.speed_wlan is not None else '',
            'rxrate': self._serialize_enum_and_str(self.rxrate) if self.rxrate is not None else '',
            'txrate': self._serialize_enum_and_str(self.txrate) if self.txrate is not None else '',
            'usa_vpn': self._serialize_enum_and_str(self.usa_vpn) if self.usa_vpn is not None else '',
            'busca_potencia': self._serialize_enum_and_str(self.busca_potencia) if self.busca_potencia is not None else '',
            'perfil_neutro_bridge': str(self.perfil_neutro_bridge) if self.perfil_neutro_bridge is not None else '',
            'perfil_neutro_router': str(self.perfil_neutro_router) if self.perfil_neutro_router is not None else '',
            'id_pv_grupo_backup': str(self.id_pv_grupo_backup) if self.id_pv_grupo_backup is not None else '',
            'operador_neutro': str(self.operador_neutro) if self.operador_neutro is not None else '',
        }
        return {key: serialize(value) for key, value in data.items()}

    def is_valid(self) -> bool:
        return self.descricao is not None and self.id_pop is not None and self.ip is not None and self.login is not None and self.senha is not None
