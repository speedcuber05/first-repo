import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

s=pd.Series([1,24,2,5,np.nan,23,6])
print(s)
dates=pd.date_range('20051210',periods=5)
df=pd.DataFrame(np.arange(20).reshape(5,4),index=dates,columns=list("abcd"))
print(df)