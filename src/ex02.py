import pandas as pd

data_path = r"..\data\Iris_Data.csv"
data_frame = pd.read_csv(data_path)

############################################################################

# data_frame['species'] = data_frame.species.str.replace('(Iris-)', '')
data_frame['species'] = data_frame.species.apply(lambda input_str: input_str.replace('Iris-', ''))
# data_frame['species'] = data_frame.species.apply(lambda input_str, to_remove='Iris-', to_input='': input_str.replace(to_remove, to_input))
print(data_frame)
