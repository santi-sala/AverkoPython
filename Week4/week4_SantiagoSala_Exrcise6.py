from sympy import symbols, Eq, solve
import math
print("Santiago Sala")
print("Week 4 Exercise 6: Solve equation")
print("This program will solve a given equation.")


x = symbols('x')
eq1 = Eq(3*x*x*x-4*x*x+9*x+5, x)

sol = solve(eq1, dict=True)

print("The solutions are: \n")
print(f"{sol[0]}\n")
print(f"{sol[1]}\n")
print(f"{sol[2]}\n")

print("Thank you for playing")
