# Use a Module

# import 58ModulesPart01 # This is how you normal import modules however there cannot be numbers at the front
mymodule = __import__("58ModulesPart01") # This is how you would do it with numbers at the front of the file

mymodule.greeting("Jonathan")

# Variables in Module

a = mymodule.person1["age"]
print(a)

# Re-naming a Module

# import 58ModulesPart01 as mx # This is how you would normally rename a module
mx = __import__("58ModulesPart01") # This is how you would rename a module if it starts with numbers

a = mx.person1["age"]
print(a)

# Built-in Modules

import platform

x = platform.system()
print(x)

# Using the dir() Function

x = dir(platform)
print(x)

# Import From Module

# from 58ModulesPart01 import person1 # This is how you normally would import from module in numbers where not at the from of the file
# print (person1["age"])