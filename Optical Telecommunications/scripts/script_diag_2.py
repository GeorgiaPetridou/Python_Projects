import numpy as np
import matplotlib.pyplot as plt
import subprocess

# Range of spokes to test
spokes_range = np.arange(10, 101, 10)  # From 10 to 100 spokes in steps of 10
hub_capacity = 10  # Fixed hub capacity
num_simulations = 20  # Number of repetitions for averaging

# Lists to store results
avg_hubs_required = []
avg_spoke_load = []

# Loop over different spoke numbers
for num_spokes in spokes_range:
    hubs_per_simulation = []
    spoke_load_per_simulation = []
    
    for _ in range(num_simulations):
        # Run script.py with modified spokes count
        result = subprocess.run(['python', 'script.py'], capture_output=True, text=True)
        try:
            hubs_required = float(result.stdout.strip())
            hubs_per_simulation.append(hubs_required)
            spoke_load_per_simulation.append(num_spokes / hubs_required)
        except ValueError:
            print(f"Error: Could not extract float output from script.py. Raw output: {result.stdout.strip()}")
            continue  
    
    # Store the average values for this spoke count
    avg_hubs_required.append(np.mean(hubs_per_simulation))
    avg_spoke_load.append(np.mean(spoke_load_per_simulation))

# Plot the results
plt.figure(figsize=(8, 5))
plt.plot(avg_spoke_load, avg_hubs_required, marker='s', linestyle='-', color='r')
plt.xlabel("Average Spoke Load")
plt.ylabel("Average Required Hubs")
plt.title("Required Hubs vs Average Spoke Load")
plt.grid(True)
plt.show()
