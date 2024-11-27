import time
import json

def merge(left, right):
    """
    Realiza a junção de duas listas ordenadas em uma única lista ordenada.
    
    Args:
        left (list): Sublista esquerda.
        right (list): Sublista direita.
    
    Returns:
        list: Lista ordenada resultante da junção.
    """
    global qtd_trocas, qtd_comps
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        qtd_comps += 1  # Contar comparação
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def merge_sort_with_metrics(arr):
    """
    Realiza o Merge Sort em uma lista e coleta métricas de desempenho.
    
    Args:
        arr (list): Lista de números a ser ordenada.
    
    Returns:
        list: Lista ordenada.
    """
    global qtd_trocas, qtd_comps
    qtd_trocas = 0
    qtd_comps = 0
    step = 1  # Começa com sublistas de comprimento 1
    length = len(arr)
    
    while step < length:
        for i in range(0, length, 2 * step):
            left = arr[i:i + step]
            right = arr[i + step:i + 2 * step]
            
            merged = merge(left, right)
            
            # Coloca a lista mesclada de volta no array original
            for j, val in enumerate(merged):
                arr[i + j] = val
                qtd_trocas += 1  # Contar troca
                
        step *= 2  # Dobra o comprimento da sublista para a próxima iteração
        
    return arr

def run_merge_sort_with_metrics(json_file, list_name):
    """
    Executa o Merge Sort em uma lista especificada de um arquivo JSON, calculando métricas.
    
    Args:
        json_file (str): Caminho para o arquivo JSON contendo as listas.
        list_name (str): Nome da lista a ser ordenada.
    
    Returns:
        dict: Dicionário contendo as métricas e o tempo de execução.
    """
    # Carregar os dados do arquivo JSON
    with open(json_file, "r") as arquivo:
        dados = json.load(arquivo)
    my_array = dados[list_name]

    # Medir o tempo de execução
    tempo_inicial = time.time()
    sorted_array = merge_sort_with_metrics(my_array)
    tempo = time.time() - tempo_inicial

    # Retornar resultados
    return {
        "Algoritmo": "merge sort",
        "Lista": list_name,
        "Trocas": qtd_trocas,
        "Comparacoes": qtd_comps,
        "Tempo": tempo
    }

if __name__ == "__main__":
    # Exemplo de uso
    resultado = run_merge_sort_with_metrics("listas_numeros.json", "lista_melhor_1k")
    print(resultado)


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