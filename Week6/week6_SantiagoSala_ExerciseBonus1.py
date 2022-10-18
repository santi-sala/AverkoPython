import numpy
import random
print("Santiago Sala")
print("Week 6 Exercise Bon us 1: Selection sort.")
print("This program will sort from smallest to biggest from randomly generated array.\n")


def isInt(message):
    while True:
        my_number = input(message)
        try:
            val_number = int(my_number)
            if val_number > 0:
                return val_number
            else:
                print("Enter a number bigger than 0.")
        except ValueError:
            print("Please enter a valid WHOLE number between 0 and 9.\n")

def generateArray(size):
    number_array = []
    for x in range(size):
        random_number = random.randint(-100, 100)
        number_array.append(random_number)
    return number_array

def selectionSort(array, size):
    for index in range(size):
        minimum_index = index
        for i in range(index + 1, size):
            if array[i] < array[minimum_index]:
                minimum_index = i
        # Where magic happens, "swapping"
        (array[index], array[minimum_index]) = (array[minimum_index], array[index])
       
size = isInt("What is the size of the array? ")
random_array = generateArray(size)

print(f"The random array is: {random_array}")

selectionSort(random_array, size)
print(f"After sorting it becomes: {random_array}")

print("\nThank you for playing.")
