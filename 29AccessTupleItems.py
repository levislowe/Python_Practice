# Access Tuple Items

thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) # prints the item in index 1

# Negative Indexing

print(thistuple[-1]) # prints the item in index -1 (also 2)

# Range of Indexes

thistuple = ("apple", "banana", "cherry", "kiwi", "melon", "mango")
print(thistuple[2:5]) # display the items in indexs 2 through 5 not including 5
print(thistuple[:5]) # display the items from the beginning to 5 not including 5
print(thistuple[2:]) # displays the items from 2 till the end of the tuple

# Range of Negative Indexes

print(thistuple[-4:-1]) # displays the items from -4 (also 2) through -1 (also 5) not including -1

# Check if Item Exists

if "apple" in thistuple: # checks to see if the item 'apple' is in the tuple
    print("Yes. apple is in this fruit tuple")