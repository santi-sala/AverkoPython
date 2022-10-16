import math
print("Santiago Sala")
print("Week 6 Exercise 4: Factorial of a given number.")
print("This program will calculate the FACTORIAL of a given number.\n")

def is_int(message):
    while True:
        my_number = input(message)
        try:
            val_number = int(my_number)
            if val_number > 0:
                return val_number
            else:
                print("Please enter a number bigger than 0.\n")
        except ValueError:
            print("Please enter a valid WHOLE number.\n")
            
def factorialNumber(number):
    result = math.factorial(number)
    return result
    
factorial_num = is_int("What is the number you want to know its factorial? ")

factorial_result = factorialNumber(factorial_num)

print(f"The factorial number of ({factorial_num}) is: {factorial_result}")

print("\nThank you for playing.")
