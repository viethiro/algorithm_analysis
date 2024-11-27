import json
import random

# Gerar listas de números
lista_melhor_1k = [i for i in range(1000)]
lista_melhor_10k = [i for i in range(10000)]
lista_melhor_100k = [i for i in range(100000)]

lista_medio_1k = [random.randint(0, 1000) for _ in range(1000)]  # Lista com 1000 elementos
lista_medio_10k = [random.randint(0, 10000) for _ in range(10000)]  # Lista com 10000 elementos
lista_medio_100k = [random.randint(0, 100000) for _ in range(100000)]  # Lista com 100000 elementos

lista_pior_1k = [i for i in range(1000, 0, -1)]
lista_pior_10k = [i for i in range(10000, 0, -1)]
lista_pior_100k = [i for i in range(100000, 0, -1)]

dados = {
    "lista_melhor_1k": lista_melhor_1k,
    "lista_melhor_10k": lista_melhor_10k,
    "lista_melhor_100k": lista_melhor_100k,
    "lista_medio_1k": lista_medio_1k,
    "lista_medio_10k": lista_medio_10k,
    "lista_medio_100k": lista_medio_100k,
    "lista_pior_1k": lista_pior_1k,
    "lista_pior_10k": lista_pior_10k,
    "lista_pior_100k": lista_pior_100k,
}

with open("listas_numeros.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4)  

print("Listas geradas e salvas em 'listas_numeros.json'.")


with open("listas_numeros.json", "r") as arquivo:
    dados = json.load(arquivo)
    # nome_lista = 'lista_melhor_2'
for nome_lista in dados:
    lista_selecionada = dados[nome_lista]
    print(f"\nA lista '{nome_lista}' contém {len(lista_selecionada)} elementos.")
    print(f"Primeiros 10 elementos da lista: {lista_selecionada[:10]}")  # Exibe os 10 primeiros elementos
