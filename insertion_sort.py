import time
import json

def insertion_sort_with_metrics(json_file, list_name):
    """
    Realiza o Insertion Sort em uma lista especificada dentro de um arquivo JSON e retorna métricas.

    Args:
        json_file (str): Caminho para o arquivo JSON contendo as listas.
        list_name (str): Nome da lista a ser ordenada.

    Returns:
        dict: Dicionário contendo as métricas e o tempo de execução.
    """
    # Variáveis globais para métricas
    global qtd_trocas, qtd_comps
    qtd_trocas = 0
    qtd_comps = 0

    # Carregar os dados do arquivo JSON
    with open(json_file, "r") as arquivo:
        dados = json.load(arquivo)
    my_array = dados[list_name]

    # Inicializar métricas
    elementos = len(my_array)

    # Medir tempo de execução
    tempo_inicial = time.time()

    # Algoritmo de Insertion Sort
    n = len(my_array)
    for i in range(1, n):
        insert_index = i
        current_value = my_array[i]
        for j in range(i - 1, -1, -1):
            qtd_comps += 1  # Contar comparação
            if my_array[j] > current_value:
                my_array[j + 1] = my_array[j]
                qtd_trocas += 1  # Contar troca
                insert_index = j
            else:
                break
        my_array[insert_index] = current_value
        qtd_trocas += 1  # Contar troca

    tempo = time.time() - tempo_inicial

    # Retornar resultados
    return {
        "Algoritmo": "insertion sort",
        "Lista": list_name,
        "Trocas": qtd_trocas,
        "Comparacoes": qtd_comps,
        "Tempo": tempo
    }

if __name__ == "__main__":
    # Exemplo de uso
    resultado = insertion_sort_with_metrics("listas_numeros.json", "lista_1")
    print(resultado)


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