import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom

def geometric_pmf(p, x):
    return geom.pmf(x, p)

def geometric_cdf(p, x):
    return geom.cdf(x, p)

# Parameter
p = 0.3  # Probability of success

# Values for x
x = np.arange(1, 11)

# Calculate PMF and CDF
pmf = geometric_pmf(p, x)
cdf = geometric_cdf(p, x)

# Plot PMF
plt.subplot(1, 2, 1)
plt.stem(x, pmf, use_line_collection=True)
plt.xlabel('x')
plt.ylabel('P(X = x)')
plt.title('Geometric PMF')

# Plot CDF
plt.subplot(1, 2, 2)
plt.step(x, cdf, where='post')
plt.xlabel('x')
plt.ylabel('P(X ≤ x)')
plt.title('Geometric CDF')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()