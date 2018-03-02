import pandas as pd

data_path = r"..\data\Iris_Data.csv"
data_frame = pd.read_csv(data_path)
data_frame['species'] = data_frame.species.apply(lambda input_str, to_remove='Iris-', to_input='': input_str.replace(to_remove, to_input))

############################################################################

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(data_frame.sepal_length, data_frame.sepal_width, ls = '', marker = 'o')
ax.set(xlabel='Length', ylabel='Width', title='Sepal Length X Width')