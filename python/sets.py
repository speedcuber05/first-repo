se={'nice','ok','good','ok'}    #sets don't have a order, the elements in a set can be shown in any random order
print(se)
for i in se:
    print(i)
print(len(se))
emp=set()                       #empty curly will set empty dictionary
se.add('fine')
print(se)
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)        #tropical(in this example) still remains btw
print(thisset)
thisset.remove('apple')
print(thisset)         #or you can also use discard or pop
set1 = {"a", "b", "c"}
set2 = {1, 2, 3,'a','b'}
set3 = {"John", "Elena",'a'}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)    #you can also join other data types with this method rather than | this method
print(myset)
myset2 = set1 | set2 | set3 |set4   #another way for union
print(myset2)
myset3=set1.intersection(set2)       #you can also join other data types with this method rather than & this method
print(myset3)
myset4=set1 & set2 & set3                 #another way for intersection
print(myset4)
myset5=set1.intersection_update(set2)
set5 = {"apple", "banana", "cherry"}
set6 = {"google", "microsoft", "apple"}
set5.intersection_update(set6)         #now set 5 only intersecting elements from set 6
print(set5)
set7 = {"apple", "banana", "cherry",'pineapple','orange'}
set8 = {"google", "microsoft", "apple",'orange'}
myset6=set7.difference(set8)    #you can also join other data types with this method rather than -   this method
print(myset6)
myset7=set7 - set8   #another way for difference
#difference_update is similar to intersection_update
myset8=set7.symmetric_difference(set8)    #removes all the common elements
print(myset8)
myset9=set7 ^ set8 #another way for symmetric difference
#symmetric_difference_update is similar to intersection_update

#ek baar https://www.w3schools.com/python/python_sets_methods.asp dekhlo aur bhi similar functions hai