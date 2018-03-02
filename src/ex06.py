import pandas as pd
import matplotlib.pyplot as plt

path = r"data\Iris_Data.csv"
data_frame = pd.read_csv(path)
data_frame['species'] = data_frame.species.str.replace('(Iris-)', '')

############################################################################

fig, ax = plt.subplots()
ax.hist(data_frame.petal_length, bins = 25)
ax.set(xlabel='Length', ylabel='Number of specimens', title='Petal Length')
