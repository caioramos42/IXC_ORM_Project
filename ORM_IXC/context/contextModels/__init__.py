"""Contextos da ORM IXC."""

from importlib import import_module

__all__ = [
    "AReceber",
    "Assunto",
    "Atendimento",
    "CaixaDeAtendimento",
    "CarteiraDeConbranca",
    "CarteiraCobranca",
    "Cidade",
    "ClasseFinanceiraAnalitica",
    "Cliente",
    "Colaboradores",
    "ContaContabilSintetica",
    "Contrato",
    "ContratoDoCliente",
    "ClienteFibra",
    "GrupoDeUsuarios",
    "Login",
    "MovimentoDeProdutos",
    "Patrimonio",
    "PlanoDeVenda",
    "PlanosPorContrato",
    "Produtos",
    "Radacct",
    "RastreadoresDeVeIculos",
    "ServiceOrder",
    "TipoDeCobrancaDoContrato",
    "TipoDocumento",
    "Transmissor",
    "Usuarios",
    "Veiculos",
    "Vendedor",
]


def __getattr__(name):
    module_name = {
        "AReceber": ".areceber",
        "Assunto": ".assunto",
        "Atendimento": ".atendimento",
        "CaixaDeAtendimento": ".caixaDeAtendimento",
        "CarteiraDeConbranca": ".carteiraCobranca",
        "Cidade": ".cidade",
        "ClasseFinanceiraAnalitica": ".classeFinanceiraAnalitica",
        "Cliente": ".cliente",
        "Colaboradores": ".colaboradores",
        "ContaContabilSintetica": ".contabil",
        "ContratoDoCliente": ".contratoDoCliente",
        "ClienteFibra": ".fiberClient",
        "GrupoDeUsuarios": ".grupoDeUsuarios",
        "Login": ".login",
        "MovimentoDeProdutos": ".movimentoDeProdutos",
        "Patrimonio": ".patrimonio",
        "PlanoDeVenda": ".planoDeVenda",
        "PlanosPorContrato": ".planosPorContrato",
        "Produtos": ".produtos",
        "Radacct": ".radacct",
        "RastreadoresDeVeIculos": ".rastreadoresDeVeiculos",
        "ServiceOrder": ".serviceOrder",
        "TipoDeCobrancaDoContrato": ".tipoDeCobrancaDoContrato",
        "TipoDocumento": ".tipoDocumento",
        "Transmissor": ".transmissor",
        "Usuarios": ".usuarios",
        "Veiculos": ".veiculos",
        "Vendedor": ".vendedor",
    }.get(name)
    if module_name is not None:
        return getattr(import_module(module_name, __name__), name)
    if name == "CarteiraCobranca":
        return __getattr__("CarteiraDeConbranca")
    if name == "Contrato":
        return __getattr__("ContratoDoCliente")
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")