import random
print("Santiago Sala")
print("Week 6 Exercise Bonus 2: Multiply 2 arrays.")
print("This program will multiply the values of two randomly generated arrays.\n")


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
        random_number = random.randint(-10, 10)
        while random_number == 0:
            random_number = random.randint(-10, 10)
            #print("It was  0!!")
        number_array.append(random_number)
    return number_array

def multiplyArray(array):
    result = 1
    for x in range(len(array)):
        result *= array[x]
    return result
    
       
size_one = isInt("What is the size of the first array? ")
first_array = generateArray(size_one)
result_one = multiplyArray(first_array)

size_two = isInt("What is the size of the second array? ")
second_array = generateArray(size_two)
result_two = multiplyArray(second_array)

result_final = result_one * result_two

print(f"The first random array is: {first_array}")
print(f"The second random array is: {second_array}")
print(f"The result of multiplying its elements is: {result_final}")
print("\nThank you for playing.")
