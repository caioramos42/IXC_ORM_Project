"""Modelos de tabela da ORM IXC."""

from importlib import import_module

__all__ = [
    "AssuntoModel",
    "AtendimentoModel",
    "CaixaDeAtendimentoModel",
    "CarteiraDeCobrancaModel",
    "CidadeModel",
    "ClienteFibraModel",
    "ClientModel",
    "ColaboradoresModel",
    "ContasAReceberModel",
    "ContratoDoClienteModel",
    "DefaultPayload",
    "BaseModel",
    "GrupoDeUsuariosModel",
    "LoginModel",
    "MovimentoDeProdutosModel",
    "PatrimonioModel",
    "PlanoDeVendaModel",
    "PlanosPorContratoModel",
    "ProdutosModel",
    "RastreadoresDeVeIculosModel",
    "ServiceOrderModel",
    "TipoDeCobrancaDoContratoModel",
    "TipoDocumentoModel",
    "TransmissorModel",
    "UsuariosModel",
    "VeiculosModel",
    "VendedorModel",
]


def __getattr__(name):
    module_name = {
        "AssuntoModel": ".assuntoModel",
        "AtendimentoModel": ".atendimentoModel",
        "CaixaDeAtendimentoModel": ".caixaDeAtendimentoModel",
        "CarteiraDeCobrancaModel": ".carteiraDeCobrancaModel",
        "CidadeModel": ".cidadeModel",
        "ClienteFibraModel": ".clienteFibraModel",
        "ClientModel": ".clienteModel",
        "ColaboradoresModel": ".colaboradoresModel",
        "ContasAReceberModel": ".contasAReceber",
        "ContratoDoClienteModel": ".contratoDoClienteModel",
        "DefaultPayload": ".defaultModel",
        "BaseModel": ".defaultModel",
        "GrupoDeUsuariosModel": ".grupoDeUsuariosModel",
        "LoginModel": ".loginModel",
        "MovimentoDeProdutosModel": ".movimentoDeProdutosModel",
        "PatrimonioModel": ".patrimonioModel",
        "PlanoDeVendaModel": ".planoDeVendaModel",
        "PlanosPorContratoModel": ".planosPorContratoModel",
        "ProdutosModel": ".produtosModel",
        "RastreadoresDeVeIculosModel": ".rastreadoresDeVeiculosModel",
        "ServiceOrderModel": ".serviceOrderModel",
        "TipoDeCobrancaDoContratoModel": ".tipoDeCobrancaDoContratoModel",
        "TipoDocumentoModel": ".tipoDocumentoModel",
        "TransmissorModel": ".transmissorModel",
        "UsuariosModel": ".usuariosModel",
        "VeiculosModel": ".veiculosModel",
        "VendedorModel": ".vendedorModel",
    }.get(name)
    if module_name is not None:
        module = import_module(module_name, __name__)
        return getattr(module, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
