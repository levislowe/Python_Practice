# Accessing Items

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
x = thisdict["model"]
print(x)

x = thisdict.get("brand")
print(x)

# Get Keys

x = thisdict.keys()
print(x)

# Get Values

x = thisdict.values()
print(x)

# Get Items

x = thisdict.items()
print(x)

# Check if Key Exists

if "model" in thisdict:
    print("Yes, model is one of the keys in the thisdict dictionary")