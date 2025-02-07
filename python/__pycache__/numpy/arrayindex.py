from numpy import *
arr=array([[1,2,3,4],[5,6,7,8]])
print(arr[arr>3])
five_up = (arr > 2) | (arr == 3)
print(five_up)
a1=array([1,2,3,4,5])
a2=a1[0:3]
print(a2)
a2[2]=100    #value of a1 also changes here, a2 made in the previous line isn't a copy, but a2 points to a part of a1 *
print(a2)
print(a1)

# *if you want to create a copy , a2=array(a1[0:3]) or a2=a1.copy()