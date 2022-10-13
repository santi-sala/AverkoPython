import random

print("Santiago Sala")
print("Week 5 Exercise 4: Calculte the sum of two Arrays.")
print("This program will search a value from an array and gives its index.")


def generateArray():
    current_index = 0
    number_array = []
    while current_index < 10:
        random_number = random.randint(0, 10)
        current_index += 1
        number_array.append(random_number)
    return number_array

array_one = generateArray()
array_two = generateArray()

print(f"This is your array: {array_one}")
print(f"This is your array: {array_two}")
print(f"This is your array: {number_array}")

print("Thank you for playing.")
