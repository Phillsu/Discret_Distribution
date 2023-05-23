import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import nbinom

def negative_binomial_pmf(k, p, x):
    return nbinom.pmf(x, k, p)

def negative_binomial_cdf(k, p, x):
    return nbinom.cdf(x, k, p)

# Parameters
k = 5  # Number of failures
p = 0.3  # Probability of success

# Values for x
x = np.arange(0, 30)

# Calculate PMF and CDF
pmf = negative_binomial_pmf(k, p, x)
cdf = negative_binomial_cdf(k, p, x)

# Plot PMF
plt.subplot(1, 2, 1)
plt.stem(x, pmf, use_line_collection=True)
plt.xlabel('x')
plt.ylabel('P(X = x)')
plt.title('Negative Binomial PMF')

# Plot CDF
plt.subplot(1, 2, 2)
plt.step(x, cdf, where='post')
plt.xlabel('x')
plt.ylabel('P(X ≤ x)')
plt.title('Negative Binomial CDF')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
