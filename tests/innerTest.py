from dotenv import load_dotenv
import os

from ORM_IXC.context.request import Manager
from ORM_IXC.context.contextModels.cliente import Cliente
from ORM_IXC.models.tableModels.clienteModel import ClientModel
from ORM_IXC.models.tableModels.loginModel import LoginModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule
from ORM_IXC.enums.operators import Operators
from ORM_IXC.statemants.CRUD.select import select

load_dotenv()

host = os.getenv("IXC_HOST")
token = os.getenv("IXC_TOKEN")

if not host or not token:
    raise EnvironmentError("Defina IXC_HOST e IXC_TOKEN no .env para executar este teste")

manager = Manager(host, token)
cliente_context = Cliente(manager)

# Pesquisa principal: todos os clientes ativos
main_search = SearchModule(
    searchField="id",
    query="0",
    oper=Operators.MORETHAN,
    context_model=cliente_context._get_context_model(),
    sortName="id",
)

# Inner independente: filtra registros do mesmo contexto usando ids do resultado principal
inner_search = SearchModule(
    searchField="id",
    query="0",
    oper=Operators.MORETHAN,
    context_model=cliente_context._get_context_model(),
    sortName="id",
)

query = select(cliente_context).where(ClientModel.id > 0).limit(20)

print("Executando main query...")
results = query.execute()
print(f"Registros principais retornados: {len(results)}")
print(f"Inner results sets: {len(query._inner_results)}")
for idx, inner_items in enumerate(query._inner_results, start=1):
    print(f" inner[{idx}] = {len(inner_items)} registros")

if results:
    print("Exemplo de primeiro registro principal:")
    print(results[0].to_dict() if hasattr(results[0], 'to_dict') else results[0])
