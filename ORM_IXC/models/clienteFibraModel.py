from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from ORM_IXC.enums.clienteFibra import *

from ORM_IXC.interfaces import IModel, IModelWithId


@dataclass(kw_only=True)
class ClienteFibraModel(IModelWithId):
    id_autoincrement: int
    id_transmissor: int
    nome: str
    radpop_estrutura: Radpop_estruturaEnum = Radpop_estruturaEnum.NAO
    id_projeto: Optional[int] = None
    id_caixa_ftth: Optional[int] = None
    porta_ftth: Optional[str] = ''
    id_hardware: Optional[int] = None
    id_contrato: Optional[int] = None
    id_login: Optional[int] = None
    id_ramal: Optional[int] = None
    mac: Optional[str] = ''
    id_perfil: Optional[int] = None
    ponid: Optional[str] = ''
    vlan: Optional[str] = ''
    onu_numero: Optional[str] = ''
    gemport: Optional[str] = ''
    service_port: Optional[str] = ''
    comandos: Optional[str] = ''
    id_chamado_radpop: Optional[str] = ''
    tipo_operacao: Optional[Tipo_operacaoEnum] = None
    vlan_pppoe: Optional[str] = ''
    vlan_dhcp: Optional[str] = ''
    vlan_tr69: Optional[str] = ''
    vlan_iptv: Optional[str] = ''
    vlan_voip: Optional[str] = ''
    vlan_outros: Optional[str] = ''
    ip_gerencia: Optional[str] = ''
    login_onu_cliente: Optional[str] = ''
    senha_onu_cliente: Optional[str] = ''
    porta_telnet_onu_cliente: Optional[str] = ''
    porta_web_onu_cliente: Optional[str] = ''
    perfil_onu_cliente: Optional[int] = None
    script_onu_cliente: Optional[str] = ''
    onu_tipo: Optional[str] = ''
    slotno: Optional[str] = ''
    ponno: Optional[str] = ''
    onu_rede_neutra: Optional[Onu_rede_neutraEnum] = Onu_rede_neutraEnum.NAO
    id_radpop_radio_porta: Optional[int] = None
    tipo_autenticacao: Optional[str] = ''
    versao: Optional[str] = ''
    sinal_rx: Optional[str] = ''
    sinal_tx: Optional[str] = ''
    temperatura: Optional[str] = ''
    voltagem: Optional[str] = ''
    data_sinal: Optional[str] = ''
    causa_ultima_queda: Optional[str] = ''
    senorid: Optional[str] = ''
    distancia_onu: Optional[str] = ''
    id_onu_unms: Optional[str] = ''
    id_activity: Optional[str] = ''
    endereco_padrao_cliente: Optional[str] = ''
    condominio_cliente: Optional[int] = None
    id_condominio: Optional[int] = None
    bloco_cliente: Optional[str] = ''
    bloco: Optional[str] = ''
    apartamento_cliente: Optional[str] = ''
    apartamento: Optional[str] = ''
    cep_cliente: Optional[str] = ''
    cep: Optional[str] = ''
    endereco_cliente: Optional[str] = ''
    endereco: Optional[str] = ''
    numero_cliente: Optional[str] = ''
    numero: Optional[str] = ''
    bairro_cliente: Optional[str] = ''
    bairro: Optional[str] = ''
    cidade_cliente: Optional[int] = None
    cidade: Optional[int] = None
    referencia_cliente: Optional[str] = ''
    referencia: Optional[str] = ''
    complemento_cliente: Optional[str] = ''
    complemento: Optional[str] = ''
    latitude: Optional[str] = ''
    longitude: Optional[str] = ''

    @property
    def id(self) -> str:
        return str(self.id_autoincrement)

    @property
    def table(self) -> str:
        return "radpop_radio_cliente_fibra"
    
    def to_dict(self) -> dict:
        return {
            'id_autoincrement': str(self.id_autoincrement),
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

    def is_valid(self) -> bool:
        return self.id_autoincrement is not None and self.id_transmissor is not None and self.nome is not None

    def __repr__(self) -> str:
        return f"ClienteFibra(id_autoincrement={self.id_autoincrement!r}, id_transmissor={self.id_transmissor!r}, nome={self.nome!r})"

    #------------------------------ CONVERSOR DTO ------------------------------#
    def dto_convert(self, data: dict[str, str]) -> IModel:
        return ClienteFibraModel(
            id_autoincrement=int(data.get('id_autoincrement', 0)),
            id_transmissor=int(data['id_transmissor']),
            nome=data.get('nome', ''),
            radpop_estrutura=Radpop_estruturaEnum(data['radpop_estrutura']),
            id_projeto=int(data['id_projeto']) if data.get('id_projeto') else None,
            id_caixa_ftth=int(data['id_caixa_ftth']) if data.get('id_caixa_ftth') else None,
            porta_ftth=data.get('porta_ftth', ''),
            id_hardware=int(data['id_hardware']) if data.get('id_hardware') else None,
            id_contrato=int(data['id_contrato']) if data.get('id_contrato') else None,
            id_login=int(data['id_login']) if data.get('id_login') else None,
            id_ramal=int(data['id_ramal']) if data.get('id_ramal') else None,
            mac=data.get('mac', ''),
            id_perfil=int(data['id_perfil']) if data.get('id_perfil') else None,
            ponid=data.get('ponid', ''),
            vlan=data.get('vlan', ''),
            onu_numero=data.get('onu_numero', ''),
            gemport=data.get('gemport', ''),
            service_port=data.get('service_port', ''),
            comandos=data.get('comandos', ''),
            id_chamado_radpop=data.get('id_chamado_radpop', ''),
            tipo_operacao=Tipo_operacaoEnum(data['tipo_operacao']) if data.get('tipo_operacao') else None,
            vlan_pppoe=data.get('vlan_pppoe', ''),
            vlan_dhcp=data.get('vlan_dhcp', ''),
            vlan_tr69=data.get('vlan_tr69', ''),
            vlan_iptv=data.get('vlan_iptv', ''),
            vlan_voip=data.get('vlan_voip', ''),
            vlan_outros=data.get('vlan_outros', ''),
            ip_gerencia=data.get('ip_gerencia', ''),
            login_onu_cliente=data.get('login_onu_cliente', ''),
            senha_onu_cliente=data.get('senha_onu_cliente', ''),
            porta_telnet_onu_cliente=data.get('porta_telnet_onu_cliente', ''),
            porta_web_onu_cliente=data.get('porta_web_onu_cliente', ''),
            perfil_onu_cliente=int(data['perfil_onu_cliente']) if data.get('perfil_onu_cliente') else None,
            script_onu_cliente=data.get('script_onu_cliente', ''),
            onu_tipo=data.get('onu_tipo', ''),
            slotno=data.get('slotno', ''),
            ponno=data.get('ponno', ''),
            onu_rede_neutra=Onu_rede_neutraEnum(data['onu_rede_neutra']) if data.get('onu_rede_neutra') else None,
            id_radpop_radio_porta=int(data['id_radpop_radio_porta']) if data.get('id_radpop_radio_porta') else None,
            tipo_autenticacao=data.get('tipo_autenticacao', ''),
            versao=data.get('versao', ''),
            sinal_rx=data.get('sinal_rx', ''),
            sinal_tx=data.get('sinal_tx', ''),
            temperatura=data.get('temperatura', ''),
            voltagem=data.get('voltagem', ''),
            data_sinal=data.get('data_sinal', ''),
            causa_ultima_queda=data.get('causa_ultima_queda', ''),
            senorid=data.get('senorid', ''),
            distancia_onu=data.get('distancia_onu', ''),
            id_onu_unms=data.get('id_onu_unms', ''),
            id_activity=data.get('id_activity', ''),
            endereco_padrao_cliente=data.get('endereco_padrao_cliente', ''),
            condominio_cliente=int(data['condominio_cliente']) if data.get('condominio_cliente') else None,
            id_condominio=int(data['id_condominio']) if data.get('id_condominio') else None,
            bloco_cliente=data.get('bloco_cliente', ''),
            bloco=data.get('bloco', ''),
            apartamento_cliente=data.get('apartamento_cliente', ''),
            apartamento=data.get('apartamento', ''),
            cep_cliente=data.get('cep_cliente', ''),
            cep=data.get('cep', ''),
            endereco_cliente=data.get('endereco_cliente', ''),
            endereco=data.get('endereco', ''),
            numero_cliente=data.get('numero_cliente', ''),
            numero=data.get('numero', ''),
            bairro_cliente=data.get('bairro_cliente', ''),
            bairro=data.get('bairro', ''),
            cidade_cliente=int(data['cidade_cliente']) if data.get('cidade_cliente') else None,
            cidade=int(data['cidade']) if data.get('cidade') else None,
            referencia_cliente=data.get('referencia_cliente', ''),
            referencia=data.get('referencia', ''),
            complemento_cliente=data.get('complemento_cliente', ''),
            complemento=data.get('complemento', ''),
            latitude=data.get('latitude', ''),
            longitude=data.get('longitude', ''),
        )
