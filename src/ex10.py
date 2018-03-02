import pandas as pd
import seaborn as sns

path = r"data\Iris_Data.csv"
data_frame = pd.read_csv(path)
data_frame['species'] = data_frame.species.str.replace('(Iris-)', '')

############################################################################

sns.pairplot(data_frame, hue = 'species', size = 4)
