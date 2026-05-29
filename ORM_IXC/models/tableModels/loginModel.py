from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from ORM_IXC.interfaces import IModel, IModelWithId
from ORM_IXC.enums.login import *
from ORM_IXC.statemants.mapper import Mapped, field as mapped_field
from ORM_IXC.statemants.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel

@MetaModels
class LoginModel(IModelWithId, BaseModel):
    id: Mapped[Optional[int]]
    tipo_conexao_mapa: Mapped[Tipo_conexao_mapaEnum]
    id_cliente: Mapped[int]
    id_grupo: Mapped[int]
    login: Mapped[str]
    login_simultaneo: Mapped[str]
    autenticacao: Mapped[AutenticacaoEnum] = mapped_field(AutenticacaoEnum.PPPOE)
    id_integracao: Mapped[Optional[int]] = mapped_field(None)
    lte_id: Mapped[Optional[int]] = mapped_field(None)
    pacote_lte: Mapped[Optional[str]] = mapped_field('')
    id_contrato: Mapped[Optional[int]] = mapped_field(None)
    id_filial: Mapped[Optional[int]] = mapped_field(None)
    contrato_plano_venda_: Mapped[Optional[str]] = mapped_field('')
    agent_circuit_id: Mapped[Optional[str]] = mapped_field('')
    senha_md5: Mapped[Senha_md5Enum] = mapped_field(Senha_md5Enum.NAO)
    senha: Mapped[Optional[str]] = mapped_field('')
    ping_traceroute: Mapped[Optional[str]] = mapped_field('')
    ativo: Mapped[AtivoEnum] = mapped_field(AtivoEnum.SIM)
    online: Mapped[Optional[OnlineEnum]] = mapped_field(OnlineEnum.SEM_STATUS)
    ultima_atualizacao: Mapped[Optional[str]] = mapped_field('')
    usuario_router1: Mapped[Optional[str]] = mapped_field('')
    senha_router1: Mapped[Optional[str]] = mapped_field('')
    senha_router2: Mapped[Optional[str]] = mapped_field('')
    ssid_router_wifi: Mapped[Optional[str]] = mapped_field('')
    senha_rede_sem_fio: Mapped[Optional[str]] = mapped_field('')
    ssid_router_wifi_5ghz: Mapped[Optional[str]] = mapped_field('')
    senha_rede_sem_fio_5ghz: Mapped[Optional[str]] = mapped_field('')
    redirect_interfaces: Mapped[Optional[str]] = mapped_field('')
    ip: Mapped[Optional[str]] = mapped_field('')
    ip_aviso: Mapped[Optional[str]] = mapped_field('')
    auto_preencher_ip: Mapped[Auto_preencher_ipEnum] = mapped_field(Auto_preencher_ipEnum.CONFIGURACAO_PADRAO)
    fixar_ip: Mapped[Fixar_ipEnum] = mapped_field(Fixar_ipEnum.CONFIGURACAO_PADRAO)
    relacionar_ip_ao_login: Mapped[Relacionar_ip_ao_loginEnum] = mapped_field(Relacionar_ip_ao_loginEnum.CONFIGURACAO_PADRAO)
    framed_pd_ipv6: Mapped[Optional[str]] = mapped_field('')
    framed_autopreencher_ipv6: Mapped[Optional[Framed_autopreencher_ipv6Enum]] = mapped_field(Framed_autopreencher_ipv6Enum.CONFIGURACAO_PADRAO)
    framed_fixar_ipv6: Mapped[Optional[Framed_fixar_ipv6Enum]] = mapped_field(Framed_fixar_ipv6Enum.CONFIGURACAO_PADRAO)
    framed_relacionar_ipv6_ao_login: Mapped[Optional[Framed_relacionar_ipv6_ao_loginEnum]] = mapped_field(Framed_relacionar_ipv6_ao_loginEnum.CONFIGURACAO_PADRAO)
    pd_ipv6: Mapped[Optional[str]] = mapped_field('')
    auto_preencher_ipv6: Mapped[Optional[Auto_preencher_ipv6Enum]] = mapped_field(Auto_preencher_ipv6Enum.CONFIGURACAO_PADRAO)
    fixar_ipv6: Mapped[Optional[Fixar_ipv6Enum]] = mapped_field(Fixar_ipv6Enum.CONFIGURACAO_PADRAO)
    relacionar_ipv6_ao_login: Mapped[Optional[Relacionar_ipv6_ao_loginEnum]] = mapped_field(Relacionar_ipv6_ao_loginEnum.CONFIGURACAO_PADRAO)
    mac: Mapped[Optional[str]] = mapped_field('')
    autenticacao_por_mac: Mapped[Autenticacao_por_macEnum] = mapped_field(Autenticacao_por_macEnum.PADRAO)
    usuario_wpa2aes: Mapped[Optional[str]] = mapped_field('')
    senha_wpa2aes: Mapped[Optional[str]] = mapped_field('')
    autenticacao_wpa: Mapped[Optional[str]] = mapped_field('')
    id_porta_transmissor: Mapped[Optional[int]] = mapped_field(None)
    auto_preencher_mac: Mapped[Auto_preencher_macEnum] = mapped_field(Auto_preencher_macEnum.CONFIGURACAO_PADRAO)
    relacionar_mac_ao_login: Mapped[Relacionar_mac_ao_loginEnum] = mapped_field(Relacionar_mac_ao_loginEnum.CONFIGURACAO_PADRAO)
    relacionar_concentrador_ao_login: Mapped[Optional[Relacionar_concentrador_ao_loginEnum]] = mapped_field(Relacionar_concentrador_ao_loginEnum.CONFIGURACAO_PADRAO)
    pool_radius: Mapped[Optional[int]] = mapped_field(None)
    id_radgrupos_pools: Mapped[Optional[int]] = mapped_field(None)
    id_rad_dns: Mapped[Optional[int]] = mapped_field(None)
    id_concentrador: Mapped[Optional[int]] = mapped_field(None)
    ip_concentrador: Mapped[Optional[str]] = mapped_field('')
    interface: Mapped[Optional[int]] = mapped_field(None)
    vlan: Mapped[Optional[str]] = mapped_field('')
    vlan_ip_rede: Mapped[Optional[str]] = mapped_field('')
    gw_vlan: Mapped[Optional[str]] = mapped_field('')
    service_tag_vlan: Mapped[Optional[str]] = mapped_field('')
    mtu: Mapped[Optional[str]] = mapped_field('')
    concentrador: Mapped[Optional[str]] = mapped_field('')
    conexao: Mapped[Optional[str]] = mapped_field('')
    tipo_conexao: Mapped[Optional[str]] = mapped_field('')
    porta_http_nas: Mapped[Optional[str]] = mapped_field('')
    acct_session_id: Mapped[Optional[str]] = mapped_field('')
    tipo_vinculo_plano: Mapped[Tipo_vinculo_planoEnum] = mapped_field(Tipo_vinculo_planoEnum.PADRAO)
    cliente_tem_a_senha: Mapped[Optional[str]] = mapped_field('')
    autenticacao_wps: Mapped[Optional[str]] = mapped_field('')
    autenticacao_mac: Mapped[Optional[str]] = mapped_field('')
    tipo_acesso: Mapped[Optional[Tipo_acessoEnum]] = mapped_field(Tipo_acessoEnum.HTTP)
    porta_http: Mapped[Optional[str]] = mapped_field('')
    porta_router2: Mapped[Optional[str]] = mapped_field('')
    ip_aux: Mapped[Optional[str]] = mapped_field('')
    porta_aux: Mapped[Optional[str]] = mapped_field('')
    ultima_conexao_inicial: Mapped[Optional[str]] = mapped_field('')
    ultima_conexao_final: Mapped[Optional[str]] = mapped_field('')
    motivo_desconexao: Mapped[Optional[str]] = mapped_field('')
    count_desconexao: Mapped[Optional[str]] = mapped_field('')
    tempo_conexao: Mapped[Optional[str]] = mapped_field('')
    tempo_conectado: Mapped[Optional[str]] = mapped_field('')
    download_atual: Mapped[Optional[str]] = mapped_field('')
    upload_atual: Mapped[Optional[str]] = mapped_field('')
    franquia_maximo: Mapped[Optional[str]] = mapped_field('')
    franquia_consumo: Mapped[Optional[str]] = mapped_field('')
    franquia_consumo_up: Mapped[Optional[str]] = mapped_field('')
    franquia_atingida: Mapped[Optional[Franquia_atingidaEnum]] = mapped_field(Franquia_atingidaEnum.NAO)
    onu_compartilhada: Mapped[Optional[Onu_compartilhadaEnum]] = mapped_field(None)
    id_df_projeto: Mapped[Optional[int]] = mapped_field(None)
    id_transmissor: Mapped[Optional[int]] = mapped_field(None)
    modelo_tranmissor: Mapped[Optional[str]] = mapped_field('')
    interface_transmissao: Mapped[Optional[int]] = mapped_field(None)
    interface_transmissao_fibra: Mapped[Optional[int]] = mapped_field(None)
    id_caixa_ftth: Mapped[Optional[int]] = mapped_field(None)
    ftth_porta: Mapped[Optional[str]] = mapped_field('')
    tronco: Mapped[Optional[str]] = mapped_field('')
    splitter: Mapped[Optional[str]] = mapped_field('')
    onu_mac: Mapped[Optional[str]] = mapped_field('')
    sinal_ultimo_atendimento: Mapped[Optional[str]] = mapped_field('')
    id_hardware: Mapped[Optional[int]] = mapped_field(None)
    tipo_equipamento: Mapped[Optional[Tipo_equipamentoEnum]] = mapped_field(None)
    metragem_interna: Mapped[Optional[str]] = mapped_field('')
    metragem_externa: Mapped[Optional[str]] = mapped_field('')
    id_reserva_rede_neutra: Mapped[Optional[int]] = mapped_field(None)
    endereco_padrao_cliente: Mapped[Endereco_padrao_clienteEnum] = mapped_field(Endereco_padrao_clienteEnum.PADRAO_CLIENTE)
    ponta: Mapped[Optional[PontaEnum]] = mapped_field(None)
    id_condominio: Mapped[Optional[int]] = mapped_field(None)
    id_predio: Mapped[Optional[int]] = mapped_field(None)
    condominio_novo: Mapped[Optional[int]] = mapped_field(None)
    bloco: Mapped[Optional[str]] = mapped_field('')
    bloco_novo: Mapped[Optional[str]] = mapped_field('')
    apartamento: Mapped[Optional[str]] = mapped_field('')
    apartamento_novo: Mapped[Optional[str]] = mapped_field('')
    cep: Mapped[Optional[str]] = mapped_field('')
    cep_novo: Mapped[Optional[str]] = mapped_field('')
    endereco: Mapped[Optional[str]] = mapped_field('')
    endereco_novo: Mapped[Optional[str]] = mapped_field('')
    numero: Mapped[Optional[str]] = mapped_field('')
    numero_novo: Mapped[Optional[str]] = mapped_field('')
    bairro: Mapped[Optional[str]] = mapped_field('')
    bairro_novo: Mapped[Optional[str]] = mapped_field('')
    cidade: Mapped[Optional[int]] = mapped_field(None)
    cidade_novo: Mapped[Optional[int]] = mapped_field(None)
    referencia: Mapped[Optional[str]] = mapped_field('')
    referencia_novo: Mapped[Optional[str]] = mapped_field('')
    complemento: Mapped[Optional[str]] = mapped_field('')
    complemento_novo: Mapped[Optional[str]] = mapped_field('')
    latitude: Mapped[Optional[str]] = mapped_field('')
    latitude_novo: Mapped[Optional[str]] = mapped_field('')
    longitude: Mapped[Optional[str]] = mapped_field('')
    longitude_novo: Mapped[Optional[str]] = mapped_field('')
    obs: Mapped[Optional[str]] = mapped_field('')

    @property
    def table(self) -> str:
        return "radusuarios"

    def _serialize_enum(self, value) -> str:
        """Serializa um valor de enum ou retorna string vazia se None"""
        if value is None:
            return ''
        if hasattr(value, 'value'):
            return str(value.value)
        return str(value)
    
    def to_dict(self) -> dict[str, str]:
        def serialize(value) -> str:
            if value is None:
                return ''
            raw = getattr(value, 'value', value)
            return '' if raw is None else str(raw)

        data = {
            'id': self.id,
            'tipo_conexao_mapa': self._serialize_enum(self.tipo_conexao_mapa) if self.tipo_conexao_mapa is not None else '',
            'id_cliente': str(self.id_cliente) if self.id_cliente is not None else '',
            'id_grupo': str(self.id_grupo) if self.id_grupo is not None else '',
            'login': self.login if self.login is not None else '',
            'login_simultaneo': self.login_simultaneo if self.login_simultaneo is not None else '',
            'autenticacao': self._serialize_enum(self.autenticacao) if self.autenticacao is not None else '',
            'id_integracao': str(self.id_integracao) if self.id_integracao is not None else '',
            'lte_id': str(self.lte_id) if self.lte_id is not None else '',
            'pacote_lte': self.pacote_lte if self.pacote_lte is not None else '',
            'id_contrato': str(self.id_contrato) if self.id_contrato is not None else '',
            'id_filial': str(self.id_filial) if self.id_filial is not None else '',
            'contrato_plano_venda_': self.contrato_plano_venda_ if self.contrato_plano_venda_ is not None else '',
            'agent_circuit_id': self.agent_circuit_id if self.agent_circuit_id is not None else '',
            'senha_md5': self._serialize_enum(self.senha_md5) if self.senha_md5 is not None else '',
            'senha': self.senha if self.senha is not None else '',
            'ping_traceroute': self.ping_traceroute if self.ping_traceroute is not None else '',
            'ativo': self._serialize_enum(self.ativo) if self.ativo is not None else '',
            'online': self._serialize_enum(self.online) if self.online is not None else '',
            'ultima_atualizacao': self.ultima_atualizacao if self.ultima_atualizacao is not None else '',
            'usuario_router1': self.usuario_router1 if self.usuario_router1 is not None else '',
            'senha_router1': self.senha_router1 if self.senha_router1 is not None else '',
            'senha_router2': self.senha_router2 if self.senha_router2 is not None else '',
            'ssid_router_wifi': self.ssid_router_wifi if self.ssid_router_wifi is not None else '',
            'senha_rede_sem_fio': self.senha_rede_sem_fio if self.senha_rede_sem_fio is not None else '',
            'ssid_router_wifi_5ghz': self.ssid_router_wifi_5ghz if self.ssid_router_wifi_5ghz is not None else '',
            'senha_rede_sem_fio_5ghz': self.senha_rede_sem_fio_5ghz if self.senha_rede_sem_fio_5ghz is not None else '',
            'redirect_interfaces': self.redirect_interfaces if self.redirect_interfaces is not None else '',
            'ip': self.ip if self.ip is not None else '',
            'ip_aviso': self.ip_aviso if self.ip_aviso is not None else '',
            'auto_preencher_ip': self._serialize_enum(self.auto_preencher_ip) if self.auto_preencher_ip is not None else '',
            'fixar_ip': self._serialize_enum(self.fixar_ip) if self.fixar_ip is not None else '',
            'relacionar_ip_ao_login': self._serialize_enum(self.relacionar_ip_ao_login) if self.relacionar_ip_ao_login is not None else '',
            'framed_pd_ipv6': self.framed_pd_ipv6 if self.framed_pd_ipv6 is not None else '',
            'framed_autopreencher_ipv6': self._serialize_enum(self.framed_autopreencher_ipv6) if self.framed_autopreencher_ipv6 is not None else '',
            'framed_fixar_ipv6': self._serialize_enum(self.framed_fixar_ipv6) if self.framed_fixar_ipv6 is not None else '',
            'framed_relacionar_ipv6_ao_login': self._serialize_enum(self.framed_relacionar_ipv6_ao_login) if self.framed_relacionar_ipv6_ao_login is not None else '',
            'pd_ipv6': self.pd_ipv6 if self.pd_ipv6 is not None else '',
            'auto_preencher_ipv6': self._serialize_enum(self.auto_preencher_ipv6) if self.auto_preencher_ipv6 is not None else '',
            'fixar_ipv6': self._serialize_enum(self.fixar_ipv6) if self.fixar_ipv6 is not None else '',
            'relacionar_ipv6_ao_login': self._serialize_enum(self.relacionar_ipv6_ao_login) if self.relacionar_ipv6_ao_login is not None else '',
            'mac': self.mac if self.mac is not None else '',
            'autenticacao_por_mac': self._serialize_enum(self.autenticacao_por_mac) if self.autenticacao_por_mac is not None else '',
            'usuario_wpa2aes': self.usuario_wpa2aes if self.usuario_wpa2aes is not None else '',
            'senha_wpa2aes': self.senha_wpa2aes if self.senha_wpa2aes is not None else '',
            'autenticacao_wpa': self.autenticacao_wpa if self.autenticacao_wpa is not None else '',
            'id_porta_transmissor': str(self.id_porta_transmissor) if self.id_porta_transmissor is not None else '',
            'auto_preencher_mac': self._serialize_enum(self.auto_preencher_mac) if self.auto_preencher_mac is not None else '',
            'relacionar_mac_ao_login': self._serialize_enum(self.relacionar_mac_ao_login) if self.relacionar_mac_ao_login is not None else '',
            'relacionar_concentrador_ao_login': self._serialize_enum(self.relacionar_concentrador_ao_login) if self.relacionar_concentrador_ao_login is not None else '',
            'pool_radius': str(self.pool_radius) if self.pool_radius is not None else '',
            'id_radgrupos_pools': str(self.id_radgrupos_pools) if self.id_radgrupos_pools is not None else '',
            'id_rad_dns': str(self.id_rad_dns) if self.id_rad_dns is not None else '',
            'id_concentrador': str(self.id_concentrador) if self.id_concentrador is not None else '',
            'ip_concentrador': self.ip_concentrador if self.ip_concentrador is not None else '',
            'interface': str(self.interface) if self.interface is not None else '',
            'vlan': self.vlan if self.vlan is not None else '',
            'vlan_ip_rede': self.vlan_ip_rede if self.vlan_ip_rede is not None else '',
            'gw_vlan': self.gw_vlan if self.gw_vlan is not None else '',
            'service_tag_vlan': self.service_tag_vlan if self.service_tag_vlan is not None else '',
            'mtu': self.mtu if self.mtu is not None else '',
            'concentrador': self.concentrador if self.concentrador is not None else '',
            'conexao': self.conexao if self.conexao is not None else '',
            'tipo_conexao': self.tipo_conexao if self.tipo_conexao is not None else '',
            'porta_http_nas': self.porta_http_nas if self.porta_http_nas is not None else '',
            'acct_session_id': self.acct_session_id if self.acct_session_id is not None else '',
            'tipo_vinculo_plano': self._serialize_enum(self.tipo_vinculo_plano) if self.tipo_vinculo_plano is not None else '',
            'cliente_tem_a_senha': self.cliente_tem_a_senha if self.cliente_tem_a_senha is not None else '',
            'autenticacao_wps': self.autenticacao_wps if self.autenticacao_wps is not None else '',
            'autenticacao_mac': self.autenticacao_mac if self.autenticacao_mac is not None else '',
            'tipo_acesso': self._serialize_enum(self.tipo_acesso) if self.tipo_acesso is not None else '',
            'porta_http': self.porta_http if self.porta_http is not None else '',
            'porta_router2': self.porta_router2 if self.porta_router2 is not None else '',
            'ip_aux': self.ip_aux if self.ip_aux is not None else '',
            'porta_aux': self.porta_aux if self.porta_aux is not None else '',
            'ultima_conexao_inicial': self.ultima_conexao_inicial if self.ultima_conexao_inicial is not None else '',
            'ultima_conexao_final': self.ultima_conexao_final if self.ultima_conexao_final is not None else '',
            'motivo_desconexao': self.motivo_desconexao if self.motivo_desconexao is not None else '',
            'count_desconexao': self.count_desconexao if self.count_desconexao is not None else '',
            'tempo_conexao': self.tempo_conexao if self.tempo_conexao is not None else '',
            'tempo_conectado': self.tempo_conectado if self.tempo_conectado is not None else '',
            'download_atual': self.download_atual if self.download_atual is not None else '',
            'upload_atual': self.upload_atual if self.upload_atual is not None else '',
            'franquia_maximo': self.franquia_maximo if self.franquia_maximo is not None else '',
            'franquia_consumo': self.franquia_consumo if self.franquia_consumo is not None else '',
            'franquia_consumo_up': self.franquia_consumo_up if self.franquia_consumo_up is not None else '',
            'franquia_atingida': self._serialize_enum(self.franquia_atingida) if self.franquia_atingida is not None else '',
            'onu_compartilhada': self._serialize_enum(self.onu_compartilhada) if self.onu_compartilhada is not None else '',
            'id_df_projeto': str(self.id_df_projeto) if self.id_df_projeto is not None else '',
            'id_transmissor': str(self.id_transmissor) if self.id_transmissor is not None else '',
            'modelo_tranmissor': self.modelo_tranmissor if self.modelo_tranmissor is not None else '',
            'interface_transmissao': str(self.interface_transmissao) if self.interface_transmissao is not None else '',
            'interface_transmissao_fibra': str(self.interface_transmissao_fibra) if self.interface_transmissao_fibra is not None else '',
            'id_caixa_ftth': str(self.id_caixa_ftth) if self.id_caixa_ftth is not None else '',
            'ftth_porta': self.ftth_porta if self.ftth_porta is not None else '',
            'tronco': self.tronco if self.tronco is not None else '',
            'splitter': self.splitter if self.splitter is not None else '',
            'onu_mac': self.onu_mac if self.onu_mac is not None else '',
            'sinal_ultimo_atendimento': self.sinal_ultimo_atendimento if self.sinal_ultimo_atendimento is not None else '',
            'id_hardware': str(self.id_hardware) if self.id_hardware is not None else '',
            'tipo_equipamento': self._serialize_enum(self.tipo_equipamento) if self.tipo_equipamento is not None else '',
            'metragem_interna': self.metragem_interna if self.metragem_interna is not None else '',
            'metragem_externa': self.metragem_externa if self.metragem_externa is not None else '',
            'id_reserva_rede_neutra': str(self.id_reserva_rede_neutra) if self.id_reserva_rede_neutra is not None else '',
            'endereco_padrao_cliente': self._serialize_enum(self.endereco_padrao_cliente) if self.endereco_padrao_cliente is not None else '',
            'ponta': self._serialize_enum(self.ponta) if self.ponta is not None else '',
            'id_condominio': str(self.id_condominio) if self.id_condominio is not None else '',
            'id_predio': str(self.id_predio) if self.id_predio is not None else '',
            'condominio_novo': str(self.condominio_novo) if self.condominio_novo is not None else '',
            'bloco': self.bloco if self.bloco is not None else '',
            'bloco_novo': self.bloco_novo if self.bloco_novo is not None else '',
            'apartamento': self.apartamento if self.apartamento is not None else '',
            'apartamento_novo': self.apartamento_novo if self.apartamento_novo is not None else '',
            'cep': self.cep if self.cep is not None else '',
            'cep_novo': self.cep_novo if self.cep_novo is not None else '',
            'endereco': self.endereco if self.endereco is not None else '',
            'endereco_novo': self.endereco_novo if self.endereco_novo is not None else '',
            'numero': self.numero if self.numero is not None else '',
            'numero_novo': self.numero_novo if self.numero_novo is not None else '',
            'bairro': self.bairro if self.bairro is not None else '',
            'bairro_novo': self.bairro_novo if self.bairro_novo is not None else '',
            'cidade': str(self.cidade) if self.cidade is not None else '',
            'cidade_novo': str(self.cidade_novo) if self.cidade_novo is not None else '',
            'referencia': self.referencia if self.referencia is not None else '',
            'referencia_novo': self.referencia_novo if self.referencia_novo is not None else '',
            'complemento': self.complemento if self.complemento is not None else '',
            'complemento_novo': self.complemento_novo if self.complemento_novo is not None else '',
            'latitude': self.latitude if self.latitude is not None else '',
            'latitude_novo': self.latitude_novo if self.latitude_novo is not None else '',
            'longitude': self.longitude if self.longitude is not None else '',
            'longitude_novo': self.longitude_novo if self.longitude_novo is not None else '',
            'obs': self.obs if self.obs is not None else '',
        }
        return {key: serialize(value) for key, value in data.items()}

    def is_valid(self) -> bool:
        return self.id is not None and self.tipo_conexao_mapa is not None and self.id_cliente is not None and self.id_grupo is not None and self.login is not None and self.login_simultaneo is not None
