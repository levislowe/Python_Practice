# Add Items

thisset = {"apple", "banana", "cherry"}
thisset.add("orange") # adds orange to thisset
print(thisset)

# Add Sets

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical) # adds tropical to thisset
print(thisset)

# Add Any Iterable

mylist = ["tomato", "grape"]
thisset.update(mylist) # adds mylist to thisset
print(thisset)