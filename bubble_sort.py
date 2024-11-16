my_array = [7, 3, 9, 12, 11]

n = len(my_array)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
            swapped = True
    if not swapped:
        break

print("Sorted array:", my_array)

# Etapa 1: começamos com uma matriz não classificada.
# [7, 12, 9, 11, 3]

# Etapa 2: olhamos para os dois primeiros valores. O menor valor vem primeiro? Sim, então não precisamos trocá-los.
# [7, 12, 9, 11, 3]

# Passo 3: Dê um passo à frente e olhe para os valores 12 e 9. O menor valor vem primeiro? Não.
# [7, 12, 9, 11, 3]

# Etapa 4: Precisamos trocá-los para que o 9 venha primeiro.
# [7, 9, 12, 11, 3]

# Passo 5: Dando um passo à frente, olhando para 12 e 11.
# [7, 9, 12, 11, 3]

# Etapa 6: Precisamos trocar para que 11 venha antes de 12.
# [7, 9, 11, 12, 3]

# Etapa 7: Olhando para 12 e 3, precisamos trocá-los? Sim.
# [7, 9, 11, 12, 3]

# Etapa 8: Trocar 12 e 3 para que 3 venha primeiro.
# [7, 9, 11, 3, 12]