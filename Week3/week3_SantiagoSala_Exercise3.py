import math
print("Santiago Sala")
print("Week 3 Exercise 3: BMI calculator and description")
print("This program will calculate your BMI and will provide a description of your current situation.")

while True:
    height = input("To proceed enter your height in metres: ")    
    try:
        val = float(height)
        if val > 2.5:
            print("Your height is too much. Please enter height in metres.")
        else:
            break;
    except ValueError:
        print("This is not a number. Please enter a valid number.")

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
            print("This is not a number. Please enter a valid number.")

bmi = float(weight) / (float(height) * float(height))
current_bmi = round(bmi, 1)

if current_bmi >= 40:
    print("Your BMI result is: " + str(current_bmi) + ", according to the results your: MORBID OBESITY.")
elif current_bmi >= 30:
    print("Your BMI result is: " + str(current_bmi) + ", according to the results your: OBESITY.")
elif current_bmi >= 25:
    print("Your BMI result is: " + str(current_bmi) + ", according to the results your: OVERWEIGHT.")
elif current_bmi >= 18.5:
    print("Your BMI result is: " + str(current_bmi) + ", according to the results your: NORMAL WEIGHT.")
else:
    print("Your BMI result is: " + str(current_bmi) + ", according to the results your: UNDERWEIGHT.")



     

print("Thank you for playing.")
