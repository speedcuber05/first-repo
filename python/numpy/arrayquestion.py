from numpy import *
arrq1=array([[1,1,1,1,1],
           [1,0,0,0,1],
           [1,0,9,0,1],
           [1,0,0,0,1],
           [1,1,1,1,1]])

arrans1=ones((5,5),dtype=int)
arr1=zeros((3,3),dtype=int)
arr1[1,1]=9
arrans1[1:4,1:4]=arr1
print(arrans1)

arrq2=arange(1,31).reshape(6,5)
print(arrq2)
arrans2i= arrq2[2:4,0:2]
print(arrans2i)
arrans2ii=arrq2[[0,1,2,3],[1,2,3,4]]
print(arrans2ii)
