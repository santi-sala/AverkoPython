import random

print("Santiago Sala")
print("Week 5 Exercise 2: Array maximum finder.")
print("This program will generate 30 random numbers, insert them into an array and finally finds the maximum value.")

number_array = []
current_index = 0

while current_index < 10:
    random_number = random.randint(0, 101)
    #print(str(random_number))
    current_index += 1
    number_array.append(random_number)

max_value = max(number_array)

print(f"This is the resulted array: {number_array}")
print(f"The MAX value of the array is : {max_value}.")

print("Thank you for playing.")
