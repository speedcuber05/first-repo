import numpy as np
ar0=np.zeros(3)                 #will create floats 
ar1=np.ones(4,dtype=np.int8)    #will give me integer because I mentioned it
arem=np.empty(5)                #any 5 values at random will come, usually its 0 only idk why
arar=np.arange(2,9,2,dtype=np.int8)           # will get me [2,4,6,8] in integer
ares=np.linspace(0,100,5)       #this will get me [0,25,50,75,100]  in float
ard21=np.array([[1,2,3],
               [4,5,6]])
ard22=np.array([[7,8,9],
                [10,11,12]])
arr=np.array([11,22,33,44,55,66])
print(ar0)
print(ar1)
print(arem)
print(arar)
print(ares)
print(np.sort(ares))            #will give ascending order, ares is already ascending in this case btw
print(np.concatenate((ar1,arar,ares))) #add them up
print()
print(np.concatenate((ard21,ard22),axis=0))
print()
print(np.concatenate((ard21,ard22),axis=1))
print(np.reshape((arr),shape=(2,3)))