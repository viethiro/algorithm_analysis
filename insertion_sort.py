my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(1,n):
    insert_index = i
    current_value = my_array[i]
    for j in range(i-1, -1, -1):
        if my_array[j] > current_value:
            my_array[j+1] = my_array[j]
            insert_index = j
        else:
            break
    my_array[insert_index] = current_value

print("Sorted array:", my_array)

# Etapa 1: começamos com uma matriz não classificada.
# [ 7, 12, 9, 11, 3]

# Etapa 2: Podemos considerar o primeiro valor como a parte inicial ordenada do array. Se for apenas um valor, ele deve ser ordenado, certo?
# [ 7, 12, 9, 11, 3]

# Etapa 3: O próximo valor 12 agora deve ser movido para a posição correta na parte ordenada do array. Mas 12 é maior que 7, então ele já está na posição correta.
# [ 7, 12, 9, 11, 3]

# Etapa 4: considere o próximo valor 9.
# [ 7, 12, 9, 11, 3]

# Etapa 5: O valor 9 agora deve ser movido para a posição correta dentro da parte classificada da matriz, então movemos 9 entre 7 e 12.
# [ 7, 9, 12, 11, 3]

# Etapa 6: O próximo valor é 11.
# [ 7, 9, 12, 11, 3]

# Etapa 7: movemos o número entre 9 e 12 na parte classificada do array.
# [ 7, 9, 11, 12, 3]

# Etapa 8: O último valor a ser inserido na posição correta é 3.
# [ 7, 9, 11, 12, 3]

# Etapa 9: Inserimos 3 na frente de todos os outros valores porque é o valor mais baixo.
# [ 3,7, 9, 11, 12]