import numpy as np
import matplotlib.pyplot as plt

a = np.array([1, 2, 3, 4, 5, 6])
np.save('savearrayfile', a)
b = np.load('savearrayfile.npy')
csv_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
np.savetxt('new_file.csv', csv_arr)
c=np.loadtxt('new_file.csv')