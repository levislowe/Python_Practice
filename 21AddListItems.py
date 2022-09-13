# Append Items

thislist = ["apple", "banana", "cherry"]
thislist.append("orange") # adds orange to the end of the list
print(thislist)

# Insert Item

thislist.insert(1, "orange") # inserts orange into index 1 and pushes everthing to the right to the next index
print(thislist)

# Extend List

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) # adds the items in tropical to thislist
print(thislist)

# Add Any Iterable

thistuple = ("kiwi", "orange")
thislist.extend(thistuple) # adds the items in the tuple to thislist
print(thislist)