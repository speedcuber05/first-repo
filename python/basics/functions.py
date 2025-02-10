def name(fname,lname,mname="kumar"):         #default arugments are put in last
    print(fname,mname,lname)

name("devansh","mehrotra",)               
name("devansh","mehrotra",'you can change that')                            #default argument can be changed like this
name(mname='you can still change that',lname='mehrotra',fname='devansh')    #or like this
#keyword and positional have no practical difference, mainly terminology hai

cube= lambda x : x**3    #function without a name, even I don't understand it
print(cube(8))   

def area(l,b):
    return l*b      #returns the value
print(area(4,5))

def something():
    '''this is docstring, its like a special kind of comment'''    #this HAS to be the first line after defining the function
    print('something')
something()
print(something.__doc__)

def factorial(n):
    if n==0 or n==1:
        f=1
    else:
        f=n*factorial(n-1)     #this is called recursion, using the function inside the function itself
    return f
print(factorial(5))

def vowels(s: str) -> str:
    c=0
    for i in s:
        if i in "aeiouAEIOU":
            c+=1
    if c%2==0:
        return "yes"
    else:
        return "no"
    pass

a=vowels("xayyqez")
print(a)
b=vowels("ssty")
print(b)
#another way of writing functions