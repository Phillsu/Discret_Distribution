import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

def uniform_pdf(a, b, x):
    return uniform.pdf(x, loc=a, scale=b-a)

def uniform_cdf(a, b, x):
    return uniform.cdf(x, loc=a, scale=b-a)

# Parameters
a = 0    # Lower bound
b = 10   # Upper bound

# Values for x
x = np.linspace(a, b, 100)

# Calculate PDF and CDF
pdf = uniform_pdf(a, b, x)
cdf = uniform_cdf(a, b, x)

# Plot PDF
plt.subplot(1, 2, 1)
plt.plot(x, pdf)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Uniform PDF')

# Plot CDF
plt.subplot(1, 2, 2)
plt.plot(x, cdf)
plt.xlabel('x')
plt.ylabel('F(x)')
plt.title('Uniform CDF')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
