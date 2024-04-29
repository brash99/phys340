import sympy as sp

# Define symbols for the real and imaginary parts
a1, b1, a2, b2 = sp.symbols('a1 b1 a2 b2')

# Define the complex numbers
z1 = a1 + b1 * sp.I
z2 = a2 + b2 * sp.I

# Compute the product of z1 and z2
product = z1 * z2

# Extract the real and imaginary parts of the product
real_part = sp.re(product)
imaginary_part = sp.im(product)

# The condition for a purely real product
condition = sp.simplify(imaginary_part) == 0

# Solve for the relationship between the real and imaginary parts of z2
solution = sp.solve(condition, b2)

# Compute the real number 'r' such that z2 = r * z1
r = sp.symbols('r')
r_expression = sp.solve(z2 - r * z1, r)[0]

# Display results
print("Condition for a purely real product:")
print(condition)
#
# print("Solution for b2 in terms of a1, b1, a2:")
print(solution)

print("Value of 'r' such that z1 = r * z2:")
sp.pprint(r_expression)
