import numpy as np

ar1=np.arange(1,11)
ar2=np.arange(1,21).reshape(-1,5)
ar3=np.arange(1,28).reshape(-1,3,3)
print(ar1,ar1[4],sep="\n\n",end="\n\n")
print(ar1,ar1[-3],sep="\n\n",end="\n\n")
print(ar2,ar2[1,2],sep="\n\n",end="\n\n")
print(ar2,ar2[2][1],sep="\n\n",end="\n\n") 
print(ar2,ar2[2,...],sep="\n\n",end="\n\n")
print(ar1,ar1[np.array([4,1,2])],sep="\n\n",end="\n\n")  #prints indexes 4,1,2 individually in a 1d array form
print(ar2,ar2[np.array([0,1,2]),np.array([2,1,2])],sep="\n\n",end="\n\n")
print(ar2,ar2[np.array([1,2]),np.array([0,3])],sep="\n\n",end="\n\n")
print(ar2,ar2[np.ix_(np.array([1,2]),np.array([0,3]))],sep="\n\n",end="\n\n")
print(ar3.base is None)  #checks if an array is a view or a copy, reshape makes a view hence in this example this is false

#x = np.arange(5)
#print(x[:, np.newaxis] + x[np.newaxis, :])
#print(x)
