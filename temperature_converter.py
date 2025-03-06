# Tempature converter

unit = input("Is the temperature is in C or F: ")
temp = float(input("Enter the temperature: "))

if unit == "C" or unit == "c":
    # C to F = 9*C/5+32
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is {temp} F")
elif unit == "F" or unit == "f":
    # F to C = F-32*5/9
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Fahrenheit is {temp} C")
else: 
    print(f"{unit} is an invalid unit")
