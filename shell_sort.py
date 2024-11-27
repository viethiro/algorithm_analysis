import time
import json

def shell_sort(json_file, list_name):
    """
    Executa o algoritmo Shell Sort em uma lista e retorna as estatísticas de execução.
    
    Args:
        my_array (list): A lista de números a ser ordenada.
    
    Returns:
        dict: Um dicionário contendo:
            - 'sorted_array': A lista ordenada.
            - 'elementos': O número de elementos na lista.
            - 'qtd_trocas': O número de trocas realizadas.
            - 'qtd_comps': O número de comparações realizadas.
            - 'tempo': O tempo de execução em segundos.
    """

    with open(json_file, "r") as arquivo:
        dados = json.load(arquivo)
    my_array = dados[list_name]

    qtd_trocas = 0
    qtd_comps = 0
    elementos = len(my_array)

    tempo_inicial = time.time()
    
    n = len(my_array)
    gap = n // 2  # Define o intervalo inicial

    while gap > 0:
        for i in range(gap, n):
            temp = my_array[i]
            j = i
            qtd_comps += 1  # Contar comparação
            # Comparação e troca
            while j >= gap and my_array[j - gap] > temp:
                qtd_comps += 1  # Contar comparação
                my_array[j] = my_array[j - gap]
                qtd_trocas += 1  # Contar troca
                j -= gap

            my_array[j] = temp
            qtd_trocas += 1  # Contar troca final

        gap //= 2  # Reduz o intervalo

    tempo = time.time() - tempo_inicial

    return {
        "Algoritmo": "shell sort",
        "Lista": list_name,
        "Trocas": qtd_trocas,
        "Comparacoes": qtd_comps,
        "Tempo": tempo
    }

if __name__ == "__main__":
    resultado = shell_sort("listas_numeros.json", "lista_melhor_1k")
    print(resultado)



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
