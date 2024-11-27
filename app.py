import json
from bubble_sort import bubble_sort_with_metrics
from heap_sort import heap_sort_with_metrics
from insertion_sort import insertion_sort_with_metrics
from merge_sort import run_merge_sort_with_metrics
from quicksort import run_quicksort_with_metrics
from selection_sort import run_selection_sort
from shell_sort import shell_sort

with open("listas_numeros.json", "r") as arquivo:
    dados = json.load(arquivo)  # Lê o conteúdo do JSON
    # nome_lista = 'lista_melhor_2'

resultados = {}
indice = 0
for lista in dados:
    resultados[indice] = bubble_sort_with_metrics("listas_numeros.json", lista)
    indice += 1
    resultados[indice] = heap_sort_with_metrics("listas_numeros.json", lista)
    indice += 1
    resultados[indice] = insertion_sort_with_metrics("listas_numeros.json", lista)
    indice += 1
    resultados[indice] = run_merge_sort_with_metrics("listas_numeros.json", lista)
    indice += 1
    # resultados[indice] = run_quicksort_with_metrics("listas_numeros.json", lista)
    # indice += 1
    resultados[indice] = run_selection_sort("listas_numeros.json", lista)
    indice += 1
    resultados[indice] = shell_sort("listas_numeros.json", lista)
    indice += 1
    print(indice)

with open("resultados.json", "w") as arquivo:
    json.dump(resultados, arquivo, indent=4)