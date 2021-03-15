import pandas as pd
df = pd.read_csv("senzalitio.csv")
smiles = df.smiles
print(smiles[smiles.isnull()])
