# List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x: # if the item in fruits has an 'a' in it
        newlist.append(x) # add it to the newlist
print(newlist)

newlist = [x for x in fruits if "a" in x] # if the item in fruits has an 'a' in it add it to newlist
print(newlist)

newlist = [x for x in fruits if x != "apple"] # if the item in fruits in not 'apple' then add it to newlist
print(newlist)

newlist = [x for x in fruits] # add the items in fruits to newlist
print(newlist)

newlist = [x for x in range(10)] # add the items within range(10) to newlist
print(newlist)

newlist = [x for x in range(10) if x < 5] # if the item in range(10) is less than 5 add it to newlist
print(newlist)

newlist = [x.upper() for x in fruits] # add the items in fruits to newlist and capitalize them all
print(newlist)

newlist = ['hello' for x in fruits] # add hello to newlist for every item in fruits
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits] # add the items in fruits to newlist and if one is banana replace it with orange
print(newlist)