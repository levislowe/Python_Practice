# Access Items

thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # Gives banana
print(thislist[-1]) # -1 give the last item wich is cherry

# Range Index

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # prints index 2 through 5 while not including 5
print(thislist[:5]) # prints from beginning to index 5 while not including 5
print(thislist[2:]) # prints from index 2 to throught to the end
print(thislist[-4:-1]) # starting from index -4 (aka 3) and goes to -1 (aka 6)

# Check if Item Exists

if "apple" in thislist:
    print("Yes, 'apple' is in thislist")