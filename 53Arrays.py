# Arrays

cars = ["Ford", "Volvo", "BMW"]

# What is an Array?

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

# Access the Elements of an Array

x = cars[0] #Defining x as the item set at cars[0]
print(x)

cars[0] = "Toyota"
x = cars[0]
print(x)

# The Length of an Array

x = len(cars)
print(x)

# Looping Array Elements

for x in cars:
    print(x)
    
# Adding Array Elements

cars.append("Honda")
print(cars)

# Removing Array Elements

cars.pop(3)
print(cars)

cars.remove("Volvo")
print(cars)