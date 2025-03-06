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

# -----------------------------------------------------------------------------------------------------------------------------------
# elif statements
# if condition: 
#   perform
# elif condition:
#   perform
# else:
#   perform

age = int(input("Enter age: "))
if age < 0:
    print("Please enter proper age")
elif age >= 100:
    print("You should be dead")
elif age >= 18:
    print("You are an adult")
else:
    print("You are not an adult.")

# -----------------------------------------------------------------------------------------------------------------------------------
# 1 examples
# 1 - to check whether the items are in sales or not. - item_sales.py