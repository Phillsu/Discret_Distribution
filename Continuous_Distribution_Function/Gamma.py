import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

def gamma_pdf(k, theta, x):
    return gamma.pdf(x, k, scale=theta)

def gamma_cdf(k, theta, x):
    return gamma.cdf(x, k, scale=theta)

# Parameters
k = 2     # Shape parameter
theta = 2 # Scale parameter

# Values for x
x = np.linspace(0, 10, 100)

# Calculate PDF and CDF
pdf = gamma_pdf(k, theta, x)
cdf = gamma_cdf(k, theta, x)

# Plot PDF
plt.subplot(1, 2, 1)
plt.plot(x, pdf)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gamma PDF')

# Plot CDF
plt.subplot(1, 2, 2)
plt.plot(x, cdf)
plt.xlabel('x')
plt.ylabel('F(x)')
plt.title('Gamma CDF')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
