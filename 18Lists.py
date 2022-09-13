# List

thislist = ["apple", "banana", "cherry"] # this is a string (ordered and changable)
print(thislist)

# Lists allow dupicates

newlist = ["apple", "banana", "cherry", "apple"]
print(newlist)

# List Length

print(len(thislist))
print(len(newlist))

# List Item - Data Types

list01 = ["apple", "banana", "cherry"]
list02 = [1, 2, 3, 4, 5]
list03 = [True, False, False]

list04 = ["abc", 34, True, 40, "Male"]

print(list01, list02, list03, list04)

# type()

print(type(thislist))

# The list() Constructor

thislist = list(("apple", "banana", "cherry")) # Needs double round brackets