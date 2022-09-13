# Sort List Autoanumerically

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() # default sort is by alphabet with strings
print(thislist)

thatlist = [100, 50, 65, 82, 23]
thatlist.sort() # default sort is least to greatest with integers
print(thatlist)

# Sort Descending

thislist.sort(reverse = True) # sorts by alphabet by backwards
print(thislist)

thatlist.sort(reverse = True) # sorts from greatest to least
print(thatlist)

# Customize Sort Function

def myfunc(n):
    return abs(n - 50)
thatlist.sort(key = myfunc)
print(thatlist)

# Case Insensitive Sort

thislist = ["banana", "Orange", "kiwi", "Cherry"] # All capitals will be sorted before lowercase
thislist.sort()
print(thislist)
thislist.sort(key = str.lower) # compares each letter as a lowercase letter before sorting
print(thislist)

# Reverse Order

thislist.reverse() # sorts backwards but is not case sensitive
print(thislist)