import numpy as np
a1 = np.array([[1, 1],
               [2, 2]])

a2 = np.array([[3, 3],
               [4, 4]])
print(np.vstack((a1,a2)))
print()
print(np.hstack((a1,a2)))

x=np.arange(1,25).reshape(2,12)
print(x)
x4=np.hsplit(x,4)  #gives a list of 3 arrays 
for i in x4:
    print(i)
    print()

def fun(a,b):
    return 10*a + b

a3=np.fromfunction(fun,(3,4))
print(a3)
