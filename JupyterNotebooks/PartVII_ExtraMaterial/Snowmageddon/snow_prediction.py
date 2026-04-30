import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, lognorm
from scipy.optimize import curve_fit

# -----------------------------
# Given data (exceedance probs)
# -----------------------------
x_data = np.array([3, 8, 12, 18])          # snowfall thresholds (inches)
p_exceed = np.array([0.86, 0.54, 0.32, 0.24])

# -----------------------------
# Lognormal exceedance function
# -----------------------------
def lognormal_exceedance(x, mu, sigma):
    z = (np.log(x) - mu) / sigma
    return 1.0 - norm.cdf(z)

# -----------------------------
# Fit parameters (mu, sigma)
# -----------------------------
initial_guess = (2.0, 1.0)  # reasonable starting point

params, cov = curve_fit(
    lognormal_exceedance,
    x_data,
    p_exceed,
    p0=initial_guess,
    bounds=((-np.inf, 1e-3), (np.inf, np.inf))
)

mu_fit, sigma_fit = params

print(f"Fitted parameters:")
print(f"  mu    = {mu_fit:.3f}")
print(f"  sigma = {sigma_fit:.3f}")

# -----------------------------
# Smooth x grid for plotting
# -----------------------------
x = np.linspace(0.5, 25, 400)

# Exceedance curve from fit
p_fit = lognormal_exceedance(x, mu_fit, sigma_fit)

# PDF from fit (scipy parameterization)
pdf = lognorm.pdf(x, s=sigma_fit, scale=np.exp(mu_fit))

# -----------------------------
# Plot
# -----------------------------
fig, axes = plt.subplots(2, 1, figsize=(7, 8), sharex=True)

# --- Top: Exceedance probabilities ---
axes[0].scatter(x_data, p_exceed, s=70, label="Given probabilities", zorder=3)
axes[0].plot(x, p_fit, linewidth=2, label="Lognormal fit")

# draw a 95% confidence interval (approx) for the fit
std_dev = np.sqrt(np.diag(cov))
p_upper = lognormal_exceedance(x, mu_fit + 2*std_dev[0], sigma_fit + 2*std_dev[1])
p_lower = lognormal_exceedance(x, mu_fit - 2*std_dev[0], sigma_fit - 2*std_dev[1])
axes[0].fill_between(x, p_lower, p_upper, color='gray', alpha=0.3, label="Approx. 95% CI")


axes[0].set_ylabel("P(X > x)")
axes[0].set_title("Snowfall Uncertainty: Lognormal Fit")
axes[0].set_ylim(0, 1)
axes[0].grid(True, alpha=0.3)
axes[0].legend()

# --- Bottom: Probability density ---
axes[1].plot(x, pdf, linewidth=2)

# plot a 95% confidence interval (approx) for the PDF
pdf_upper = lognorm.pdf(x, s=sigma_fit + 2*std_dev[1], scale=np.exp(mu_fit + 2*std_dev[0]))
pdf_lower = lognorm.pdf(x, s=sigma_fit - 2*std_dev[1], scale=np.exp(mu_fit - 2*std_dev[0]))
axes[1].fill_between(x, pdf_lower, pdf_upper, color='gray', alpha=0.3, label="Approx. 95% CI")

axes[1].set_xlabel("Snowfall amount x (inches)")
axes[1].set_ylabel("Probability density f(x)")
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()