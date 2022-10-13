import random

print("Santiago Sala")
print("Week 5 Exercise 1: Calculate random values from an array")
print("This program will generate 30 random numbers, insert them into an array and finally sum their values")

number_array = []
current_index = 0

while current_index < 30:
    random_number = random.randint(0, 101)
    #print(str(random_number))
    current_index += 1
    number_array.append(random_number)

def getSum(myArray):
    my_sum = 0
    for x in myArray:
        my_sum += x
    return my_sum

sum_result = getSum(number_array)
array_elements = len(number_array)
average_result = round(sum_result / array_elements, 2)


print(f"The sum of the array is : {sum_result}.")
print(f"The average of the the array is: {average_result}.")

print("Thank you for playing.")
