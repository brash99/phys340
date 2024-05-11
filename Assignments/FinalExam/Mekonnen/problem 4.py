import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
# Define the symbols
x = sym.symbols('x')
n = sym.symbols('n', integer=True)
L = sym.symbols('L', real=True, positive=True)
pi = sym.pi

# Define the function
f = sym.Abs(x)
L = pi

# Calculate the Fourier coefficients
a0 = 1/L*sym.integrate(f, (x, -pi, pi))

an = 1/L*sym.integrate(f*sym.cos(n*pi*x/L), (x, -pi, pi))

bn = 1/L*sym.integrate(f*sym.sin(n*pi*x/L), (x, -pi, pi))


print(f'The Fourier coefficients are:')
print(f'a0:')
sym.pprint(a0)
print(f'an:')
sym.pprint(an)
print(f'bn:')
sym.pprint(bn)

fourier_series = a0/2 + sym.Sum(an*sym.cos(n*pi*x/L) + bn*sym.sin(n*pi*x/L), (n, 1, 5))
print("The Fourier series:")
sym.pprint(fourier_series)

# Plot the function and its Fourier series
x_vals = np.linspace(-1, 1, 1000)
f_vals = np.array([f.subs(x, val) for val in x_vals])
fourier_vals = np.array([fourier_series.subs(x, val) for val in x_vals])

plt.plot(x_vals, f_vals, label='f(x)')
plt.plot(x_vals, fourier_vals, label='Fourier series')
plt.legend()
plt.show()