import random
import matplotlib.pyplot as plt

# Function to simulate Point-to-Multipoint (PtMP) communication
def simulate_ptmp(num_antennas, max_hub_capacity):
    """
    Simulate PtMP communication where antennas connect to hubs.

    Args:
        num_antennas (int): Number of antennas.
        max_hub_capacity (int): Maximum capacity of a single hub.

    Returns:
        hubs (list of lists): List of hubs and their connected antennas.
        num_transceivers (int): Total number of transceivers used.
        num_subcarriers (int): Total number of subcarriers used.
    """
    antennas = list(range(1, num_antennas + 1))
    hubs = []

    # Distribute antennas to hubs using a best-fit approach
    while antennas:
        hub = []
        while antennas and len(hub) < max_hub_capacity:
            hub.append(antennas.pop(0))
        hubs.append(hub)

    num_transceivers = len(hubs)
    num_subcarriers = num_antennas
    return hubs, num_transceivers, num_subcarriers

# Function to simulate Point-to-Point (PtP) communication
def simulate_ptp(num_antennas):
    """
    Simulate PtP communication where each antenna connects to its own transceiver.

    Args:
        num_antennas (int): Number of antennas.

    Returns:
        connections (list of tuples): List of PtP connections.
        num_transceivers (int): Total number of transceivers used.
        num_subcarriers (int): Total number of subcarriers used.
    """
    connections = [(i, i) for i in range(1, num_antennas + 1)]
    num_transceivers = num_antennas
    num_subcarriers = num_antennas
    return connections, num_transceivers, num_subcarriers

# Function to visualize PtMP and PtP networks
def visualize_network(hubs, ptp_connections):
    """
    Visualize PtMP and PtP networks using Matplotlib.

    Args:
        hubs (list of lists): Hubs and their connected antennas for PtMP.
        ptp_connections (list of tuples): PtP connections.
    """
    fig, ax = plt.subplots(1, 2, figsize=(14, 7))

    # PtMP network visualization
    ax[0].set_title("Point-to-Multipoint (PtMP) Network")
    hub_positions = [(i * 2, 5) for i in range(len(hubs))]
    antenna_positions = []
    for hub_idx, hub in enumerate(hubs):
        hub_x, hub_y = hub_positions[hub_idx]
        ax[0].scatter(hub_x, hub_y, c='blue', label=f"Hub-{hub_idx+1}" if hub_idx == 0 else None)
        for antenna in hub:
            antenna_x = random.uniform(hub_x - 1, hub_x + 1)
            antenna_y = random.uniform(1, 4)
            antenna_positions.append((antenna_x, antenna_y))
            ax[0].plot([hub_x, antenna_x], [hub_y, antenna_y], 'gray')
            ax[0].scatter(antenna_x, antenna_y, c='red')

    # PtP network visualization
    ax[1].set_title("Point-to-Point (PtP) Network")
    for connection in ptp_connections:
        x1, y1 = random.uniform(1, 5), random.uniform(5, 7)
        x2, y2 = random.uniform(6, 10), random.uniform(1, 3)
        ax[1].plot([x1, x2], [y1, y2], 'gray')
        ax[1].scatter([x1, x2], [y1, y2], c='green')

    for axes in ax:
        axes.set_xlim(0, 10)
        axes.set_ylim(0, 8)
        axes.legend()

    plt.tight_layout()
    plt.show()

# Main simulation
if __name__ == "__main__":
    # Parameters
    num_antennas = random.randint(10, 30)  # Random number of antennas
    max_hub_capacity = 5  # Maximum antennas a hub can support

    # Simulate PtMP
    ptmp_hubs, ptmp_transceivers, ptmp_subcarriers = simulate_ptmp(num_antennas, max_hub_capacity)

    # Simulate PtP
    ptp_connections, ptp_transceivers, ptp_subcarriers = simulate_ptp(num_antennas)

    # Visualize networks
    visualize_network(ptmp_hubs, ptp_connections)

    # Print results
    print("PtMP Results:")
    print(f"Number of hubs: {len(ptmp_hubs)}")
    print(f"Number of transceivers: {ptmp_transceivers}")
    print(f"Number of subcarriers: {ptmp_subcarriers}")
    print()

    print("PtP Results:")
    print(f"Number of transceivers: {ptp_transceivers}")
    print(f"Number of subcarriers: {ptp_subcarriers}")
