import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Carboxylic.csv',  index_col="smiles")
ALOGP = df.loc[:, "ALOGP"]
MW= df.loc[:, "MW"] 
HBA= df.loc[:, "HBA"] 
HBD= df.loc[:, "HBD"] 
PSA=df.loc[:, "PSA"] 
ROTB=df.loc[:, "ROTB"] 
AROM=df.loc[:, "AROM"] 
ALERTS=df.loc[:, "ALERTS"] 
#plt.hist(ALOGP, range=(-20, +50), bins=100, histtype='step', log=True, label="ALOGP")
#plt.hist(MW, range=(-20, +2000), bins=100, histtype='step', log=True, label="MW")
#plt.hist(HBA, range=(-20, +50), bins=100, histtype='step', log=True, label="HBA")
#plt.hist(PSA, range=(-20, +50), bins=100, histtype='step', log=True, label="PSA")
#plt.hist(ROTB, range=(-20, +50), bins=100, histtype='step', log=True, label="ROTB")
#plt.hist(HBD, range=(-20, +50), bins=100, histtype='step', log=True, label="HBD")
#define number of rows and columns for subplots
nrow=3
ncol=3
# make a list of all dataframes 
df_list = [ALOGP, MW ,HBA, HBD, PSA, ROTB, AROM, ALERTS]
fig, axes = plt.subplots(nrow, ncol)
# plot counter
count=0
for r in range(nrow):
    for c in range(ncol):
        df_list[count].plot(kind="hist")
        count+=1


#axis name and legend
#plt.xlabel("Property", size=14)
#plt.ylabel('N. Compounds', size=14)
#plt.legend(frameon=False, loc='upper right', ncol=2, title='Property')
#avoid cropping the labels
#plt.tight_layout() 
#plt.show()
#save picture
#plt.savefig("plot_logP.png", dpi=300)