class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)

print(p1.name)
print(p1.age) 
p1.myfunc() 

class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')

# unexpectedly shared by all dogs
print(d.tricks,e.tricks)    

class Cat:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each cat
    
    def add_trick(self, trick):
        self.tricks.append(trick)
    

d = Cat('Fido')
e = Cat('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks,e.tricks)




# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g():
        return 'hello world'

    h = g

instance = C

print(instance.h(),instance.f(C,10,12))
