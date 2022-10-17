import math
import statistics
print("Santiago Sala")
print("Week 6 Exercise 9: Calculate the standard deviation.")
print("This program will calculate the standard deviation of an array.\n")

def deviationType():
    
    while True:
        deviation_type = input("Are you calculating the standard deviation of a (S)AMPLE or a (P)OPULATION? ")
        if deviation_type.lower() == "s":
            result = "sample"
            return result
        elif deviation_type.lower() == "p":
            result = "population"
            return result
        else:
            print("Please type either \"s\" for SAMPLE or \"p\" for POPULATION. \n")
         
def is_int(message):
    while True:
        my_number = input(message)
        try:
            val_number = int(my_number)
            if val_number > 1:
                return val_number
            else:
                print("Enter a number bigger than 0")
        except ValueError:
            print("Please enter a valid WHOLE number.\n")
            
def createNumbersArray(array_items):
    my_numbers = []
    
    for x in range(array_items):
        new_item = is_float(f"This is the {x + 1} number out of {array_items}. Type a number. ")
        my_numbers.append(new_item)
        
    return my_numbers

def is_float(message):
    while True:
        my_number = input(message)
        try:
            val_number = float(my_number)
            if val_number > 0:
                return val_number
            else:
                print("Enter a number bigger than 0")
        except ValueError:
            print("Please enter a valid number.\n")

def standardDeviation(deviation_type, data):
    if deviation_type == "sample":
        result = statistics.stdev(data)
    else:
        result = statistics.pstdev(data)
    return result
            
    
deviation_type = deviationType()
numbers_array = createNumbersArray(is_int(f"How many numbers does your {deviation_type} have? "))
result_deviation = standardDeviation(deviation_type, numbers_array)

print(f"The standard deviation of the {deviation_type} {numbers_array} is {round(result_deviation, 2)}.")

print("\nThank you for playing.")
