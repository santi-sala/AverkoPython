import math
print("Santiago Sala")
print("Week 6 Exercise 13: Calculate proximation of sin(x) and cos(x).")
print("This program will calculate the proximate sin and cos of a given number.\n")

def isFloat(message):
    while True:
        my_number = input(message)
        try:
            val_number = float(my_number)
            return val_number
        except ValueError:
            print("Please enter a valid WHOLE number.\n")
            
def factorial(number):
    index = 1
    result = 1
    while index <= number:
        result *= index
        index += 1
    return result

def calcSin(x):
    result = x
    factor = 3
    for index in range(10):
        
        result -= x**factor / factorial(factor)
        factor += 2
        
        result += x**factor / factorial(factor)
        factor += 2
    return result

def calcCos(x):
    result = 1
    factor = 2
    for index in range(10):
        
        result -= x**factor / factorial(factor)
        factor += 2
        
        result += x**factor / factorial(factor)
        factor += 2
    return result


number_x = isFloat("Which number do you want to know the proximation of its sin and cos?  ")
number_radians = math.radians(number_x)
result_sin = calcSin(number_radians)
result_cos = calcCos(number_radians)
#sup = math.sin(number_radians)
#cos = math.cos(number_radians)
print(f"The sin({number_x}) is {round(result_sin, 4)} and the cos({number_x}) is {round(result_cos, 4)}.)")
#print(sup)
#print(cos)
print("\nThank you for playing.")
