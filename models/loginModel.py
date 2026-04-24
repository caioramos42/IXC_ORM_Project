# from dataclasses import dataclass
# from enums.login import *
# from datetime import time, datetime
# from enums.utils import BoolEnum
# from interfaces.IModel import IModel

# @dataclass
# class LoginModel(IModel):
#     #id: int | None = None # -1 garante que o campo não será utilizado na hora de atualizar/criar o login
#     client_id: int#
#     group_id: int#
#     login: str#
#     password: str#
#     sales_plan_contract: str | None#
#     md5_password: BoolEnum = BoolEnum.YES#
#     authentication = Authentication.PPPOE#
#     map_connection_type = MapConextionsTypes.FIBER#
#     active: BoolEnum = BoolEnum.YES#
#     simultaneous_login: str = '1'#
#     auto_compleate_ip: IPConfigurations = IPConfigurations.DEFAUTCONFIGURATION#
#     set_fixed_ip: IPConfigurations = IPConfigurations.DEFAUTCONFIGURATION#
#     link_ip_to_login: IPConfigurations = IPConfigurations.DEFAUTCONFIGURATION#
#     mac_authentication: MacAltentication = MacAltentication.DEFAULT#
#     plan_binding_type: BondPlan = BondPlan.DEFAULT#
#     client_has_password: BoolEnum = BoolEnum.NO#
#     wps_authentication: BoolEnum = BoolEnum.NO#
#     mac_authentication_enabled: BoolEnum = BoolEnum.NO#
#     access_type: AcessTipe = AcessTipe.HTTP#
#     default_client_address: BoolEnum = BoolEnum.YES#

#     integration_id: int | None = None#
#     lte_id: int | None = None#
#     contract_id: int | None = None#
#     branch_id: int | None = None#
    
#     agent_circuit_id: str | None = None#
#     ping_traceroute: str | None = ''#
#     online: Online | None = Online.WITHOUTSTATUS#
#     last_update: str | None = 'CURRENT_TIMESTAMP'#
#     router1_user: str | None = ''#
#     router1_password: str | None = ''#
#     router2_password: str | None = ''#
#     ssid_router_wifi: str | None = ''#
#     wireless_network_password: str | None = ''#
#     ssid_router_wifi_5ghz: str | None = ''#
#     wireless_network_password_5ghz: str | None = ''#
#     redirect_interfaces: str | None = ''#
#     ip: str | None = ''#
#     ip_aviso: str | None = ''#
#     framed_pd_ipv6: str | None = ''#
#     pd_ipv6: str | None = ''#
#     mac: str | None = ''#
#     wpa2aes_user: str | None = ''#
#     wpa2aes_password: str | None = ''#
#     wpa_authentication: str | None = ''#

#     transmitter_port_id: int | None = None#
#     radius_pool_id: int | None = None#
#     radgrupos_pools_id: int | None = None#
#     rad_dns_id: int | None = None#
#     concentrator_id: int | None = None#
#     interface_id: int | None = None#

#     http_port: int | None = None#
#     router2_port: int | None = None#
#     port_aux: int | None = None#

#     df_project_id: int | None = None#
#     transmitter_id: int | None = None#
#     transmission_interface_id: int | None = None#
#     fiber_transmission_interface_id: int | None = None#
#     ftth_box_id: int | None = None#
#     ftth_port: int | None = None#
#     hardware_id: int | None = None#
#     internal_cable_length: int | None = None#
#     external_cable_length: int | None = None#
#     neutral_network_reservation_id: int | None = None#
#     condominium_id: int | None = None#
#     building_id: int | None = None#
#     new_condominium_id: int | None = None#
#     address_number: int | None = None#
#     new_number: int | None = None#
#     city_id: int | None#
#     new_city_id: int | None#

#     vlan: str | None = ''#
#     vlan_network_ip: str | None = ''#
#     vlan_gateway: str | None = ''#
#     service_tag_vlan: str | None = 'S'#
#     mtu: int | None = 1500#
#     concentrator: str | None = ''#
#     connection: str | None = ''#
#     connection_type: str | None = ''#
#     nas_http_port: str | None = ''#
#     acct_session_id: str | None = ''#
#     ip_concentrator: str = ''#

#     last_connection_start: time | None = ''#
#     last_connection_end: time | None = datetime.now()#
#     disconnection_reason: str | None = ''#
#     disconnection_count: str | None = ''#
#     connection_time: str | None = ''#
#     connected_time: str | None = ''#
#     current_download: str | None = ''#
#     current_upload: str | None = ''#
#     max_quota: str | None = ''#
#     quota_usage: str | None = ''#
#     upload_quota_usage: str | None = ''#

#     shared_onu: BoolEnum | None = BoolEnum.NO#
#     quota_reached: BoolEnum | None = BoolEnum.NO#

#     transmitter_model: str | None = ''#
#     trunk: str | None = ''#
#     splitter: str | None = ''#
#     onu_mac: str | None = ''#
#     last_signal_strength: str | None = ''#
#     equipment_type: EquipmentType | None = ''#

#     endpoint: Tip | None = ''#
#     block: str | None = ''#
#     new_block: str | None = ''#
#     apartment: str | None = ''#
#     new_apartment: str | None = ''#
#     zip_code: str | None = ''#
#     new_zip_code: str | None = ''#
#     address: str | None = ''#
#     new_address: str | None = ''#
#     neighborhood: str | None = ''#
#     new_neighborhood: str | None = ''#
#     adreess_reference: str | None = ''#
#     new_adreess_reference: str | None = ''#
#     complement: str | None = ''#
#     new_complement: str | None = ''#
#     latitude: float | None = ''#
#     new_latitude: float | None = ''#
#     longitude: float | None = ''#
#     new_longitude: float | None = ''#
#     notes: str | None = ''#
    

# def __post_init__(self):
#     self.id = str(self.id)

#     self.integration_id = str(self.integration_id) if self.integration_id is not None else ''
#     self.lte_id = str(self.lte_id) if self.lte_id is not None else ''
#     self.contract_id = str(self.contract_id) if self.contract_id is not None else ''
#     self.branch_id = str(self.branch_id) if self.branch_id is not None else ''
#     self.transmitter_port_id = str(self.transmitter_port_id) if self.transmitter_port_id is not None else ''
#     self.radius_pool_id = str(self.radius_pool_id) if self.radius_pool_id is not None else ''
#     self.radgrupos_pools_id = str(self.radgrupos_pools_id) if self.radgrupos_pools_id is not None else ''
#     self.rad_dns_id = str(self.rad_dns_id) if self.rad_dns_id is not None else ''
#     self.concentrator_id = str(self.concentrator_id) if self.concentrator_id is not None else ''
#     self.interface_id = str(self.interface_id) if self.interface_id is not None else ''
#     self.router2_port = str(self.router2_port) if self.router2_port is not None else ''

#     self.df_project_id = str(self.df_project_id) if self.df_project_id is not None else ''
#     self.transmitter_id = str(self.transmitter_id) if self.transmitter_id is not None else ''
#     self.transmission_interface_id = str(self.transmission_interface_id) if self.transmission_interface_id is not None else ''
#     self.fiber_transmission_interface_id = str(self.fiber_transmission_interface_id) if self.fiber_transmission_interface_id is not None else ''
#     self.ftth_box_id = str(self.ftth_box_id) if self.ftth_box_id is not None else ''
#     self.ftth_port = str(self.ftth_port) if self.ftth_port is not None else ''
#     self.hardware_id = str(self.hardware_id) if self.hardware_id is not None else ''
#     self.internal_cable_length = str(self.internal_cable_length) if self.internal_cable_length is not None else ''
#     self.external_cable_length = str(self.external_cable_length) if self.external_cable_length is not None else ''
#     self.neutral_network_reservation_id = str(self.neutral_network_reservation_id) if self.neutral_network_reservation_id is not None else ''

#     self.condominium_id = str(self.condominium_id) if self.condominium_id is not None else ''
#     self.building_id = str(self.building_id) if self.building_id is not None else ''
#     self.new_condominium_id = str(self.new_condominium_id) if self.new_condominium_id is not None else ''
#     self.address_number = str(self.address_number) if self.address_number is not None else ''
#     self.new_number = str(self.new_number) if self.new_number is not None else ''
#     self.city_id = str(self.city_id) if self.city_id is not None else ''
#     self.new_city_id = str(self.new_city_id) if self.new_city_id is not None else ''
#     self.mtu = str(self.mtu) if self.mtu is not None else ''
    
#     self.latitude = str(self.latitude) if self.latitude is not None else ''#
#     self.new_latitude = str(self.new_latitude) if self.new_latitude is not None else ''#
#     self.longitude = str(self.longitude) if self.longitude is not None else ''#
#     self.new_longitude = str(self.new_longitude) if self.new_longitude is not None else ''#
    
#     self.last_connection_start = str(self.last_connection_start.strptime("%Y-%m-%d")) if self.last_connection_start is not None else ''#
#     self.last_connection_end = str(self.last_connection_end.strptime("%Y-%m-%d")) if self.last_connection_end is not None else ''#
    
# def to_dict(self):
#     return {
#         'autenticacao': self.authentication,
#         'tipo_conexao_mapa': self.map_connection_type,
#         'id_integracao': self.integration_id,
#         'lte_id': self.lte_id,
#         'pacote_lte': self.package_lte,
#         'id_cliente': self.client_id,
#         'id_contrato': self.contract_id,
#         'id_filial': self.branch_id,
#         'contrato_plano_venda_': self.sales_plan_contract,
#         'id_grupo': self.group_id,
#         'login': self.login,
#         'agent_circuit_id': self.agent_circuit_id,
#         'senha_md5': self.md5_password,
#         'senha': self.password,
#         'ping_traceroute': self.ping_traceroute,
#         'ativo': self.active,
#         'online': self.online,
#         'login_simultaneo': self.simultaneous_login,
#         'ultima_atualizacao': self.last_update,
#         'usuario_router1': self.router1_user,
#         'senha_router1': self.router1_password,
#         'senha_router2': self.router2_password,
#         'ssid_router_wifi': self.ssid_router_wifi,
#         'senha_rede_sem_fio': self.wireless_network_password,
#         'ssid_router_wifi_5ghz': self.ssid_router_wifi_5ghz,
#         'senha_rede_sem_fio_5ghz': self.wireless_network_password_5ghz,
#         'redirect_interfaces': self.redirect_interfaces,
#         'ip': self.ip,
#         'ip_aviso': self.ip_aviso,
#         'auto_preencher_ip': self.auto_compleate_ip,
#         'fixar_ip': self.set_fixed_ip,
#         'relacionar_ip_ao_login': self.link_ip_to_login,
#         'framed_pd_ipv6': self.framed_pd_ipv6,
#         'framed_autopreencher_ipv6': self.auto_fill_framed_ipv6,
#         'framed_fixar_ipv6': self.set_fixed_framed_ipv6,
#         'framed_relacionar_ipv6_ao_login': self.link_framed_ipv6_to_login,
#         'pd_ipv6': self.pd_ipv6,
#         'auto_preencher_ipv6': self.auto_fill_ipv6,
#         'fixar_ipv6': self.set_fixed_ipv6,
#         'relacionar_ipv6_ao_login': self.link_ipv6_to_login,
#         'mac': self.mac,
#         'autenticacao_por_mac': self.mac_authentication,
#         'usuario_wpa2aes': self.wpa2aes_user,
#         'senha_wpa2aes': self.wpa2aes_password,
#         'autenticacao_wpa': self.wpa_authentication,
#         'id_porta_transmissor': self.transmitter_port_id,
#         'auto_preencher_mac': self.auto_fill_mac,
#         'relacionar_mac_ao_login': self.link_mac_to_login,
#         'relacionar_concentrador_ao_login': self.link_concentrator_to_login,
#         'pool_radius': self.radius_pool_id,
#         'id_radgrupos_pools': self.radgrupos_pools_id,
#         'id_rad_dns': self.rad_dns_id,
#         'id_concentrador': self.concentrator_id,
#         'ip_concentrador': self.ip_concentrator,
#         'interface': self.interface_id,
#         'vlan': self.vlan,
#         'vlan_ip_rede': self.vlan_network_ip,
#         'gw_vlan': self.vlan_gateway,
#         'service_tag_vlan': self.service_tag_vlan,
#         'mtu': self.mtu,
#         'concentrador': self.concentrator,
#         'conexao': self.connection,
#         'tipo_conexao': self.connection_type,
#         'porta_http_nas': self.nas_http_port,
#         'acct_session_id': self.acct_session_id,
#         'tipo_vinculo_plano': self.plan_binding_type,
#         'cliente_tem_a_senha': self.client_has_password,
#         'autenticacao_wps': self.wps_authentication,
#         'autenticacao_mac': self.mac_authentication_enabled,
#         'tipo_acesso': self.access_type,
#         'porta_http': self.http_port,
#         'porta_router2': self.router2_port,
#         'ip_aux': self.ip_aux,
#         'porta_aux': self.port_aux,
#         'ultima_conexao_inicial': self.last_connection_start,
#         'ultima_conexao_final': self.last_connection_end,
#         'motivo_desconexao': self.disconnection_reason,
#         'count_desconexao': self.disconnection_count,
#         'tempo_conexao': self.connection_time,
#         'tempo_conectado': self.connected_time,
#         'download_atual': self.current_download,
#         'upload_atual': self.current_upload,
#         'franquia_maximo': self.max_quota,
#         'franquia_consumo': self.quota_usage,
#         'franquia_consumo_up': self.upload_quota_usage,
#         'franquia_atingida': self.quota_reached,
#         'onu_compartilhada': self.shared_onu,
#         'id_df_projeto': self.df_project_id,
#         'id_transmissor': self.transmitter_id,
#         'modelo_tranmissor': self.transmitter_model,
#         'interface_transmissao': self.transmission_interface_id,
#         'interface_transmissao_fibra': self.fiber_transmission_interface_id,
#         'id_caixa_ftth': self.ftth_box_id,
#         'ftth_porta': self.ftth_port,
#         'tronco': self.trunk,
#         'splitter': self.splitter,
#         'onu_mac': self.onu_mac,
#         'sinal_ultimo_atendimento': self.last_signal_strength,
#         'id_hardware': self.hardware_id,
#         'tipo_equipamento': self.equipment_type,
#         'metragem_interna': self.internal_cable_length,
#         'metragem_externa': self.external_cable_length,
#         'id_reserva_rede_neutra': self.neutral_network_reservation_id,
#         'endereco_padrao_cliente': self.default_client_address,
#         'ponta': self.endpoint,
#         'id_condominio': self.condominium_id,
#         'id_predio': self.building_id,
#         'condominio_novo': self.new_condominium_id,
#         'bloco': self.block,
#         'bloco_novo': self.new_block,
#         'apartamento': self.apartment,
#         'apartamento_novo': self.new_apartment,
#         'cep': self.zip_code,
#         'cep_novo': self.new_zip_code,
#         'endereco': self.address,
#         'endereco_novo': self.new_address,
#         'numero': self.address_number,
#         'numero_novo': self.new_number,
#         'bairro': self.neighborhood,
#         'bairro_novo': self.new_neighborhood,
#         'cidade': self.city_id,
#         'cidade_novo': self.new_city_id,
#         'referencia': self.adreess_reference,
#         'referencia_novo': self.new_adreess_reference,
#         'complemento': self.complement,
#         'complemento_novo': self.new_complement,
#         'latitude': self.latitude,
#         'latitude_novo': self.new_latitude,
#         'longitude': self.longitude,
#         'longitude_novo': self.new_longitude,
#         'obs': self.notes,
#     }
    
# def to_class(self, json:dict):
#     {
#         'autenticacao': self.authentication,
#         'tipo_conexao_mapa': self.map_connection_type,
#         'id_integracao': self.integration_id,
#         'lte_id': self.lte_id,
#         'pacote_lte': self.package_lte,
#         'id_cliente': self.client_id,
#         'id_contrato': self.contract_id,
#         'id_filial': self.branch_id ,
#         'contrato_plano_venda_': self.sales_plan_contract,
#         'id_grupo': self.group_id,
#         'login': self.login,
#         'agent_circuit_id': self.agent_circuit_id,
#         'senha_md5': self.md5_password,
#         'senha': self.password,
#         'ping_traceroute': self.ping_traceroute,
#         'ativo': self.active,
#         'online': self.online,
#         'login_simultaneo': self.simultaneous_login,
#         'ultima_atualizacao': self.last_update,
#         'usuario_router1': self.router1_user,
#         'senha_router1': self.router1_password,
#         'senha_router2': self.router2_password,
#         'ssid_router_wifi': self.ssid_router_wifi,
#         'senha_rede_sem_fio': self.wireless_network_password,
#         'ssid_router_wifi_5ghz': self.ssid_router_wifi_5ghz,
#         'senha_rede_sem_fio_5ghz': self.wireless_network_password_5ghz,
#         'redirect_interfaces': self.redirect_interfaces,
#         'ip': self.ip,
#         'ip_aviso': self.ip_aviso,
#         'auto_preencher_ip': self.auto_compleate_ip,
#         'fixar_ip': self.set_fixed_ip,
#         'relacionar_ip_ao_login': self.link_ip_to_login,
#         'framed_pd_ipv6': self.framed_pd_ipv6,
#         'framed_autopreencher_ipv6': self.auto_fill_framed_ipv6,
#         'framed_fixar_ipv6': self.set_fixed_framed_ipv6,
#         'framed_relacionar_ipv6_ao_login': self.link_framed_ipv6_to_login,
#         'pd_ipv6': self.pd_ipv6,
#         'auto_preencher_ipv6': self.auto_fill_ipv6,
#         'fixar_ipv6': self.set_fixed_ipv6,
#         'relacionar_ipv6_ao_login': self.link_ipv6_to_login,
#         'mac': self.mac,
#         'autenticacao_por_mac': self.mac_authentication,
#         'usuario_wpa2aes': self.wpa2aes_user,
#         'senha_wpa2aes': self.wpa2aes_password,
#         'autenticacao_wpa': self.wpa_authentication,
#         'id_porta_transmissor': self.transmitter_port_id,
#         'auto_preencher_mac': self.auto_fill_mac,
#         'relacionar_mac_ao_login': self.link_mac_to_login,
#         'relacionar_concentrador_ao_login': self.link_concentrator_to_login,
#         'pool_radius': self.radius_pool_id,
#         'id_radgrupos_pools': self.radgrupos_pools_id,
#         'id_rad_dns': self.rad_dns_id,
#         'id_concentrador': self.concentrator_id,
#         'ip_concentrador': self.ip_concentrator,
#         'interface': self.interface_id,
#         'vlan': self.vlan,
#         'vlan_ip_rede': self.vlan_network_ip,
#         'gw_vlan': self.vlan_gateway,
#         'service_tag_vlan': self.service_tag_vlan,
#         'mtu': self.mtu,
#         'concentrador': self.concentrator,
#         'conexao': self.connection,
#         'tipo_conexao': self.connection_type,
#         'porta_http_nas': self.nas_http_port,
#         'acct_session_id': self.acct_session_id,
#         'tipo_vinculo_plano': self.plan_binding_type,
#         'cliente_tem_a_senha': self.client_has_password,
#         'autenticacao_wps': self.wps_authentication,
#         'autenticacao_mac': self.mac_authentication_enabled,
#         'tipo_acesso': self.access_type,
#         'porta_http': self.http_port,
#         'porta_router2': self.router2_port,
#         'ip_aux': self.ip_aux,
#         'porta_aux': self.port_aux,
#         'ultima_conexao_inicial': self.last_connection_start,
#         'ultima_conexao_final': self.last_connection_end,
#         'motivo_desconexao': self.disconnection_reason,
#         'count_desconexao': self.disconnection_count,
#         'tempo_conexao': self.connection_time,
#         'tempo_conectado': self.connected_time,
#         'download_atual': self.current_download,
#         'upload_atual': self.current_upload,
#         'franquia_maximo': self.max_quota,
#         'franquia_consumo': self.quota_usage,
#         'franquia_consumo_up': self.upload_quota_usage,
#         'franquia_atingida': self.quota_reached,
#         'onu_compartilhada': self.shared_onu,
#         'id_df_projeto': self.df_project_id,
#         'id_transmissor': self.transmitter_id,
#         'modelo_tranmissor': self.transmitter_model,
#         'interface_transmissao': self.transmission_interface_id,
#         'interface_transmissao_fibra': self.fiber_transmission_interface_id,
#         'id_caixa_ftth': self.ftth_box_id,
#         'ftth_porta': self.ftth_port,
#         'tronco': self.trunk,
#         'splitter': self.splitter,
#         'onu_mac': self.onu_mac,
#         'sinal_ultimo_atendimento': self.last_signal_strength,
#         'id_hardware': self.hardware_id,
#         'tipo_equipamento': self.equipment_type,
#         'metragem_interna': self.internal_cable_length,
#         'metragem_externa': self.external_cable_length,
#         'id_reserva_rede_neutra': self.neutral_network_reservation_id,
#         'endereco_padrao_cliente': self.default_client_address,
#         'ponta': self.endpoint,
#         'id_condominio': self.condominium_id,
#         'id_predio': self.building_id,
#         'condominio_novo': self.new_condominium_id,
#         'bloco': self.block,
#         'bloco_novo': self.new_block,
#         'apartamento': self.apartment,
#         'apartamento_novo': self.new_apartment,
#         'cep': self.zip_code,
#         'cep_novo': self.new_zip_code,
#         'endereco': self.address,
#         'endereco_novo': self.new_address,
#         'numero': self.address_number,
#         'numero_novo': self.new_number,
#         'bairro': self.neighborhood,
#         'bairro_novo': self.new_neighborhood,
#         'cidade': self.city_id,
#         'cidade_novo': self.new_city_id,
#         'referencia': self.adreess_reference,
#         'referencia_novo': self.new_adreess_reference,
#         'complemento': self.complement,
#         'complemento_novo': self.new_complement,
#         'latitude': self.latitude,
#         'latitude_novo': self.new_latitude,
#         'longitude': self.longitude,
#         'longitude_novo': self.new_longitude,
#         'obs': self.notes,
#     }
