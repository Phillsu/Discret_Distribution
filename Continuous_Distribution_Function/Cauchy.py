import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import cauchy

def cauchy_pdf(x, x0, gamma):
    return cauchy.pdf(x, loc=x0, scale=gamma)

def cauchy_cdf(x, x0, gamma):
    return cauchy.cdf(x, loc=x0, scale=gamma)

# Parameters
x0 = 0    # Location parameter
gamma = 1 # Scale parameter

# Values for x
x = np.linspace(-10, 10, 100)

# Calculate PDF and CDF
pdf = cauchy_pdf(x, x0, gamma)
cdf = cauchy_cdf(x, x0, gamma)

# Plot PDF and CDF
plt.subplot(1, 2, 1)
plt.plot(x, pdf)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Cauchy PDF')

plt.subplot(1, 2, 2)
plt.plot(x, cdf)
plt.xlabel('x')
plt.ylabel('F(x)')
plt.title('Cauchy CDF')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
