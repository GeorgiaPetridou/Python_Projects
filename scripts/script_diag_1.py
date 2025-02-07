import numpy as np
import matplotlib.pyplot as plt
import subprocess

# Range of spokes to test
spokes_range = np.arange(10, 101, 10)  # From 10 to 100 spokes in steps of 10
hub_capacity = 10  # Fixed hub capacity
num_simulations = 20  # Number of repetitions for averaging

# List to store results
avg_hubs_required = []

# Loop over different spoke numbers
for num_spokes in spokes_range:
    hubs_per_simulation = []
    
    for _ in range(num_simulations):
        # Run script.py with modified spokes count
        result = subprocess.run(['python', 'script.py'], capture_output=True, text=True)
        try:
            hubs_required = float(result.stdout.strip())
            hubs_per_simulation.append(hubs_required)
        except ValueError:
            print(f"Error: Could not extract float output from script.py. Raw output: {result.stdout.strip()}")
            continue  
    
    # Store the average required hubs for this spoke count
    avg_hubs_required.append(np.mean(hubs_per_simulation))

# Plot the results
plt.figure(figsize=(8, 5))
plt.plot(spokes_range, avg_hubs_required, marker='o', linestyle='-', color='b')
plt.xlabel("Number of Spokes")
plt.ylabel("Average Required Hubs")
plt.title("Required Hubs vs Number of Spokes")
plt.grid(True)
plt.show()
