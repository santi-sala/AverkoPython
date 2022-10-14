import random

print("Santiago Sala")
print("Week 5 Exercise 5: Calculate the sum of two Arrays.")
print("This program will generate two random arrays, sum each element of the two arrays and sum each element of an arrays index and create a new array.\n")


def generateArray():
    current_index = 0
    number_array = []
    while current_index < 10:
        random_number = random.randint(0, 10)
        current_index += 1
        number_array.append(random_number)
        
    return number_array


def sumArray(first_array, second_array):
    i = 0
    result_array = []
    
    while i < len(first_array):
        array_element = first_array[i] + second_array[i]
        result_array.append(array_element)
        i += 1
        
    return result_array


def totalArraySum(first_array, second_array):
    i = 0
    total_result = 0

    while i < len(first_array):
        total_result += first_array[i] + second_array[i]
        i += 1

    return total_result
    

array_one = generateArray()
array_two = generateArray()
sum_array = sumArray(array_one, array_two)
total_sum = totalArraySum(array_one, array_two)

print(f"This is the first randomly generated array: {array_one}")
print(f"This is the second randomly generated array: {array_two}")
print(f"The result of the sum of each element of the array is: {sum_array}")
print(f"The total sum of all the elements of both arrays is: {total_sum}")


print("\nThank you for playing.")
