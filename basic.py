
# this is a single line comments

'''
This is a multiple line comments
'''
# the interpeter ignore the comments.
# most of the time we will use the comments as a guide so that the others person can known about the particular function do

# -----------------------------------------------------------------------------------------------------------------------------------
# to print some thing we can use print("")
print("Hello...")

# -----------------------------------------------------------------------------------------------------------------------------------
# Data types
# Python has various types of data types but the basic data types are string, boolean, integers, float.

# string
first_name = "Tarun"
string_age = "21"

# integers
age = 21
fav_number = 1

# float
gpa = 9.5
price_of_a_manga = 500.00

# Boolean
i_like_manga = True
do_i_like_insect = False

# -----------------------------------------------------------------------------------------------------------------------------------
# variables
# variables are the containers to store the data.
# for example.
first_name = "Tarun Bhandari" # first_name is a variable that store the "Tarun Bhandari" as a value.

# so if i print the first_name variable, then it will print Tarun Bhandari as it's value
print("My name is " + first_name)

'''
    Below is the simple program which will print the basic information about myself. 
'''

name = "Tarun Bhandari"
age = 21
email = "heytaru@gmail.com"
contact_number = 1234567890

print(f"Hey it nice to meet you. My name is {name}")
print(f"I am {age} yrs old. I like many things but out of all I really like to code at night.")
print(f"My contact number is {contact_number}. You can connect with through my email, my email address is {email}")

# -----------------------------------------------------------------------------------------------------------------------------------
# Typecasting
# it is a process of converting one data type to another.
# let convert an integer type to float type

# integer
age = 21
print(f"age: {age}")
print(f"age is of {type(age)} data type") # type() can tell the data class of the value

# typecasting to float type
age = float(age)
print(age)
print(f"afte typecasting the age is of {type(age)} data type")

# like this we can convert the any data type to another data type by using below functions
# to convert in string data type str()
# to convert in integer data type int()
# to convert in float data type float()
# to convert in boolean data type bool()

# -----------------------------------------------------------------------------------------------------------------------------------
# Input()
# Input() helps us to take the input from the users.
# example

# taking the user name and printing it on the screen
name_of_user = input("Enter your name: ")
print(f"Your name is {name_of_user}")

# we can take others data type too from the user
user_age = int(input("Enter your age: "))
print(f"Your age is {user_age}")
