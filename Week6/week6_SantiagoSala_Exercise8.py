print("Santiago Sala")
print("Week 6 Exercise 8: Amount of combinations.")
print("This program will calculate the amount of combinations given the the whole set and the subset.\n")

def isInt(message):
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
            
def factorial(number):
    index = 1
    result = 1
    while index < number:
        result *= index
        index += 1
    return result

def amountCombinations(whole_set, subset):
    result = factorial(whole_set)/factorial(whole_set - subset) * factorial(subset)
    return result

whole_set = isInt("What is the the whole set? ")
subset = isInt("What is the subset? ")
result_combination = amountCombinations(whole_set, subset)
print(f"The amopunt of combinations of are: {result_combination}")

print("\nThank you for playing.")
