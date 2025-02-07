import numpy as np
import pandas as pd
from scipy.stats import norm, binom

# Load the data
data = pd.read_csv('datasept.txt', sep="\t", names=['y'])

y = pd.to_numeric(data['y'], errors='coerce').fillna(0).astype(int).values

# Model parameters
phi = 0.9  # Example value for φ
sigma = 0.5  # Example value for σ
N = 1000  # Number of particles

# Initialization
T = len(y)
a_particles = np.zeros((N, T))  # Particles for a_t
weights = np.ones(N) / N  # Initial weights

# Initialize a1 from N(0, σ^2 / (1 - φ^2))
a_particles[:, 0] = np.random.normal(0, sigma / np.sqrt(1 - phi**2), N)

# Run particle filter
for t in range(1, T):
    # Step 1: Propagate particles a_t based on a_{t-1}
    a_particles[:, t] = np.random.normal(phi * a_particles[:, t-1], sigma, N)

    # Calculate probabilities p_t = exp(a_t) / (1 + exp(a_t))
    p_particles = np.exp(a_particles[:, t]) / (1 + np.exp(a_particles[:, t]))

    # Step 2: Update weights based on observed y_t
    weights *= binom.pmf(y[t], 50, p_particles)
    weights += 1e-300  # Avoid zero weights

    # Normalize weights
    weights /= np.sum(weights)

    # Step 3: Resample particles based on weights
    indices = np.random.choice(N, size=N, replace=True, p=weights)
    a_particles[:, t] = a_particles[indices, t]
    weights.fill(1.0 / N)

# Estimate p_t values as the mean of exp(a_particles) / (1 + exp(a_particles))
p_estimates = np.mean(np.exp(a_particles) / (1 + np.exp(a_particles)), axis=0)

# Print estimated probabilities
print("Estimated probabilities p_t:", p_estimates)
# print(p_estimates)
