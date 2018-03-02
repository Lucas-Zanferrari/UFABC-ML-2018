import pandas as pd

data_path = r"..\data\Iris_Data.csv"
data_frame = pd.read_csv(data_path)
data_frame['species'] = data_frame.species.str.replace('(Iris-)', '')

############################################################################

import seaborn as sns
sns.boxplot(data = data_frame)
