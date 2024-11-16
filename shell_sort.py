def shell_sort(my_array):
    n = len(my_array)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = my_array[i]
            j = i

            while j >= gap and my_array[j - gap] > temp:
                my_array[j] = my_array[j - gap]
                j -= gap

            my_array[j] = temp

        gap //= 2

    return my_array

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
sorted_array = shell_sort(my_array)
print("Sorted array:", sorted_array)

# Passo 1: Início com o array não ordenado.
# Array inicial: [64, 34, 25, 12, 22, 11, 90, 5]

# Passo 2: Definição do primeiro valor de gap.
# gap = n // 2 = 4. O array é dividido em sublistas baseadas nesse intervalo.
# Sublistas para gap = 4:
# [64, 22]
# [34, 11]
# [25, 90]
# [12, 5]

# Passo 3: Realiza a inserção ordenada nas sublistas.
# Ordena cada sublista:
# [64, 22] → [22, 64]
# [34, 11] → [11, 34]
# [25, 90] → [25, 90]
# [12, 5] → [5, 12]
# Array atualizado após gap = 4:
# [22, 11, 25, 5, 64, 34, 90, 12]

# Passo 4: Reduz o valor de gap.
# gap = gap // 2 = 2.
# Agora, trabalha com elementos separados por dois índices.
# Sublistas para gap = 2:
# [22, 25, 64, 90]
# [11, 5, 34, 12]

# Passo 5: Realiza a inserção ordenada nas novas sublistas.
# Ordena cada sublista:
# [22, 25, 64, 90] → [22, 25, 64, 90] (já ordenada)
# [11, 5, 34, 12] → [5, 11, 12, 34]
# Array atualizado após gap = 2:
# [5, 11, 22, 25, 12, 34, 64, 90]

# Passo 6: Reduz o valor de gap.
# gap = gap // 2 = 1.
# Agora realiza uma inserção ordenada simples para o array completo.

# Passo 7: Realiza a ordenação final com gap = 1.
# Inserção ordenada:
# [5, 11] → [5, 11]
# [11, 22] → [5, 11, 22]
# [22, 25] → [5, 11, 22, 25]
# [25, 12] → [5, 11, 12, 22, 25]
# [25, 34] → [5, 11, 12, 22, 25, 34]
# [34, 64] → [5, 11, 12, 22, 25, 34, 64]
# [64, 90] → [5, 11, 12, 22, 25, 34, 64, 90]

# Passo 8: Array ordenado final.
# [5, 11, 12, 22, 25, 34, 64, 90]
