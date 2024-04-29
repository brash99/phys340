import sympy as sp

# Define the variables
x, y = sp.symbols('x y')

# Define the function for G(x, y, z)
G = x

# Define the surface element dS
ds = sp.sqrt(1 + 4 * x * x)

# Define the integral
integral = sp.integrate(x * ds, (x, 0, sp.sqrt(2)), (y, 0, 4))

print(integral)