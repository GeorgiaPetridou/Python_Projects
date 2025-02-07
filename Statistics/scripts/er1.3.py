import numpy as np
import matplotlib.pyplot as plt

# EROTIMA 3

# # Probability density function f(x) = 3x + 1 for 0 < x < 1
def f(x):
    return 3 * x + 1

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
