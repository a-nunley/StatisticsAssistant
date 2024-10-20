import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

x = sp.Symbol('x')

C = 0.5 * x**2 + 5 * x + 50
R = 10 * x

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


