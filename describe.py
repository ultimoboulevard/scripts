import pandas as pd
data = pd.read_csv('Carboxylic.csv', index_col="smiles")
print(data.describe())