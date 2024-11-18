import time


qtd_trocas = 0 # Quantidade de Trocas
qtd_comps = 0# Quantidade de Comparações
my_array = [64, 34, 25, 12, 22, 11, 90, 5]
elementos = len(my_array)
tempo_inicial = time.time()

def heapify(arr, n, i):
    global qtd_trocas, qtd_comps
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    qtd_comps+=1 # count comparacao
    if left < n and arr[left] > arr[largest]:
        largest = left

    qtd_comps+=1 # count comparacao
    if right < n and arr[right] > arr[largest]:
        largest = right

    qtd_comps+=1 # count comparacao
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        qtd_trocas+=1 # count troca
        heapify(arr, n, largest)

def heap_sort(arr):
    global qtd_trocas, qtd_comps
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        qtd_trocas+=1 # count troca
        heapify(arr, i, 0)

    return arr


tempo = time.time() - tempo_inicial

sorted_array = heap_sort(my_array)
print(f'{sorted_array}\nElemen: {elementos}\nTrocas: {qtd_trocas}\nCompar: {qtd_comps}\nTempo : {tempo}')



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
