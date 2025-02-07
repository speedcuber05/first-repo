import numpy as np
ar11=np.array([1,2,3])
ar12=np.array([4,5,6])
print("sum",ar11+ar12)
print("\ndiff",ar11-ar12)
print("\nprod",ar11*ar12)
print("\nquo",ar11/ar12)
print(ar11*10)
print(ar11.sum())       #sum of all elements

# you can also use ar.min max mean std for standard deviation

ar21=np.array([[1,2],
              [3,4],
              [5,6]])

ar22=np.array([[7,8],
              [9,10],
              [11,12]])
ar23=np.array([[1,2,3],
             [4,5,6]])
print()
print("\nsum",ar21+ar22)
print("\ndiff",ar21-ar22)
print("\nprod",ar21*ar22)
print("\nquo",ar21/ar22)
print("\nmatrix product",ar21@ar23)
print("\ncumsum",ar21.cumsum(axis=0))
print("\ncumprod",ar23.cumprod(axis=1))
print(ar21*10)
print(ar21.sum(axis=0)) # [9 12]
print(ar21.sum(axis=1)) # [3 7 11]
                        #print(ar21+ar23) not possible
print()
print(ar21.transpose())
print(ar21.T)           #both transpose the array
print(np.flip(ar21))
print(ar21.ravel())
print(ar21.flatten())   #changes 2d to 1d, flatten assigns a copy to the varaible but in ravel, the variable points to the og one, like when you change the index

arran=np.random.default_rng().integers(10,size=(3,4))
print()
print(arran)
