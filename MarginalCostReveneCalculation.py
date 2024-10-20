import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

a = float(input("Enter the coefficient a for the cost function (ax^2): "))
b = float(input("Enter the coefficient b for the cost function (bx): "))
c = float(input("Enter the constant c for the cost function: "))
d = float(input("Enter the coefficient d for the revenue function (dx): "))

x = sp.Symbol('x')

C = a * x**2 + b * x + c
R = d * x

MC = sp.diff(C, x)
MR = sp.diff(R, x)

print(f"Marginal Cost: {MC}")
print(f"Marginal Revenue: {MR}")

x_vals = np.linspace(0, 20, 100)
C_vals = [C.subs(x, i) for i in x_vals]
R_vals = [R.subs(x, i) for i in x_vals]
MC_vals = [MC.subs(x, i) for i in x_vals]
MR_vals = [MR.subs(x, i) for i in x_vals]

plt.plot(x_vals, C_vals, label='Total Cost')
plt.plot(x_vals, R_vals, label='Total Revenue')
plt.plot(x_vals, MC_vals, label='Marginal Cost', linestyle='dashed')
plt.plot(x_vals, MR_vals, label='Marginal Revenue', linestyle='dashed')
plt.xlabel('Quantity')
plt.ylabel('Cost/Revenue')
plt.title("Cost and Revenue Analysis")
plt.legend()
plt.show()
