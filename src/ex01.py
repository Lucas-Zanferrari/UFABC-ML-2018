import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

############################################################################

data_path = r"..\data\Iris_Data.csv"
data_frame = pd.read_csv(data_path)

print(f"Número de linhas: \t{data_frame.shape[0]}")
print(f"Número de colunas: \t{data_frame.shape[1]}\n")
print(f"Nome das colunas:")

# fiz o laço para remover o dtype do Index data_frame.columns, já
# que ele não era pedido pelo exercício
for column_name in data_frame.columns.base: # type = pandas.core.indexes.base.Index
  print(column_name, end = ";\t")

# pelo mesmo motivo, também removi o dtype da Series data_frame.dtypes
print(f"\n\nTipos das colunas:")
for key in data_frame.dtypes.keys(): # type = pandas.core.series.Series
  print(f"{key}: {data_frame.dtypes[key]}", end = ";\t")
