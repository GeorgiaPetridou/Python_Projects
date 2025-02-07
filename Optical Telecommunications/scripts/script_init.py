import random
import matplotlib.pyplot as plt

# Function to simulate Point-to-Multipoint (PtMP) communication with capacities
def simulate_ptmp_with_capacity(num_spokes, hub_capacity, num_simulations=100):
    """
    Simulate PtMP communication considering capacity constraints on hubs.

    Args:
        num_spokes (int): Number of spokes (antennas).
        hub_capacity (int): Maximum capacity of a hub.
        num_simulations (int): Number of simulations to perform.

    Returns:
        avg_hubs (float): Average number of hubs required.
        avg_utilization (float): Average hub utilization.
    """
    total_hubs = []
    total_utilization = []

    for _ in range(num_simulations):
        # Generate random capacities for spokes
        spokes = [random.randint(1, hub_capacity // 2) for _ in range(num_spokes)]
        hubs = []

        while spokes:
            current_hub = []
            current_hub_capacity = 0

            for spoke in spokes[:]:  # Iterate over a copy of the list
                if current_hub_capacity + spoke <= hub_capacity:
                    current_hub.append(spoke)
                    current_hub_capacity += spoke
                    spokes.remove(spoke)

            hubs.append(current_hub)

        total_hubs.append(len(hubs))
        total_utilization.append(sum(sum(hub) for hub in hubs) / (len(hubs) * hub_capacity))

    avg_hubs = sum(total_hubs) / num_simulations
    avg_utilization = sum(total_utilization) / num_simulations

    return avg_hubs, avg_utilization

# Function to visualize the PtMP network
def visualize_ptmp(hub_capacity, hubs):
    """
    Visualize PtMP network showing hubs and their connected spokes.

    Args:
        hub_capacity (int): Capacity of each hub.
        hubs (list of lists): List of hubs and their connected spokes.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    hub_positions = [(i * 2, 5) for i in range(len(hubs))]

    for hub_idx, hub in enumerate(hubs):
        hub_x, hub_y = hub_positions[hub_idx]
        ax.scatter(hub_x, hub_y, c='blue', label=f"Hub-{hub_idx + 1}" if hub_idx == 0 else None)
        for spoke_idx, spoke in enumerate(hub):
            spoke_x = random.uniform(hub_x - 1, hub_x + 1)
            spoke_y = random.uniform(1, 4)
            ax.plot([hub_x, spoke_x], [hub_y, spoke_y], 'gray')
            ax.scatter(spoke_x, spoke_y, c='red', label=f"Spoke-{spoke_idx + 1}" if hub_idx == 0 and spoke_idx == 0 else None)

    ax.set_title(f"Point-to-Multipoint (PtMP) Network\nHub Capacity: {hub_capacity}")
    ax.legend()
    plt.show()

# Main simulation
if __name__ == "__main__":
    # Parameters
    num_spokes = random.randint(20, 50)  # Random number of spokes
    hub_capacity = 100  # Fixed capacity of each hub
    num_simulations = 100  # Number of simulations to calculate averages

    # Perform simulation
    avg_hubs, avg_utilization = simulate_ptmp_with_capacity(num_spokes, hub_capacity, num_simulations)

    # Generate a single example for visualization
    example_spokes = [random.randint(1, hub_capacity // 2) for _ in range(num_spokes)]
    example_hubs = []
    while example_spokes:
        current_hub = []
        current_hub_capacity = 0

        for spoke in example_spokes[:]:
            if current_hub_capacity + spoke <= hub_capacity:
                current_hub.append(spoke)
                current_hub_capacity += spoke
                example_spokes.remove(spoke)

        example_hubs.append(current_hub)

    # Print results
    print(f"Average number of hubs required: {avg_hubs:.2f}")
    print(f"Average hub utilization: {avg_utilization:.2%}")


    # Visualize the example
    visualize_ptmp(hub_capacity, example_hubs)

    