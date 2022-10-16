print("Santiago Sala")
print("Week 6 Exercise 1: Average of 2 integers.")
print("This program will calculate the the average of two integers. \n")

def is_int(message):
    while True:
        first_number = input(message)
        try:
            val_number = int(first_number)
            return val_number
        except ValueError:
            print("Please enter a valid WHOLE number.\n")

def calc_average(first_int, second_int):
    result = (first_int + second_int) / 2
    return result

first_number = is_int("To proceed, provide a WHOLE number. ")
second_number = is_int("Next, provide another whole number. ")

average = calc_average(first_number, second_number)

print(f"The average of the chosen numbers is: {average}")

print("\nThank you for playing.")
