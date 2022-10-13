import math
print("Santiago Sala")
print("Week 4 Exercise 6: Solve equation")
print("This program will solve a equation give x")

while True:
    x = input("To proceed, what is the value of X: ")    
    try:
        val_x = float(x)
        break;
    except ValueError:
        print("This is not a number. Please enter a valid number")

solution_one = 3*val_x**3-4*val_x**2+9*val_x+5
solution = math.sqrt(solution_one)


print(f'If X is {val_x}, the answer is: {solution_one} and its aquare root is: {round(solution, 2)}')
print("Thank you for playing")
