import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

v0, omega, R, L, C, t = sym.symbols('v0 omega R L C t', real=True, positive=True)

V = v0*sym.exp(sym.I*omega*t)
ZR = R
ZL = sym.I*omega*L
ZC = 1/(sym.I*omega*C)

Z = ZR + ZL + ZC

I = V/Z

sym.pretty_print(I)

# Resistor, capacitor, and inductor values
R_val = 1000  # Resistance in ohms
C_val = 1e-5  # Capacitance in farads (1 µF)
L_val = 10e-4  # Inductance in henries (10 mH)

# Frequency range to analyze (10 Hz to 1 MHz)
frequencies = np.logspace(1, 6, 100)  # Logarithmic scale

# Angular frequencies
omega_vals = 2 * np.pi * frequencies

# Complex impedance of the parallel capacitor-inductor combination
Z_CL_num = (L_val * 1j * omega_vals) / (L_val * 1j * omega_vals +
                R_val * (C_val * L_val * -1 * omega_vals**2 + 1))

# Magnitude of the output voltage
magnitude_vals = np.abs(Z_CL_num)

# Phase of the output voltage
phase_vals = np.angle(Z_CL_num, deg=True)  # Phase in degrees

# Plot the magnitude and phase
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

# Magnitude plot
ax1.plot(omega_vals, magnitude_vals)
ax1.set_xscale('log')
ax1.set_title("Magnitude of V_out")
ax1.set_ylabel("Magnitude")
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)

# Phase plot
ax2.plot(omega_vals, phase_vals)
ax2.set_xscale('log')
ax2.set_title("Phase of V_out")
ax2.set_xlabel("Frequency (Hz)")
ax2.set_ylabel("Phase (degrees)")
ax2.grid(True, which='both', linestyle='--', linewidth=0.5)

# Display plots
plt.tight_layout()
plt.show()  # Show the plots

