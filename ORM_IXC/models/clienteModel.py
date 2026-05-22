from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional
from ORM_IXC.enums.client import *
from ORM_IXC.interfaces.IModel import IModel, IModelWithId

@dataclass(kw_only=True)
class ClientModel(IModelWithId):
    id_autoincrement: int
    razao: str
    endereco: str
    numero: str
    bairro: str
    cidade: int
    dica_imposto_retido_cliente: str
    ativo: AtivoEnum = AtivoEnum.SIM
    id_tipo_cliente: Optional[int] = None
    tipo_cliente_scm: Optional[Tipo_cliente_scmEnum] = Tipo_cliente_scmEnum.COMERCIAL
    tipo_ente_governamental: Optional[Tipo_ente_governamentalEnum] = None
    pais: Optional[str] = ''
    tipo_pessoa: Tipo_pessoaEnum = Tipo_pessoaEnum.FISICA
    regime_fiscal_col: Optional[Regime_fiscal_colEnum] = None
    nome_social: Optional[str] = ''
    fantasia: Optional[str] = ''
    tipo_documento_identificacao: Optional[Tipo_documento_identificacaoEnum] = None
    cnpj_cpf: Optional[str] = ''
    ie_identidade: Optional[str] = ''
    contribuinte_icms: Optional[Contribuinte_icmsEnum] = Contribuinte_icmsEnum.NAO
    contribuinte_icms_alert: Optional[str] = ''
    rg_orgao_emissor: Optional[str] = ''
    nacionalidade: Optional[str] = ''
    cidade_naturalidade: Optional[int] = None
    estado_nascimento: Optional[int] = None
    data_nascimento: Optional[str] = ''
    Sexo: Optional[SexoEnum] = None
    profissao: Optional[str] = ''
    estado_civil: Optional[Estado_civilEnum] = None
    inscricao_municipal: Optional[str] = ''
    isuf: Optional[str] = ''
    tipo_assinante: Optional[Tipo_assinanteEnum] = Tipo_assinanteEnum.RESIDENCIAL_PESSOA_FISICA
    filial_id: Optional[int] = None
    filtra_filial: Optional[Filtra_filialEnum] = Filtra_filialEnum.SIM
    idx: Optional[str] = ''
    data_cadastro: Optional[str] = ''
    ativo_serasa: Optional[Ativo_serasaEnum] = None
    convert_cliente_forn: Optional[Convert_cliente_fornEnum] = Convert_cliente_fornEnum.NAO
    atualizar_cadastro_galaxPay: Optional[str] = ''
    grau_satisfacao: Optional[Grau_satisfacaoEnum] = None
    id_condominio: Optional[int] = None
    bloco: Optional[str] = ''
    apartamento: Optional[str] = ''
    cep: Optional[str] = ''
    cif: Optional[str] = ''
    complemento: Optional[str] = ''
    uf: Optional[int] = None
    referencia: Optional[str] = ''
    moradia: Optional[MoradiaEnum] = None
    tipo_localidade: Tipo_localidadeEnum = Tipo_localidadeEnum.ZONA_URBANA
    latitude: Optional[str] = ''
    longitude: Optional[str] = ''
    cep_cob: Optional[str] = ''
    endereco_cob: Optional[str] = ''
    numero_cob: Optional[str] = ''
    bairro_cob: Optional[str] = ''
    cidade_cob: Optional[int] = None
    complemento_cob: Optional[str] = ''
    referencia_cob: Optional[str] = ''
    uf_cob: Optional[str] = ''
    fone: Optional[str] = ''
    telefone_comercial: Optional[str] = ''
    ramal: Optional[str] = ''
    id_operadora_celular: Optional[int] = None
    telefone_celular: Optional[str] = ''
    whatsapp: Optional[str] = ''
    email: Optional[str] = ''
    contato: Optional[str] = ''
    website: Optional[str] = ''
    skype: Optional[str] = ''
    facebook: Optional[str] = ''
    hotsite_email: Optional[str] = ''
    senha: Optional[Any] = None
    acesso_automatico_central: Optional[Acesso_automatico_centralEnum] = Acesso_automatico_centralEnum.PADRAO
    alterar_senha_primeiro_acesso: Optional[Alterar_senha_primeiro_acessoEnum] = Alterar_senha_primeiro_acessoEnum.PADRAO
    senha_hotsite_md5: Optional[Senha_hotsite_md5Enum] = Senha_hotsite_md5Enum.NAO
    hotsite_acesso: Optional[str] = ''
    crm: Optional[CrmEnum] = CrmEnum.NAO
    id_segmento: Optional[int] = None
    id_candato_tipo: Optional[int] = None
    id_campanha: Optional[int] = None
    id_concorrente: Optional[int] = None
    id_perfil: Optional[int] = None
    responsavel: Optional[int] = None
    indicado_por: Optional[int] = None
    cadastrado_via_viabilidade: Optional[Cadastrado_via_viabilidadeEnum] = Cadastrado_via_viabilidadeEnum.NAO
    status_prospeccao: Optional[Status_prospeccaoEnum] = Status_prospeccaoEnum.NOVO
    crm_data_novo: Optional[str] = ''
    crm_data_sondagem: Optional[str] = ''
    crm_data_apresentando: Optional[str] = ''
    crm_data_negociando: Optional[str] = ''
    crm_data_vencemos: Optional[str] = ''
    crm_data_perdemos: Optional[str] = ''
    crm_data_abortamos: Optional[str] = ''
    crm_data_sem_porta_disponivel: Optional[str] = ''
    crm_data_sem_viabilidade: Optional[str] = ''
    pipe_id_organizacao: Optional[str] = ''
    foto_cartao: Optional[Any] = None
    participa_cobranca: Optional[str] = ''
    num_dias_cob: Optional[str] = ''
    participa_pre_cobranca: Optional[Participa_pre_cobrancaEnum] = Participa_pre_cobrancaEnum.SIM
    cob_envia_email: Optional[Cob_envia_emailEnum] = Cob_envia_emailEnum.SIM
    cob_envia_sms: Optional[Cob_envia_smsEnum] = Cob_envia_smsEnum.SIM
    fieldset_mensagem_atencao_regua_crm: Optional[str] = ''
    id_conta: Optional[int] = None
    cond_pagamento: Optional[int] = None
    id_vendedor: Optional[int] = None
    tabela_preco: Optional[int] = None
    deb_automatico: Optional[str] = ''
    deb_agencia: Optional[str] = ''
    deb_conta: Optional[str] = ''
    codigo_operacao: Optional[str] = ''
    tipo_pessoa_titular_conta: Optional[Tipo_pessoa_titular_contaEnum] = Tipo_pessoa_titular_contaEnum.FISICA
    cnpj_cpf_titular_conta: Optional[str] = ''
    ultima_atualizacao: Optional[str] = ''
    regua_cobranca_considera: Optional[Regua_cobranca_consideraEnum] = Regua_cobranca_consideraEnum.PADRAO
    regua_cobranca_wpp: Optional[Regua_cobranca_wppEnum] = Regua_cobranca_wppEnum.SIM
    regua_cobranca_notificacao: Optional[Regua_cobranca_notificacaoEnum] = Regua_cobranca_notificacaoEnum.SIM
    fieldset_mensagem_atencao_regua: Optional[str] = ''
    nome_pai: Optional[str] = ''
    cpf_pai: Optional[str] = ''
    identidade_pai: Optional[str] = ''
    nascimento_pai: Optional[str] = ''
    nome_mae: Optional[str] = ''
    cpf_mae: Optional[str] = ''
    identidade_mae: Optional[str] = ''
    nascimento_mae: Optional[str] = ''
    quantidade_dependentes: Optional[str] = ''
    nome_conjuge: Optional[str] = ''
    fone_conjuge: Optional[str] = ''
    cpf_conjuge: Optional[str] = ''
    rg_conjuge: Optional[str] = ''
    data_nascimento_conjuge: Optional[str] = ''
    nome_contador: Optional[str] = ''
    telefone_contador: Optional[str] = ''
    orgao_publico: Optional[Orgao_publicoEnum] = Orgao_publicoEnum.NAO
    im: Optional[str] = ''
    nome_representante_1: Optional[str] = ''
    cpf_representante_1: Optional[str] = ''
    identidade_representante_1: Optional[str] = ''
    nome_representante_2: Optional[str] = ''
    cpf_representante_2: Optional[str] = ''
    identidade_representante_2: Optional[str] = ''
    emp_empresa: Optional[str] = ''
    emp_cnpj: Optional[str] = ''
    emp_cep: Optional[str] = ''
    emp_endereco: Optional[str] = ''
    emp_cidade: Optional[str] = ''
    emp_fone: Optional[str] = ''
    emp_cargo: Optional[str] = ''
    emp_remuneracao: Optional[str] = ''
    emp_data_admissao: Optional[str] = ''
    iss_classificacao_padrao: Iss_classificacao_padraoEnum = Iss_classificacao_padraoEnum.PADRAO
    pis_retem: Optional[str] = ''
    cofins_retem: Optional[str] = ''
    csll_retem: Optional[str] = ''
    irrf_retem: Optional[str] = ''
    desconto_irrf_valor_inferior: Optional[Desconto_irrf_valor_inferiorEnum] = Desconto_irrf_valor_inferiorEnum.NAO
    inss_retem: Optional[str] = ''
    cli_desconta_iss_retido_total: Optional[str] = ''
    percentual_reducao: Optional[str] = ''
    ref_com_empresa1: Optional[str] = ''
    ref_com_fone1: Optional[str] = ''
    ref_com_empresa2: Optional[str] = ''
    ref_com_fone2: Optional[str] = ''
    ref_pes_nome1: Optional[str] = ''
    ref_pes_fone1: Optional[str] = ''
    ref_pes_nome2: Optional[str] = ''
    ref_pes_fone2: Optional[str] = ''
    obs: Optional[str] = ''
    alerta: Optional[str] = ''

    @property
    def id(self) -> str:
        return str(self.id_autoincrement)

    @property
    def table(self) -> str:
        return "cliente"

    def to_dict(self) -> dict[str, str]:
        return {
            'id_autoincrement': str(self.id_autoincrement),
            'razao': self.razao if self.razao is not None else '',
            'endereco': self.endereco if self.endereco is not None else '',
            'numero': self.numero if self.numero is not None else '',
            'bairro': self.bairro if self.bairro is not None else '',
            'cidade': str(self.cidade) if self.cidade is not None else '',
            'dica_imposto_retido_cliente': self.dica_imposto_retido_cliente if self.dica_imposto_retido_cliente is not None else '',
            'ativo': self.ativo.value if self.ativo is not None else '',
            'id_tipo_cliente': str(self.id_tipo_cliente) if self.id_tipo_cliente is not None else '',
            'tipo_cliente_scm': self.tipo_cliente_scm.value if self.tipo_cliente_scm is not None else '',
            'tipo_ente_governamental': self.tipo_ente_governamental.value if self.tipo_ente_governamental is not None else '',
            'pais': self.pais if self.pais is not None else '',
            'tipo_pessoa': self.tipo_pessoa.value if self.tipo_pessoa is not None else '',
            'regime_fiscal_col': self.regime_fiscal_col.value if self.regime_fiscal_col is not None else '',
            'nome_social': self.nome_social if self.nome_social is not None else '',
            'fantasia': self.fantasia if self.fantasia is not None else '',
            'tipo_documento_identificacao': self.tipo_documento_identificacao.value if self.tipo_documento_identificacao is not None else '',
            'cnpj_cpf': self.cnpj_cpf if self.cnpj_cpf is not None else '',
            'ie_identidade': self.ie_identidade if self.ie_identidade is not None else '',
            'contribuinte_icms': self.contribuinte_icms.value if self.contribuinte_icms is not None else '',
            'contribuinte_icms_alert': self.contribuinte_icms_alert if self.contribuinte_icms_alert is not None else '',
            'rg_orgao_emissor': self.rg_orgao_emissor if self.rg_orgao_emissor is not None else '',
            'nacionalidade': self.nacionalidade if self.nacionalidade is not None else '',
            'cidade_naturalidade': str(self.cidade_naturalidade) if self.cidade_naturalidade is not None else '',
            'estado_nascimento': str(self.estado_nascimento) if self.estado_nascimento is not None else '',
            'data_nascimento': self.data_nascimento if self.data_nascimento is not None else '',
            'Sexo': self.Sexo.value if self.Sexo is not None else '',
            'profissao': self.profissao if self.profissao is not None else '',
            'estado_civil': self.estado_civil.value if self.estado_civil is not None else '',
            'inscricao_municipal': self.inscricao_municipal if self.inscricao_municipal is not None else '',
            'isuf': self.isuf if self.isuf is not None else '',
            'tipo_assinante': self.tipo_assinante.value if self.tipo_assinante is not None else '',
            'filial_id': str(self.filial_id) if self.filial_id is not None else '',
            'filtra_filial': self.filtra_filial.value if self.filtra_filial is not None else '',
            'idx': self.idx if self.idx is not None else '',
            'data_cadastro': self.data_cadastro if self.data_cadastro is not None else '',
            'ativo_serasa': self.ativo_serasa.value if self.ativo_serasa is not None else '',
            'convert_cliente_forn': self.convert_cliente_forn.value if self.convert_cliente_forn is not None else '',
            'atualizar_cadastro_galaxPay': self.atualizar_cadastro_galaxPay if self.atualizar_cadastro_galaxPay is not None else '',
            'grau_satisfacao': self.grau_satisfacao.value if self.grau_satisfacao is not None else '',
            'id_condominio': str(self.id_condominio) if self.id_condominio is not None else '',
            'bloco': self.bloco if self.bloco is not None else '',
            'apartamento': self.apartamento if self.apartamento is not None else '',
            'cep': self.cep if self.cep is not None else '',
            'cif': self.cif if self.cif is not None else '',
            'complemento': self.complemento if self.complemento is not None else '',
            'uf': str(self.uf) if self.uf is not None else '',
            'referencia': self.referencia if self.referencia is not None else '',
            'moradia': self.moradia.value if self.moradia is not None else '',
            'tipo_localidade': self.tipo_localidade.value if self.tipo_localidade is not None else '',
            'latitude': self.latitude if self.latitude is not None else '',
            'longitude': self.longitude if self.longitude is not None else '',
            'cep_cob': self.cep_cob if self.cep_cob is not None else '',
            'endereco_cob': self.endereco_cob if self.endereco_cob is not None else '',
            'numero_cob': self.numero_cob if self.numero_cob is not None else '',
            'bairro_cob': self.bairro_cob if self.bairro_cob is not None else '',
            'cidade_cob': str(self.cidade_cob) if self.cidade_cob is not None else '',
            'complemento_cob': self.complemento_cob if self.complemento_cob is not None else '',
            'referencia_cob': self.referencia_cob if self.referencia_cob is not None else '',
            'uf_cob': self.uf_cob if self.uf_cob is not None else '',
            'fone': self.fone if self.fone is not None else '',
            'telefone_comercial': self.telefone_comercial if self.telefone_comercial is not None else '',
            'ramal': self.ramal if self.ramal is not None else '',
            'id_operadora_celular': str(self.id_operadora_celular) if self.id_operadora_celular is not None else '',
            'telefone_celular': self.telefone_celular if self.telefone_celular is not None else '',
            'whatsapp': self.whatsapp if self.whatsapp is not None else '',
            'email': self.email if self.email is not None else '',
            'contato': self.contato if self.contato is not None else '',
            'website': self.website if self.website is not None else '',
            'skype': self.skype if self.skype is not None else '',
            'facebook': self.facebook if self.facebook is not None else '',
            'hotsite_email': self.hotsite_email if self.hotsite_email is not None else '',
            'senha': self.senha if self.senha is not None else '',
            'acesso_automatico_central': self.acesso_automatico_central.value if self.acesso_automatico_central is not None else '',
            'alterar_senha_primeiro_acesso': self.alterar_senha_primeiro_acesso.value if self.alterar_senha_primeiro_acesso is not None else '',
            'senha_hotsite_md5': self.senha_hotsite_md5.value if self.senha_hotsite_md5 is not None else '',
            'hotsite_acesso': self.hotsite_acesso if self.hotsite_acesso is not None else '',
            'crm': self.crm.value if self.crm is not None else '',
            'id_segmento': str(self.id_segmento) if self.id_segmento is not None else '',
            'id_candato_tipo': str(self.id_candato_tipo) if self.id_candato_tipo is not None else '',
            'id_campanha': str(self.id_campanha) if self.id_campanha is not None else '',
            'id_concorrente': str(self.id_concorrente) if self.id_concorrente is not None else '',
            'id_perfil': str(self.id_perfil) if self.id_perfil is not None else '',
            'responsavel': str(self.responsavel) if self.responsavel is not None else '',
            'indicado_por': str(self.indicado_por) if self.indicado_por is not None else '',
            'cadastrado_via_viabilidade': self.cadastrado_via_viabilidade.value if self.cadastrado_via_viabilidade is not None else '',
            'status_prospeccao': self.status_prospeccao.value if self.status_prospeccao is not None else '',
            'crm_data_novo': self.crm_data_novo if self.crm_data_novo is not None else '',
            'crm_data_sondagem': self.crm_data_sondagem if self.crm_data_sondagem is not None else '',
            'crm_data_apresentando': self.crm_data_apresentando if self.crm_data_apresentando is not None else '',
            'crm_data_negociando': self.crm_data_negociando if self.crm_data_negociando is not None else '',
            'crm_data_vencemos': self.crm_data_vencemos if self.crm_data_vencemos is not None else '',
            'crm_data_perdemos': self.crm_data_perdemos if self.crm_data_perdemos is not None else '',
            'crm_data_abortamos': self.crm_data_abortamos if self.crm_data_abortamos is not None else '',
            'crm_data_sem_porta_disponivel': self.crm_data_sem_porta_disponivel if self.crm_data_sem_porta_disponivel is not None else '',
            'crm_data_sem_viabilidade': self.crm_data_sem_viabilidade if self.crm_data_sem_viabilidade is not None else '',
            'pipe_id_organizacao': self.pipe_id_organizacao if self.pipe_id_organizacao is not None else '',
            'foto_cartao': self.foto_cartao if self.foto_cartao is not None else '',
            'participa_cobranca': self.participa_cobranca if self.participa_cobranca is not None else '',
            'num_dias_cob': self.num_dias_cob if self.num_dias_cob is not None else '',
            'participa_pre_cobranca': self.participa_pre_cobranca.value if self.participa_pre_cobranca is not None else '',
            'cob_envia_email': self.cob_envia_email.value if self.cob_envia_email is not None else '',
            'cob_envia_sms': self.cob_envia_sms.value if self.cob_envia_sms is not None else '',
            'fieldset_mensagem_atencao_regua_crm': self.fieldset_mensagem_atencao_regua_crm if self.fieldset_mensagem_atencao_regua_crm is not None else '',
            'id_conta': str(self.id_conta) if self.id_conta is not None else '',
            'cond_pagamento': str(self.cond_pagamento) if self.cond_pagamento is not None else '',
            'id_vendedor': str(self.id_vendedor) if self.id_vendedor is not None else '',
            'tabela_preco': str(self.tabela_preco) if self.tabela_preco is not None else '',
            'deb_automatico': self.deb_automatico if self.deb_automatico is not None else '',
            'deb_agencia': self.deb_agencia if self.deb_agencia is not None else '',
            'deb_conta': self.deb_conta if self.deb_conta is not None else '',
            'codigo_operacao': self.codigo_operacao if self.codigo_operacao is not None else '',
            'tipo_pessoa_titular_conta': self.tipo_pessoa_titular_conta.value if self.tipo_pessoa_titular_conta is not None else '',
            'cnpj_cpf_titular_conta': self.cnpj_cpf_titular_conta if self.cnpj_cpf_titular_conta is not None else '',
            'ultima_atualizacao': self.ultima_atualizacao if self.ultima_atualizacao is not None else '',
            'regua_cobranca_considera': self.regua_cobranca_considera.value if self.regua_cobranca_considera is not None else '',
            'regua_cobranca_wpp': self.regua_cobranca_wpp.value if self.regua_cobranca_wpp is not None else '',
            'regua_cobranca_notificacao': self.regua_cobranca_notificacao.value if self.regua_cobranca_notificacao is not None else '',
            'fieldset_mensagem_atencao_regua': self.fieldset_mensagem_atencao_regua if self.fieldset_mensagem_atencao_regua is not None else '',
            'nome_pai': self.nome_pai if self.nome_pai is not None else '',
            'cpf_pai': self.cpf_pai if self.cpf_pai is not None else '',
            'identidade_pai': self.identidade_pai if self.identidade_pai is not None else '',
            'nascimento_pai': self.nascimento_pai if self.nascimento_pai is not None else '',
            'nome_mae': self.nome_mae if self.nome_mae is not None else '',
            'cpf_mae': self.cpf_mae if self.cpf_mae is not None else '',
            'identidade_mae': self.identidade_mae if self.identidade_mae is not None else '',
            'nascimento_mae': self.nascimento_mae if self.nascimento_mae is not None else '',
            'quantidade_dependentes': self.quantidade_dependentes if self.quantidade_dependentes is not None else '',
            'nome_conjuge': self.nome_conjuge if self.nome_conjuge is not None else '',
            'fone_conjuge': self.fone_conjuge if self.fone_conjuge is not None else '',
            'cpf_conjuge': self.cpf_conjuge if self.cpf_conjuge is not None else '',
            'rg_conjuge': self.rg_conjuge if self.rg_conjuge is not None else '',
            'data_nascimento_conjuge': self.data_nascimento_conjuge if self.data_nascimento_conjuge is not None else '',
            'nome_contador': self.nome_contador if self.nome_contador is not None else '',
            'telefone_contador': self.telefone_contador if self.telefone_contador is not None else '',
            'orgao_publico': self.orgao_publico.value if self.orgao_publico is not None else '',
            'im': self.im if self.im is not None else '',
            'nome_representante_1': self.nome_representante_1 if self.nome_representante_1 is not None else '',
            'cpf_representante_1': self.cpf_representante_1 if self.cpf_representante_1 is not None else '',
            'identidade_representante_1': self.identidade_representante_1 if self.identidade_representante_1 is not None else '',
            'nome_representante_2': self.nome_representante_2 if self.nome_representante_2 is not None else '',
            'cpf_representante_2': self.cpf_representante_2 if self.cpf_representante_2 is not None else '',
            'identidade_representante_2': self.identidade_representante_2 if self.identidade_representante_2 is not None else '',
            'emp_empresa': self.emp_empresa if self.emp_empresa is not None else '',
            'emp_cnpj': self.emp_cnpj if self.emp_cnpj is not None else '',
            'emp_cep': self.emp_cep if self.emp_cep is not None else '',
            'emp_endereco': self.emp_endereco if self.emp_endereco is not None else '',
            'emp_cidade': self.emp_cidade if self.emp_cidade is not None else '',
            'emp_fone': self.emp_fone if self.emp_fone is not None else '',
            'emp_cargo': self.emp_cargo if self.emp_cargo is not None else '',
            'emp_remuneracao': self.emp_remuneracao if self.emp_remuneracao is not None else '',
            'emp_data_admissao': self.emp_data_admissao if self.emp_data_admissao is not None else '',
            'iss_classificacao_padrao': self.iss_classificacao_padrao.value if self.iss_classificacao_padrao is not None else '',
            'pis_retem': self.pis_retem if self.pis_retem is not None else '',
            'cofins_retem': self.cofins_retem if self.cofins_retem is not None else '',
            'csll_retem': self.csll_retem if self.csll_retem is not None else '',
            'irrf_retem': self.irrf_retem if self.irrf_retem is not None else '',
            'desconto_irrf_valor_inferior': self.desconto_irrf_valor_inferior.value if self.desconto_irrf_valor_inferior is not None else '',
            'inss_retem': self.inss_retem if self.inss_retem is not None else '',
            'cli_desconta_iss_retido_total': self.cli_desconta_iss_retido_total if self.cli_desconta_iss_retido_total is not None else '',
            'percentual_reducao': self.percentual_reducao if self.percentual_reducao is not None else '',
            'ref_com_empresa1': self.ref_com_empresa1 if self.ref_com_empresa1 is not None else '',
            'ref_com_fone1': self.ref_com_fone1 if self.ref_com_fone1 is not None else '',
            'ref_com_empresa2': self.ref_com_empresa2 if self.ref_com_empresa2 is not None else '',
            'ref_com_fone2': self.ref_com_fone2 if self.ref_com_fone2 is not None else '',
            'ref_pes_nome1': self.ref_pes_nome1 if self.ref_pes_nome1 is not None else '',
            'ref_pes_fone1': self.ref_pes_fone1 if self.ref_pes_fone1 is not None else '',
            'ref_pes_nome2': self.ref_pes_nome2 if self.ref_pes_nome2 is not None else '',
            'ref_pes_fone2': self.ref_pes_fone2 if self.ref_pes_fone2 is not None else '',
            'obs': self.obs if self.obs is not None else '',
            'alerta': self.alerta if self.alerta is not None else '',
        }

    def is_valid(self) -> bool:
        return self.id_autoincrement is not None and self.razao is not None and self.endereco is not None and self.numero is not None and self.bairro is not None and self.cidade is not None and self.dica_imposto_retido_cliente is not None

    def __repr__(self) -> str:
        return f"Cliente(id_autoincrement={self.id_autoincrement!r}, razao={self.razao!r}, endereco={self.endereco!r}, numero={self.numero!r}, bairro={self.bairro!r}, cidade={self.cidade!r}, dica_imposto_retido_cliente={self.dica_imposto_retido_cliente!r})"

    #------------------------------ CONVERSOR DTO ------------------------------#
    def dto_convert(self, data: dict[str, str]) -> IModel:
        return ClientModel(
            id_autoincrement=int(data.get('id_autoincrement', 0)),
            razao=data.get('razao', ''),
            endereco=data.get('endereco', ''),
            numero=data.get('numero', ''),
            bairro=data.get('bairro', ''),
            cidade=int(data['cidade']),
            dica_imposto_retido_cliente=data.get('dica_imposto_retido_cliente', ''),
            ativo=AtivoEnum(data['ativo']),
            id_tipo_cliente=int(data['id_tipo_cliente']) if data.get('id_tipo_cliente') else None,
            tipo_cliente_scm=Tipo_cliente_scmEnum(data['tipo_cliente_scm']) if data.get('tipo_cliente_scm') else None,
            tipo_ente_governamental=Tipo_ente_governamentalEnum(data['tipo_ente_governamental']) if data.get('tipo_ente_governamental') else None,
            pais=data.get('pais', ''),
            tipo_pessoa=Tipo_pessoaEnum(data['tipo_pessoa']),
            regime_fiscal_col=Regime_fiscal_colEnum(data['regime_fiscal_col']) if data.get('regime_fiscal_col') else None,
            nome_social=data.get('nome_social', ''),
            fantasia=data.get('fantasia', ''),
            tipo_documento_identificacao=Tipo_documento_identificacaoEnum(data['tipo_documento_identificacao']) if data.get('tipo_documento_identificacao') else None,
            cnpj_cpf=data.get('cnpj_cpf', ''),
            ie_identidade=data.get('ie_identidade', ''),
            contribuinte_icms=Contribuinte_icmsEnum(data['contribuinte_icms']) if data.get('contribuinte_icms') else None,
            contribuinte_icms_alert=data.get('contribuinte_icms_alert', ''),
            rg_orgao_emissor=data.get('rg_orgao_emissor', ''),
            nacionalidade=data.get('nacionalidade', ''),
            cidade_naturalidade=int(data['cidade_naturalidade']) if data.get('cidade_naturalidade') else None,
            estado_nascimento=int(data['estado_nascimento']) if data.get('estado_nascimento') else None,
            data_nascimento=data.get('data_nascimento', ''),
            Sexo=SexoEnum(data['Sexo']) if data.get('Sexo') else None,
            profissao=data.get('profissao', ''),
            estado_civil=Estado_civilEnum(data['estado_civil']) if data.get('estado_civil') else None,
            inscricao_municipal=data.get('inscricao_municipal', ''),
            isuf=data.get('isuf', ''),
            tipo_assinante=Tipo_assinanteEnum(data['tipo_assinante']) if data.get('tipo_assinante') else None,
            filial_id=int(data['filial_id']) if data.get('filial_id') else None,
            filtra_filial=Filtra_filialEnum(data['filtra_filial']) if data.get('filtra_filial') else None,
            idx=data.get('idx', ''),
            data_cadastro=data.get('data_cadastro', ''),
            ativo_serasa=Ativo_serasaEnum(data['ativo_serasa']) if data.get('ativo_serasa') else None,
            convert_cliente_forn=Convert_cliente_fornEnum(data['convert_cliente_forn']) if data.get('convert_cliente_forn') else None,
            atualizar_cadastro_galaxPay=data.get('atualizar_cadastro_galaxPay', ''),
            grau_satisfacao=Grau_satisfacaoEnum(data['grau_satisfacao']) if data.get('grau_satisfacao') else None,
            id_condominio=int(data['id_condominio']) if data.get('id_condominio') else None,
            bloco=data.get('bloco', ''),
            apartamento=data.get('apartamento', ''),
            cep=data.get('cep', ''),
            cif=data.get('cif', ''),
            complemento=data.get('complemento', ''),
            uf=int(data['uf']) if data.get('uf') else None,
            referencia=data.get('referencia', ''),
            moradia=MoradiaEnum(data['moradia']) if data.get('moradia') else None,
            tipo_localidade=Tipo_localidadeEnum(data['tipo_localidade']),
            latitude=data.get('latitude', ''),
            longitude=data.get('longitude', ''),
            cep_cob=data.get('cep_cob', ''),
            endereco_cob=data.get('endereco_cob', ''),
            numero_cob=data.get('numero_cob', ''),
            bairro_cob=data.get('bairro_cob', ''),
            cidade_cob=int(data['cidade_cob']) if data.get('cidade_cob') else None,
            complemento_cob=data.get('complemento_cob', ''),
            referencia_cob=data.get('referencia_cob', ''),
            uf_cob=data.get('uf_cob', ''),
            fone=data.get('fone', ''),
            telefone_comercial=data.get('telefone_comercial', ''),
            ramal=data.get('ramal', ''),
            id_operadora_celular=int(data['id_operadora_celular']) if data.get('id_operadora_celular') else None,
            telefone_celular=data.get('telefone_celular', ''),
            whatsapp=data.get('whatsapp', ''),
            email=data.get('email', ''),
            contato=data.get('contato', ''),
            website=data.get('website', ''),
            skype=data.get('skype', ''),
            facebook=data.get('facebook', ''),
            hotsite_email=data.get('hotsite_email', ''),
            senha=data.get('senha', ''),
            acesso_automatico_central=Acesso_automatico_centralEnum(data['acesso_automatico_central']) if data.get('acesso_automatico_central') else None,
            alterar_senha_primeiro_acesso=Alterar_senha_primeiro_acessoEnum(data['alterar_senha_primeiro_acesso']) if data.get('alterar_senha_primeiro_acesso') else None,
            senha_hotsite_md5=Senha_hotsite_md5Enum(data['senha_hotsite_md5']) if data.get('senha_hotsite_md5') else None,
            hotsite_acesso=data.get('hotsite_acesso', ''),
            crm=CrmEnum(data['crm']) if data.get('crm') else None,
            id_segmento=int(data['id_segmento']) if data.get('id_segmento') else None,
            id_candato_tipo=int(data['id_candato_tipo']) if data.get('id_candato_tipo') else None,
            id_campanha=int(data['id_campanha']) if data.get('id_campanha') else None,
            id_concorrente=int(data['id_concorrente']) if data.get('id_concorrente') else None,
            id_perfil=int(data['id_perfil']) if data.get('id_perfil') else None,
            responsavel=int(data['responsavel']) if data.get('responsavel') else None,
            indicado_por=int(data['indicado_por']) if data.get('indicado_por') else None,
            cadastrado_via_viabilidade=Cadastrado_via_viabilidadeEnum(data['cadastrado_via_viabilidade']) if data.get('cadastrado_via_viabilidade') else None,
            status_prospeccao=Status_prospeccaoEnum(data['status_prospeccao']) if data.get('status_prospeccao') else None,
            crm_data_novo=data.get('crm_data_novo', ''),
            crm_data_sondagem=data.get('crm_data_sondagem', ''),
            crm_data_apresentando=data.get('crm_data_apresentando', ''),
            crm_data_negociando=data.get('crm_data_negociando', ''),
            crm_data_vencemos=data.get('crm_data_vencemos', ''),
            crm_data_perdemos=data.get('crm_data_perdemos', ''),
            crm_data_abortamos=data.get('crm_data_abortamos', ''),
            crm_data_sem_porta_disponivel=data.get('crm_data_sem_porta_disponivel', ''),
            crm_data_sem_viabilidade=data.get('crm_data_sem_viabilidade', ''),
            pipe_id_organizacao=data.get('pipe_id_organizacao', ''),
            foto_cartao=data.get('foto_cartao', ''),
            participa_cobranca=data.get('participa_cobranca', ''),
            num_dias_cob=data.get('num_dias_cob', ''),
            participa_pre_cobranca=Participa_pre_cobrancaEnum(data['participa_pre_cobranca']) if data.get('participa_pre_cobranca') else None,
            cob_envia_email=Cob_envia_emailEnum(data['cob_envia_email']) if data.get('cob_envia_email') else None,
            cob_envia_sms=Cob_envia_smsEnum(data['cob_envia_sms']) if data.get('cob_envia_sms') else None,
            fieldset_mensagem_atencao_regua_crm=data.get('fieldset_mensagem_atencao_regua_crm', ''),
            id_conta=int(data['id_conta']) if data.get('id_conta') else None,
            cond_pagamento=int(data['cond_pagamento']) if data.get('cond_pagamento') else None,
            id_vendedor=int(data['id_vendedor']) if data.get('id_vendedor') else None,
            tabela_preco=int(data['tabela_preco']) if data.get('tabela_preco') else None,
            deb_automatico=data.get('deb_automatico', ''),
            deb_agencia=data.get('deb_agencia', ''),
            deb_conta=data.get('deb_conta', ''),
            codigo_operacao=data.get('codigo_operacao', ''),
            tipo_pessoa_titular_conta=Tipo_pessoa_titular_contaEnum(data['tipo_pessoa_titular_conta']) if data.get('tipo_pessoa_titular_conta') else None,
            cnpj_cpf_titular_conta=data.get('cnpj_cpf_titular_conta', ''),
            ultima_atualizacao=data.get('ultima_atualizacao', ''),
            regua_cobranca_considera=Regua_cobranca_consideraEnum(data['regua_cobranca_considera']) if data.get('regua_cobranca_considera') else None,
            regua_cobranca_wpp=Regua_cobranca_wppEnum(data['regua_cobranca_wpp']) if data.get('regua_cobranca_wpp') else None,
            regua_cobranca_notificacao=Regua_cobranca_notificacaoEnum(data['regua_cobranca_notificacao']) if data.get('regua_cobranca_notificacao') else None,
            fieldset_mensagem_atencao_regua=data.get('fieldset_mensagem_atencao_regua', ''),
            nome_pai=data.get('nome_pai', ''),
            cpf_pai=data.get('cpf_pai', ''),
            identidade_pai=data.get('identidade_pai', ''),
            nascimento_pai=data.get('nascimento_pai', ''),
            nome_mae=data.get('nome_mae', ''),
            cpf_mae=data.get('cpf_mae', ''),
            identidade_mae=data.get('identidade_mae', ''),
            nascimento_mae=data.get('nascimento_mae', ''),
            quantidade_dependentes=data.get('quantidade_dependentes', ''),
            nome_conjuge=data.get('nome_conjuge', ''),
            fone_conjuge=data.get('fone_conjuge', ''),
            cpf_conjuge=data.get('cpf_conjuge', ''),
            rg_conjuge=data.get('rg_conjuge', ''),
            data_nascimento_conjuge=data.get('data_nascimento_conjuge', ''),
            nome_contador=data.get('nome_contador', ''),
            telefone_contador=data.get('telefone_contador', ''),
            orgao_publico=Orgao_publicoEnum(data['orgao_publico']) if data.get('orgao_publico') else None,
            im=data.get('im', ''),
            nome_representante_1=data.get('nome_representante_1', ''),
            cpf_representante_1=data.get('cpf_representante_1', ''),
            identidade_representante_1=data.get('identidade_representante_1', ''),
            nome_representante_2=data.get('nome_representante_2', ''),
            cpf_representante_2=data.get('cpf_representante_2', ''),
            identidade_representante_2=data.get('identidade_representante_2', ''),
            emp_empresa=data.get('emp_empresa', ''),
            emp_cnpj=data.get('emp_cnpj', ''),
            emp_cep=data.get('emp_cep', ''),
            emp_endereco=data.get('emp_endereco', ''),
            emp_cidade=data.get('emp_cidade', ''),
            emp_fone=data.get('emp_fone', ''),
            emp_cargo=data.get('emp_cargo', ''),
            emp_remuneracao=data.get('emp_remuneracao', ''),
            emp_data_admissao=data.get('emp_data_admissao', ''),
            iss_classificacao_padrao=Iss_classificacao_padraoEnum(data['iss_classificacao_padrao']),
            pis_retem=data.get('pis_retem', ''),
            cofins_retem=data.get('cofins_retem', ''),
            csll_retem=data.get('csll_retem', ''),
            irrf_retem=data.get('irrf_retem', ''),
            desconto_irrf_valor_inferior=Desconto_irrf_valor_inferiorEnum(data['desconto_irrf_valor_inferior']) if data.get('desconto_irrf_valor_inferior') else None,
            inss_retem=data.get('inss_retem', ''),
            cli_desconta_iss_retido_total=data.get('cli_desconta_iss_retido_total', ''),
            percentual_reducao=data.get('percentual_reducao', ''),
            ref_com_empresa1=data.get('ref_com_empresa1', ''),
            ref_com_fone1=data.get('ref_com_fone1', ''),
            ref_com_empresa2=data.get('ref_com_empresa2', ''),
            ref_com_fone2=data.get('ref_com_fone2', ''),
            ref_pes_nome1=data.get('ref_pes_nome1', ''),
            ref_pes_fone1=data.get('ref_pes_fone1', ''),
            ref_pes_nome2=data.get('ref_pes_nome2', ''),
            ref_pes_fone2=data.get('ref_pes_fone2', ''),
            obs=data.get('obs', ''),
            alerta=data.get('alerta', ''),
        )
