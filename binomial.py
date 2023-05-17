import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

def binomial_pmf(n, p, x):
    return binom.pmf(x, n, p)

def binomial_cdf(n, p, x):
    return binom.cdf(x, n, p)

# Parameters
n = 10  # Number of trials
p = 0.3  # Probability of success

# Values for x
x = np.arange(0, n+1)

# Calculate PMF and CDF
pmf = binomial_pmf(n, p, x)
cdf = binomial_cdf(n, p, x)

# Plot PMF
plt.subplot(1, 2, 1)
plt.stem(x, pmf, use_line_collection=True)
plt.xlabel('x')
plt.ylabel('P(X = x)')
plt.title('Binomial PMF')

# Plot CDF
plt.subplot(1, 2, 2)
plt.step(x, cdf, where='post')
plt.xlabel('x')
plt.ylabel('P(X ≤ x)')
plt.title('Binomial CDF')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()