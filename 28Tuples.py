# Tuple

thistuple = ("apple", "banana", "cherry") # this is a tuple (ordered and unchangeable)
print(thistuple)

# Allow Duplicates

thistuple = ("apple", "banana", "cherry", "apple", "pineapple") # Tuples allow duplicates
print(thistuple)

# Tuple Length

print(len(thistuple)) # displays the length of the tuple

# Create Tuple With One Item

thistuple = ("apple",) # this is a tuple
print(type(thistuple))
thistuple = ("apple") # this is not a tuple
print(type(thistuple))

# Tuple Items - Data Types

tuple1 = ("apple", "banana", "cherry") # string type
tuple2 = (1, 5, 7, 9, 3) # integer type
tuple3 = (True, False, False) # boolean type
tuple4 = ("abc", 34, True, 40, "male")

# type()

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# The tuple() Constructor

thistuple = tuple(("apple", "banana", "cherry")) # not the double round-brackets
print(thistuple)