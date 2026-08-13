"""Modelos de tabela da ORM IXC."""

from .assuntoModel import AssuntoModel
from .atendimentoModel import AtendimentoModel
from .caixaDeAtendimentoModel import CaixaDeAtendimentoModel
from .carteiraDeCobrancaModel import CarteiraDeCobrancaModel
from .cidadeModel import CidadeModel
from .clienteFibraModel import ClienteFibraModel
from .clienteModel import ClientModel
from .colaboradoresModel import ColaboradoresModel
from .contasAReceber import ContasAReceberModel
from .contratoDoClienteModel import ContratoDoClienteModel
from .defaultModel import DefaultPayload, BaseModel
from .grupoDeUsuariosModel import GrupoDeUsuariosModel
from .loginModel import LoginModel
from .movimentoDeProdutosModel import MovimentoDeProdutosModel
from .patrimonioModel import PatrimonioModel
from .planoDeVendaModel import PlanoDeVendaModel
from .planosPorContratoModel import PlanosPorContratoModel
from .produtosModel import ProdutosModel
from .rastreadoresDeVeiculosModel import RastreadoresDeVeIculosModel
from .serviceOrderModel import ServiceOrderModel
from .tipoDeCobrancaDoContratoModel import TipoDeCobrancaDoContratoModel
from .tipoDocumentoModel import TipoDocumentoModel
from .transmissorModel import TransmissorModel
from .usuariosModel import UsuariosModel
from .veiculosModel import VeiculosModel
from .vendedorModel import VendedorModel

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
