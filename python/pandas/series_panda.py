import pandas as pd
import numpy as np

d = {'a': 1, 'b': 2, 'c': 3}
ser = pd.Series(data=d, index=['a', 'y', 'c','d'],name="the name is on the bottom in this",copy=False)  
print(ser)
print('\n')

#copy decides if the input is going to be a copy or a view

cities = ['Kolkata', 'Chicago', 'Toronto', 'Lisbon']
populations = [14.85, 2.71, 2.93, 0.51]
city_series = pd.Series(populations,cities)
print(city_series.index)
print(city_series)