# Remove Item

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") # Removes the item banana from the thisset
print(thisset)

thisset.discard("apple") # Discard can also be used to remove and item from a set
print(thisset)

thisset.add("apple")
thisset.add("banana")
print(thisset)

x = thisset.pop() # pop can be used to move the item in the set to another variable
print(x)
print(thisset)

thisset.clear() # clear will remove all items inside of the set
print(thisset)

del thisset # deletes the entire set
print(thisset) 