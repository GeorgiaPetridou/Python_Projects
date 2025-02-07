
import numpy as np
import matplotlib.pyplot as plt

# Sample size
n = 1000

# # Probability density function f(x) = 3x + 1 for 0 < x < 1
# def f(x):
#     return 3 * x + 1

# Inverse CDF function
def inverse_cdf(u):
    return (-1 + np.sqrt(1 + 15 * u)) / 3

# Generate samples from U(0, 1)
u_samples = np.random.uniform(0, 1, n)

# Transform samples using the inverse CDF
x_samples = inverse_cdf(u_samples)

print(x_samples)

# Visualization of results
plt.figure(figsize=(10, 6))
plt.hist(x_samples, bins=30, density=True, alpha=0.7, label="Generated samples")
# Plot the true probability density function (PDF) for comparison
x = np.linspace(0, 1, 1000)
plt.plot(x, (2 / 5) * (3 * x + 1), 'r-', label="f(x) = (2/5)*(3x + 1)")
plt.xlabel("x")
plt.ylabel("Density")
plt.legend()
plt.title("Generated Samples vs True PDF")
plt.grid(alpha=0.3)
plt.show()

# Calculate basic statistics for analysis
sample_mean = np.mean(x_samples)
sample_variance = np.var(x_samples)
sample_mean, sample_variance
