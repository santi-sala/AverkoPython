import numpy
import random
print("Santiago Sala")
print("Week 6 Exercise 10: Find an elemnt in a array.")
print("This program will find the locations of a number from 0 to 9 from a randomly generated array.\n")


def isInt(message):
    while True:
        my_number = input(message)
        try:
            val_number = int(my_number)
            if val_number > -1 and val_number < 10:
                return val_number
            else:
                print("Enter a number bigger between 0 and 9.")
        except ValueError:
            print("Please enter a valid WHOLE number between 0 and 9.\n")

def generateArray():
    number_array = []
    for x in range(10):
        random_number = random.randint(0, 9)
        number_array.append(random_number)
    return number_array

def locateNumber(array, number):
    result = numpy.where(array == number)
    if len(result[0]) == 0:
        result = ["Sorry its not in the array...."]   
    return result

random_array = numpy.array(generateArray())
find_number = isInt("Which number from 0 to 9 do you want to know its location(s)? ")
number_location = locateNumber(random_array, find_number)

print(f"The indexes of {find_number} in the array {random_array} are: {number_location[0]}.")

print("\nThank you for playing.")
