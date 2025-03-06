# -----------------------------------------------------------------------------------------------------------------------------------
# to check whether the sales is there or not.

# varibale which will acts as timer
sales_timing = 10

# user response will be save here
user_buy = 0

# Looping till the sales_timing is in range of 1 to 10
for sales_timing in range(0, 10):
    
    print("If you have buy anything then,  ")
    user_response = input("Enter Y for Yes or N for No: ")

    if user_response == 'Y' or user_response == 'y':
        print("Thank you for shopping with us")
    else:
        print("The sale is gonna end soon.... Hurry buy the necessary things, everything is 50% off.")
    
    sales_timing -= 1
else:
    print("\n")
    print("The sales has end. Thank you for coming to us.")
