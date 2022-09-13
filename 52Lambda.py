# Syntax

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Why Use Lambda Functions?

def myFunc(n):
    return lambda a : a * n
mydoubler = myFunc(2)
print(mydoubler(11))

mytripler = myFunc(3)
print(mytripler(11))