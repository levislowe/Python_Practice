# Creating a Function

def my_function():
    print("Hello from a function")
    
# Calling a function

my_function()

# Arguments

def name_function(fname):
    print(fname + " Refsnes")
name_function("Emil")
name_function("Tobias")
name_function("Linus")

# Number of Arguments

def full_function(fname, lname):
    print(fname + " " + lname)
full_function("Emil", "Refsnes")

# Arbitrary Arguments, *args

def my_kids(*kids):
    print("The youngest child is " + kids[2])
my_kids("Emil", "Tobias", "Linus")

# Keyword Arguments

def my_children(child1, child2, child3):
    print("The youngest is " + child3)
my_children(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs

def new_function(**kid):
    print("His last name is " + kid["lname"])
new_function(fname = "Tobias", lname = "Regsnes")

# Default Parameter Value

def this_function(country = "Norway"):
    print("I am from " + country)
this_function("Sweden")
this_function("India")
this_function()
this_function("Brazil")

# Pass a List as an Argument

def my_meal(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_meal(fruits)

# Return Values

def num_function(x):
    return 5 * x
print(num_function(3))
print(num_function(5))
print(num_function(9))

# The pass Statement

def passfunction():
    pass # pass allows a function to exist without having anything in it

# Recursion

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print("\n\nRecursion Example Results")
tri_recursion(6)