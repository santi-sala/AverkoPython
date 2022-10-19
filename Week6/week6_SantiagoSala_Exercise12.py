print("Santiago Sala")
print("Week 6 Exercise 12: Calculate proximation of Neper's Value.")
print("This program will calculate the proximate of Nepers value.\n")

def isInt(message):
    while True:
        my_number = input(message)
        try:
            val_number = int(my_number)
            if val_number >= 0:
                return val_number
            else:
                print("Please enter a a number 0 or BIGGER.\n")
        except ValueError:
            print("Please enter a valid WHOLE number.\n")
            
def factorial(number):
    index = 1
    result = 1
    while index <= number:
        result *= index
        index += 1
    return result

def nepersAproximation(aprox_number):
    result = 2
    if aprox_number == 0:
        result = 1
    elif aprox_number == 1:
        result = 2
    else:
        for x in range(2, aprox_number + 1):
            print(x)
            result += 1 / factorial(x)
    return result

members = isInt("How close you want to get to Neper's value? ")
result = nepersAproximation(members)
print(f"The Nepers value is {result} with an aproximation of {members}.")


print("\nThank you for playing.")
