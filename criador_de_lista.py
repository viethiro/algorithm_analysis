import json
import random

# Gerar listas de números inteiros aleatórios
lista_1 = [random.randint(0, 1000) for _ in range(1000)]  # Lista com 1000 elementos
lista_2 = [random.randint(0, 10000) for _ in range(10000)]  # Lista com 10000 elementos
lista_3 = [random.randint(0, 100000) for _ in range(100000)]  # Lista com 100000 elementos

# Criar um dicionário para armazenar as listas
dados = {
    "lista_1": lista_1,
    "lista_2": lista_2,
    "lista_3": lista_3,
}

# Escrever o dicionário em um arquivo JSON
with open("listas_numeros.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4)  # Usar indentação para facilitar a leitura

print("Listas geradas e salvas em 'listas_numeros.json'.")


# Carregar o arquivo JSON
with open("listas_numeros.json", "r") as arquivo:
    dados = json.load(arquivo)  # Lê o conteúdo do JSON
nome_lista = 'lista_2'
lista_selecionada = dados[nome_lista]
print(f"\nA lista '{nome_lista}' contém {len(lista_selecionada)} elementos.")
print(f"Primeiros 10 elementos da lista: {lista_selecionada[:10]}")  # Exibe os 10 primeiros elementos
