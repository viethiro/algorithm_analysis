import time
import json

def bubble_sort_with_metrics(json_file, list_name):
    """
    Realiza o Bubble Sort em uma lista especificada dentro de um arquivo JSON e retorna métricas.

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

    # Inicialização das métricas
    qtd_trocas = 0
    qtd_comps = 0
    elementos = len(my_array)

    # Medir o tempo de execução
    tempo_inicial = time.time()

    # Algoritmo de Bubble Sort
    n = len(my_array)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            qtd_comps += 1  # Contar comparações
            if my_array[j] > my_array[j + 1]:
                my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]
                qtd_trocas += 1  # Contar trocas
                swapped = True
        qtd_comps += 1  # Contar comparações
        if not swapped:
            break

    # Calcular tempo total
    tempo = time.time() - tempo_inicial

    # Retornar métricas
    return {
        "Algoritmo": "bubble sort",
        "Lista": list_name,
        "Trocas": qtd_trocas,
        "Comparacoes": qtd_comps,
        "Tempo": tempo
    }

if __name__ == "__main__":
    # Exemplo de uso
    resultado = bubble_sort_with_metrics("listas_numeros.json", "lista_1")
    print(resultado)


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