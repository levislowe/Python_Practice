# Unpacking a Tuple

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits # defining each index within the tuple by a color
print(green)
print(yellow)
print(red)

# Using Asterisk *

fruits = ("apple", "banana", "cherry", "strawberry", "respberry")
(green, yellow, *red) = fruits # Red is defined all of the rest of the values left after green and yellow
print(green)
print(yellow)
print(red)
(green, *tropic, red) = fruits # tropic is defined as all of the values left after green while leaving one for red at the end
print(green)
print(tropic)
print(red)