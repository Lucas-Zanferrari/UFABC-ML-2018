import pandas as pd

data_path = r"..\data\Iris_Data.csv"
data_frame = pd.read_csv(data_path)
data_frame['species'] = data_frame.species.str.replace('(Iris-)', '')

############################################################################

print("Quantidade de cada espécie:")

# assim como no exercício 01, criei o loop para remover o Name e o dtype da Serie 
for key in data_frame.species.value_counts().keys():
  print(f"{key}: {data_frame.species.value_counts()[key]}")

print("\nEstatísticas sobre a massa de dados:")

# gerando quantiles mais precisos
df_stats = data_frame.describe([x * 0.1 for x in range(1, 10)])

# removendo linhas que o exercício não pede para facilitar visualização
df_stats = df_stats.drop(['count', 'std'])

# calculando a faixa
max_row = df_stats.loc['max']
min_row = df_stats.loc['min']
faixa = max_row - min_row

# inserindo a faixa no data frame de estatísticas
faixa.name = "faixa"
df_stats = df_stats.append(faixa)

# mostrando o data frame tratado apenas com o dados relevantes (pedidos pelo exercício)
print(df_stats)
