# Loop Through a List

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
    
# Loop Through the Index Numbers

for i in range(len(thislist)):
    print(thislist[i])
    
# Using a While Loop

i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
    
# Looping Using List Comprehension

[print(x) for x in thislist]