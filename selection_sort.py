my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j   
    my_array[i], my_array[min_index] = my_array[min_index], my_array[i]

print("Sorted array:", my_array)

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