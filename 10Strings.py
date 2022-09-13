# Strings

print("Hello")
print('Hello')

# Assign String to a Variable

a = "Hello"
print(a)

# Multiple Strings

a = """This is an example of
multiline string"""
print(a)

a = '''This is another example
of a multiline string'''
print(a)

# String are Arrays

a = "Hello World!"
print(a[1])

# Looping Through a String

for x in "banana":
    print(x)
    
# String Length

a = "Hello World!"
print(len(a))

# Check String

txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
    print("Yes, 'free' is present.")
    
# Check if NOT

print("expensive" not in txt)

if "expensive" not in txt:
    print("No, 'expensive' is NOT present")