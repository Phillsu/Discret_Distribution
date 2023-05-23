import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

def weibull_pdf(k, lambda_, x):
    return weibull_min.pdf(x, k, scale=lambda_)

def weibull_cdf(k, lambda_, x):
    return weibull_min.cdf(x, k, scale=lambda_)

# Parameters
k = 2       # Shape parameter
lambda_ = 1 # Scale parameter

# Values for x
x = np.linspace(0, 5, 100)

# Calculate PDF and CDF
pdf = weibull_pdf(k, lambda_, x)
cdf = weibull_cdf(k, lambda_, x)

# Plot PDF
plt.subplot(1, 2, 1)
plt.plot(x, pdf)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Weibull PDF')

# Plot CDF
plt.subplot(1, 2, 2)
plt.plot(x, cdf)
plt.xlabel('x')
plt.ylabel('F(x)')
plt.title('Weibull CDF')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
