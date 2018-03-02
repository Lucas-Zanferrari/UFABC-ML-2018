import pandas as pd

data_path = r"..\data\Iris_Data.csv"
data_frame = pd.read_csv(data_path)
data_frame['species'] = data_frame.species.str.replace('(Iris-)', '')

############################################################################

data_frame.plot.hist(alpha = 0.5).set_xlabel('Units')
