import csv


def makecsv(objetos, arquivo_saida="saida"):
    if not objetos:
        raise ValueError("Lista vazia")
    
    arquivo_saida = f"{arquivo_saida}.csv"
    
    # Obtém headers do primeiro objeto usando to_dict()
    primeiro_dict = objetos[0].to_dict()
    headers = list(primeiro_dict.keys())
    
    # Escreve o arquivo CSV
    with open(arquivo_saida, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        
        # Escreve o cabeçalho
        writer.writeheader()
        
        # Escreve cada linha convertendo o objeto para dicionário
        for obj in objetos:
            writer.writerow(obj.to_dict())
    
    print(f"Arquivo gerado: {arquivo_saida}")


def makeCSVStream(arquivo_saida, async_iterador):
    arquivo_saida = f"{arquivo_saida}.csv"
    headers = None
    
    with open(arquivo_saida, 'w', newline='', encoding='utf-8') as csvfile:
        writer = None
        
        for item in async_iterador:
            # Obtém os dados do objeto usando to_dict()
            dados = item.to_dict()
            
            # Inicializa o writer com os headers na primeira iteração
            if headers is None:
                headers = list(dados.keys())
                writer = csv.DictWriter(csvfile, fieldnames=headers)
                writer.writeheader()
            
            # Escreve a linha
            writer.writerow(dados) # type: ignore
    
    print(f"Arquivo gerado: {arquivo_saida}")
