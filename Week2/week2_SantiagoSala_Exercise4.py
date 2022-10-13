import math
print("Santiago Sala")
print("Week 2 Tasks")
print("Exercise 4: Calculate BMIl")
print("This program will calculate BMI given the user height and weigth.")

while True:
    height = input("To proceed enter your height in metres: ")    
    try:
        val = float(height)
        if val > 2.5:
            print("Your height is too much. Please enter height in metres.")
        else:
            break;
    except ValueError:
        print("This is not a number. Please enter a valid number")


while True:
    weight = input("Next, what is your weight: ")
    try:
        val = int(weight)
        break;
    except ValueError:
        try:
            float(weight)
            break;
        except ValueError:
            print("This is not a number. Please enter a valid number")

bmi = float(weight) / (float(height) * float(height))
print("Your BMI is: " + str(round(bmi, 1)))

print("Thank you. Have a nice day.")




