import pandas as pd
import matplotlib.pyplot as plt
#header of the columns
col_list = ["MW"]
#Extract only defined column from all dataframes
df1 = pd.read_csv('Amines.csv',  usecols=col_list)
df2 = pd.read_csv('Carboxylic.csv',  usecols=col_list)
df3 = pd.read_csv('Imines.csv',  usecols=col_list)
df4 = pd.read_csv('Sulphonic.csv',  usecols=col_list)
df5 = pd.read_csv('Phosphorous.csv',  usecols=col_list)
#df6 = pd.read_csv('Zwitterions.csv',  usecols=col_list)
#Plot histograms as step lines in a range of values
#plt.hist(df6, range=(-50, +100), bins=100, histtype='step', log=True, label="Zwitterions")
plt.hist(df5, range=(40, +7000), bins=100, histtype='step', log=True, label="Phosphorous")
plt.hist(df4, range=(40, +7000), bins=100, histtype='step', log=True, label="Sulphonates")
plt.hist(df3, range=(40, +7000), bins=100, histtype='step', log=True, label="Imines")
plt.hist(df2, range=(40, +7000), bins=100, histtype='step', log=True, label="Carboxylic")
plt.hist(df1, range=(40, +7000), bins=100, histtype='step', log=True, label="Amines")
#axis name and legend
plt.xlabel("MW", size=14)
plt.ylabel('Frequency', size=14)
plt.legend(frameon=False, loc='upper right', ncol=2, title='Anchoring Group')
#avoid cropping the labels
plt.tight_layout() 
#plt.show()
#save picture
plt.savefig("plot_MW.png", dpi=300)