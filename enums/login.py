from enum import Enum

class Authentication(Enum):
    PPPOE = 'L'
    HOTSPOT = 'H'
    IPXMAC = 'M'
    VLAN = 'V'
    IPOE = 'D'
    INTEGRATION = 'I'
    EXTERNAL = 'E'
    
class MapConextionsTypes(Enum):
    M58 = '58'
    M24 = '24'
    FIBER = 'F'
    CABO = 'L'
    ADSL = 'A'
    LTE = 'LTE'
    DEDICATELINK = 'LDD'

class Online(Enum):
    NOT = 'N'
    YES = 'S'
    WITHOUTSTATUS = 'SS'

class IPConfigurations(Enum):
    DEFAUTCONFIGURATION = 'H'
    EVER = 'S'
    NEVER = 'N'
    
class MacAltentication(Enum):
    NO = 'N'
    YES = 'S'
    DEFAULT = 'P'
    MICROTIK = 'MK'
    UBNT = 'UN'
    WPA2AES = 'WP'
    
class BondPlan(Enum):
    DEFAULT = 'D'
    CONTRACT = 'C'
    PREPAID = 'P'
    FREE = 'G'

class AcessTipe(Enum):
    HTTP = 'http'
    HTTPS = 'https'
    
class Tip(Enum):
    A = 'A'
    B = 'B'
    C = 'C'
    
class EquipmentType(Enum):
    LENDING = 'C'
    OWN = 'P'
