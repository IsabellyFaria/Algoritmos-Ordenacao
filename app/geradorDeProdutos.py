import pandas as pd
import random

num_rows = 10000
ids = list(range(1, num_rows+1))

nomes = [f"Produto {i}" for i in ids]
descricoes = [f"Descrição detalhada do Produto {i}" for i in ids]
precos = [round(random.uniform(5.0, 1500.0), 2) for _ in ids]
estoques = [random.randint(0, 500) for _ in ids]

df = pd.DataFrame({
    "id": ids,
    "nome": nomes,
    "descrição": descricoes,
    "preço": precos,
    "estoque": estoques
})

file_path = "produtos_5000.csv"
df.to_csv(file_path, index=False, sep=";", encoding="utf-8")

file_path