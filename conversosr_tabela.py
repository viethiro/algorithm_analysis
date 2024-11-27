import json
import pandas as pd

with open("resultados.json", "r") as arquivo:
    data = json.load(arquivo)

records = [value for value in data.values()]

df = pd.DataFrame(records)

csv_filename = "resultados_ordenacao.csv"
df.to_csv(csv_filename, index=False)

print(f"Tabela exportada para {csv_filename}")
