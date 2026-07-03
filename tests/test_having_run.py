from ORM_IXC.statemants.CRUD.select import select
from ORM_IXC.statemants.sqlFunctions.count import count
from ORM_IXC.statemants.sqlFunctions.sum import sum as sql_sum
from ORM_IXC.statemants.sqlFunctions.avg import avg as sql_avg
from ORM_IXC.statemants.maps.classBase import Field
from ORM_IXC.models.searchUtils.searchModel import SearchModule
from ORM_IXC.context.request.manager import Manager
from ORM_IXC.context.contextModels.cliente import Cliente
from ORM_IXC.models.tableModels.clienteModel import ClientModel
from dotenv import load_dotenv
import os
from ORM_IXC.utils.makejson import makeJson

load_dotenv()

host = str(os.getenv("IXC_HOST"))
token = str(os.getenv("IXC_TOKEN"))

manager = Manager(host, token)
cliente = Cliente(manager)

print('\n=== HAVING: COUNT per `razao` with contador > 1 ===')
try:
    result = select(count(cliente, ClientModel.id, "contador"))\
        .where(ClientModel.id > 0)\
        .limit(500)\
        .groupby(ClientModel.razao)\
        .having(cliente.contador > 1)\
        .execute()
    for row in result:
        try:
            print('ROW:', row.output_dict() if hasattr(row, 'output_dict') else vars(row))
        except Exception:
            print('ROW RAW:', row)
    makeJson('test_having_count', result)
except Exception as e:
    print('Error executing count having test:', e)

print('\n=== HAVING: SUM of `cidade` per `razao` with soma_cidade > 100 ===')
try:
    result = select(sql_sum(cliente, ClientModel.cidade, "soma_cidade"))\
        .where(ClientModel.id > 0)\
        .limit(500)\
        .groupby(ClientModel.razao, ClientModel.cidade)\
        .having(cliente.soma_cidade > 100)\
        .execute()
    for row in result:
        try:
            print('ROW:', row.output_dict() if hasattr(row, 'output_dict') else vars(row))
        except Exception:
            print('ROW RAW:', row)
    makeJson('test_having_sum', result)
except Exception as e:
    print('Error executing sum having test:', e)

print('\n=== HAVING: AVG of `cidade` per `razao` with media_cidade >= 10 ===')
try:
    result = select(sql_avg(cliente, ClientModel.cidade, "media_cidade"))\
        .where(ClientModel.id > 0)\
        .limit(500)\
        .groupby(ClientModel.razao)\
        .having(cliente.media_cidade >= 10)\
        .execute()
    for row in result:
        try:
            print('ROW:', row.output_dict() if hasattr(row, 'output_dict') else vars(row))
        except Exception:
            print('ROW RAW:', row)
    makeJson('test_having_avg', result)
except Exception as e:
    print('Error executing avg having test:', e)

print('\n=== Finished having run tests (no asserts) ===')
