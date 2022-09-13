# RegEx Module

import re

# RegEx in Python

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

# The findall() Function

x = re.findall("ai", txt)
print(x)

x = re.findall("Portugal", txt)
print(x)

# The search() Function

x = re.search("\s", txt)
print("The first white-space character is located in position: ", x.start())

x = re.search("Portugal", txt)
print(x)

# The split() Function

x = re.split("\s", txt)
print(x)

x = re.split("\s", txt, 1)
print(x)

# The sub() Function

x = re.sub("\s", "9", txt)
print(x)

x = re.sub("\s", "9", txt, 2)
print(x)

# Match Object

x = re.search("ai", txt)
print(x)

x = re.search(r"\bS\w+", txt)
print(x.span())

print(x.string)

print(x.group())