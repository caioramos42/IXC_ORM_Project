from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from ORM_IXC.interfaces import IModel, IModelWithId
from ORM_IXC.enums.login import *
from ORM_IXC.statemants.metaManager import MetaModels

@MetaModels
class LoginModel():
    id: int
    tipo_conexao_mapa: Tipo_conexao_mapaEnum
    id_cliente: int
    id_grupo: int
    login: str
    login_simultaneo: str
    autenticacao: AutenticacaoEnum = AutenticacaoEnum.PPPOE
    id_integracao: Optional[int] = None
    lte_id: Optional[int] = None
    pacote_lte: Optional[str] = ''
    id_contrato: Optional[int] = None
    id_filial: Optional[int] = None
    contrato_plano_venda_: Optional[str] = ''
    agent_circuit_id: Optional[str] = ''
    senha_md5: Senha_md5Enum = Senha_md5Enum.NAO
    senha: Optional[str] = ''
    ping_traceroute: Optional[str] = ''
    ativo: AtivoEnum = AtivoEnum.SIM
    online: Optional[OnlineEnum] = OnlineEnum.SEM_STATUS
    ultima_atualizacao: Optional[str] = ''
    usuario_router1: Optional[str] = ''
    senha_router1: Optional[str] = ''
    senha_router2: Optional[str] = ''
    ssid_router_wifi: Optional[str] = ''
    senha_rede_sem_fio: Optional[str] = ''
    ssid_router_wifi_5ghz: Optional[str] = ''
    senha_rede_sem_fio_5ghz: Optional[str] = ''
    redirect_interfaces: Optional[str] = ''
    ip: Optional[str] = ''
    ip_aviso: Optional[str] = ''
    auto_preencher_ip: Auto_preencher_ipEnum = Auto_preencher_ipEnum.CONFIGURACAO_PADRAO
    fixar_ip: Fixar_ipEnum = Fixar_ipEnum.CONFIGURACAO_PADRAO
    relacionar_ip_ao_login: Relacionar_ip_ao_loginEnum = Relacionar_ip_ao_loginEnum.CONFIGURACAO_PADRAO
    framed_pd_ipv6: Optional[str] = ''
    framed_autopreencher_ipv6: Optional[Framed_autopreencher_ipv6Enum] = Framed_autopreencher_ipv6Enum.CONFIGURACAO_PADRAO
    framed_fixar_ipv6: Optional[Framed_fixar_ipv6Enum] = Framed_fixar_ipv6Enum.CONFIGURACAO_PADRAO
    framed_relacionar_ipv6_ao_login: Optional[Framed_relacionar_ipv6_ao_loginEnum] = Framed_relacionar_ipv6_ao_loginEnum.CONFIGURACAO_PADRAO
    pd_ipv6: Optional[str] = ''
    auto_preencher_ipv6: Optional[Auto_preencher_ipv6Enum] = Auto_preencher_ipv6Enum.CONFIGURACAO_PADRAO
    fixar_ipv6: Optional[Fixar_ipv6Enum] = Fixar_ipv6Enum.CONFIGURACAO_PADRAO
    relacionar_ipv6_ao_login: Optional[Relacionar_ipv6_ao_loginEnum] = Relacionar_ipv6_ao_loginEnum.CONFIGURACAO_PADRAO
    mac: Optional[str] = ''
    autenticacao_por_mac: Autenticacao_por_macEnum = Autenticacao_por_macEnum.PADRAO
    usuario_wpa2aes: Optional[str] = ''
    senha_wpa2aes: Optional[str] = ''
    autenticacao_wpa: Optional[str] = ''
    id_porta_transmissor: Optional[int] = None
    auto_preencher_mac: Auto_preencher_macEnum = Auto_preencher_macEnum.CONFIGURACAO_PADRAO
    relacionar_mac_ao_login: Relacionar_mac_ao_loginEnum = Relacionar_mac_ao_loginEnum.CONFIGURACAO_PADRAO
    relacionar_concentrador_ao_login: Optional[Relacionar_concentrador_ao_loginEnum] = Relacionar_concentrador_ao_loginEnum.CONFIGURACAO_PADRAO
    pool_radius: Optional[int] = None
    id_radgrupos_pools: Optional[int] = None
    id_rad_dns: Optional[int] = None
    id_concentrador: Optional[int] = None
    ip_concentrador: Optional[str] = ''
    interface: Optional[int] = None
    vlan: Optional[str] = ''
    vlan_ip_rede: Optional[str] = ''
    gw_vlan: Optional[str] = ''
    service_tag_vlan: Optional[str] = ''
    mtu: Optional[str] = ''
    concentrador: Optional[str] = ''
    conexao: Optional[str] = ''
    tipo_conexao: Optional[str] = ''
    porta_http_nas: Optional[str] = ''
    acct_session_id: Optional[str] = ''
    tipo_vinculo_plano: Tipo_vinculo_planoEnum = Tipo_vinculo_planoEnum.PADRAO
    cliente_tem_a_senha: Optional[str] = ''
    autenticacao_wps: Optional[str] = ''
    autenticacao_mac: Optional[str] = ''
    tipo_acesso: Optional[Tipo_acessoEnum] = Tipo_acessoEnum.HTTP
    porta_http: Optional[str] = ''
    porta_router2: Optional[str] = ''
    ip_aux: Optional[str] = ''
    porta_aux: Optional[str] = ''
    ultima_conexao_inicial: Optional[str] = ''
    ultima_conexao_final: Optional[str] = ''
    motivo_desconexao: Optional[str] = ''
    count_desconexao: Optional[str] = ''
    tempo_conexao: Optional[str] = ''
    tempo_conectado: Optional[str] = ''
    download_atual: Optional[str] = ''
    upload_atual: Optional[str] = ''
    franquia_maximo: Optional[str] = ''
    franquia_consumo: Optional[str] = ''
    franquia_consumo_up: Optional[str] = ''
    franquia_atingida: Optional[Franquia_atingidaEnum] = Franquia_atingidaEnum.NAO
    onu_compartilhada: Optional[Onu_compartilhadaEnum] = None
    id_df_projeto: Optional[int] = None
    id_transmissor: Optional[int] = None
    modelo_tranmissor: Optional[str] = ''
    interface_transmissao: Optional[int] = None
    interface_transmissao_fibra: Optional[int] = None
    id_caixa_ftth: Optional[int] = None
    ftth_porta: Optional[str] = ''
    tronco: Optional[str] = ''
    splitter: Optional[str] = ''
    onu_mac: Optional[str] = ''
    sinal_ultimo_atendimento: Optional[str] = ''
    id_hardware: Optional[int] = None
    tipo_equipamento: Optional[Tipo_equipamentoEnum] = None
    metragem_interna: Optional[str] = ''
    metragem_externa: Optional[str] = ''
    id_reserva_rede_neutra: Optional[int] = None
    endereco_padrao_cliente: Endereco_padrao_clienteEnum = Endereco_padrao_clienteEnum.PADRAO_CLIENTE
    ponta: Optional[PontaEnum] = None
    id_condominio: Optional[int] = None
    id_predio: Optional[int] = None
    condominio_novo: Optional[int] = None
    bloco: Optional[str] = ''
    bloco_novo: Optional[str] = ''
    apartamento: Optional[str] = ''
    apartamento_novo: Optional[str] = ''
    cep: Optional[str] = ''
    cep_novo: Optional[str] = ''
    endereco: Optional[str] = ''
    endereco_novo: Optional[str] = ''
    numero: Optional[str] = ''
    numero_novo: Optional[str] = ''
    bairro: Optional[str] = ''
    bairro_novo: Optional[str] = ''
    cidade: Optional[int] = None
    cidade_novo: Optional[int] = None
    referencia: Optional[str] = ''
    referencia_novo: Optional[str] = ''
    complemento: Optional[str] = ''
    complemento_novo: Optional[str] = ''
    latitude: Optional[str] = ''
    latitude_novo: Optional[str] = ''
    longitude: Optional[str] = ''
    longitude_novo: Optional[str] = ''
    obs: Optional[str] = ''

    @property
    def table(self) -> str:
        return "radusuarios"
    
    # @property
    # def id(self) -> str:
    #     return str(self)
    
    def to_dict(self) -> dict[str, str]:
        def serialize(value) -> str:
            if value is None:
                return ''
            raw = getattr(value, 'value', value)
            return '' if raw is None else str(raw)

        data = {
            'id': self.id,
            'tipo_conexao_mapa': self.tipo_conexao_mapa.value if self.tipo_conexao_mapa is not None else '',
            'id_cliente': str(self.id_cliente) if self.id_cliente is not None else '',
            'id_grupo': str(self.id_grupo) if self.id_grupo is not None else '',
            'login': self.login if self.login is not None else '',
            'login_simultaneo': self.login_simultaneo if self.login_simultaneo is not None else '',
            'autenticacao': self.autenticacao.value if self.autenticacao is not None else '',
            'id_integracao': str(self.id_integracao) if self.id_integracao is not None else '',
            'lte_id': str(self.lte_id) if self.lte_id is not None else '',
            'pacote_lte': self.pacote_lte if self.pacote_lte is not None else '',
            'id_contrato': str(self.id_contrato) if self.id_contrato is not None else '',
            'id_filial': str(self.id_filial) if self.id_filial is not None else '',
            'contrato_plano_venda_': self.contrato_plano_venda_ if self.contrato_plano_venda_ is not None else '',
            'agent_circuit_id': self.agent_circuit_id if self.agent_circuit_id is not None else '',
            'senha_md5': self.senha_md5.value if self.senha_md5 is not None else '',
            'senha': self.senha if self.senha is not None else '',
            'ping_traceroute': self.ping_traceroute if self.ping_traceroute is not None else '',
            'ativo': self.ativo.value if self.ativo is not None else '',
            'online': self.online.value if self.online is not None else '',
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
            'auto_preencher_ip': self.auto_preencher_ip.value if self.auto_preencher_ip is not None else '',
            'fixar_ip': self.fixar_ip.value if self.fixar_ip is not None else '',
            'relacionar_ip_ao_login': self.relacionar_ip_ao_login.value if self.relacionar_ip_ao_login is not None else '',
            'framed_pd_ipv6': self.framed_pd_ipv6 if self.framed_pd_ipv6 is not None else '',
            'framed_autopreencher_ipv6': self.framed_autopreencher_ipv6.value if self.framed_autopreencher_ipv6 is not None else '',
            'framed_fixar_ipv6': self.framed_fixar_ipv6.value if self.framed_fixar_ipv6 is not None else '',
            'framed_relacionar_ipv6_ao_login': self.framed_relacionar_ipv6_ao_login.value if self.framed_relacionar_ipv6_ao_login is not None else '',
            'pd_ipv6': self.pd_ipv6 if self.pd_ipv6 is not None else '',
            'auto_preencher_ipv6': self.auto_preencher_ipv6.value if self.auto_preencher_ipv6 is not None else '',
            'fixar_ipv6': self.fixar_ipv6.value if self.fixar_ipv6 is not None else '',
            'relacionar_ipv6_ao_login': self.relacionar_ipv6_ao_login.value if self.relacionar_ipv6_ao_login is not None else '',
            'mac': self.mac if self.mac is not None else '',
            'autenticacao_por_mac': self.autenticacao_por_mac.value if self.autenticacao_por_mac is not None else '',
            'usuario_wpa2aes': self.usuario_wpa2aes if self.usuario_wpa2aes is not None else '',
            'senha_wpa2aes': self.senha_wpa2aes if self.senha_wpa2aes is not None else '',
            'autenticacao_wpa': self.autenticacao_wpa if self.autenticacao_wpa is not None else '',
            'id_porta_transmissor': str(self.id_porta_transmissor) if self.id_porta_transmissor is not None else '',
            'auto_preencher_mac': self.auto_preencher_mac.value if self.auto_preencher_mac is not None else '',
            'relacionar_mac_ao_login': self.relacionar_mac_ao_login.value if self.relacionar_mac_ao_login is not None else '',
            'relacionar_concentrador_ao_login': self.relacionar_concentrador_ao_login.value if self.relacionar_concentrador_ao_login is not None else '',
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
            'tipo_vinculo_plano': self.tipo_vinculo_plano.value if self.tipo_vinculo_plano is not None else '',
            'cliente_tem_a_senha': self.cliente_tem_a_senha if self.cliente_tem_a_senha is not None else '',
            'autenticacao_wps': self.autenticacao_wps if self.autenticacao_wps is not None else '',
            'autenticacao_mac': self.autenticacao_mac if self.autenticacao_mac is not None else '',
            'tipo_acesso': self.tipo_acesso.value if self.tipo_acesso is not None else '',
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
            'franquia_atingida': self.franquia_atingida.value if self.franquia_atingida is not None else '',
            'onu_compartilhada': self.onu_compartilhada.value if self.onu_compartilhada is not None else '',
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
            'tipo_equipamento': self.tipo_equipamento.value if self.tipo_equipamento is not None else '',
            'metragem_interna': self.metragem_interna if self.metragem_interna is not None else '',
            'metragem_externa': self.metragem_externa if self.metragem_externa is not None else '',
            'id_reserva_rede_neutra': str(self.id_reserva_rede_neutra) if self.id_reserva_rede_neutra is not None else '',
            'endereco_padrao_cliente': self.endereco_padrao_cliente.value if self.endereco_padrao_cliente is not None else '',
            'ponta': self.ponta.value if self.ponta is not None else '',
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

    #def __repr__(self) -> str:
    #    return f"Login(id_autoincrement={self.id_autoincrement!r}, tipo_conexao_mapa={self.tipo_conexao_mapa!r}, id_cliente={self.id_cliente!r}, id_grupo={self.id_grupo!r}, login={self.login!r}, login_simultaneo={self.login_simultaneo!r})"
