from __future__ import annotations
from typing import Optional
from ORM_IXC.interfaces import IModelWithId
from ORM_IXC.enums.colaboradores import *
from ORM_IXC.statemants.maps.mapper import Mapped, field as mapped_field
from ORM_IXC.statemants.maps.metaManager import MetaModels
from ORM_IXC.models.tableModels.defaultModel import BaseModel


@MetaModels
class ColaboradoresModel(IModelWithId, BaseModel):
    funcionario :Mapped[str] = mapped_field('')
    filial_id :Mapped[int] = mapped_field('')
    cidade :Mapped[int] = mapped_field('')
    id_conta :Mapped[int] = mapped_field('')
    envia_email_os :Mapped[Envia_email_osEnum] = mapped_field('')
    envia_sms_os :Mapped[Envia_sms_osEnum] = mapped_field('')
    ferias_colaborador :Mapped[str] = mapped_field('')
    id :Mapped[Optional[int]] = mapped_field('')
    ativo :Mapped[Optional[AtivoEnum]] = mapped_field(None)
    data_admissao :Mapped[Optional[str]] = mapped_field('')
    data_demissao :Mapped[Optional[str]] = mapped_field('')
    data_nascimento :Mapped[Optional[str]] = mapped_field('')
    id_funcao :Mapped[Optional[int]] = mapped_field(None)
    id_departamento :Mapped[Optional[int]] = mapped_field(None)
    usuario_id :Mapped[Optional[int]] = mapped_field(None)
    id_conta_old :Mapped[Optional[str]] = mapped_field('')
    id_conta_decimo_old :Mapped[Optional[str]] = mapped_field('')
    percen_max_desc_areceber :Mapped[Optional[str]] = mapped_field('')
    obs :Mapped[Optional[str]] = mapped_field('')
    ctps_seleciona :Mapped[Optional[Ctps_selecionaEnum]] = mapped_field(None)
    ctps_numero :Mapped[Optional[str]] = mapped_field('')
    ctps_serie :Mapped[Optional[str]] = mapped_field('')
    ctps_data_emissao :Mapped[Optional[str]] = mapped_field('')
    ctps_cidade_emissao :Mapped[Optional[int]] = mapped_field(None)
    cpf_seleciona :Mapped[Optional[Cpf_selecionaEnum]] = mapped_field(None)
    cpf_cnpj :Mapped[Optional[str]] = mapped_field('')
    tipo_documento_identificacao_col :Mapped[Optional[Tipo_documento_identificacao_colEnum]] = mapped_field(None)
    pis_seleciona :Mapped[Optional[Pis_selecionaEnum]] = mapped_field(None)
    pis_numero :Mapped[Optional[str]] = mapped_field('')
    pis_data :Mapped[Optional[str]] = mapped_field('')
    rg_seleciona :Mapped[Optional[Rg_selecionaEnum]] = mapped_field(None)
    ie_identidade :Mapped[Optional[str]] = mapped_field('')
    rg_orgao_emissor :Mapped[Optional[str]] = mapped_field('')
    rg_data_emissao :Mapped[Optional[str]] = mapped_field('')
    nacionalidade :Mapped[Optional[str]] = mapped_field('')
    cnh_seleciona :Mapped[Optional[Cnh_selecionaEnum]] = mapped_field(None)
    cnh_numero :Mapped[Optional[str]] = mapped_field('')
    cnh_categoria :Mapped[Optional[str]] = mapped_field('')
    cnh_vencimento :Mapped[Optional[str]] = mapped_field('')
    titulo_eleitoral_seleciona :Mapped[Optional[Titulo_eleitoral_selecionaEnum]] = mapped_field(None)
    titulo_numero :Mapped[Optional[str]] = mapped_field('')
    titulo_zona :Mapped[Optional[str]] = mapped_field('')
    titulo_secao :Mapped[Optional[str]] = mapped_field('')
    ramal :Mapped[Optional[int]] = mapped_field(None)
    coeficiente :Mapped[Optional[str]] = mapped_field('')
    mostrar_no_quadro_kanban :Mapped[Optional[Mostrar_no_quadro_kanbanEnum]] = mapped_field(None)
    exibir_colaborador_inmap :Mapped[Optional[Exibir_colaborador_inmapEnum]] = mapped_field(None)
    cor_mapa :Mapped[Optional[str]] = mapped_field('')
    rastreador_tipo :Mapped[Optional[Rastreador_tipoEnum]] = mapped_field(None)
    rastreador :Mapped[Optional[str]] = mapped_field('')
    id_veiculo_padrao :Mapped[Optional[int]] = mapped_field(None)
    obrigar_marcar_quilometragem :Mapped[Optional[Obrigar_marcar_quilometragemEnum]] = mapped_field(None)
    ultima_atualizacao :Mapped[Optional[str]] = mapped_field('')
    cep :Mapped[Optional[str]] = mapped_field('')
    endereco :Mapped[Optional[str]] = mapped_field('')
    numero :Mapped[Optional[str]] = mapped_field('')
    bairro :Mapped[Optional[str]] = mapped_field('')
    complemento :Mapped[Optional[str]] = mapped_field('')
    uf :Mapped[Optional[str]] = mapped_field('')
    referencia :Mapped[Optional[str]] = mapped_field('')
    estado_civil :Mapped[Optional[Estado_civilEnum]] = mapped_field(None)
    nome_pai :Mapped[Optional[str]] = mapped_field('')
    nome_mae :Mapped[Optional[str]] = mapped_field('')
    nome_conjuge :Mapped[Optional[str]] = mapped_field('')
    cpf_conjuge :Mapped[Optional[str]] = mapped_field('')
    rg_conjuge :Mapped[Optional[str]] = mapped_field('')
    dependentes_ir :Mapped[Optional[str]] = mapped_field('')
    num_dependentes :Mapped[Optional[str]] = mapped_field('')
    dep_um_nome :Mapped[Optional[str]] = mapped_field('')
    dep_um_rg :Mapped[Optional[str]] = mapped_field('')
    dep_um_cpf :Mapped[Optional[str]] = mapped_field('')
    dep_dois_nome :Mapped[Optional[str]] = mapped_field('')
    dep_dois_rg :Mapped[Optional[str]] = mapped_field('')
    dep_dois_cpf :Mapped[Optional[str]] = mapped_field('')
    dep_tres_nome :Mapped[Optional[str]] = mapped_field('')
    dep_tres_rg :Mapped[Optional[str]] = mapped_field('')
    dep_tres_cpf :Mapped[Optional[str]] = mapped_field('')
    cor_raca :Mapped[Optional[Cor_racaEnum]] = mapped_field(None)
    num_manequim :Mapped[Optional[str]] = mapped_field('')
    camiseta :Mapped[Optional[CamisetaEnum]] = mapped_field(None)
    possui_deficiencia :Mapped[Optional[Possui_deficienciaEnum]] = mapped_field(None)
    tipo_deficiencia :Mapped[Optional[Tipo_deficienciaEnum]] = mapped_field(None)
    grau_escolaridade :Mapped[Optional[Grau_escolaridadeEnum]] = mapped_field(None)
    estagio_escolaridade :Mapped[Optional[Estagio_escolaridadeEnum]] = mapped_field(None)
    periodo_escolaridade :Mapped[Optional[Periodo_escolaridadeEnum]] = mapped_field(None)
    fone :Mapped[Optional[str]] = mapped_field('')
    fone_celular :Mapped[Optional[str]] = mapped_field('')
    fone_emergencia :Mapped[Optional[str]] = mapped_field('')
    falar_com :Mapped[Optional[str]] = mapped_field('')
    telefone_comercial :Mapped[Optional[str]] = mapped_field('')
    email :Mapped[Optional[str]] = mapped_field('')
    id_email_smtp :Mapped[Optional[int]] = mapped_field(None)
    assinatura_email :Mapped[Optional[str]] = mapped_field('')
    salario :Mapped[Optional[str]] = mapped_field('')
    id_conta_salario :Mapped[Optional[int]] = mapped_field(None)
    cod_integracao_folha :Mapped[Optional[str]] = mapped_field('')
    banco :Mapped[Optional[str]] = mapped_field('')
    agencia :Mapped[Optional[str]] = mapped_field('')
    agencia_dv :Mapped[Optional[str]] = mapped_field('')
    conta :Mapped[Optional[str]] = mapped_field('')
    numero_conta_dv :Mapped[Optional[str]] = mapped_field('')
    tipo_chave_pix :Mapped[Optional[Tipo_chave_pixEnum]] = mapped_field(None)
    chave_pix :Mapped[Optional[str]] = mapped_field('')
    tipo_recebimento :Mapped[Optional[Tipo_recebimentoEnum]] = mapped_field(None)
    camara_centralizadora :Mapped[Optional[Camara_centralizadoraEnum]] = mapped_field(None)
    id_conta_decimo :Mapped[Optional[int]] = mapped_field(None)
    regra_centro_rateio :Mapped[Optional[Regra_centro_rateioEnum]] = mapped_field(None)
    id_centro_custo_categoria_filtro :Mapped[Optional[int]] = mapped_field(None)
    id_centro_custo_criterio_rateio :Mapped[Optional[int]] = mapped_field(None)
    id_centro_custo_rel_centro_custo_categoria :Mapped[Optional[int]] = mapped_field(None)
    integracao_calendario :Mapped[Optional[Integracao_calendarioEnum]] = mapped_field(None)
    envia_telegram_os :Mapped[Optional[str]] = mapped_field('')
    telegram_chat_id_funcionario :Mapped[Optional[str]] = mapped_field('')
    id_chat_telegram_funcionario :Mapped[Optional[str]] = mapped_field('')
    id_setor_padrao :Mapped[Optional[int]] = mapped_field(None)
    img_assinatura :Mapped[Optional[str]] = mapped_field(None)
    dica_formato_arquivo :Mapped[Optional[str]] = mapped_field('')
    id_perfil_jornada_trabalho :Mapped[Optional[int]] = mapped_field(None)
    maximo_os_dia :Mapped[Optional[str]] = mapped_field('')
    prj_custo_hora_base :Mapped[Optional[str]] = mapped_field('')
    prj_custo_hora_adicionais :Mapped[Optional[str]] = mapped_field('')

    @property
    def table(self) -> str:
        return "funcionarios"

    def _serialize_enum_and_str(self, value) -> str:
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

        data = {
            'funcionario': self._serialize_enum_and_str(self.funcionario) if self.funcionario is not None else '',
            'filial_id': str(self.filial_id) if self.filial_id is not None else '',
            'cidade': str(self.cidade) if self.cidade is not None else '',
            'id_conta': str(self.id_conta) if self.id_conta is not None else '',
            'envia_email_os': self._serialize_enum_and_str(self.envia_email_os) if self.envia_email_os is not None else '',
            'envia_sms_os': self._serialize_enum_and_str(self.envia_sms_os) if self.envia_sms_os is not None else '',
            'ferias_colaborador': self._serialize_enum_and_str(self.ferias_colaborador) if self.ferias_colaborador is not None else '',
            'id': str(self.id) if self.id is not None else '',
            'ativo': self._serialize_enum_and_str(self.ativo) if self.ativo is not None else '',
            'data_admissao': self._serialize_enum_and_str(self.data_admissao) if self.data_admissao is not None else '',
            'data_demissao': self._serialize_enum_and_str(self.data_demissao) if self.data_demissao is not None else '',
            'data_nascimento': self._serialize_enum_and_str(self.data_nascimento) if self.data_nascimento is not None else '',
            'id_funcao': str(self.id_funcao) if self.id_funcao is not None else '',
            'id_departamento': str(self.id_departamento) if self.id_departamento is not None else '',
            'usuario_id': str(self.usuario_id) if self.usuario_id is not None else '',
            'id_conta_old': self._serialize_enum_and_str(self.id_conta_old) if self.id_conta_old is not None else '',
            'id_conta_decimo_old': self._serialize_enum_and_str(self.id_conta_decimo_old) if self.id_conta_decimo_old is not None else '',
            'percen_max_desc_areceber': self._serialize_enum_and_str(self.percen_max_desc_areceber) if self.percen_max_desc_areceber is not None else '',
            'obs': self._serialize_enum_and_str(self.obs) if self.obs is not None else '',
            'ctps_seleciona': self._serialize_enum_and_str(self.ctps_seleciona) if self.ctps_seleciona is not None else '',
            'ctps_numero': self._serialize_enum_and_str(self.ctps_numero) if self.ctps_numero is not None else '',
            'ctps_serie': self._serialize_enum_and_str(self.ctps_serie) if self.ctps_serie is not None else '',
            'ctps_data_emissao': self._serialize_enum_and_str(self.ctps_data_emissao) if self.ctps_data_emissao is not None else '',
            'ctps_cidade_emissao': str(self.ctps_cidade_emissao) if self.ctps_cidade_emissao is not None else '',
            'cpf_seleciona': self._serialize_enum_and_str(self.cpf_seleciona) if self.cpf_seleciona is not None else '',
            'cpf_cnpj': self._serialize_enum_and_str(self.cpf_cnpj) if self.cpf_cnpj is not None else '',
            'tipo_documento_identificacao_col': self._serialize_enum_and_str(self.tipo_documento_identificacao_col) if self.tipo_documento_identificacao_col is not None else '',
            'pis_seleciona': self._serialize_enum_and_str(self.pis_seleciona) if self.pis_seleciona is not None else '',
            'pis_numero': self._serialize_enum_and_str(self.pis_numero) if self.pis_numero is not None else '',
            'pis_data': self._serialize_enum_and_str(self.pis_data) if self.pis_data is not None else '',
            'rg_seleciona': self._serialize_enum_and_str(self.rg_seleciona) if self.rg_seleciona is not None else '',
            'ie_identidade': self._serialize_enum_and_str(self.ie_identidade) if self.ie_identidade is not None else '',
            'rg_orgao_emissor': self._serialize_enum_and_str(self.rg_orgao_emissor) if self.rg_orgao_emissor is not None else '',
            'rg_data_emissao': self._serialize_enum_and_str(self.rg_data_emissao) if self.rg_data_emissao is not None else '',
            'nacionalidade': self._serialize_enum_and_str(self.nacionalidade) if self.nacionalidade is not None else '',
            'cnh_seleciona': self._serialize_enum_and_str(self.cnh_seleciona) if self.cnh_seleciona is not None else '',
            'cnh_numero': self._serialize_enum_and_str(self.cnh_numero) if self.cnh_numero is not None else '',
            'cnh_categoria': self._serialize_enum_and_str(self.cnh_categoria) if self.cnh_categoria is not None else '',
            'cnh_vencimento': self._serialize_enum_and_str(self.cnh_vencimento) if self.cnh_vencimento is not None else '',
            'titulo_eleitoral_seleciona': self._serialize_enum_and_str(self.titulo_eleitoral_seleciona) if self.titulo_eleitoral_seleciona is not None else '',
            'titulo_numero': self._serialize_enum_and_str(self.titulo_numero) if self.titulo_numero is not None else '',
            'titulo_zona': self._serialize_enum_and_str(self.titulo_zona) if self.titulo_zona is not None else '',
            'titulo_secao': self._serialize_enum_and_str(self.titulo_secao) if self.titulo_secao is not None else '',
            'ramal': str(self.ramal) if self.ramal is not None else '',
            'coeficiente': self._serialize_enum_and_str(self.coeficiente) if self.coeficiente is not None else '',
            'mostrar_no_quadro_kanban': self._serialize_enum_and_str(self.mostrar_no_quadro_kanban) if self.mostrar_no_quadro_kanban is not None else '',
            'exibir_colaborador_inmap': self._serialize_enum_and_str(self.exibir_colaborador_inmap) if self.exibir_colaborador_inmap is not None else '',
            'cor_mapa': self._serialize_enum_and_str(self.cor_mapa) if self.cor_mapa is not None else '',
            'rastreador_tipo': self._serialize_enum_and_str(self.rastreador_tipo) if self.rastreador_tipo is not None else '',
            'rastreador': self._serialize_enum_and_str(self.rastreador) if self.rastreador is not None else '',
            'id_veiculo_padrao': str(self.id_veiculo_padrao) if self.id_veiculo_padrao is not None else '',
            'obrigar_marcar_quilometragem': self._serialize_enum_and_str(self.obrigar_marcar_quilometragem) if self.obrigar_marcar_quilometragem is not None else '',
            'ultima_atualizacao': self._serialize_enum_and_str(self.ultima_atualizacao) if self.ultima_atualizacao is not None else '',
            'cep': self._serialize_enum_and_str(self.cep) if self.cep is not None else '',
            'endereco': self._serialize_enum_and_str(self.endereco) if self.endereco is not None else '',
            'numero': self._serialize_enum_and_str(self.numero) if self.numero is not None else '',
            'bairro': self._serialize_enum_and_str(self.bairro) if self.bairro is not None else '',
            'complemento': self._serialize_enum_and_str(self.complemento) if self.complemento is not None else '',
            'uf': self._serialize_enum_and_str(self.uf) if self.uf is not None else '',
            'referencia': self._serialize_enum_and_str(self.referencia) if self.referencia is not None else '',
            'estado_civil': self._serialize_enum_and_str(self.estado_civil) if self.estado_civil is not None else '',
            'nome_pai': self._serialize_enum_and_str(self.nome_pai) if self.nome_pai is not None else '',
            'nome_mae': self._serialize_enum_and_str(self.nome_mae) if self.nome_mae is not None else '',
            'nome_conjuge': self._serialize_enum_and_str(self.nome_conjuge) if self.nome_conjuge is not None else '',
            'cpf_conjuge': self._serialize_enum_and_str(self.cpf_conjuge) if self.cpf_conjuge is not None else '',
            'rg_conjuge': self._serialize_enum_and_str(self.rg_conjuge) if self.rg_conjuge is not None else '',
            'dependentes_ir': self._serialize_enum_and_str(self.dependentes_ir) if self.dependentes_ir is not None else '',
            'num_dependentes': self._serialize_enum_and_str(self.num_dependentes) if self.num_dependentes is not None else '',
            'dep_um_nome': self._serialize_enum_and_str(self.dep_um_nome) if self.dep_um_nome is not None else '',
            'dep_um_rg': self._serialize_enum_and_str(self.dep_um_rg) if self.dep_um_rg is not None else '',
            'dep_um_cpf': self._serialize_enum_and_str(self.dep_um_cpf) if self.dep_um_cpf is not None else '',
            'dep_dois_nome': self._serialize_enum_and_str(self.dep_dois_nome) if self.dep_dois_nome is not None else '',
            'dep_dois_rg': self._serialize_enum_and_str(self.dep_dois_rg) if self.dep_dois_rg is not None else '',
            'dep_dois_cpf': self._serialize_enum_and_str(self.dep_dois_cpf) if self.dep_dois_cpf is not None else '',
            'dep_tres_nome': self._serialize_enum_and_str(self.dep_tres_nome) if self.dep_tres_nome is not None else '',
            'dep_tres_rg': self._serialize_enum_and_str(self.dep_tres_rg) if self.dep_tres_rg is not None else '',
            'dep_tres_cpf': self._serialize_enum_and_str(self.dep_tres_cpf) if self.dep_tres_cpf is not None else '',
            'cor_raca': self._serialize_enum_and_str(self.cor_raca) if self.cor_raca is not None else '',
            'num_manequim': self._serialize_enum_and_str(self.num_manequim) if self.num_manequim is not None else '',
            'camiseta': self._serialize_enum_and_str(self.camiseta) if self.camiseta is not None else '',
            'possui_deficiencia': self._serialize_enum_and_str(self.possui_deficiencia) if self.possui_deficiencia is not None else '',
            'tipo_deficiencia': self._serialize_enum_and_str(self.tipo_deficiencia) if self.tipo_deficiencia is not None else '',
            'grau_escolaridade': self._serialize_enum_and_str(self.grau_escolaridade) if self.grau_escolaridade is not None else '',
            'estagio_escolaridade': self._serialize_enum_and_str(self.estagio_escolaridade) if self.estagio_escolaridade is not None else '',
            'periodo_escolaridade': self._serialize_enum_and_str(self.periodo_escolaridade) if self.periodo_escolaridade is not None else '',
            'fone': self._serialize_enum_and_str(self.fone) if self.fone is not None else '',
            'fone_celular': self._serialize_enum_and_str(self.fone_celular) if self.fone_celular is not None else '',
            'fone_emergencia': self._serialize_enum_and_str(self.fone_emergencia) if self.fone_emergencia is not None else '',
            'falar_com': self._serialize_enum_and_str(self.falar_com) if self.falar_com is not None else '',
            'telefone_comercial': self._serialize_enum_and_str(self.telefone_comercial) if self.telefone_comercial is not None else '',
            'email': self._serialize_enum_and_str(self.email) if self.email is not None else '',
            'id_email_smtp': str(self.id_email_smtp) if self.id_email_smtp is not None else '',
            'assinatura_email': self._serialize_enum_and_str(self.assinatura_email) if self.assinatura_email is not None else '',
            'salario': self._serialize_enum_and_str(self.salario) if self.salario is not None else '',
            'id_conta_salario': str(self.id_conta_salario) if self.id_conta_salario is not None else '',
            'cod_integracao_folha': self._serialize_enum_and_str(self.cod_integracao_folha) if self.cod_integracao_folha is not None else '',
            'banco': self._serialize_enum_and_str(self.banco) if self.banco is not None else '',
            'agencia': self._serialize_enum_and_str(self.agencia) if self.agencia is not None else '',
            'agencia_dv': self._serialize_enum_and_str(self.agencia_dv) if self.agencia_dv is not None else '',
            'conta': self._serialize_enum_and_str(self.conta) if self.conta is not None else '',
            'numero_conta_dv': self._serialize_enum_and_str(self.numero_conta_dv) if self.numero_conta_dv is not None else '',
            'tipo_chave_pix': self._serialize_enum_and_str(self.tipo_chave_pix) if self.tipo_chave_pix is not None else '',
            'chave_pix': self._serialize_enum_and_str(self.chave_pix) if self.chave_pix is not None else '',
            'tipo_recebimento': self._serialize_enum_and_str(self.tipo_recebimento) if self.tipo_recebimento is not None else '',
            'camara_centralizadora': self._serialize_enum_and_str(self.camara_centralizadora) if self.camara_centralizadora is not None else '',
            'id_conta_decimo': str(self.id_conta_decimo) if self.id_conta_decimo is not None else '',
            'regra_centro_rateio': self._serialize_enum_and_str(self.regra_centro_rateio) if self.regra_centro_rateio is not None else '',
            'id_centro_custo_categoria_filtro': str(self.id_centro_custo_categoria_filtro) if self.id_centro_custo_categoria_filtro is not None else '',
            'id_centro_custo_criterio_rateio': str(self.id_centro_custo_criterio_rateio) if self.id_centro_custo_criterio_rateio is not None else '',
            'id_centro_custo_rel_centro_custo_categoria': str(self.id_centro_custo_rel_centro_custo_categoria) if self.id_centro_custo_rel_centro_custo_categoria is not None else '',
            'integracao_calendario': self._serialize_enum_and_str(self.integracao_calendario) if self.integracao_calendario is not None else '',
            'envia_telegram_os': self._serialize_enum_and_str(self.envia_telegram_os) if self.envia_telegram_os is not None else '',
            'telegram_chat_id_funcionario': self._serialize_enum_and_str(self.telegram_chat_id_funcionario) if self.telegram_chat_id_funcionario is not None else '',
            'id_chat_telegram_funcionario': self._serialize_enum_and_str(self.id_chat_telegram_funcionario) if self.id_chat_telegram_funcionario is not None else '',
            'id_setor_padrao': str(self.id_setor_padrao) if self.id_setor_padrao is not None else '',
            'img_assinatura': self._serialize_enum_and_str(self.img_assinatura) if self.img_assinatura is not None else '',
            'dica_formato_arquivo': self._serialize_enum_and_str(self.dica_formato_arquivo) if self.dica_formato_arquivo is not None else '',
            'id_perfil_jornada_trabalho': str(self.id_perfil_jornada_trabalho) if self.id_perfil_jornada_trabalho is not None else '',
            'maximo_os_dia': self._serialize_enum_and_str(self.maximo_os_dia) if self.maximo_os_dia is not None else '',
            'prj_custo_hora_base': self._serialize_enum_and_str(self.prj_custo_hora_base) if self.prj_custo_hora_base is not None else '',
            'prj_custo_hora_adicionais': self._serialize_enum_and_str(self.prj_custo_hora_adicionais) if self.prj_custo_hora_adicionais is not None else '',
        }
        return {key: serialize(value) for key, value in data.items()}

    def is_valid(self) -> bool:
        return self.funcionario is not None and self.filial_id is not None and self.cidade is not None and self.id_conta is not None and self.envia_email_os is not None and self.envia_sms_os is not None and self.ferias_colaborador is not None
