import time
import json
import sys
sys.setrecursionlimit(10000000)  # Ajuste conforme necessário


# Função para particionar o array em torno do pivô
def partition(array, low, high):
    """
    Particiona o array para o Quick Sort, colocando os elementos menores que o pivô à esquerda
    e os maiores à direita.

    Args:
        array (list): Lista de elementos.
        low (int): Índice inferior.
        high (int): Índice superior (pivô).

    Returns:
        int: Índice do pivô após a partição.
    """
    global qtd_comps, qtd_trocas
    pivot = array[high]  # Escolhe o último elemento como pivô
    i = low - 1  # Índice para os elementos menores que o pivô

    for j in range(low, high):
        qtd_comps += 1  # Contar comparação
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]  # Trocar elementos
            qtd_trocas += 1  # Contar troca

    # Coloca o pivô na posição correta
    array[i+1], array[high] = array[high], array[i+1]
    qtd_trocas += 1  # Contar troca
    return i+1

# Função principal do Quick Sort
def quicksort(array, low=0, high=None):
    """
    Implementação do Quick Sort com recursão.

    Args:
        array (list): Lista de elementos.
        low (int, optional): Índice inferior. Padrão é 0.
        high (int, optional): Índice superior. Padrão é o tamanho da lista - 1.

    Returns:
        None: A ordenação é feita no próprio array.
    """
    global qtd_comps, qtd_trocas
    if high is None:
        high = len(array) - 1

    if low < high:
        # Particiona o array e obtém o índice do pivô
        pivot_index = partition(array, low, high)
        # Ordena os subarrays à esquerda e à direita do pivô
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)

# Função para executar o Quick Sort com métricas
def run_quicksort_with_metrics(json_file, list_name):
    """
    Executa o Quick Sort em uma lista especificada de um arquivo JSON, calculando métricas.

    Args:
        json_file (str): Caminho para o arquivo JSON contendo as listas.
        list_name (str): Nome da lista a ser ordenada.

    Returns:
        dict: Dicionário contendo as métricas e o tempo de execução.
    """
    global qtd_trocas, qtd_comps
    qtd_trocas = 0  # Reseta contagem de trocas
    qtd_comps = 0   # Reseta contagem de comparações

    # Carrega os dados do JSON
    with open(json_file, "r") as arquivo:
        dados = json.load(arquivo)
    my_array = dados[list_name]

    # Mede o tempo de execução
    tempo_inicial = time.time()
    quicksort(my_array)
    tempo = time.time() - tempo_inicial

    # Retorna as métricas
    return {
        "Algoritmo": "quicksort",
        "Lista": list_name,
        "Trocas": qtd_trocas,
        "Comparacoes": qtd_comps,
        "Tempo": tempo
    }

if __name__ == "__main__":
    # Exemplo de uso
    resultado = run_quicksort_with_metrics("listas_numeros.json", "lista_melhor_1k")
    print(resultado)



# Etapa 1: começamos com uma matriz não classificada.
# [ 11, 9, 12, 7, 3]

# Etapa 2: escolhemos o último valor 3 como elemento pivô.
# [ 11, 9, 12, 7, 3]

# Etapa 3: O restante dos valores na matriz são todos maiores que 3 e devem estar no lado direito de 3. Troque 3 por 11.
# [ 3, 9, 12, 7, 11]

# Etapa 4: O valor 3 agora está na posição correta. Precisamos classificar os valores à direita de 3. Escolhemos o último valor 11 como o novo elemento pivô.
# [ 3, 9, 12, 7, 11]

# Etapa 5: O valor 7 deve estar à esquerda do valor de pivô 11, e 12 deve estar à direita dele. Mova 7 e 12.
# [ 3, 9, 7, 12, 11]

# Etapa 6: troque 11 por 12 de modo que os valores menores, 9 e 7, fiquem no lado esquerdo de 11, e 12, no lado direito.
# [ 3, 9, 7, 11, 12]

# Passo 7: 11 e 12 estão nas posições corretas. Escolhemos 7 como o elemento pivô na submatriz [ 9, 7], à esquerda de 11.
# [ 3, 9, 7, 11, 12]

# Passo 8: Devemos trocar 9 por 7.
# [ 3, 7, 9, 11, 12]
