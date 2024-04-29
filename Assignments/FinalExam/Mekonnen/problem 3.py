import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
# Define the variables and the transformation matrix
x, y, t = sp.symbols('x y t')
lambda_symbol = sp.symbols('lambda')
A = sp.Matrix([
    [2, 1],
    [16, 2]
])

# Find eigenvalues and eigenvectors
eigenvalues = list(A.eigenvals().keys())
eigenvectors = A.eigenvects()

# print(f"eigenvalues:")
# print(eigenvalues)
# print(f"eigenvectors:")
# print(eigenvectors)
# Print eigenvalues
print("Eigenvalues:")
for eigenvalue in eigenvalues:
    print(eigenvalue)

# Print eigenvectors
print("\nEigenvectors:")
for eigenvector in eigenvectors:
    sp.pprint(eigenvector[2][0])

# Write the general solution
c1, c2 = sp.symbols('c1 c2')
eigenvector1 = eigenvectors[0][2][0]  # First eigenvector
eigenvector2 = eigenvectors[1][2][0]  # Second eigenvector

# Construct the general solution
general_solution = c1 * eigenvector1 * sp.exp(eigenvalues[0] * t) + c2 * eigenvector2 * sp.exp(eigenvalues[1] * t)

print("\nGeneral Solution:")
sp.pprint(general_solution)

# Use initial conditions x(0) = 1 and y(0) = 0
initial_conditions = general_solution.subs(t, 0)  # Plug in t = 0

# System of equations for initial conditions
equations = [
    sp.Eq(initial_conditions[0], 1),  # x(0) = 1
    sp.Eq(initial_conditions[1], 0)  # y(0) = 0
]

# Solve for c1 and c2
constants = sp.solve(equations, (c1, c2))

# Specific solution using the found constants
specific_solution = general_solution.subs(constants)
print("\nSpecific Solution:")
sp.pprint(specific_solution)  # Return the specific solution given the initial conditions

# Define the variable range
t = np.linspace(0, 2, 100)  # from -2 to 2 with 100 points

# Define the functions
f_x = (np.exp(6 * t) / 2) + (np.exp(-2 * t) / 2)
f_y = -2 * np.exp(6 * t) + 2 * np.exp(-2 * t)

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(t, f_x, label='f(x) = (e^(6t) / 2) + (e^(-2t) / 2)', linestyle='-', color='b')
plt.plot(t, f_y, label='f(y) = -2 * e^(6t) + 2 * e^(-2t)', linestyle='-', color='r')
plt.xlabel('t')
plt.ylabel('Function Value')
plt.title('Plot of Functions f(x) and f(y) with respect to t')
plt.legend()
plt.grid(True)
plt.show()