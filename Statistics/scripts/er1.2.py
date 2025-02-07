import numpy as np
import matplotlib.pyplot as plt

# Probability density function f(x) = 3x + 1 for 0 < x < 1
def f(x):
    return 3 * x + 1

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
