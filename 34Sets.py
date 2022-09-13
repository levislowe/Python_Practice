# Set

thisset = {"apple", "banana", "cherry"} # sets are unordered (unindexed) and unchangeable except items can be added and removed
print(thisset)

# Duplicates Not Allowed

thisset = {"apple", "banana", "cherry", "apple"} # the second 'apple' will be ignored
print(thisset)

# Get the Length of a Set

print(len(thisset))

# Set Items - Data Types

set1 = {"apple", "banana", "cherry"}
set2 = {1, 2, 3, 4, 5}
set3 = {True, False, True}
set4 = {"abc", 34, True, 40, "male"}

# tyoe()

print(type(thisset))

# The set() Constructor

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)