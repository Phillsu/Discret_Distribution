import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def normal_pdf(mu, sigma, x):
    return norm.pdf(x, mu, sigma)

def normal_cdf(mu, sigma, x):
    return norm.cdf(x, mu, sigma)

# Parameters
mu = 0    # Mean
sigma = 1 # Standard deviation

# Values for x
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)

# Calculate PDF and CDF
pdf = normal_pdf(mu, sigma, x)
cdf = normal_cdf(mu, sigma, x)

# Plot PDF
plt.subplot(1, 2, 1)
plt.plot(x, pdf)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Normal PDF')

# Plot CDF
plt.subplot(1, 2, 2)
plt.plot(x, cdf)
plt.xlabel('x')
plt.ylabel('F(x)')
plt.title('Normal CDF')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
