import statistics
import random

print("Santiago Sala")
print("Week 5 Exercise 8: Calculating standard deviation")
print("This program will calculate the standard deviation of a random array with 20 elements. \n")


def generateArray(max_elements, min_number, max_number):
    current_index = 0
    number_array = []
    while current_index < max_elements:
        random_number = random.randint(min_number, max_number)
        current_index += 1
        number_array.append(random_number)
        
    return number_array

my_array = generateArray(20, 1, 20)
standard_deviation_sample = statistics.stdev(my_array)
standard_deviation_population = statistics.pstdev(my_array)
print(f"The array is: {my_array}")
print(f"The standard deviation of the current array (sample) is: {standard_deviation_sample}")
print(f"The standard deviation of the current array (population) is: {standard_deviation_population}")

print("\nThank you for playing.")
