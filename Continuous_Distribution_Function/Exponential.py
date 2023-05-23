import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

def exponential_pdf(lambd, x):
    return expon.pdf(x, scale=1/lambd)

def exponential_cdf(lambd, x):
    return expon.cdf(x, scale=1/lambd)

# Parameter
lambd = 0.5    # Rate parameter

# Values for x
x = np.linspace(0, 10, 100)

# Calculate PDF and CDF
pdf = exponential_pdf(lambd, x)
cdf = exponential_cdf(lambd, x)

# Plot PDF
plt.subplot(1, 2, 1)
plt.plot(x, pdf)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Exponential PDF')

# Plot CDF
plt.subplot(1, 2, 2)
plt.plot(x, cdf)
plt.xlabel('x')
plt.ylabel('F(x)')
plt.title('Exponential CDF')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
