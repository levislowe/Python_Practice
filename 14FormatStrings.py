# String Format

age = 36
txt = "My name is John, I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

myneworder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myneworder.format(quantity, itemno, price))