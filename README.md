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

pip install git+https://github.com/caioramos42/IXC_ORM_Project.git

## Uso básico

### Inicializar o manager

```python
from ORM_IXC.context.request.manager import Manager

manager = Manager('meu-servidor-ixc.com', 'usuario:senha')
```

### Criar um contexto

```python
from ORM_IXC.context.cliente import Cliente

cliente = Cliente(manager)
```

### Buscar por ID

```python
response = cliente.SearchById(123)
print(response.json())
```

### Buscar todos os registros

```python
response = cliente.SearchAll()
print(response.json())
```

### Buscar com filtros

```python
from ORM_IXC.models.searchUtils.searchModel import SearchModule
from ORM_IXC.models.searchUtils.gridParamModel import GridParam
from ORM_IXC.enums.operators import Operators

search = SearchModule(
    searchField='nome',
    query='João',
    oper=Operators.EQUALS,
    table='cliente'
)

search.appendGridParams(GridParam('cliente.cidade', Operators.EQUALS, 'São Paulo'))
response = cliente.getByFilter(search)
print(response.json())
```

### Enviar payload genérico

```python
from ORM_IXC.models.defaultModel import DefaultPayload

payload = DefaultPayload({
    'nome': 'Novo Cliente',
    'email': 'contato@exemplo.com'
})
response = cliente._MakePost(payload)
print(response.status_code, response.text)
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
