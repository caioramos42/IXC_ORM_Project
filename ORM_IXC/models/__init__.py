"""Modelos de dados para ORM IXC."""

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
    "SetorModel",
    "TipoDeCobrancaDoContratoModel",
    "TipoDocumentoModel",
    "TransmissorModel",
    "UsuariosModel",
    "VeiculosModel",
    "VendedorModel",
]


def __getattr__(name):
    if name in {"AssuntoModel", "AtendimentoModel", "CaixaDeAtendimentoModel", "CarteiraDeCobrancaModel", "CidadeModel", "ClienteFibraModel", "ClientModel", "ColaboradoresModel", "ContasAReceberModel", "ContratoDoClienteModel", "DefaultPayload", "BaseModel", "GrupoDeUsuariosModel", "LoginModel", "MovimentoDeProdutosModel", "PatrimonioModel", "PlanoDeVendaModel", "PlanosPorContratoModel", "ProdutosModel", "RastreadoresDeVeIculosModel", "ServiceOrderModel", "SetorModel", "TipoDeCobrancaDoContratoModel", "TipoDocumentoModel", "TransmissorModel", "UsuariosModel", "VeiculosModel", "VendedorModel"}:
        module = import_module(".tableModels", __name__)
        return getattr(module, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
