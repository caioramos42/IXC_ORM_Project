"""
Conversores para formatos Python nativos: pandas DataFrame e numpy arrays.
Funções similares ao padrão de makecsv e makeexcel, mas retornam estruturas de dados.
"""

from typing import Any


def to_pandas_dataframe(objetos):
    try:
        import pandas as pd
    except ImportError:
        raise ImportError("pandas não está instalado. Execute: pip install pandas")
    
    if not objetos:
        raise ValueError("Lista vazia")
    
    dados = [obj.to_dict() for obj in objetos]
    
    df = pd.DataFrame(dados)
    
    return df


def to_pandas_dataframe_stream(iterador, chunk_size: int = 1000):
    try:
        import pandas as pd
    except ImportError:
        raise ImportError("pandas não está instalado. Execute: pip install pandas")
    
    dados = []
    chunk = []
    
    for item in iterador:
        chunk.append(item.to_dict())
        
        if len(chunk) >= chunk_size:
            dados.extend(chunk)
            chunk = []
    
    if chunk:
        dados.extend(chunk)
    
    if not dados:
        raise ValueError("Nenhum dado fornecido pelo iterador")
    
    df = pd.DataFrame(dados)
    
    return df


def to_numpy_array(objetos, dtype: Any = None):
    try:
        import numpy as np
    except ImportError:
        raise ImportError("numpy não está instalado. Execute: pip install numpy")
    
    if not objetos:
        raise ValueError("Lista vazia")
    
    # Converte cada objeto para dicionário usando to_dict()
    dados = [obj.to_dict() for obj in objetos]
    
    # Cria array a partir dos dados
    # Primeiro tenta criar um array estruturado com campos nomeados
    if dados:
        primeiro = dados[0]
        # Define os tipos e nomes dos campos
        campos = [(nome, object) for nome in primeiro.keys()]
        arr = np.array([tuple(d.values()) for d in dados], dtype=campos if campos else dtype)
    else:
        arr = np.array([], dtype=dtype)
    
    return arr


def to_numpy_array_stream(iterador, chunk_size: int = 1000, dtype: Any = None):
    try:
        import numpy as np
    except ImportError:
        raise ImportError("numpy não está instalado. Execute: pip install numpy")
    
    dados = []
    chunk = []
    
    for item in iterador:
        # Converte item para dicionário usando to_dict()
        chunk.append(item.to_dict())
        
        # Processa chunk quando atinge o tamanho limite
        if len(chunk) >= chunk_size:
            dados.extend(chunk)
            chunk = []
    
    # Processa o último chunk
    if chunk:
        dados.extend(chunk)
    
    if not dados:
        raise ValueError("Nenhum dado fornecido pelo iterador")
    
    # Cria array a partir de todos os dados
    if dados:
        primeiro = dados[0]
        # Define os tipos e nomes dos campos
        campos = [(nome, object) for nome in primeiro.keys()]
        arr = np.array([tuple(d.values()) for d in dados], dtype=campos if campos else dtype)
    else:
        arr = np.array([], dtype=dtype)
    
    return arr
