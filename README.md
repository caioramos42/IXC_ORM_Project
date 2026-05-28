# ORM_IXC

Uma ORM leve para facilitar interações com a API IXCSoft.

## Visão geral

`ORM_IXC` oferece uma camada de abstração para consumir os serviços REST da IXCSoft usando objetos Python e modelos de pesquisa.

Os principais recursos incluem:
- gerenciamento de requisições HTTP com autenticação básica
- classes de contexto para entidades comuns (cliente, contrato, atendimento, etc.)
- operações CRUD genéricas e buscas por filtro
- modelos de busca com parâmetros e ordenação

## Instalação

> Este projeto depende de `requests` para realizar chamadas HTTP.

```bash
pip install requests
pip install .
```

Se preferir instalar localmente no repositório:

```bash
python setup.py install
```
## Instalação
```bash
pip install git+https://github.com/caioramos42/IXC_ORM_Project.git
```
## Uso básico

### Inicializar o manager

```python
from ORM_IXC.context.request.manager import Manager

manager = Manager('Ip_servidor', 'chave_api')
```

### Criar um contexto de serviço

```python
from ORM_IXC.context.contextModels.serviceOrder import ServiceOrder

service_order = ServiceOrder(manager)
```

### Buscar por ID

```python
result = service_order.SearchById(308364)
print(result)
```

### Buscar todos os registros

```python
all_records = service_order.SelectAll()
for item in all_records:
    print(item)
```

### Buscar com filtros

```python
from ORM_IXC.models.searchUtils.searchModel import SearchModule
from ORM_IXC.models.searchUtils.gridParamModel import GridParam
from ORM_IXC.enums.operators import Operators

search = SearchModule(
    searchField='status',
    query='F',
    oper=Operators.EQUALS
)
search.appendGridParams(GridParam('id_cliente', Operators.EQUALS, '32099'))

results = service_order.getByFilter(search)
for item in results:
    print(item)
```

### Buscar com mais de um parâmetro e aplicar paginação

```python
search = SearchModule(
    searchField='status',
    query='F',
    oper=Operators.EQUALS
)
search.appendGridParams(GridParam('id_cliente', Operators.EQUALS, '32099'))
search.appendGridParams(GridParam('tipo', Operators.EQUALS, 'C'))
search.setPage(2)
search.setaAmount(50)

results = service_order.getByFilter(search)
print(f'Total encontrados: {len(results)}')
```

### Consumir resultados com cursor

```python
search = SearchModule(
    searchField='tipo',
    query='C',
    oper=Operators.EQUALS
)
for item in service_order.cursorByFilter(search, page_size=100):
    print(item)
```

### Procurar usando statements + execute (`newLoginTest`)
```python

from dotenv import load_dotenv
from ORM_IXC.context.contextModels.login import Login
from ORM_IXC.models.tableModels.loginModel import LoginModel
from ORM_IXC.statemants.select import select
from ORM_IXC.context.request import Manager
import os

from ORM_IXC.utils.makejson import makeJson

load_dotenv()

host = str(os.getenv("IXC_HOST"))
token = str(os.getenv("IXC_TOKEN"))

manager = Manager(host, token)
login = Login(manager)
query = select(login)\
            .where(LoginModel.id > 0,\
                LoginModel.tipo_conexao_mapa == 'F')\
            .limit(500)\
            .order_by("id")\
            .execute()
print([i.id for i in query])
makeJson("myJson", query)
```

### Procurar usando statements + cursor (`newContasAReceberTest`)
``` python
from dotenv import load_dotenv

from ORM_IXC.models.tableModels.contasAReceber import ContasAReceberModel
from ORM_IXC.models.searchUtils.searchModel import SearchModule
from ORM_IXC.context.contextModels.areceber import AReceber
from ORM_IXC.statemants.select import select
from ORM_IXC.context.request import Manager
import os

from ORM_IXC.utils.makejson import makeJsonStream

load_dotenv()

host = str(os.getenv("IXC_HOST"))
token = str(os.getenv("IXC_TOKEN"))

manager = Manager(host, token)
aReceber = AReceber(manager)
query = select(aReceber)\
                        .where(ContasAReceberModel.id > 0)\
                        .limit(300)\
                        .order_by("id")\
                        .cursor()

makeJsonStream("neymarJr", query)
```


### Procurar usando selectAll() (`newContasAReceberTest`)
``` python

from dotenv import load_dotenv

from ORM_IXC.models.tableModels.clienteModel import ClientModel
from ORM_IXC.context.contextModels.cliente import Cliente
from ORM_IXC.statemants.select import select
from ORM_IXC.context.request import Manager
import os

from ORM_IXC.utils.makejson import makeJsonStream

load_dotenv()

host = str(os.getenv("IXC_HOST"))
token = str(os.getenv("IXC_TOKEN"))

manager = Manager(host, token)
contabilSintetica = Cliente(manager)
query = select(contabilSintetica)\
                        .all()

makeJsonStream("neymarJr", query)


```

### Procurar usando selectAllAssync() (`newContasAReceberTest`)
``` python

from dotenv import load_dotenv

from ORM_IXC.models.tableModels.clienteModel import ClientModel
from ORM_IXC.context.contextModels.cliente import Cliente
from ORM_IXC.statemants.select import select
from ORM_IXC.context.request import Manager
import os

from ORM_IXC.utils.makejson import makeJsonStream

load_dotenv()

host = str(os.getenv("IXC_HOST"))
token = str(os.getenv("IXC_TOKEN"))

manager = Manager(host, token)
contabilSintetica = Cliente(manager)
query = select(contabilSintetica)\
                        .allAssync()

makeJsonStream("neymarJr", query)


```

### Inserir usando statements (`newCreateServiceOrderInsertTest.py`)

```python
from ORM_IXC.statemants.insert import insert
from ORM_IXC.models.tableModels.serviceOrderModel import ServiceOrderModel

response = insert(service_order).values(
    ServiceOrderModel(
        id=None,
        id_assunto=217,
        id_atendente='',
        id_cliente=32099,
        tipo='C',
        id_filial=1,
        origem_endereco='M',
        origem_endereco_estrutura='E',
        prioridade='N',
        melhor_horario_agenda='Q',
        setor=2,
        mensagem='Teste Api',
        status='A',
        status_assinatura='A',
        gera_comissao='S',
        liberado='1',
        impresso='N',
        origem_cadastro='P',
        origem_os_aberta='C',
        valor_unit_comissao='0,00',
        valor_total_comissao='0,00',
    )
).execute()

print(response[0].text)
```

### Atualizar usando statements (`newServiceOrderUpdateTest.py`)

```python
from ORM_IXC.statemants.update import update
from ORM_IXC.models.tableModels.serviceOrderModel import ServiceOrderModel

responses = update(service_order) \
    .where(ServiceOrderModel.id == 308364) \
    .values(ServiceOrderModel(status='F')) \
    .execute()

for resp in responses:
    print(resp.status_code, resp.text)
```

### Excluir usando statements (`newServiceOrderDelete.py`)

```python
from ORM_IXC.statemants.update import delete
from ORM_IXC.models.tableModels.serviceOrderModel import ServiceOrderModel

responses = delete(service_order) \
    .where(ServiceOrderModel.id == 308364) \
    .execute()

for resp in responses:
    print(resp.status_code, resp.text)
```

## Estrutura principal

- `ORM_IXC/context/request/manager.py`: gerencia chamadas HTTP, cabeçalhos e URL base
- `ORM_IXC/context/defaultActions/defaultActions.py`: implementa ações comuns de busca e envio
- `ORM_IXC/context/*.py`: contextos para entidades específicas da IXCSoft
- `ORM_IXC/models/searchUtils`: modelos para busca com filtros
- `ORM_IXC/models/defaultModel.py`: payload genérico para envio de dados
- `ORM_IXC/interfaces`: contratos de contexto e modelo
- `ORM_IXC/enums`: enums de ações, operadores e ordenação

## Observações

- A autenticação é feita via header `Authorization` com `Basic` encoding
- O `Manager` constrói a URL base para o serviço IXCSoft em `https://{host}/webservice/v1/`
- Os métodos CRUD são expostos pelas classes de contexto e podem ser estendidos conforme necessário

## Contribuição

1. Faça um fork do repositório
2. Crie uma branch para sua feature ou correção
3. Abra um pull request explicando a mudança

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
