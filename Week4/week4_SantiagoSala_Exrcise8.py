print("Santiago Sala")
print("Week 4 Exercise 8: Factorial of a number")
print("This program will calculate tthe factorial of a given number.\n")

first_number = 1
result = 1
while True:
    factorial = input("To proceed, what is your number? ")    
    try:
        val_factorial = int(factorial)
        print("")
        if val_factorial > 0:
            while first_number < val_factorial:
                first_number += 1
                result = first_number * result
        else:
            print("Please insert a POSITIVE number.")
        break;
    except ValueError:
        print("This is not a number. Please enter a valid WHOLE number")

print(f"The factorial of {factorial} is: {result}")
print("Thank you for playing")
