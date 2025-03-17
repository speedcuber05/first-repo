import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"C:\Users\devan\Downloads\student_performance.csv")
print(df)
df.insert(4,'Total score',df['Math Score']+ df['Science Score']+ df['English Score'])
print(df)

print()

print(df.loc[0])    #here you provide the name of the row
print(df.iloc[1])   #here you provide index

print()
print(df.iloc[1:3 , 1:4])

print()
print(df.T)

