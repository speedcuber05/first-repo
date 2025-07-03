import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data={'a':np.arange(11,16),'b':np.arange(10,51,10)}
df=pd.DataFrame(data)
print(df)

df['c']=df['a']+df['b']  #you can also do df.assign(column_name=data), this is create a copy of the df instead of editing it.
print(df)

df['no']=0     
print(df)
del df['no']
print(df)

df.insert(1,'middle',10)
print(df)

