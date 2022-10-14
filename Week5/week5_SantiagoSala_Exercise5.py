import random

print("Santiago Sala")
print("Week 5 Exercise 5: Generate a lotto row.")
print("This program will generate lotto rows.\n")


def is_int(message):
    while True:
        number_rows = input(message)
        try:
            val_rows = int(number_rows)
            if val_rows > 0:
                return val_rows
            else:
                print("Please enter a number BIGGER than 0.\n")
        except ValueError:
            print("Please enter a valid WHOLE number.\n")
            
def generate_numbers(message_one, message_two):
    starting_number = is_int(message_one)
    ending_number = is_int(message_two)
    result = []
    
    while starting_number <= ending_number:
        result.append(starting_number)
        starting_number += 1
    return result
        

def generate_lotto_row(rows, sequence):
    i = 0
    while i < rows:
        lotto_row = random.sample(sequence, 7)
        lotto_row.sort()
        print(f"{lotto_row}")
        i += 1
    return ""

number_rows = is_int("How many rows do you want for your lotto? ")
lotto_numbers = generate_numbers("What is the starting number? ", "What is the ending number? " )


print("\nYour lotto rows are:")
print(f"{generate_lotto_row(number_rows, lotto_numbers)}")


print("Thank you for playing.")
