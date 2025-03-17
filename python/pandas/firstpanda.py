import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

s=pd.Series([1,24,2,5,np.nan,23,6])
print(s)

s1=pd.Series([2,3,4,5],['a','b','c','d'],name='something') 
print(s1)
s11=s1.rename('anything')    #this copies the series
s1.rename('anything else',inplace=True)
print(s1)

d = {"b": 1, "a": "d", "c": 2}
s2=pd.Series(d)
print(s2)
s3=pd.Series(d, index=["b", "c", "d", "a"])
print(s3)

print(s3.iloc[1])
print()
print(s3.iloc[0:2])
print(s1[s1 >=4])

s1['e']=25
print(s1)

s4=pd.Series(np.arange(10,51,10))
s5=pd.Series(np.arange(5))
print(s4+s5)
print(s4*2)