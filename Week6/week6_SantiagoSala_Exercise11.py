print("Santiago Sala")
print("Week 6 Exercise 11: Find the square root.")
print("This program will the square root of a given number\n")


def isFloat(message):
    while True:
        my_number = input(message)
        try:
            val_number = float(my_number)
            return val_number
        except ValueError:
            print("Please enter a valid number.\n")

def squareRoot(number):
    result = 0
    if number == 0:
        result = 0
    elif number > 0:
        result = number**(1/2)        
    else:
        number = number * (-1)
        result = number**(1/2) * (-1)
    return result
        

my_number = isFloat("Which number do you want to find the square root? ")
result_root = squareRoot(my_number)

print(f"The square root of {my_number} is {round(result_root, 2)}.")

print("\nThank you for playing.")
