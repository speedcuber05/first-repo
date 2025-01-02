thistuple = ("apple", "banana", "cherry", True, 1)
print(thistuple)
print(len(thistuple))
t=()               #its a tuple
tt=('hello',)      #without comma it is string
print(type(tt))

#indexing works the same as strings and lists
# to edit a value in tuple you can convert a tuple into list, edit and then convert back

l=list(thistuple)
ttt=tt+thistuple
tup=('pen','pencil','marker')
(a,b,c)=tup
print(a)     #this is called unpacking
fruits = ("apple", "banana", "cherry", "strawberry", "strawberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
fruit = ("apples", "mango", "papaya", "pineapple", "cherry",'pear')   
(grean, *tropic, read) = fruit    #asterrisk adjusts the length of lists depending on how many others are
print(grean)
print(tropic)
print(read)
print(fruits.count('strawberry'))
print(fruits.index('strawberry'))

