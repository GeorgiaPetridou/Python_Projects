import numpy as np
import matplotlib.pyplot as plt

# EROTIMA 1

# Probability density function f(x) = 3x + 1 for 0 < x < 1
def f(x):
    return 3 * x + 1

# Sample size
n = 1000

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


# EROTIMA 2

# # Probability density function f(x) = 3x + 1 for 0 < x < 1
# def f(x):
#     return 3 * x + 1

# Maximum value of the function f(x) in the interval [0, 1]
M = 4  # The maximum value of the function occurs when x=1, i.e., f(1) = 4

# Probability density function of the uniform distribution g(x) in the interval [0, 1]
def g(x):
    return 1  # The density of the uniform distribution is 1

# Rejection sampling method
def rejection_sampling(sample_size):
    samples = []
    
    while len(samples) < sample_size:
        # Randomly select x from the uniform distribution [0, 1]
        y = np.random.uniform(0, 1)
        
        # Randomly select u from the uniform distribution [0, 1]
        u = np.random.uniform(0, 1)
        
        # If the random value u is less than f(x) / (M * g(x)), accept x
        if u <= f(y) / (M * g(y)):
            samples.append(y)
    
    return np.array(samples)

# Generate a sample of size 1000
samples = rejection_sampling(1000)

print(samples)

# Visualization of the sample
plt.hist(samples, bins=30, density=True, alpha=0.6, label="Sample")

# Probability density of f(x)
x = np.linspace(0, 1, 100)
plt.plot(x, f(x) / np.sum(f(x) * (x[1] - x[0])), label="f(x)", color="red")

plt.xlabel("x")
plt.ylabel("Probability Density Function")
plt.legend()
plt.title("Sample from f(x) using Rejection Sampling")
plt.show()


# EROTIMA 3

# # Probability density function f(x) = 3x + 1 for 0 < x < 1
# def f(x):
#     return 3 * x + 1

# Metropolis algorithm for generating samples from f(x)
def metropolis_algorithm(sample_size, proposal_width=0.1):
    samples = []
    
    # Step 1: Initialize the first sample (randomly chosen from [0, 1])
    current = np.random.uniform(0, 1)
    
    for _ in range(sample_size):
        # Step 2: Propose a new candidate by adding a random step
        candidate = current + np.random.uniform(-proposal_width, proposal_width)
        
        # Make sure the candidate is within the valid range [0, 1]
        candidate = np.clip(candidate, 0, 1)
        
        # Step 3: Accept or reject the candidate based on the Metropolis rule
        acceptance_ratio = min(1, f(candidate) / f(current))
        
        # Step 4: Accept the candidate with the computed probability
        if np.random.uniform(0, 1) < acceptance_ratio:
            current = candidate
        
        samples.append(current)
    
    return np.array(samples)

# Generate a sample of size 1000 using the Metropolis algorithm
samples = metropolis_algorithm(1000)

print(samples)

# Visualization of the sample
plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')

# Probability density of f(x)
x = np.linspace(0, 1, 100)
plt.plot(x, f(x) / 4, label=r'$f(x) = \frac{3x + 1}{4}$', color='r', lw=2)

plt.title("Metropolis Algorithm Sampling from f(x) = 3x + 1 (0 < x < 1)")
plt.xlabel("x")
plt.ylabel("Density")
plt.legend()
plt.show()
