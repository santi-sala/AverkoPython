import numpy
import random

print("Santiago Sala")
print("Week 5 Exercise 9: Calculate the correlation of students grades.")
print("This program will calculate the correlation of 10 students in their grades at math and english. \n")


def generateArray(max_elements, min_number, max_number):
    current_index = 0
    number_array = []
    while current_index < max_elements:
        random_number = random.randint(min_number, max_number)
        current_index += 1
        number_array.append(random_number)
        
    return number_array

# There are 10 students, and grades can be from 0 to 5
math_grades = generateArray(10, 0, 5)
english_grades = generateArray(10, 0, 5)

grades_correlation = numpy.corrcoef(math_grades, english_grades)

print(f"The students grades in math are: {math_grades}")
print(f"The students grades in english are: {english_grades}")
print("The coefficient correlation between math and english grades are:\n", grades_correlation)
print("\nThank you for playing.")
