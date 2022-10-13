print("Santiago Sala")
print("Week 4 Exercise 9: Calculate the exponential value.")
print("This program will calculate tthe factorial of a given number.\n")


while True:
    base = input("To proceed, what is your BASE number? ")    
    try:
        val_base = float(base)
        break;
    except ValueError:
        print("This is not a number. Please enter a valid number")

while True:
    exponent = input("Next, what is the exponent? ")
    try:
        val_exponent = int(exponent)
        break
    except ValueError:
        print("Please enter a valid WHOLE number")

result = val_base ** val_exponent

print(f"The result of {val_base} with exponent {val_exponent} is {round(result, 2)}.")
print("Thank you for playing")
