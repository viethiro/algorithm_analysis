def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)

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
