# Remove Specified Item

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") # removes item banana from the list
print(thislist)

# Remove Specified Index

thislist = ["apple", "banana", "cherry"]
thislist.pop(1) # removes the item that is in index 1
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop() # removes the last item in the list
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0] # removes the item located in index 0
print(thislist)

del thislist # deletes the entire list

# Clear the List

thislist = ["apple", "banana", "cherry"]
thislist.clear() # clears all of the items out of the list
print(thislist)