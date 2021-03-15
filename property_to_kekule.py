##A script to find the smile(s) corresponding to a specific value or range of values for a property (here HBA) and convert the smiles string to a 2D Kekulè##
import pandas as pd
import numpy as np
from rdkit.Chem import PandasTools

df = pd.read_csv('Carboxylic.csv', index_col=False)
superacceptors=(df[df["HBA"]>177])
PandasTools.AddMoleculeColumnToFrame(superacceptors, smilesCol='smiles', molCol='rdkit_molecules')
superacceptors