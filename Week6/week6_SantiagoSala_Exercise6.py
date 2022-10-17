import math
print("Santiago Sala")
print("Week 6 Exercise 6: BMI calculator.")
print("This program will calculate the BMI given the height and the weight.\n")

def isFloat(message, height):
    while True:
        my_number = input(message)
        try:
            val_number = float(my_number)
            if height == True and val_number < 2.75 and val_number > 0.5:
                return val_number
            elif height == True and val_number > 2.75:
                print("You are the tallest person ever!! (You cant be more than 2.75 METRES...)")
            elif height == True and val_number < 0.5:
                print("You are the shortest person ever!! (You cant be less than 0.5 METRES...)")
            elif height == False and val_number < 640 and val_number > 10:
                return val_number
            elif height == False and val_number < 10:
                print("You are very skinny, maybe you should check your weight?")
            else:
                print("You are the heaviest person ever!! (You cant be more than 640 KGs...)")
        except ValueError:
            print("Please enter a valid number.\n")

def calculateBMI(height, weight):
    bmi = weight / (height * height)
    return bmi

height = isFloat("Enter your height in METRES: ", True)
weight = isFloat("Enter your weight in KILOGRAMS: ", False)

bmi = round(calculateBMI(height, weight), 2)

print(f"Your height is {height} METRES and your weight is {weight}. Your current BMI is {bmi}")

print("\nThank you for playing.")
