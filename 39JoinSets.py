# Join Two Sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) # joins set1 and set2 together as set3
print(set3)

set1.update(set2) # joins set2 with set1
print(set1)

# Keep ONLY the Duplicates

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y) # creates a new set and adds the items that are in both sets x and y
print(z)

x.intersection_update(y) # checks to see if there is two of the same item in the set and defines those items as x
print(x)

# Keep All, But NOT the Duplicates

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y) # returns the items in both sets unless the item in is both sets
print(z)

x.symmetric_difference_update(y) # returns and updates set x will all items in both x and y unless both sets have the same item
print(x)