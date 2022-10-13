import math
print("Santiago Sala")
print("Week 3 Exercise 6: Which number is bigger")
print("This program will tell which number is bigger given 3 different numbers.")

while True:
    first_number = input("What is the FIRST number: ")
    try:
        first_value = float(first_number)
        break
    except ValueError:
        print("This is not a number. Please enter a valid number.")

while True:
    second_number = input("What is the SECOND number: ")
    try:
        second_value = float(second_number)
        if first_value == second_value:
            print("This number already exists, please pick another number.")
        else:
            break
    except ValueError:
        print("This is not a number. Please enter a valid number.")


while True:
    third_number = input("What is the THIRD number:  ")
    try:
        third_value = float(third_number)
        if third_value == first_value:
            print("Your number is the the same as the FIRST number. Please pick another number.")
        elif third_value == second_value:
            print("Your number is the the same as the SECOND number. Please pick another number.")
        else:    
            break
    except ValueError:
        print("This is not a number. Please enter a valid number.")

# First way
if first_value > second_value:
    result = first_value
else:
    result = second_value
    
if result < third_value:
    result = third_value

# Second way
def maxNumber (first, second, third):
    number_list = [first, second, third]
    return max(number_list)

# Third way
to_sort_list = [first_value, second_value, third_value]
sorted_list = sorted(to_sort_list)
 
print("First way: The biggest value of the given numbers is: " + str(result))
print("Second way: The biggest value of the given numbers is: " + str(maxNumber(first_value, second_value, third_value)))
print("Third way: The biggest value of the given numbers is: " + str(sorted_list[2]))   

print("Thank you for playing.")
