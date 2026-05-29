from __future__ import annotations

from typing import Optional
from ORM_IXC.enums.client import *
from ORM_IXC.interfaces.IModel import IModel, IModelWithId
from ORM_IXC.statemants.classBase import Field
from ORM_IXC.statemants.mapper import Mapped, field as mapped_field
from ORM_IXC.statemants.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel

@MetaModels
class ClientModel(IModelWithId, BaseModel):
    id: Mapped[Optional[int]]
    razao: Mapped[str]
    endereco: Mapped[str]
    numero: Mapped[str]
    bairro: Mapped[str]
    cidade: Mapped[int]
    dica_imposto_retido_cliente: Mapped[str]
    ativo: Mapped[AtivoEnum] = mapped_field(AtivoEnum.SIM)
    id_tipo_cliente: Mapped[Optional[int]] = mapped_field(None)
    tipo_cliente_scm: Mapped[Optional[Tipo_cliente_scmEnum]] = mapped_field(Tipo_cliente_scmEnum.COMERCIAL)
    tipo_ente_governamental: Mapped[Optional[Tipo_ente_governamentalEnum]] = mapped_field(None)
    pais: Mapped[Optional[str]] = mapped_field('')
    tipo_pessoa: Mapped[Tipo_pessoaEnum] = mapped_field(Tipo_pessoaEnum.FISICA)
    regime_fiscal_col: Mapped[Optional[Regime_fiscal_colEnum]] = mapped_field(None)
    nome_social: Mapped[Optional[str]] = mapped_field('')
    fantasia: Mapped[Optional[str]] = mapped_field('')
    tipo_documento_identificacao: Mapped[Optional[Tipo_documento_identificacaoEnum]] = mapped_field(None)
    cnpj_cpf: Mapped[Optional[str]] = mapped_field('')
    ie_identidade: Mapped[Optional[str]] = mapped_field('')
    contribuinte_icms: Mapped[Optional[Contribuinte_icmsEnum]] = mapped_field(Contribuinte_icmsEnum.NAO)
    contribuinte_icms_alert: Mapped[Optional[str]] = mapped_field('')
    rg_orgao_emissor: Mapped[Optional[str]] = mapped_field('')
    nacionalidade: Mapped[Optional[str]] = mapped_field('')
    cidade_naturalidade: Mapped[Optional[int]] = mapped_field(None)
    estado_nascimento: Mapped[Optional[int]] = mapped_field(None)
    data_nascimento: Mapped[Optional[str]] = mapped_field('')
    Sexo: Mapped[Optional[SexoEnum]] = mapped_field(None)
    profissao: Mapped[Optional[str]] = mapped_field('')
    estado_civil: Mapped[Optional[Estado_civilEnum]] = mapped_field(None)
    inscricao_municipal: Mapped[Optional[str]] = mapped_field('')
    isuf: Mapped[Optional[str]] = mapped_field('')
    tipo_assinante: Mapped[Optional[Tipo_assinanteEnum]] = mapped_field(Tipo_assinanteEnum.RESIDENCIAL_PESSOA_FISICA)
    filial_id: Mapped[Optional[int]] = mapped_field(None)
    filtra_filial: Mapped[Optional[Filtra_filialEnum]] = mapped_field(Filtra_filialEnum.SIM)
    idx: Mapped[Optional[str]] = mapped_field('')
    data_cadastro: Mapped[Optional[str]] = mapped_field('')
    ativo_serasa: Mapped[Optional[Ativo_serasaEnum]] = mapped_field(None)
    convert_cliente_forn: Mapped[Optional[Convert_cliente_fornEnum]] = mapped_field(Convert_cliente_fornEnum.NAO)
    atualizar_cadastro_galaxPay: Mapped[Optional[str]] = mapped_field('')
    grau_satisfacao: Mapped[Optional[Grau_satisfacaoEnum]] = mapped_field(None)
    id_condominio: Mapped[Optional[int]] = mapped_field(None)
    bloco: Mapped[Optional[str]] = mapped_field('')
    apartamento: Mapped[Optional[str]] = mapped_field('')
    cep: Mapped[Optional[str]] = mapped_field('')
    cif: Mapped[Optional[str]] = mapped_field('')
    complemento: Mapped[Optional[str]] = mapped_field('')
    uf: Mapped[Optional[int]] = mapped_field(None)
    referencia: Mapped[Optional[str]] = mapped_field('')
    moradia: Mapped[Optional[MoradiaEnum]] = mapped_field(None)
    tipo_localidade: Mapped[Tipo_localidadeEnum] = mapped_field(Tipo_localidadeEnum.ZONA_URBANA)
    latitude: Mapped[Optional[str]] = mapped_field('')
    longitude: Mapped[Optional[str]] = mapped_field('')
    cep_cob: Mapped[Optional[str]] = mapped_field('')
    endereco_cob: Mapped[Optional[str]] = mapped_field('')
    numero_cob: Mapped[Optional[str]] = mapped_field('')
    bairro_cob: Mapped[Optional[str]] = mapped_field('')
    cidade_cob: Mapped[Optional[int]] = mapped_field(None)
    complemento_cob: Mapped[Optional[str]] = mapped_field('')
    referencia_cob: Mapped[Optional[str]] = mapped_field('')
    uf_cob: Mapped[Optional[str]] = mapped_field('')
    fone: Mapped[Optional[str]] = mapped_field('')
    telefone_comercial: Mapped[Optional[str]] = mapped_field('')
    ramal: Mapped[Optional[str]] = mapped_field('')
    id_operadora_celular: Mapped[Optional[int]] = mapped_field(None)
    telefone_celular: Mapped[Optional[str]] = mapped_field('')
    whatsapp: Mapped[Optional[str]] = mapped_field('')
    email: Mapped[Optional[str]] = mapped_field('')
    contato: Mapped[Optional[str]] = mapped_field('')
    website: Mapped[Optional[str]] = mapped_field('')
    skype: Mapped[Optional[str]] = mapped_field('')
    facebook: Mapped[Optional[str]] = mapped_field('')
    hotsite_email: Mapped[Optional[str]] = mapped_field('')
    senha: Mapped[Optional[str]] = mapped_field(None)
    acesso_automatico_central: Mapped[Optional[Acesso_automatico_centralEnum]] = mapped_field(Acesso_automatico_centralEnum.PADRAO)
    alterar_senha_primeiro_acesso: Mapped[Optional[Alterar_senha_primeiro_acessoEnum]] = mapped_field(Alterar_senha_primeiro_acessoEnum.PADRAO)
    senha_hotsite_md5: Mapped[Optional[Senha_hotsite_md5Enum]] = mapped_field(Senha_hotsite_md5Enum.NAO)
    hotsite_acesso: Mapped[Optional[str]] = mapped_field('')
    crm: Mapped[Optional[CrmEnum]] = mapped_field(CrmEnum.NAO)
    id_segmento: Mapped[Optional[int]] = mapped_field(None)
    id_candato_tipo: Mapped[Optional[int]] = mapped_field(None)
    id_campanha: Mapped[Optional[int]] = mapped_field(None)
    id_concorrente: Mapped[Optional[int]] = mapped_field(None)
    id_perfil: Mapped[Optional[int]] = mapped_field(None)
    responsavel: Mapped[Optional[int]] = mapped_field(None)
    indicado_por: Mapped[Optional[int]] = mapped_field(None)
    cadastrado_via_viabilidade: Mapped[Optional[Cadastrado_via_viabilidadeEnum]] = mapped_field(Cadastrado_via_viabilidadeEnum.NAO)
    status_prospeccao: Mapped[Optional[Status_prospeccaoEnum]] = mapped_field(Status_prospeccaoEnum.NOVO)
    crm_data_novo: Mapped[Optional[str]] = mapped_field('')
    crm_data_sondagem: Mapped[Optional[str]] = mapped_field('')
    crm_data_apresentando: Mapped[Optional[str]] = mapped_field('')
    crm_data_negociando: Mapped[Optional[str]] = mapped_field('')
    crm_data_vencemos: Mapped[Optional[str]] = mapped_field('')
    crm_data_perdemos: Mapped[Optional[str]] = mapped_field('')
    crm_data_abortamos: Mapped[Optional[str]] = mapped_field('')
    crm_data_sem_porta_disponivel: Mapped[Optional[str]] = mapped_field('')
    crm_data_sem_viabilidade: Mapped[Optional[str]] = mapped_field('')
    pipe_id_organizacao: Mapped[Optional[str]] = mapped_field('')
    foto_cartao: Mapped[Optional[str]] = mapped_field(None)
    participa_cobranca: Mapped[Optional[str]] = mapped_field('')
    num_dias_cob: Mapped[Optional[str]] = mapped_field('')
    participa_pre_cobranca: Mapped[Optional[Participa_pre_cobrancaEnum]] = mapped_field(Participa_pre_cobrancaEnum.SIM)
    cob_envia_email: Mapped[Optional[Cob_envia_emailEnum]] = mapped_field(Cob_envia_emailEnum.SIM)
    cob_envia_sms: Mapped[Optional[Cob_envia_smsEnum]] = mapped_field(Cob_envia_smsEnum.SIM)
    fieldset_mensagem_atencao_regua_crm: Mapped[Optional[str]] = mapped_field('')
    id_conta: Mapped[Optional[int]] = mapped_field(None)
    cond_pagamento: Mapped[Optional[int]] = mapped_field(None)
    id_vendedor: Mapped[Optional[int]] = mapped_field(None)
    tabela_preco: Mapped[Optional[int]] = mapped_field(None)
    deb_automatico: Mapped[Optional[str]] = mapped_field('')
    deb_agencia: Mapped[Optional[str]] = mapped_field('')
    deb_conta: Mapped[Optional[str]] = mapped_field('')
    codigo_operacao: Mapped[Optional[str]] = mapped_field('')
    tipo_pessoa_titular_conta: Mapped[Optional[Tipo_pessoa_titular_contaEnum]] = mapped_field(Tipo_pessoa_titular_contaEnum.FISICA)
    cnpj_cpf_titular_conta: Mapped[Optional[str]] = mapped_field('')
    ultima_atualizacao: Mapped[Optional[str]] = mapped_field('')
    regua_cobranca_considera: Mapped[Optional[Regua_cobranca_consideraEnum]] = mapped_field(Regua_cobranca_consideraEnum.PADRAO)
    regua_cobranca_wpp: Mapped[Optional[Regua_cobranca_wppEnum]] = mapped_field(Regua_cobranca_wppEnum.SIM)
    regua_cobranca_notificacao: Mapped[Optional[Regua_cobranca_notificacaoEnum]] = mapped_field(Regua_cobranca_notificacaoEnum.SIM)
    fieldset_mensagem_atencao_regua: Mapped[Optional[str]] = mapped_field('')
    nome_pai: Mapped[Optional[str]] = mapped_field('')
    cpf_pai: Mapped[Optional[str]] = mapped_field('')
    identidade_pai: Mapped[Optional[str]] = mapped_field('')
    nascimento_pai: Mapped[Optional[str]] = mapped_field('')
    nome_mae: Mapped[Optional[str]] = mapped_field('')
    cpf_mae: Mapped[Optional[str]] = mapped_field('')
    identidade_mae: Mapped[Optional[str]] = mapped_field('')
    nascimento_mae: Mapped[Optional[str]] = mapped_field('')
    quantidade_dependentes: Mapped[Optional[str]] = mapped_field('')
    nome_conjuge: Mapped[Optional[str]] = mapped_field('')
    fone_conjuge: Mapped[Optional[str]] = mapped_field('')
    cpf_conjuge: Mapped[Optional[str]] = mapped_field('')
    rg_conjuge: Mapped[Optional[str]] = mapped_field('')
    data_nascimento_conjuge: Mapped[Optional[str]] = mapped_field('')
    nome_contador: Mapped[Optional[str]] = mapped_field('')
    telefone_contador: Mapped[Optional[str]] = mapped_field('')
    orgao_publico: Mapped[Optional[Orgao_publicoEnum]] = mapped_field(Orgao_publicoEnum.NAO)
    im: Mapped[Optional[str]] = mapped_field('')
    nome_representante_1: Mapped[Optional[str]] = mapped_field('')
    cpf_representante_1: Mapped[Optional[str]] = mapped_field('')
    identidade_representante_1: Mapped[Optional[str]] = mapped_field('')
    nome_representante_2: Mapped[Optional[str]] = mapped_field('')
    cpf_representante_2: Mapped[Optional[str]] = mapped_field('')
    identidade_representante_2: Mapped[Optional[str]] = mapped_field('')
    emp_empresa: Mapped[Optional[str]] = mapped_field('')
    emp_cnpj: Mapped[Optional[str]] = mapped_field('')
    emp_cep: Mapped[Optional[str]] = mapped_field('')
    emp_endereco: Mapped[Optional[str]] = mapped_field('')
    emp_cidade: Mapped[Optional[str]] = mapped_field('')
    emp_fone: Mapped[Optional[str]] = mapped_field('')
    emp_cargo: Mapped[Optional[str]] = mapped_field('')
    emp_remuneracao: Mapped[Optional[str]] = mapped_field('')
    emp_data_admissao: Mapped[Optional[str]] = mapped_field('')
    iss_classificacao_padrao: Mapped[Iss_classificacao_padraoEnum] = mapped_field(Iss_classificacao_padraoEnum.PADRAO)
    pis_retem: Mapped[Optional[str]] = mapped_field('')
    cofins_retem: Mapped[Optional[str]] = mapped_field('')
    csll_retem: Mapped[Optional[str]] = mapped_field('')
    irrf_retem: Mapped[Optional[str]] = mapped_field('')
    desconto_irrf_valor_inferior: Mapped[Optional[Desconto_irrf_valor_inferiorEnum]] = mapped_field(Desconto_irrf_valor_inferiorEnum.NAO)
    inss_retem: Mapped[Optional[str]] = mapped_field('')
    cli_desconta_iss_retido_total: Mapped[Optional[str]] = mapped_field('')
    percentual_reducao: Mapped[Optional[str]] = mapped_field('')
    ref_com_empresa1: Mapped[Optional[str]] = mapped_field('')
    ref_com_fone1: Mapped[Optional[str]] = mapped_field('')
    ref_com_empresa2: Mapped[Optional[str]] = mapped_field('')
    ref_com_fone2: Mapped[Optional[str]] = mapped_field('')
    ref_pes_nome1: Mapped[Optional[str]] = mapped_field('')
    ref_pes_fone1: Mapped[Optional[str]] = mapped_field('')
    ref_pes_nome2: Mapped[Optional[str]] = mapped_field('')
    ref_pes_fone2: Mapped[Optional[str]] = mapped_field('')
    obs: Mapped[Optional[str]] = mapped_field('')
    alerta: Mapped[Optional[str]] = mapped_field('')

    @property
    def table(self) -> str:
        return "cliente"
    
    def _serialize_enum(self, value) -> str:
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

        data =  {
            'id': str(self.id),
            'razao': self.razao if self.razao is not None else '',
            'endereco': self.endereco if self.endereco is not None else '',
            'numero': self.numero if self.numero is not None else '',
            'bairro': self.bairro if self.bairro is not None else '',
            'cidade': str(self.cidade) if self.cidade is not None else '',
            'dica_imposto_retido_cliente': self.dica_imposto_retido_cliente if self.dica_imposto_retido_cliente is not None else '',
            'ativo': self._serialize_enum(self.ativo),
            'id_tipo_cliente': str(self.id_tipo_cliente) if self.id_tipo_cliente is not None else '',
            'tipo_cliente_scm': self._serialize_enum(self.tipo_cliente_scm),
            'tipo_ente_governamental': self._serialize_enum(self.tipo_ente_governamental),
            'pais': self.pais if self.pais is not None else '',
            'tipo_pessoa': self._serialize_enum(self.tipo_pessoa),
            'regime_fiscal_col': self._serialize_enum(self.regime_fiscal_col),
            'nome_social': self.nome_social if self.nome_social is not None else '',
            'fantasia': self.fantasia if self.fantasia is not None else '',
            'tipo_documento_identificacao': self._serialize_enum(self.tipo_documento_identificacao),
            'cnpj_cpf': self.cnpj_cpf if self.cnpj_cpf is not None else '',
            'ie_identidade': self.ie_identidade if self.ie_identidade is not None else '',
            'contribuinte_icms': self._serialize_enum(self.contribuinte_icms),
            'contribuinte_icms_alert': self.contribuinte_icms_alert if self.contribuinte_icms_alert is not None else '',
            'rg_orgao_emissor': self.rg_orgao_emissor if self.rg_orgao_emissor is not None else '',
            'nacionalidade': self.nacionalidade if self.nacionalidade is not None else '',
            'cidade_naturalidade': str(self.cidade_naturalidade) if self.cidade_naturalidade is not None else '',
            'estado_nascimento': str(self.estado_nascimento) if self.estado_nascimento is not None else '',
            'data_nascimento': self.data_nascimento if self.data_nascimento is not None else '',
            'Sexo': self._serialize_enum(self.Sexo),
            'profissao': self.profissao if self.profissao is not None else '',
            'estado_civil': self._serialize_enum(self.estado_civil),
            'inscricao_municipal': self.inscricao_municipal if self.inscricao_municipal is not None else '',
            'isuf': self.isuf if self.isuf is not None else '',
            'tipo_assinante': self._serialize_enum(self.tipo_assinante),
            'filial_id': str(self.filial_id) if self.filial_id is not None else '',
            'filtra_filial': self._serialize_enum(self.filtra_filial),
            'idx': self.idx if self.idx is not None else '',
            'data_cadastro': self.data_cadastro if self.data_cadastro is not None else '',
            'ativo_serasa': self._serialize_enum(self.ativo_serasa),
            'convert_cliente_forn': self._serialize_enum(self.convert_cliente_forn),
            'atualizar_cadastro_galaxPay': self.atualizar_cadastro_galaxPay if self.atualizar_cadastro_galaxPay is not None else '',
            'grau_satisfacao': self._serialize_enum(self.grau_satisfacao),
            'id_condominio': str(self.id_condominio) if self.id_condominio is not None else '',
            'bloco': self.bloco if self.bloco is not None else '',
            'apartamento': self.apartamento if self.apartamento is not None else '',
            'cep': self.cep if self.cep is not None else '',
            'cif': self.cif if self.cif is not None else '',
            'complemento': self.complemento if self.complemento is not None else '',
            'uf': str(self.uf) if self.uf is not None else '',
            'referencia': self.referencia if self.referencia is not None else '',
            'moradia': self._serialize_enum(self.moradia),
            'tipo_localidade': self._serialize_enum(self.tipo_localidade),
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
            'acesso_automatico_central': self._serialize_enum(self.acesso_automatico_central),
            'alterar_senha_primeiro_acesso': self._serialize_enum(self.alterar_senha_primeiro_acesso),
            'senha_hotsite_md5': self._serialize_enum(self.senha_hotsite_md5),
            'hotsite_acesso': self.hotsite_acesso if self.hotsite_acesso is not None else '',
            'crm': self._serialize_enum(self.crm),
            'id_segmento': str(self.id_segmento) if self.id_segmento is not None else '',
            'id_candato_tipo': str(self.id_candato_tipo) if self.id_candato_tipo is not None else '',
            'id_campanha': str(self.id_campanha) if self.id_campanha is not None else '',
            'id_concorrente': str(self.id_concorrente) if self.id_concorrente is not None else '',
            'id_perfil': str(self.id_perfil) if self.id_perfil is not None else '',
            'responsavel': str(self.responsavel) if self.responsavel is not None else '',
            'indicado_por': str(self.indicado_por) if self.indicado_por is not None else '',
            'cadastrado_via_viabilidade': self._serialize_enum(self.cadastrado_via_viabilidade),
            'status_prospeccao': self._serialize_enum(self.status_prospeccao),
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
            'participa_pre_cobranca': self._serialize_enum(self.participa_pre_cobranca),
            'cob_envia_email': self._serialize_enum(self.cob_envia_email),
            'cob_envia_sms': self._serialize_enum(self.cob_envia_sms),
            'fieldset_mensagem_atencao_regua_crm': self.fieldset_mensagem_atencao_regua_crm if self.fieldset_mensagem_atencao_regua_crm is not None else '',
            'id_conta': str(self.id_conta) if self.id_conta is not None else '',
            'cond_pagamento': str(self.cond_pagamento) if self.cond_pagamento is not None else '',
            'id_vendedor': str(self.id_vendedor) if self.id_vendedor is not None else '',
            'tabela_preco': str(self.tabela_preco) if self.tabela_preco is not None else '',
            'deb_automatico': self.deb_automatico if self.deb_automatico is not None else '',
            'deb_agencia': self.deb_agencia if self.deb_agencia is not None else '',
            'deb_conta': self.deb_conta if self.deb_conta is not None else '',
            'codigo_operacao': self.codigo_operacao if self.codigo_operacao is not None else '',
            'tipo_pessoa_titular_conta': self._serialize_enum(self.tipo_pessoa_titular_conta),
            'cnpj_cpf_titular_conta': self.cnpj_cpf_titular_conta if self.cnpj_cpf_titular_conta is not None else '',
            'ultima_atualizacao': self.ultima_atualizacao if self.ultima_atualizacao is not None else '',
            'regua_cobranca_considera': self._serialize_enum(self.regua_cobranca_considera),
            'regua_cobranca_wpp': self._serialize_enum(self.regua_cobranca_wpp),
            'regua_cobranca_notificacao': self._serialize_enum(self.regua_cobranca_notificacao),
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
            'orgao_publico': self._serialize_enum(self.orgao_publico),
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
            'iss_classificacao_padrao': self._serialize_enum(self.iss_classificacao_padrao),
            'pis_retem': self.pis_retem if self.pis_retem is not None else '',
            'cofins_retem': self.cofins_retem if self.cofins_retem is not None else '',
            'csll_retem': self.csll_retem if self.csll_retem is not None else '',
            'irrf_retem': self.irrf_retem if self.irrf_retem is not None else '',
            'desconto_irrf_valor_inferior': self._serialize_enum(self.desconto_irrf_valor_inferior),
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
        return {key: serialize(value) for key, value in data.items()}


    def is_valid(self) -> bool:
        return self.id is not None and self.razao is not None and self.endereco is not None and self.numero is not None and self.bairro is not None and self.cidade is not None and self.dica_imposto_retido_cliente is not None


