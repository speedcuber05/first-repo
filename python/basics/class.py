class person:
    def __init__(self,n,a):                #we are giving variables wrt self
        self.name=n 
        self.age=a
    def fuct(t):
        print("hello my name is",t.name)   #t here is playing the same role as n for name
        return 1+2
    def __str__(t):                        #this is the only way to get an return value from a class
        return "right"
    
p1=person("devansh", 19)
print(p1.fuct())
print(p1)


class student(person):                    #this is what we call in heritance
    def __init__(self, n, a, y):
        super().__init__(n,a)            #import everything from person class
        self.gradyear= y
    def __str__(grad):
        return str(grad.gradyear)

s1=student("devansh", 19,2028)
print(s1)


mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))


class number:
  def __iter__(self):
    self.a = 1
    print(self.a)
    return self

  def __next__(self):
    self.a += 1
    if self.a > 20:
        raise StopIteration
    return self.a

n1=iter(number())
print(next(n1))
print(next(n1))
print(next(n1))
print(next(n1))
for x in n1:
   print("this is loop ",x) 


class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")      
boat1 = Boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747")     

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()