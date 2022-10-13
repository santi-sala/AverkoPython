import sympy as sp
import numpy as np
print("Santiago Sala")
print("Week 4 Exercise 6: Solve equation")
print("This program will solve a equation give x")

x = sp.Symbol("x")

equation = sp.Eq(3*x**3-4*x**2+9*x+5, 0)

solution = sp.solve(3*x**3-4*x**2+9*x+5, cubics=False)

#sol_root = np.roots(sol)
print(solution)



print("Thank you for playing")
