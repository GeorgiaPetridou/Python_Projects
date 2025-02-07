import subprocess
import numpy as np

# Number of times to run script.py
NUM_SIMULATIONS = 20

# List to store results
hubs_required_per_simulation = []

# Run script.py multiple times and collect results
for _ in range(NUM_SIMULATIONS):
    result = subprocess.run(['python', 'script.py'], capture_output=True, text=True)
    try:
        hubs_required = float(result.stdout.strip())
    except ValueError:
        print(f"Error: Could not extract float output from script.py. Raw output: {result.stdout.strip()}")
        continue  # Extract output as float
    hubs_required_per_simulation.append(hubs_required)
        

# Compute the average hubs required
if hubs_required_per_simulation:
    average_hubs_required = np.mean(hubs_required_per_simulation)
    print(f"Average Required Hubs over {NUM_SIMULATIONS} simulations: {average_hubs_required}")
else:
    print("No valid data collected from script.py execution.")
