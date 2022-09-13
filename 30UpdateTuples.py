# Change Puple Values

x = ("apple", "banana", "cherry")
y = list(x) # since tuples are unchanging, convert the tuple into a list
y[1] = "kiwi" # change to value of index 1 to 'kiwi'
x = tuple(y) # convert the list back into a tuple
print(x)

# Add Items

thistuple = ("apple", "banana", "cherry")
y = list(thistuple) # convert the tuple into a list
y.append("orange") # append 'orange' to the end of the list
thistuple = tuple(y) # convert the list back to a tuple
print(thistuple)

y = ("grape",) # defining y as a tuple
thistuple += y # adding y to thistuple
print(thistuple)

# Remove Items

thistuple = ("apple", "banana", "cherry")
y = list(thistuple) # convert thistuple into a list
y.remove("apple") # remove 'apple'
thistuple = tuple(y) # convert the list back into a tuple
print(thistuple)

del thistuple # this deletes the entire tuple