from dotenv import load_dotenv
import os

from ORM_IXC.context.contextModels.cliente import Cliente
from ORM_IXC.context.contextModels.contratoDoCliente import ContratoDoCliente
from ORM_IXC.context.request import Manager
from ORM_IXC.models.tableModels.clienteModel import ClientModel
from ORM_IXC.models.tableModels.contratoDoClienteModel import ContratoDoClienteModel
from ORM_IXC.statemants.CRUD.select import select
from ORM_IXC.utils.makejson import makeJson

def _contexts():
    load_dotenv()

    host = os.getenv("IXC_HOST")
    token = os.getenv("IXC_TOKEN")

    if not host or not token:
        raise EnvironmentError("Defina IXC_HOST e IXC_TOKEN no .env para executar este teste")

    manager = Manager(host, token)
    return Cliente(manager), ContratoDoCliente(manager)


def test_select_join_output_dict_with_alias():
    cliente, contrato = _contexts()

    rows = select(cliente)\
        .columns(
            ClientModel.id,
            ClientModel.razao,
            ContratoDoClienteModel.id,
            ContratoDoClienteModel.id_cliente,
            ContratoDoClienteModel.contrato,
        )\
        .where(ClientModel.id > 0)\
        .join(contrato, ClientModel.id == ContratoDoClienteModel.id_cliente)\
        .limit(5)\
        .execute()

    assert rows

    rows[0]._inners[0].set_alias("contrato")
    data = rows[0].output_dict()
    print(data)
    makeJson("flamengoooo", rows)
    
    assert "cliente.id" in data
    assert "cliente.razao" in data
    assert "contrato.id" in data
    assert "contrato.id_cliente" in data
    assert "contrato.contrato" in data


def test_select_join_output_dict_without_alias_uses_table_name():
    cliente, contrato = _contexts()

    rows = (
        select(cliente)
        .columns(
            ClientModel.id,
            ClientModel.razao,
            ContratoDoClienteModel.id,
            ContratoDoClienteModel.id_cliente,
        )
        .where(ClientModel.id > 0)
        .join(contrato, ClientModel.id == ContratoDoClienteModel.id_cliente)
        .limit(5)
        .execute()
    )

    assert rows

    data = rows[0].output_dict()

    assert "cliente.id" in data
    assert "cliente.razao" in data
    assert "cliente_contrato.id" in data
    assert "cliente_contrato.id_cliente" in data
test_select_join_output_dict_with_alias()