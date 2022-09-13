# Boolean Values

print(10 > 9) # Returns true
print(10 == 9) # Returns false
print(10 < 9) # Returns false

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
    
# Evaluate Values and Variables

# Most values are true
print(bool("Hello"))
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

# Some Values are False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# Functions can Return a Boolean

def myFunction():
    return True

if myFunction():
    print("YES")
else:
    print("NO")
    
x = 200
print(isinstance(x, int))