import time
import json

# Função principal do Selection Sort com contagem de métricas
def selection_sort(array):
    """
    Implementação do Selection Sort com contagem de trocas e comparações.

    Args:
        array (list): Lista de elementos a ser ordenada.

    Returns:
        tuple: (array ordenado, qtd_trocas, qtd_comps, tempo_execucao)
    """
    n = len(array)
    qtd_trocas = 0  # Contador de trocas
    qtd_comps = 0   # Contador de comparações

    tempo_inicial = time.time()
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            qtd_comps += 1  # Contar comparação
            if array[j] < array[min_index]:
                min_index = j
        # Trocar o elemento atual com o menor encontrado
        array[i], array[min_index] = array[min_index], array[i]
        qtd_trocas += 1  # Contar troca

    tempo_execucao = time.time() - tempo_inicial
    return array, qtd_trocas, qtd_comps, tempo_execucao

# Função para executar o Selection Sort em uma lista de um arquivo JSON
def run_selection_sort(json_file, list_name):
    """
    Executa o Selection Sort em uma lista especificada de um arquivo JSON, calculando métricas.

    Args:
        json_file (str): Caminho para o arquivo JSON contendo as listas.
        list_name (str): Nome da lista a ser ordenada.

    Returns:
        dict: Dicionário contendo as métricas e o tempo de execução.
    """
    # Carregar dados do JSON
    with open(json_file, "r") as arquivo:
        dados = json.load(arquivo)
    my_array = dados[list_name]

    # Ordenar e coletar métricas
    sorted_array, qtd_trocas, qtd_comps, tempo_execucao = selection_sort(my_array)

    # Retornar métricas
    return {
        "Algoritmo": "selection sort",
        "Lista": list_name,
        "Trocas": qtd_trocas,
        "Comparacoes": qtd_comps,
        "Tempo": tempo_execucao
    }

if __name__ == "__main__":
    # Exemplo de uso
    resultado = run_selection_sort("listas_numeros.json", "lista_1")
    print(resultado)


# Etapa 1: começamos com uma matriz não classificada.
# [ 7, 12, 9, 11, 3]

# Etapa 2: Percorra o array, um valor de cada vez. Qual valor é o mais baixo? 3, certo?
# [ 7, 12, 9, 11, 3]

# Etapa 3: mova o menor valor 3 para a frente da matriz.
# [ 3, 7, 12, 9, 11]

# Etapa 4: analise o restante dos valores, começando pelo 7. 7 é o valor mais baixo e já está na frente da matriz, então não precisamos movê-lo.
# [ 3, 7, 12, 9, 11]

# Etapa 5: examine o restante da matriz: 12, 9 e 11. 9 é o menor valor.
# [ 3, 7, 12, 9, 11]

# Etapa 6: mova o 9 para a frente.
# [ 3, 7, 9, 12, 11]

# Etapa 7: Olhando para 12 e 11, 11 é o mais baixo.
# [ 3, 7, 9, 12, 11]

# Passo 8: Mova-o para a frente.
# [ 3, 7, 9, 11, 12]