
import pandas as pd

# load data
data=pd.read_excel("ori.xlsx",sheet_name="Sheet1")

# generate dic
dic_kvs = {}
for icol in range(data.shape[0]):
    k = data.iloc[icol,0]
    v = data.iloc[icol,1]
    if k in dic_kvs:
        dic_kvs[k] = dic_kvs[k] + ";" + v
    else:
        dic_kvs[k] = v

# add " " for value
for k in dic_kvs:
    val = "\"" + dic_kvs[k] + "\""
    dic_kvs.update({k:val})

# convert dic to framedata
df = pd.DataFrame(list(dic_kvs.items()))
# write
writer = pd.ExcelWriter("/home/zvision/zvision/data/da_save.xlsx")
df.to_excel(writer,sheet_name='sheet_1',index=False,header=False)
# save
writer.save()