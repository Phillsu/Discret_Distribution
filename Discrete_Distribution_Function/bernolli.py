import numpy as np
import matplotlib.pyplot as plt

def bernoulli_pmf(p, x):
    return np.where(x == 1, p, 1 - p)

def bernoulli_cdf(p, x):
    return np.where(x < 1, 1 - p, 1)

# Parameters
p = 0.3  # Probability of success

# Values for x
x = np.array([0, 1])

# Calculate PMF and CDF
pmf = bernoulli_pmf(p, x)
cdf = bernoulli_cdf(p, x)

# Plot PMF
plt.subplot(1, 2, 1)
plt.stem(x, pmf, use_line_collection=True)
plt.xlabel('x')
plt.ylabel('P(X = x)')
plt.title('Bernoulli PMF')

# Plot CDF
plt.subplot(1, 2, 2)
plt.step(x, cdf, where='post')
plt.xlabel('x')
plt.ylabel('P(X ≤ x)')
plt.title('Bernoulli CDF')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()