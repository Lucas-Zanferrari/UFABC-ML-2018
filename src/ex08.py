import pandas as pd
import matplotlib.pyplot as plt

data_path = r"..\data\Iris_Data.csv"
data_frame = pd.read_csv(data_path)
data_frame['species'] = data_frame.species.str.replace('(Iris-)', '')

############################################################################

data_frame['petal_length'].plot.box()
plt.figure()
data_frame['petal_width'].plot.box()
plt.figure()
data_frame['sepal_length'].plot.box()
plt.figure()
data_frame['sepal_width'].plot.box()
