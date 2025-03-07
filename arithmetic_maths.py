import math

# Basic arithmetic operator
# + Addition operator
print(f"3 + 5 = {3 + 5}")

# - Subtraction operator
print(f"3 - 5 = {3 - 5}")

# * multiplication operator
print(f"3 * 5 = {3 * 5}")

# / divison operator
print(f"3 / 5 = {3 / 5}")

# % modulus operator
print(f"3 % 5 = {3 % 5}")

# exponents operator
print(f"2 ** 3 = {2 ** 3}")

# Basic maths functions

# round(x)
# round off the number
print(f"round(2.9999) = {round(2.114)}")

# abs(x)
# absolute is distance from the 0 to whole number
print(f"abs(-4): {abs(4)}")

# pow(base, exponents)
print(f"pow(2, 3): {pow(2, 3)}")

# max(x,y,z)
# find out the maximum value
print(f"max(10,11.5,9): {max(10,11.5,9)}")
print(f"max(-10,-11.5,-9): {max(-10,-11.5,-9)}") # in negative the value which is closer to the 0 is bigger
print(f"max(-10,11.5,0.9): {max(-10,11.5,0.9)}")

print("\n\n\n")
# we can use amny maths functions by importing the maths module on the top
# import math

print("Printing the value of pi")
print(math.pi)

print("Printing the value of the e")
print(math.e)

print("Printing the square root of 9")
print(math.sqrt(9))

# math.ceil()
# it will round up the floating point number up
print("ceil(9.50): " + str(math.ceil(9.50)))
print("ceil(9.40): " + str(math.ceil(9.40)))

# math.floor()
# it will round down the floating point number up
print("floor(9.50): " + str(math.floor(9.50)))
print("floor(9.40): " + str(math.floor(9.40)))
