"""Modelos de dados para ORM IXC."""

from .tableModels.assuntoModel import AssuntoModel
from .tableModels.atendimentoModel import AtendimentoModel
from .tableModels.caixaDeAtendimentoModel import CaixaDeAtendimentoModel
from .tableModels.carteiraDeCobrancaModel import CarteiraDeCobrancaModel
from .tableModels.cidadeModel import CidadeModel
from .tableModels.clienteFibraModel import ClienteFibraModel
from .tableModels.clienteModel import ClientModel
from .tableModels.colaboradoresModel import ColaboradoresModel
from .tableModels.contasAReceber import ContasAReceberModel
from .tableModels.contratoDoClienteModel import ContratoDoClienteModel
from .tableModels.defaultModel import DefaultPayload, BaseModel
from .tableModels.grupoDeUsuariosModel import GrupoDeUsuariosModel
from .tableModels.loginModel import LoginModel
from .tableModels.movimentoDeProdutosModel import MovimentoDeProdutosModel
from .tableModels.patrimonioModel import PatrimonioModel
from .tableModels.planoDeVendaModel import PlanoDeVendaModel
from .tableModels.planosPorContratoModel import PlanosPorContratoModel
from .tableModels.produtosModel import ProdutosModel
from .tableModels.rastreadoresDeVeiculosModel import RastreadoresDeVeIculosModel
from .tableModels.serviceOrderModel import ServiceOrderModel
from .tableModels.tipoDeCobrancaDoContratoModel import TipoDeCobrancaDoContratoModel
from .tableModels.tipoDocumentoModel import TipoDocumentoModel
from .tableModels.transmissorModel import TransmissorModel
from .tableModels.usuariosModel import UsuariosModel
from .tableModels.veiculosModel import VeiculosModel
from .tableModels.vendedorModel import VendedorModel

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
