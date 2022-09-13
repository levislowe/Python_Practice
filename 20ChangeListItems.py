# Change Item Value

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant" # changes banana to blackcurrant
print(thislist)

# Change a Range of Item Values

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"] # replace banana and cherry with blackcurrant and watermelon
print(thislist)
thislist[1:3] = ["honeydew"] # replace both blackcurrent and watermelon with honeydew
print(thislist)

# Insert Items

thislist.insert(2, "watermelon") # inserts watermelon into index 2 and pushes everything else to the right down one index
print(thislist)