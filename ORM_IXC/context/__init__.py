"""Pacote de contextos da ORM IXC."""

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
    "Setor",
    "TipoDeCobrancaDoContrato",
    "TipoDocumento",
    "Transmissor",
    "Usuarios",
    "Veiculos",
    "Vendedor",
]


def __getattr__(name):
    if name in {"AReceber", "Assunto", "Atendimento", "CaixaDeAtendimento", "CarteiraDeConbranca", "Cidade", "ClasseFinanceiraAnalitica", "Cliente", "Colaboradores", "ContaContabilSintetica", "ContratoDoCliente", "ClienteFibra", "GrupoDeUsuarios", "Login", "MovimentoDeProdutos", "Patrimonio", "PlanoDeVenda", "PlanosPorContrato", "Produtos", "Radacct", "RastreadoresDeVeIculos", "ServiceOrder", "Setor", "TipoDeCobrancaDoContrato", "TipoDocumento", "Transmissor", "Usuarios", "Veiculos", "Vendedor"}:
        module = import_module(".contextModels", __name__)
        return getattr(module, name)
    if name == "CarteiraCobranca":
        return __getattr__("CarteiraDeConbranca")
    if name == "Contrato":
        return __getattr__("ContratoDoCliente")
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")