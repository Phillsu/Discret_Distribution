import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import hypergeom

def hypergeometric_pmf(N, K, n, x):
    return hypergeom.pmf(x, N, K, n)

def hypergeometric_cdf(N, K, n, x):
    return hypergeom.cdf(x, N, K, n)

# Parameters
N = 50  # Total population size
K = 10  # Number of success states in the population
n = 5   # Number of draws

# Values for x
x = np.arange(0, n+1)

# Calculate PMF and CDF
pmf = hypergeometric_pmf(N, K, n, x)
cdf = hypergeometric_cdf(N, K, n, x)

# Plot PMF
plt.subplot(1, 2, 1)
plt.stem(x, pmf, use_line_collection=True)
plt.xlabel('x')
plt.ylabel('P(X = x)')
plt.title('Hypergeometric PMF')

# Plot CDF
plt.subplot(1, 2, 2)
plt.step(x, cdf, where='post')
plt.xlabel('x')
plt.ylabel('P(X ≤ x)')
plt.title('Hypergeometric CDF')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
