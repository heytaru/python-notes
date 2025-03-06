# IF statements
# if condition:
#   Perform 
# else:
# perform
# example

age = int(input("Enter your age: "))
if age < 18:
    print("You are not adult")
else:
    print("You are adult.")

# elif statements
# if condition: 
#   perform
# elif condition:
#   perform
# else:
#   perform

age = int(input("Enter age: "))
if age >= 18:
    print("You are an adult")
elif age < 0:
    print("Please enter proper age")
else:
    print("You are not an adult.")