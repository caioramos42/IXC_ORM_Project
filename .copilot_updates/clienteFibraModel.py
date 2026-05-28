from __future__ import annotations
from typing import Optional
from ORM_IXC.enums.clienteFibra import *

from ORM_IXC.interfaces import IModel, IModelWithId
from ORM_IXC.statemants.classBase import Field
from ORM_IXC.statemants.mapper import Mapped
from ORM_IXC.statemants.metaManager import MetaModels
from ORM_IXC.models.defaultModel import BaseModel

@MetaModels
class ClienteFibraModel(IModelWithId, BaseModel):
    id: int
    id_transmissor: int
    nome: str
    radpop_estrutura: Mapped[Radpop_estruturaEnum] = Field("radpop_estrutura", Radpop_estruturaEnum, Radpop_estruturaEnum.NAO)
    id_projeto: Mapped[Optional[int]] = Field("id_projeto", int, None)
    id_caixa_ftth: Mapped[Optional[int]] = Field("id_caixa_ftth", int, None)
    porta_ftth: Mapped[Optional[str]] = Field("porta_ftth", str, '')
    id_hardware: Mapped[Optional[int]] = Field("id_hardware", int, None)
    id_contrato: Mapped[Optional[int]] = Field("id_contrato", int, None)
    id_login: Mapped[Optional[int]] = Field("id_login", int, None)
    id_ramal: Mapped[Optional[int]] = Field("id_ramal", int, None)
    mac: Mapped[Optional[str]] = Field("mac", str, '')
    id_perfil: Mapped[Optional[int]] = Field("id_perfil", int, None)
    ponid: Mapped[Optional[str]] = Field("ponid", str, '')
    vlan: Mapped[Optional[str]] = Field("vlan", str, '')
    onu_numero: Mapped[Optional[str]] = Field("onu_numero", str, '')
    gemport: Mapped[Optional[str]] = Field("gemport", str, '')
    service_port: Mapped[Optional[str]] = Field("service_port", str, '')
    comandos: Mapped[Optional[str]] = Field("comandos", str, '')
    id_chamado_radpop: Mapped[Optional[str]] = Field("id_chamado_radpop", str, '')
    tipo_operacao: Mapped[Optional[Tipo_operacaoEnum]] = Field("tipo_operacao", Tipo_operacaoEnum, None)
    vlan_pppoe: Mapped[Optional[str]] = Field("vlan_pppoe", str, '')
    vlan_dhcp: Mapped[Optional[str]] = Field("vlan_dhcp", str, '')
    vlan_tr69: Mapped[Optional[str]] = Field("vlan_tr69", str, '')
    vlan_iptv: Mapped[Optional[str]] = Field("vlan_iptv", str, '')
    vlan_voip: Mapped[Optional[str]] = Field("vlan_voip", str, '')
    vlan_outros: Mapped[Optional[str]] = Field("vlan_outros", str, '')
    ip_gerencia: Mapped[Optional[str]] = Field("ip_gerencia", str, '')
    login_onu_cliente: Mapped[Optional[str]] = Field("login_onu_cliente", str, '')
    senha_onu_cliente: Mapped[Optional[str]] = Field("senha_onu_cliente", str, '')
    porta_telnet_onu_cliente: Mapped[Optional[str]] = Field("porta_telnet_onu_cliente", str, '')
    porta_web_onu_cliente: Mapped[Optional[str]] = Field("porta_web_onu_cliente", str, '')
    perfil_onu_cliente: Mapped[Optional[int]] = Field("perfil_onu_cliente", int, None)
    script_onu_cliente: Mapped[Optional[str]] = Field("script_onu_cliente", str, '')
    onu_tipo: Mapped[Optional[str]] = Field("onu_tipo", str, '')
    slotno: Mapped[Optional[str]] = Field("slotno", str, '')
    ponno: Mapped[Optional[str]] = Field("ponno", str, '')
    onu_rede_neutra: Mapped[Optional[Onu_rede_neutraEnum]] = Field("onu_rede_neutra", Onu_rede_neutraEnum, Onu_rede_neutraEnum.NAO)
    id_radpop_radio_porta: Mapped[Optional[int]] = Field("id_radpop_radio_porta", int, None)
    tipo_autenticacao: Mapped[Optional[str]] = Field("tipo_autenticacao", str, '')
    versao: Mapped[Optional[str]] = Field("versao", str, '')
    sinal_rx: Mapped[Optional[str]] = Field("sinal_rx", str, '')
    sinal_tx: Mapped[Optional[str]] = Field("sinal_tx", str, '')
    temperatura: Mapped[Optional[str]] = Field("temperatura", str, '')
    voltagem: Mapped[Optional[str]] = Field("voltagem", str, '')
    data_sinal: Mapped[Optional[str]] = Field("data_sinal", str, '')
    causa_ultima_queda: Mapped[Optional[str]] = Field("causa_ultima_queda", str, '')
    senorid: Mapped[Optional[str]] = Field("senorid", str, '')
    distancia_onu: Mapped[Optional[str]] = Field("distancia_onu", str, '')
    id_onu_unms: Mapped[Optional[str]] = Field("id_onu_unms", str, '')
    id_activity: Mapped[Optional[str]] = Field("id_activity", str, '')
    endereco_padrao_cliente: Mapped[Optional[str]] = Field("endereco_padrao_cliente", str, '')
    condominio_cliente: Mapped[Optional[int]] = Field("condominio_cliente", int, None)
    id_condominio: Mapped[Optional[int]] = Field("id_condominio", int, None)
    bloco_cliente: Mapped[Optional[str]] = Field("bloco_cliente", str, '')
    bloco: Mapped[Optional[str]] = Field("bloco", str, '')
    apartamento_cliente: Mapped[Optional[str]] = Field("apartamento_cliente", str, '')
    apartamento: Mapped[Optional[str]] = Field("apartamento", str, '')
    cep_cliente: Mapped[Optional[str]] = Field("cep_cliente", str, '')
    cep: Mapped[Optional[str]] = Field("cep", str, '')
    endereco_cliente: Mapped[Optional[str]] = Field("endereco_cliente", str, '')
    endereco: Mapped[Optional[str]] = Field("endereco", str, '')
    numero_cliente: Mapped[Optional[str]] = Field("numero_cliente", str, '')
    numero: Mapped[Optional[str]] = Field("numero", str, '')
    bairro_cliente: Mapped[Optional[str]] = Field("bairro_cliente", str, '')
    bairro: Mapped[Optional[str]] = Field("bairro", str, '')
    cidade_cliente: Mapped[Optional[int]] = Field("cidade_cliente", int, None)
    cidade: Mapped[Optional[int]] = Field("cidade", int, None)
    referencia_cliente: Mapped[Optional[str]] = Field("referencia_cliente", str, '')
    referencia: Mapped[Optional[str]] = Field("referencia", str, '')
    complemento_cliente: Mapped[Optional[str]] = Field("complemento_cliente", str, '')
    complemento: Mapped[Optional[str]] = Field("complemento", str, '')
    latitude: Mapped[Optional[str]] = Field("latitude", str, '')
    longitude: Mapped[Optional[str]] = Field("longitude", str, '')

    @property
    def table(self) -> str:
        return "radpop_radio_cliente_fibra"

    def to_dict(self) -> dict:
        def serialize(value) -> str:
            if value is None:
                return ''
            raw = getattr(value, 'value', value)
            return '' if raw is None else str(raw)

        data = {
            'id': str(self.id),
            'id_transmissor': str(self.id_transmissor) if self.id_transmissor is not None else '',
            'nome': self.nome if self.nome is not None else '',
            'radpop_estrutura': self.radpop_estrutura.value if self.radpop_estrutura is not None else '',
            'id_projeto': str(self.id_projeto) if self.id_projeto is not None else '',
            'id_caixa_ftth': str(self.id_caixa_ftth) if self.id_caixa_ftth is not None else '',
            'porta_ftth': self.porta_ftth if self.porta_ftth is not None else '',
            'id_hardware': str(self.id_hardware) if self.id_hardware is not None else '',
            'id_contrato': str(self.id_contrato) if self.id_contrato is not None else '',
            'id_login': str(self.id_login) if self.id_login is not None else '',
            'id_ramal': str(self.id_ramal) if self.id_ramal is not None else '',
            'mac': self.mac if self.mac is not None else '',
            'id_perfil': str(self.id_perfil) if self.id_perfil is not None else '',
            'ponid': self.ponid if self.ponid is not None else '',
            'vlan': self.vlan if self.vlan is not None else '',
            'onu_numero': self.onu_numero if self.onu_numero is not None else '',
            'gemport': self.gemport if self.gemport is not None else '',
            'service_port': self.service_port if self.service_port is not None else '',
            'comandos': self.comandos if self.comandos is not None else '',
            'id_chamado_radpop': self.id_chamado_radpop if self.id_chamado_radpop is not None else '',
            'tipo_operacao': self.tipo_operacao.value if self.tipo_operacao is not None else '',
            'vlan_pppoe': self.vlan_pppoe if self.vlan_pppoe is not None else '',
            'vlan_dhcp': self.vlan_dhcp if self.vlan_dhcp is not None else '',
            'vlan_tr69': self.vlan_tr69 if self.vlan_tr69 is not None else '',
            'vlan_iptv': self.vlan_iptv if self.vlan_iptv is not None else '',
            'vlan_voip': self.vlan_voip if self.vlan_voip is not None else '',
            'vlan_outros': self.vlan_outros if self.vlan_outros is not None else '',
            'ip_gerencia': self.ip_gerencia if self.ip_gerencia is not None else '',
            'login_onu_cliente': self.login_onu_cliente if self.login_onu_cliente is not None else '',
            'senha_onu_cliente': self.senha_onu_cliente if self.senha_onu_cliente is not None else '',
            'porta_telnet_onu_cliente': self.porta_telnet_onu_cliente if self.porta_telnet_onu_cliente is not None else '',
            'porta_web_onu_cliente': self.porta_web_onu_cliente if self.porta_web_onu_cliente is not None else '',
            'perfil_onu_cliente': str(self.perfil_onu_cliente) if self.perfil_onu_cliente is not None else '',
            'script_onu_cliente': self.script_onu_cliente if self.script_onu_cliente is not None else '',
            'onu_tipo': self.onu_tipo if self.onu_tipo is not None else '',
            'slotno': self.slotno if self.slotno is not None else '',
            'ponno': self.ponno if self.ponno is not None else '',
            'onu_rede_neutra': self.onu_rede_neutra.value if self.onu_rede_neutra is not None else '',
            'id_radpop_radio_porta': str(self.id_radpop_radio_porta) if self.id_radpop_radio_porta is not None else '',
            'tipo_autenticacao': self.tipo_autenticacao if self.tipo_autenticacao is not None else '',
            'versao': self.versao if self.versao is not None else '',
            'sinal_rx': self.sinal_rx if self.sinal_rx is not None else '',
            'sinal_tx': self.sinal_tx if self.sinal_tx is not None else '',
            'temperatura': self.temperatura if self.temperatura is not None else '',
            'voltagem': self.voltagem if self.voltagem is not None else '',
            'data_sinal': self.data_sinal if self.data_sinal is not None else '',
            'causa_ultima_queda': self.causa_ultima_queda if self.causa_ultima_queda is not None else '',
            'senorid': self.senorid if self.senorid is not None else '',
            'distancia_onu': self.distancia_onu if self.distancia_onu is not None else '',
            'id_onu_unms': self.id_onu_unms if self.id_onu_unms is not None else '',
            'id_activity': self.id_activity if self.id_activity is not None else '',
            'endereco_padrao_cliente': self.endereco_padrao_cliente if self.endereco_padrao_cliente is not None else '',
            'condominio_cliente': str(self.condominio_cliente) if self.condominio_cliente is not None else '',
            'id_condominio': str(self.id_condominio) if self.id_condominio is not None else '',
            'bloco_cliente': self.bloco_cliente if self.bloco_cliente is not None else '',
            'bloco': self.bloco if self.bloco is not None else '',
            'apartamento_cliente': self.apartamento_cliente if self.apartamento_cliente is not None else '',
            'apartamento': self.apartamento if self.apartamento is not None else '',
            'cep_cliente': self.cep_cliente if self.cep_cliente is not None else '',
            'cep': self.cep if self.cep is not None else '',
            'endereco_cliente': self.endereco_cliente if self.endereco_cliente is not None else '',
            'endereco': self.endereco if self.endereco is not None else '',
            'numero_cliente': self.numero_cliente if self.numero_cliente is not None else '',
            'numero': self.numero if self.numero is not None else '',
            'bairro_cliente': self.bairro_cliente if self.bairro_cliente is not None else '',
            'bairro': self.bairro if self.bairro is not None else '',
            'cidade_cliente': str(self.cidade_cliente) if self.cidade_cliente is not None else '',
            'cidade': str(self.cidade) if self.cidade is not None else '',
            'referencia_cliente': self.referencia_cliente if self.referencia_cliente is not None else '',
            'referencia': self.referencia if self.referencia is not None else '',
            'complemento_cliente': self.complemento_cliente if self.complemento_cliente is not None else '',
            'complemento': self.complemento if self.complemento is not None else '',
            'latitude': self.latitude if self.latitude is not None else '',
            'longitude': self.longitude if self.longitude is not None else '',
        }
        return {key: serialize(value) for key, value in data.items()}
    def is_valid(self) -> bool:
        return self.id is not None and self.id_transmissor is not None and self.nome is not None
