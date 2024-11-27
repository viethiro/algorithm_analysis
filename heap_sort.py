import time
import json

def heap_sort_with_metrics(json_file, list_name):
    """
    Realiza o Heap Sort em uma lista especificada dentro de um arquivo JSON e retorna métricas.

    Args:
        json_file (str): Caminho para o arquivo JSON contendo as listas.
        list_name (str): Nome da lista a ser ordenada.

    Returns:
        dict: Dicionário contendo as métricas e o tempo de execução.
    """
    # Variáveis globais para métricas
    global qtd_trocas, qtd_comps
    qtd_trocas = 0
    qtd_comps = 0

    # Função para reorganizar o heap
    def heapify(arr, n, i):
        global qtd_trocas, qtd_comps
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        qtd_comps += 1  # Contar comparação
        if left < n and arr[left] > arr[largest]:
            largest = left

        qtd_comps += 1  # Contar comparação
        if right < n and arr[right] > arr[largest]:
            largest = right

        qtd_comps += 1  # Contar comparação
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            qtd_trocas += 1  # Contar troca
            heapify(arr, n, largest)

    # Função principal de Heap Sort
    def heap_sort(arr):
        global qtd_trocas, qtd_comps
        n = len(arr)

        # Construção do heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)

        # Extração de elementos do heap
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            qtd_trocas += 1  # Contar troca
            heapify(arr, i, 0)

        return arr

    # Carregar os dados do arquivo JSON
    with open(json_file, "r") as arquivo:
        dados = json.load(arquivo)
    my_array = dados[list_name]

    # Inicializar métricas
    elementos = len(my_array)

    # Medir tempo de execução
    tempo_inicial = time.time()
    sorted_array = heap_sort(my_array)
    tempo = time.time() - tempo_inicial

    # Retornar resultados
    return {
        "Algoritmo": "heap sort",
        "Lista": list_name,
        "Trocas": qtd_trocas,
        "Comparacoes": qtd_comps,
        "Tempo": tempo
    }

if __name__ == "__main__":
    # Exemplo de uso
    resultado = heap_sort_with_metrics("listas_numeros.json", "lista_2")
    print(resultado)


# Etapa 1: Array inicial não ordenado
# Array inicial:
# [12, 11, 13, 5, 6, 7]

# Etapa 2: Construir o Max Heap
# Constrói-se o heap começando pelo último nó não-folha:
# O nó 5 (índice 2) já é maior que seus filhos.
# O nó 11 (índice 1) é menor que seu filho 13. Trocamos:
# [12, 13, 11, 5, 6, 7]

# O nó 12 (índice 0) é menor que o maior filho 13. Trocamos:
# [13, 12, 11, 5, 6, 7]

# Resultado do Max Heap:
# [13, 12, 11, 5, 6, 7]

# Etapa 3: Extração do maior elemento
# Troca o maior elemento (raiz) com o último elemento e ajusta o heap:
# Após a troca:
# [7, 12, 11, 5, 6, 13]

# Ajusta o heap:
# [12, 7, 11, 5, 6, 13]

# Repete a extração e ajuste:
# Troca:
# [6, 7, 11, 5, 12, 13]

# Ajusta:
# [11, 7, 6, 5, 12, 13]

# Continua:
# Troca:
# [5, 7, 6, 11, 12, 13]

# Ajusta:
# [7, 5, 6, 11, 12, 13]

# Finaliza com:
# [5, 6, 7, 11, 12, 13]

# Etapa Final: Array Ordenado
# Array ordenado:
# [5, 6, 7, 11, 12, 13]
