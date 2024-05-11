import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# Part B: The Impedance becomes purely resistant at the resonant frequency
# and the circuit reaches maximum amplitude and magnitude.
# Essentially, most of the traits of the circuit are at their maximum at the resonance frequency of 1/sqrt(LC)

# Resistor, capacitor, and inductor values
Resistor = 1000  # Resistance in Ohms (1 kΩ)
Capacitor = 0.000001  # Capacitance in Farads (1 µF)
Inductor = 0.00001  # Inductance in Henry (10 µH)

# Analyzing frequency range
Frequency = np.logspace(4, 5, 1000)

# Resonance frequency.
Resonance_Frequency = (1 / (np.sqrt(Inductor * Capacitor))) * Frequency

# Angular frequency
Omega = 2 * pi * Frequency

# Impedance of the general and resonance frequency
Imp = (Inductor * 1j * Omega) / (Inductor * 1j * Omega + Resistor * (Capacitor * Inductor * -1 * Omega**2 + 1))
Res_Imp = ((Inductor * 1j * Resonance_Frequency) / (Inductor * 1j * Resonance_Frequency + Resistor *
                                                    (Capacitor * Inductor * -1 * Resonance_Frequency**2 + 1)))

# Magnitude of the output voltage/ absolute value of the Impedance
magnitude_vals = np.abs(Imp)

# Phase of the output voltage/ angle of the Impedance
phase_vals = np.angle(Imp, deg=True)  # Phase in degrees

# Phase of the output voltage, angle of the resonance Impedance
resonance_vals = np.angle(Res_Imp, deg=True)  # Phase in degrees

# Plot setup
fig, (mag, phase) = plt.subplots(2, 1, figsize=(10, 8))

# Magnitude plot
mag.plot(Omega, magnitude_vals)
mag.set_xscale('log')
mag.set_title("Magnitude Plot")
mag.set_ylabel("Magnitude")
mag.grid(True, which='both', linestyle='--', linewidth=0.5)

# Phase plot
phase.plot(Omega, phase_vals)
phase.set_xscale('log')
phase.set_title("Phase Plot")
phase.set_xlabel("(ω, Hz)")
phase.set_ylabel("Phase")
phase.grid(True, which='both', linestyle='--', linewidth=0.5)

# Resonance magnitude plot
#resonance_mag.plot(Resonance_Frequency, magnitude_vals)
#resonance_mag.set_xscale('log')
#resonance_mag.set_title('Resonance Magnitude')
#resonance_mag.set_ylabel('Magnitude')
#resonance_mag.grid(True, which='both', linestyle='--', linewidth=0.5)

# Resonance phase plot
#resonance_phase.plot(Resonance_Frequency, phase_vals)
#resonance_phase.set_xscale('log')
#resonance_phase.set_title('Resonance Phase')
#resonance_phase.set_xlabel('(ω, Hz)')
#resonance_phase.set_ylabel('Phase')
#resonance_phase.grid(True, which='both', linestyle='--', linewidth=0.5)

# Display plots
plt.tight_layout()
plt.show()
