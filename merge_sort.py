def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def mergeSort(arr):
    step = 1  # Starting with sub-arrays of length 1
    length = len(arr)
    
    while step < length:
        for i in range(0, length, 2 * step):
            left = arr[i:i + step]
            right = arr[i + step:i + 2 * step]
            
            merged = merge(left, right)
            
            # Place the merged array back into the original array
            for j, val in enumerate(merged):
                arr[i + j] = val
                
        step *= 2  # Double the sub-array length for the next iteration
        
    return arr

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergeSort(unsortedArr)
print("Sorted array:", sortedArr)

# Etapa 1: Começamos com um array não classificado, e sabemos que ele se divide ao meio até que os subarrays consistam apenas de um elemento. A função Merge Sort chama a si mesma duas vezes, uma para cada metade do array. Isso significa que o primeiro subarray será dividido nos menores pedaços primeiro.
# [ 12, 8, 9, 3, 11, 5, 4]
# [ 12, 8, 9] [ 3, 11, 5, 4]
# [ 12] [ 8, 9] [ 3, 11, 5, 4]
# [ 12] [ 8] [ 9] [ 3, 11, 5, 4]

# Etapa 2: A divisão do primeiro subarray foi concluída e agora é hora de mesclar. 8 e 9 são os dois primeiros elementos a serem mesclados. 8 é o menor valor, então ele vem antes de 9 no primeiro subarray mesclado.
# [ 12] [ 8, 9] [ 3, 11, 5, 4]

# Etapa 3: Os próximos subarrays a serem mesclados são [ 12] e [ 8, 9]. Os valores em ambos os arrays são comparados desde o início. 8 é menor que 12, então 8 vem primeiro, e 9 também é menor que 12.
# [ 8, 9, 12] [ 3, 11, 5, 4]

# Etapa 4: agora, o segundo grande subarray é dividido recursivamente.
# [ 8, 9, 12] [ 3, 11, 5, 4]
# [ 8, 9, 12] [ 3, 11] [ 5, 4]
# [ 8, 9, 12] [ 3] [ 11] [ 5, 4]

# Etapa 5: 3 e 11 são mesclados novamente na mesma ordem em que são mostrados porque 3 é menor que 11.
# [ 8, 9, 12] [ 3, 11] [ 5, 4]

# Etapa 6: a submatriz com valores 5 e 4 é dividida e depois mesclada para que 4 venha antes de 5.
# [ 8, 9, 12] [ 3, 11] [ 5] [ 4]
# [ 8, 9, 12] [ 3, 11] [ 4, 5]

# Etapa 7: Os dois subarrays à direita são mesclados. Comparações são feitas para criar elementos no novo array mesclado:
# 3 é menor que 4
# 4 é menor que 11
# 5 é menor que 11
# 11 é o último valor restante
# [ 8, 9, 12] [ 3, 4, 5, 11]

# Etapa 8: Os dois últimos subarrays restantes são mesclados. Vamos ver como as comparações são feitas em mais detalhes para criar o novo array mesclado e finalizado e ordenado:
# 3 é menor que 8:
# Before [ 8, 9, 12] [ 3, 4, 5, 11]
# After: [ 3, 8, 9, 12] [ 4, 5, 11]

# Etapa 9: 4 é menor que 8:
# Before [ 3, 8, 9, 12] [ 4, 5, 11]
# After: [ 3, 4, 8, 9, 12] [ 5, 11]

# Etapa 10: 5 é menor que 8:
# Before [ 3, 4, 8, 9, 12] [ 5, 11]
# After: [ 3, 4, 5, 8, 9, 12] [ 11]

# Passo 11: 8 e 9 são menores que 11:
# Before [ 3, 4, 5, 8, 9, 12] [ 11]
# After: [ 3, 4, 5, 8, 9, 12] [ 11]

# Etapa 12: 11 é menor que 12:
# Before [ 3, 4, 5, 8, 9, 12] [ 11]
# After: [ 3, 4, 5, 8, 9, 11, 12]