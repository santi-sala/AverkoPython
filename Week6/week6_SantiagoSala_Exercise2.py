import statistics
print("Santiago Sala")
print("Week 6 Exercise 2: Average of given floats.")
print("This program will calculate the of given numbers, be it integers or floats.\n")

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

def calc_average(my_array):
    result = statistics.mean(my_array)
    return result

number_numbers = is_int("To proceed, how many numbers do you have? ")

result_array = create_numbers_array(number_numbers)

result_average = calc_average(result_array)

print(f"The average of the chosen numbers ({result_array}) is: {result_average}")

print("\nThank you for playing.")
