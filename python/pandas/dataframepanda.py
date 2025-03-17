import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

d = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
}
df = pd.DataFrame(d)
print(df)
print(pd.DataFrame(d, index=["d", "b", "a"]))
print(pd.DataFrame(d, index=["d", "b", "a"], columns=["two", "three"]))

print()

d1 = {"one": [1.0, 2.0, 3.0, 4.0], "two": [4.0, 3.0, 2.0, 1.0]}
df1=pd.DataFrame(d1)
print(df1)

print()

d2=np.arange(1,11).reshape(-1,2)
df2=pd.DataFrame(d2)
print(df2)

print()

d3 = [{"a": 1, "b": 2}, {"a": 5, "b": 10, "c": 20}]
df3=pd.DataFrame(d3)
print(df3)  