import statistics
print("Santiago Sala")
print("Week 6 Exercise 3: Sum of given numbers.")
print("This program will calculate the SUM of given numbers, be it integers or floats.\n")

def is_int(message):
    while True:
        my_number = input(message)
        try:
            val_number = int(my_number)
            return val_number
        except ValueError:
            print("Please enter a valid WHOLE number.\n")

def is_float(message):
    while True:
        my_number = input(message)
        try:
            val_number = float(my_number)
            return val_number
        except ValueError:
            print("Please enter a valid number.\n")

def create_numbers_array(array_items):
    my_numbers = []
    
    for x in range(array_items):
        new_item = is_float(f"This is the {x + 1} number out of {array_items}. Type a number. ")
        my_numbers.append(new_item)
        
    return my_numbers

def sumArray(my_array):
    result = 0
    
    for x in range(len(my_array)):
        result += my_array[x]
    
    return result

number_numbers = is_int("To proceed, how many elements has your array? ")

result_array = create_numbers_array(number_numbers)

result_sum = sumArray(result_array)

print(f"The sum of the chosen numbers ({result_array}) is: {result_sum}")

print("\nThank you for playing.")
