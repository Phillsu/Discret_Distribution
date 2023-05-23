import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

def chi2_pdf(k, x):
    return chi2.pdf(x, k)

def chi2_cdf(k, x):
    return chi2.cdf(x, k)

# Parameters
k = 3  # Degrees of freedom

# Values for x
x = np.linspace(0, 10, 100)

# Calculate PDF and CDF
pdf = chi2_pdf(k, x)
cdf = chi2_cdf(k, x)

# Plot PDF
plt.subplot(1, 2, 1)
plt.plot(x, pdf)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Chi-square PDF')

# Plot CDF
plt.subplot(1, 2, 2)
plt.plot(x, cdf)
plt.xlabel('x')
plt.ylabel('F(x)')
plt.title('Chi-square CDF')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
