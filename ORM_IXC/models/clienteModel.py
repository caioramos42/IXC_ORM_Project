from dataclasses import dataclass
from ORM_IXC.enums.client import *
from ORM_IXC.enums.utils import BoolEnum
from ORM_IXC.interfaces.IModel import IModel

@dataclass
class Client(IModel):
    id: int
    government_entity_type: GovernmentEntityTypeEnum
    fiscal_regime: FiscalRegimeEnum
    identification_document_type: IdentificationDocumentTypeEnum
    gender: GenderEnum
    company_name: str
    marital_status: MaritalStatusEnum
    serasa_active: SerasaActiveEnum
    satisfaction_level: SatisfactionLevelEnum
    address: str
    number: str
    neighborhood: str
    city: int
    housing: HousingEnum
    client_withheld_tax_tip: str

    active: BoolEnum = BoolEnum.YES
    client_type_id: int | None = None
    scm_client_type: ScmClientTypeEnum | None = ScmClientTypeEnum.COMMERCIAL
    
    country: str = 'Brasil'
    person_type: PersonTypeEnum = PersonTypeEnum.INDIVIDUAL

    social_name: str = ''
    trade_name: str = ''

    tax_id: str = ''
    state_registration: str = ''
    icms_taxpayer: IcmsTaxpayerEnum | None = IcmsTaxpayerEnum.NO
    icms_taxpayer_alert: str = ''
    issuing_body: str = ''
    nationality: str = 'Brasileiro'
    birth_city: int | None = None
    birth_state: int | None = None
    birth_date: str = ''

    profession: str = ''

    municipal_registration: str = ''
    isuf: str = ''
    subscriber_type: SubscriberTypeEnum | None = SubscriberTypeEnum.RESIDENTIAL_INDIVIDUAL
    branch_id: int | None = None
    filter_branch: BoolEnum | None = BoolEnum.YES
    idx: str = ''
    registration_date: str = ''

    convert_client_supplier: BoolEnum | None = BoolEnum.NO
    update_galaxpay_registration: str = 'N'
    
    condo_id: int | None = None
    block: str = ''
    apartment: str = ''
    zip_code: str = ''
    cif: str = ''

    complement: str = ''

    state_uf: int | None = None
    reference: str = ''
 
    locality_type: LocationTypeEnum = LocationTypeEnum.URBAN
    latitude: str = ''
    longitude: str = ''
    billing_zip_code: str = ''
    billing_address: str = ''
    billing_number: str = ''
    billing_neighborhood: str = ''
    billing_city: int | None = None
    billing_complement: str = ''
    billing_reference: str = ''
    billing_state: str = ''
    phone: str = ''
    commercial_phone: str = ''
    extension: str = ''
    mobile_operator_id: int | None = None
    mobile_phone: str = ''
    whatsapp: str = ''
    email: str = ''
    contact: str = ''
    website: str = ''
    skype: str = ''
    facebook: str = ''
    hotsite_email: str = ''
    password: None = None
    central_automatic_access: CentralAutomaticAccessEnum | None = CentralAutomaticAccessEnum.DEFAULT
    change_password_first_access: ChangePasswordFirstAccessEnum | None = ChangePasswordFirstAccessEnum.DEFAULT
    hotsite_password_md5: BoolEnum | None = BoolEnum.NO
    hotsite_access: str = '2'
    crm: BoolEnum | None = BoolEnum.NO
    segment_id: int | None = None
    candidate_type_id: int | None = None
    campaign_id: int | None = None
    competitor_id: int | None = None
    profile_id: int | None = None
    responsible_id: int | None = None
    indicated_by: int | None = None
    registered_via_feasibility: BoolEnum | None = BoolEnum.NO
    prospecting_status: ProspectingStatusEnum | None = ProspectingStatusEnum.NEW
    crm_date_new: str = ''
    crm_date_probing: str = ''
    crm_date_presenting: str = ''
    crm_date_negotiating: str = ''
    crm_date_won: str = ''
    crm_date_lost: str = ''
    crm_date_aborted: str = ''
    crm_date_no_port: str = ''
    crm_date_no_feasibility: str = ''
    pipe_org_id: str = ''
    card_photo: None = None
    participates_billing: str = 'S'
    billing_days_num: str = ''
    participates_pre_billing: BoolEnum | None = BoolEnum.YES
    billing_send_email: BoolEnum | None = BoolEnum.YES
    billing_send_sms: BoolEnum | None = BoolEnum.YES
    crm_billing_attention_msg: str = ''
    account_id: int | None = None
    payment_condition: int | None = None
    seller_id: int | None = None
    price_table: int | None = None
    auto_debit: str = ''
    debit_agency: str = ''
    debit_account: str = ''
    operation_code: str = ''
    account_holder_person_type: AccountHolderPersonTypeEnum | None = AccountHolderPersonTypeEnum.INDIVIDUAL
    account_holder_tax_id: str = ''
    last_update: str = 'CURRENT_TIMESTAMP'
    billing_rule_considers: BillingRuleConsidersEnum | None = BillingRuleConsidersEnum.DEFAULT
    billing_rule_whatsapp: BoolEnum | None = BoolEnum.YES
    billing_rule_notification: BoolEnum | None = BoolEnum.YES
    billing_rule_attention_msg: str = ''
    father_name: str = ''
    father_tax_id: str = ''
    father_identity: str = ''
    father_birth: str = ''
    mother_name: str = ''
    mother_tax_id: str = ''
    mother_identity: str = ''
    mother_birth: str = ''
    dependents_quantity: str = ''
    spouse_name: str = ''
    spouse_phone: str = ''
    spouse_tax_id: str = ''
    spouse_identity: str = ''
    spouse_birth_date: str = ''
    accountant_name: str = ''
    accountant_phone: str = ''
    public_body: BoolEnum | None = BoolEnum.NO
    im: str = ''
    representative_1_name: str = ''
    representative_1_tax_id: str = ''
    representative_1_identity: str = ''
    representative_2_name: str = ''
    representative_2_tax_id: str = ''
    representative_2_identity: str = ''
    emp_company: str = ''
    emp_tax_id: str = ''
    emp_zip_code: str = ''
    emp_address: str = ''
    emp_city: str = ''
    emp_phone: str = ''
    emp_position: str = ''
    emp_salary: str = ''
    emp_admission_date: str = ''
    iss_default_classification: IssDefaultClassificationEnum = IssDefaultClassificationEnum.DEFAULT
    pis_withheld: str = 'S'
    cofins_withheld: str = 'S'
    csll_withheld: str = 'S'
    irrf_withheld: str = 'S'
    irrf_discount_lower_value: BoolEnum | None = BoolEnum.NO
    inss_withheld: str = 'S'
    client_deducts_total_iss_withheld: str = 'S'
    reduction_percentage: str = '0.00'
    ref_com_company1: str = ''
    ref_com_phone1: str = ''
    ref_com_company2: str = ''
    ref_com_phone2: str = ''
    ref_per_name1: str = ''
    ref_per_phone1: str = ''
    ref_per_name2: str = ''
    ref_per_phone2: str = ''
    obs: str = ''
    alert: str = ''

    def __post_init__(self):
        # Convert enums and optional IDs to strings/values
        self.client_type_id = str(self.client_type_id) if self.client_type_id is not None else ''
        self.scm_client_type = self.scm_client_type.value if self.scm_client_type is not None else ''
        self.government_entity_type = self.government_entity_type.value if self.government_entity_type is not None else ''
        self.fiscal_regime = self.fiscal_regime.value if self.fiscal_regime is not None else ''
        self.identification_document_type = self.identification_document_type.value if self.identification_document_type is not None else ''
        self.icms_taxpayer = self.icms_taxpayer.value if self.icms_taxpayer is not None else ''
        self.birth_city = str(self.birth_city) if self.birth_city is not None else ''
        self.birth_state = str(self.birth_state) if self.birth_state is not None else ''
        self.gender = self.gender.value if self.gender is not None else ''
        self.marital_status = self.marital_status.value if self.marital_status is not None else ''
        self.subscriber_type = self.subscriber_type.value if self.subscriber_type is not None else ''
        self.branch_id = str(self.branch_id) if self.branch_id is not None else ''
        self.filter_branch = self.filter_branch.value if self.filter_branch is not None else ''
        self.serasa_active = self.serasa_active.value if self.serasa_active is not None else ''
        self.convert_client_supplier = self.convert_client_supplier.value if self.convert_client_supplier is not None else ''
        self.satisfaction_level = self.satisfaction_level.value if self.satisfaction_level is not None else ''
        self.condo_id = str(self.condo_id) if self.condo_id is not None else ''
        self.state_uf = str(self.state_uf) if self.state_uf is not None else ''
        self.housing = self.housing.value if self.housing is not None else ''
        self.billing_city = str(self.billing_city) if self.billing_city is not None else ''
        self.mobile_operator_id = str(self.mobile_operator_id) if self.mobile_operator_id is not None else ''
        self.central_automatic_access = self.central_automatic_access.value if self.central_automatic_access is not None else ''
        self.change_password_first_access = self.change_password_first_access.value if self.change_password_first_access is not None else ''
        self.hotsite_password_md5 = self.hotsite_password_md5.value if self.hotsite_password_md5 is not None else ''
        self.crm = self.crm.value if self.crm is not None else ''
        self.segment_id = str(self.segment_id) if self.segment_id is not None else ''
        self.candidate_type_id = str(self.candidate_type_id) if self.candidate_type_id is not None else ''
        self.campaign_id = str(self.campaign_id) if self.campaign_id is not None else ''
        self.competitor_id = str(self.competitor_id) if self.competitor_id is not None else ''
        self.profile_id = str(self.profile_id) if self.profile_id is not None else ''
        self.responsible_id = str(self.responsible_id) if self.responsible_id is not None else ''
        self.indicated_by = str(self.indicated_by) if self.indicated_by is not None else ''
        self.registered_via_feasibility = self.registered_via_feasibility.value if self.registered_via_feasibility is not None else ''
        self.prospecting_status = self.prospecting_status.value if self.prospecting_status is not None else ''
        self.participates_pre_billing = self.participates_pre_billing.value if self.participates_pre_billing is not None else ''
        self.billing_send_email = self.billing_send_email.value if self.billing_send_email is not None else ''
        self.billing_send_sms = self.billing_send_sms.value if self.billing_send_sms is not None else ''
        self.account_id = str(self.account_id) if self.account_id is not None else ''
        self.payment_condition = str(self.payment_condition) if self.payment_condition is not None else ''
        self.seller_id = str(self.seller_id) if self.seller_id is not None else ''
        self.price_table = str(self.price_table) if self.price_table is not None else ''
        self.account_holder_person_type = self.account_holder_person_type.value if self.account_holder_person_type is not None else ''
        self.billing_rule_considers = self.billing_rule_considers.value if self.billing_rule_considers is not None else ''
        self.billing_rule_whatsapp = self.billing_rule_whatsapp.value if self.billing_rule_whatsapp is not None else ''
        self.billing_rule_notification = self.billing_rule_notification.value if self.billing_rule_notification is not None else ''
        self.public_body = self.public_body.value if self.public_body is not None else ''
        self.irrf_discount_lower_value = self.irrf_discount_lower_value.value if self.irrf_discount_lower_value is not None else ''

    def to_dict(self):
        return {
            'id_tipo_cliente': self.client_type_id,
            'tipo_cliente_scm': self.scm_client_type,
            'tipo_ente_governamental': self.government_entity_type,
            'regime_fiscal_col': self.fiscal_regime,
            'tipo_documento_identificacao': self.identification_document_type,
            'contribuinte_icms': self.icms_taxpayer,
            'cidade_naturalidade': self.birth_city,
            'estado_nascimento': self.birth_state,
            'Sexo': self.gender,
            'estado_civil': self.marital_status,
            'tipo_assinante': self.subscriber_type,
            'filial_id': self.branch_id,
            'filtra_filial': self.filter_branch,
            'ativo_serasa': self.serasa_active,
            'convert_cliente_forn': self.convert_client_supplier,
            'grau_satisfacao': self.satisfaction_level,
            'id_condominio': self.condo_id,
            'uf': self.state_uf,
            'moradia': self.housing,
            'cidade_cob': self.billing_city,
            'id_operadora_celular': self.mobile_operator_id,
            'acesso_automatico_central': self.central_automatic_access,
            'alterar_senha_primeiro_acesso': self.change_password_first_access,
            'senha_hotsite_md5': self.hotsite_password_md5,
            'crm': self.crm,
            'id_segmento': self.segment_id,
            'id_candato_tipo': self.candidate_type_id,
            'id_campanha': self.campaign_id,
            'id_concorrente': self.competitor_id,
            'id_perfil': self.profile_id,
            'responsavel': self.responsible_id,
            'indicado_por': self.indicated_by,
            'cadastrado_via_viabilidade': self.registered_via_feasibility,
            'status_prospeccao': self.prospecting_status,
            'participa_pre_cobranca': self.participates_pre_billing,
            'cob_envia_email': self.billing_send_email,
            'cob_envia_sms': self.billing_send_sms,
            'id_conta': self.account_id,
            'cond_pagamento': self.payment_condition,
            'id_vendedor': self.seller_id,
            'tabela_preco': self.price_table,
            'tipo_pessoa_titular_conta': self.account_holder_person_type,
            'regua_cobranca_considera': self.billing_rule_considers,
            'regua_cobranca_wpp': self.billing_rule_whatsapp,
            'regua_cobranca_notificacao': self.billing_rule_notification,
            'orgao_publico': self.public_body,
            'desconto_irrf_valor_inferior': self.irrf_discount_lower_value,
        }