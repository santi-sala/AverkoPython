print("Santiago Sala")
print("Week 3 Exercise 1: Greater or smaller than 100.")
print("This program will tell if given number is greater or smaller than 100")

while True:
    my_number = input("Give me a number: ")
    try:
        value = float(my_number)
        break
    except ValueError:
        print("This is not a number. Please enter a valid number.")

if value == 100:
    print("Your entered number is equal to 100.")
elif value > 100:
    print("Your entered number is GREATER than 100.")
else:
    print("Your entered number is LESS than 100.")

print("Thank you for playing.")
