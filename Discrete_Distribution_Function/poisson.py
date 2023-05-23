import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

def poisson_pmf(lmbda, x):
    return poisson.pmf(x, lmbda)

def poisson_cdf(lmbda, x):
    return poisson.cdf(x, lmbda)

# Parameter
lmbda = 3  # Mean or average number of events

# Values for x
x = np.arange(0, 15)

# Calculate PMF and CDF
pmf = poisson_pmf(lmbda, x)
cdf = poisson_cdf(lmbda, x)

# Plot PMF
plt.subplot(1, 2, 1)
plt.stem(x, pmf, use_line_collection=True)
plt.xlabel('x')
plt.ylabel('P(X = x)')
plt.title('Poisson PMF')

# Plot CDF
plt.subplot(1, 2, 2)
plt.step(x, cdf, where='post')
plt.xlabel('x')
plt.ylabel('P(X ≤ x)')
plt.title('Poisson CDF')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
