# JSON in Python

import json

x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])

# Convert from Python to JSON

x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
y = json.dumps(x)
print(y)

# Format the Result

json.dumps(x, indent = 4)

# Order the Result

json.dumps(x, indent = 4, sort_keys = True)