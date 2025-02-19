import numpy as np
arr = np.array([1, 2, 3, 4, 5])   #we are using a list to convert into an array, tuple can be used too
print("this is a sample array",arr)

ar0=np.array(1)

ar1=np.array([1,2,3])

ar2=np.array([[1,2,3],
              [4,5,6],
              [7,8,9],
              [10,11,12]])

ar3=np.array([[[1,2,3]
              ,[4,5,6]],

              [[7,8,9]
            ,[10,11,12]]])

print("0 dimensions")
print("\n",ar0)
print(ar0.shape)
print(ar0.ndim)    
print("1 dimension")
print("\n",ar1)
print(ar1.shape)     #columns
print(ar1.ndim)
print("2 dimensions")    
print("\n",ar2)
print(ar2.shape)     #columns and rows
print(ar2.ndim)
print("3 dimensions")    
print("\n",ar3)
print(ar3.shape)     #columns and rows and pages/layers
print(ar3.ndim)
print(ar3.size)  #product of all the elements in shape