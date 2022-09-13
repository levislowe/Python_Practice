# Dictionary

#Dictionary is a collection which is ordered and changeable with no duplicates
thisdict = { # creates a dictionary that information can be stored in
    "brand": "Ford",
    "electric": False,
    "model": "Mustang",
    "year": 1964,
    "year": 2020, # duplicate values will overwrite existing ones
    "color": ["red", "white", "blue"]
}
print(thisdict)

# Dictionary Items

print(thisdict["brand"])

# Dictionary Length

print(len(thisdict))

# Data Types

print(type(thisdict))