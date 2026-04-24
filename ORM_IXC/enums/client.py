from enum import Enum
class ScmClientTypeEnum(Enum):
    COMMERCIAL = '01'
    INDUSTRIAL = '02'
    RESIDENTIAL_INDIVIDUAL = '03'
    RURAL_PRODUCER = '04'
    PUBLIC_ADMINISTRATION = '05'
    TELECOM_PROVIDER = '06'
    DIPLOMATIC_MISSIONS = '07'
    CHURCHES_TEMPLES = '08'
    OTHERS_NOT_SPECIFIED = '99'
    LARGE_TAXPAYER = '0-13'
    AUTO_RETAINER = '0-15'
    VAT_RETENTION_AGENT = '0-23'
    SIMPLE_TAX_REGIME = '0-47'
    OTHERS = 'R-99-PN'

class GovernmentEntityTypeEnum(Enum):
    FEDERAL = '1'
    STATE = '2'
    FEDERAL_DISTRICT = '3'
    MUNICIPALITY = '4'

class PersonTypeEnum(Enum):
    INDIVIDUAL = 'F'
    LEGAL_ENTITY = 'J'
    FOREIGNER = 'E'
    LEGAL_ENTITY_ALT = '1'
    NATURAL = '2'
    FOREIGNER_ALT = '3'

class FiscalRegimeEnum(Enum):
    VAT_RESPONSIBLE = '48'
    NOT_VAT_RESPONSIBLE = '49'

class IdentificationDocumentTypeEnum(Enum):
    CIVIL_REGISTRY = '11'
    IDENTITY_CARD = '12'
    CITIZENSHIP_CARD = '13'
    FOREIGNER_ID_CARD = '21'
    FOREIGNER_IDENTITY_CARD = '22'
    NIT = '31'
    PASSPORT = '41'
    FOREIGN_ID_DOCUMENT = '42'
    PEP = '47'
    OTHER_COUNTRY_NIT = '50'
    NUIP = '91'
    NUIT = 'NUIT'
    RUC = 'RUC'
    CI = 'CI'
    RESIDENCE_CARD = '4'
    INNOMINATE = '5'
    DIPLOMATIC_TAX_EXEMPTION_CARD = '6'
    OTHER = '9'
    CUIT = 'CUIT'
    CARNET = 'CIBOL'
    RUT = 'RUT'
    TIN = 'TIN'
    RIF = 'RIF'
    DNI = 'DNI'
    NIR = 'NIR'
    SIREN = 'SIREN'
    RUT_URU = 'RUTURU'

class IcmsTaxpayerEnum(Enum):
    YES = 'S'
    NO = 'N'
    EXEMPT = 'I'
    EXCLUDED = 'E'

class GenderEnum(Enum):
    FEMALE = 'F'
    MALE = 'M'
    NON_BINARY = 'NB'
    OTHER = 'O'
    PREFER_NOT_TO_SAY = 'PNI'

class MaritalStatusEnum(Enum):
    MARRIED = 'Casado'
    SINGLE = 'Solteiro'
    DIVORCED = 'Divorciado'
    WIDOWED = 'Viúvo'

class SubscriberTypeEnum(Enum):
    COMMERCIAL_INDUSTRIAL = '1'
    PUBLIC_POWER = '2'
    RESIDENTIAL_INDIVIDUAL = '3'
    PUBLIC = '4'
    SEMI_PUBLIC = '5'
    OTHERS = '6'

class SerasaActiveEnum(Enum):
    YES = '1'
    NO = '2'


class SatisfactionLevelEnum(Enum):
    NOT_SATISFIED = '1'
    SLIGHTLY_SATISFIED = '2'
    SATISFIED = '3'
    VERY_SATISFIED = '4'
    COMPLETELY_SATISFIED = '5'

class HousingEnum(Enum):
    OWNED = 'P'
    RENTED = 'A'

class LocationTypeEnum(Enum):
    RURAL = 'R'
    URBAN = 'U'

class CentralAutomaticAccessEnum(Enum):
    YES = 'S'
    NO = 'N'
    DEFAULT = 'P'

class ChangePasswordFirstAccessEnum(Enum):
    YES = 'S'
    NO = 'N'
    DEFAULT = 'P'

class ProspectingStatusEnum(Enum):
    NEW = 'C'
    PROBING = 'S'
    PRESENTING = 'A'
    NEGOTIATING = 'N'
    WON = 'V'
    LOST = 'P'
    ABORTED = 'AB'
    NO_FEASIBILITY = 'SV'
    NO_PORT_AVAILABLE = 'SP'

class AccountHolderPersonTypeEnum(Enum):
    INDIVIDUAL = 'F'
    LEGAL_ENTITY = 'J'

class BillingRuleConsidersEnum(Enum):
    YES = 'S'
    NO = 'N'
    DEFAULT = 'P'

class IssDefaultClassificationEnum(Enum):
    NORMAL = '00'
    RETAINED = '01'
    SUBSTITUTE = '02'
    EXEMPT = '03'
    DEFAULT = '99'