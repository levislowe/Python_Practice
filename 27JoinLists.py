# Join Two Lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2 # Joins list1 and list2 two under list3
print(list3)

for x in list2: # all of the items in list2
    list1.append(x) # are appended at the end of list 1
print(list1) 

list1.extend(list2) # add the items from list2 to list1
print(list1)