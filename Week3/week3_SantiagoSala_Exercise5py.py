import math
print("Santiago Sala")
print("Week 3 Exercise 5: What kind of triangle.")
print("This program will tell what is the type of a triangle given its 3 sides.")

while True:
    first_side = input("Give the lenght of the traingles FIRST side: ")
    try:
        first_value = round(float(first_side), 2)
        break
    except ValueError:
        print("This is not a number. Please enter a valid number.")

while True:
    second_side = input("Give the lenght of the traingles SECOND side: ")
    try:
        second_value = round(float(second_side), 2)
        break
    except ValueError:
        print("This is not a number. Please enter a valid number.")


while True:
    third_side = input("Give the lenght of the traingles THIRD side: ")
    try:
        third_value = round(float(third_side), 2)
        break
    except ValueError:
        print("This is not a number. Please enter a valid number.")
 
if first_value == second_value and first_value == third_value:
    print("Your tringle is an EQUILATERAL TRIANGLE")
elif first_value != second_value and first_value != third_value and second_value != third_value:
    print("Your tringle is a SCALENE TRIANGLE")
else:
    print("Your tringle is a ISOCELES TRIANGLE")
    

print("Thank you for playing.")
