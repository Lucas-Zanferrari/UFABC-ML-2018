import pandas as pd

data_path = r"..\data\Iris_Data.csv"
data_frame = pd.read_csv(data_path)
data_frame['species'] = data_frame.species.str.replace('(Iris-)', '')

############################################################################

import seaborn as sns
new_data_frame = pd.melt(data_frame, id_vars = ['species'], value_name = 'size', var_name = 'measurement')
sns.boxplot(data = new_data_frame, hue = 'species', x = 'measurement', y = 'size')
