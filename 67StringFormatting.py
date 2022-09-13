# String format()

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

txt = "The price is {:.2f} dollars"
print(txt.format(price))

# Multiple Values

itemno = 567
count = 2
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(count, itemno, price))

# Index Numbers

myorder = "I want {0} peices of item number {1} for {2:.2f} dollars."
print(myorder.format(count, itemno, price))

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# Named Indexes

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))