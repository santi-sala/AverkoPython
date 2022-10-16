import math
print("Santiago Sala")
print("Week 6 Exercise 7: Biggest of them all.")
print("This program will return the biggest of the given numbers.\n")

def is_int(message):
    while True:
        my_number = input(message)
        try:
            val_number = int(my_number)
            if val_number > 0:
                return val_number
            else:
                print("Enter a number bigger than 0")
        except ValueError:
            print("Please enter a valid WHOLE number.\n")
            
def createNumbersArray(array_items):
    my_numbers = []
    
    for x in range(array_items):
        new_item = is_float(f"This is the {x + 1} number out of {array_items}. Type a number. ")
        my_numbers.append(new_item)
        
    return my_numbers

def is_float(message):
    while True:
        my_number = input(message)
        try:
            val_number = float(my_number)
            return val_number
        except ValueError:
            print("Please enter a valid number.\n")

numbers_array = createNumbersArray(is_int("How many numbers do you have? "))

result_array = numbers_array.copy()
result_array.sort(reverse = True)


print(f"The biggest number of the given numbers ({numbers_array}) is: {result_array[0]}")

print("\nThank you for playing.")
