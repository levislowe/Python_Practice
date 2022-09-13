# Create a Class

class MyClass:
    x = 5
    
# Create Object

p1 = MyClass()
print(p1.x)

# The __init__() Function

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p2 = Person("John", 36)
print(p2.name)
print(p2.age)

# Object Methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
p3 = Person("John", 36)
p3.myfunc()

# The self Parameter

class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    def newfunc(abc):
        print("Hello my name is " + abc.name)
p4 = Person("John", 36)
p4.newfunc()

# Modify Object Properties

p4.age = 40

# Delete Object Properties

del p4.age

# Delete Objects

del p4

# The pass Statement

class Person:
    pass