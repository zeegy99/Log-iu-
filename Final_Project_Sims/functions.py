import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
# from scipy.special import harmonic  

def create_ancestral_graph_with_convergence_and_trajectories(num_levels, fragmentation_rate, coagulation_rate, initial_nodes):
    G = nx.DiGraph()
    trajectories = {i: [i] for i in range(initial_nodes)}  # Initialize trajectories for each starting node

    # Start with multiple ancestor nodes
    for i in range(initial_nodes):
        G.add_node(i, subset=0)  # Base level nodes

    current_node = initial_nodes

    # Compute total rate for normalization
    total_rate = fragmentation_rate + coagulation_rate

    for level in range(1, num_levels + 1):
        nodes_at_current_level = [n for n in G.nodes if G.nodes[n]["subset"] == level - 1]
        random.shuffle(nodes_at_current_level)  # Shuffle nodes for randomness
        used_nodes = set()

        # Convergence check: If only one node remains, stop early
        if len(nodes_at_current_level) <= 1:
            return G, trajectories, level - 1  # Return graph, trajectories, and time to convergence

        # Process nodes at the current level
        for node in nodes_at_current_level:
            if node in used_nodes:
                continue  # Skip nodes already processed

            action = random.random()

            # Compute normalized probabilities
            fragmentation_prob = fragmentation_rate / total_rate
            coagulation_prob = coagulation_rate / total_rate

            if action < fragmentation_prob:
                # Fragmentation: Create 2 child nodes
                child_1 = current_node
                child_2 = current_node + 1

                # Add nodes and edges
                G.add_node(child_1, subset=level)
                G.add_edge(node, child_1)
                G.add_node(child_2, subset=level)
                G.add_edge(node, child_2)

                # Initialize trajectories for new nodes
                trajectories[child_1] = trajectories[node] + [child_1]
                trajectories[child_2] = trajectories[node] + [child_2]

                current_node += 2
            elif action < fragmentation_prob + coagulation_prob:
                # Coagulation: Try to merge with a random neighbor
                remaining_nodes = [n for n in nodes_at_current_level if n not in used_nodes and n != node]
                if remaining_nodes:
                    neighbor = random.choice(remaining_nodes)
                    child = current_node

                    # Add node and edges
                    G.add_node(child, subset=level)
                    G.add_edge(node, child)
                    G.add_edge(neighbor, child)

                    # Initialize trajectory for the new node
                    trajectories[child] = trajectories[node] + [child]
                    trajectories[child] = trajectories[neighbor] + [child]

                    used_nodes.add(node)
                    used_nodes.add(neighbor)
                    current_node += 1
                else:
                    # If no neighbors available, propagate the node
                    child = current_node

                    # Add node and edge
                    G.add_node(child, subset=level)
                    G.add_edge(node, child)

                    # Initialize trajectory for the new node
                    trajectories[child] = trajectories[node] + [child]

                    current_node += 1
            else:
                # Default: Create a single child node
                child = current_node

                # Add node and edge
                G.add_node(child, subset=level)
                G.add_edge(node, child)

                # Initialize trajectory for the new node
                trajectories[child] = trajectories[node] + [child]

                current_node += 1

    return G, trajectories, num_levels  # If no convergence, return the full number of levels


def plot_ancestral_graph_with_trajectories(G, trajectories):
    pos = nx.multipartite_layout(G, subset_key="subset")  # Use the subset attribute for layout
    plt.figure(figsize=(12, 8))

    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, edge_color='gray', arrows=True)

    # Plot trajectories in red
    for trajectory in trajectories.values():
        path_edges = list(zip(trajectory, trajectory[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)

    plt.title("Ancestral Graph with Node Trajectories")
    plt.show()

def compute_descendants(G, node):
    return len(nx.descendants(G, node))

def harmonic(n):
    return sum(1 / k for k in range(1, n + 1))

def compute_tau_total(G):
    tau_total = 0
    for edge in G.edges:
        _, child = edge
        tau_total += 1  
    return tau_total

def simulate_normalized_tau_total(num_sim, num_nodes, f_rate, c_rate): #simulation
    tau_totals = []
    for _ in range(num_sim):
        G, a, b = create_ancestral_graph_with_convergence_and_trajectories(
            num_levels=50, fragmentation_rate=f_rate, coagulation_rate=c_rate, initial_nodes=num_nodes
        )
        tau_total = compute_tau_total(G)
        tau_totals.append(tau_total)


    H_n = harmonic(num_nodes) 
    var_tau = np.var(tau_totals)
    Z = [(tau - 2 * H_n) / np.sqrt(var_tau) for tau in tau_totals]

    return Z

# Parameters
num_levels = 20
fragmentation_rate = 1.0    # Probability of splitting into 2 child nodes
coagulation_rate = 10.0     # Probability of merging with a neighbor
initial_nodes = 10           # Start with 10 initial ancestor nodes

# Create and check for convergence with trajectories
G_fixed, trajectories, convergence_time = create_ancestral_graph_with_convergence_and_trajectories(
    num_levels, fragmentation_rate, coagulation_rate, initial_nodes
)

# Plot the resulting graph with trajectories
plot_ancestral_graph_with_trajectories(G_fixed, trajectories)

# Output the time to convergence
print(f"The nodes all converged into a single node after {convergence_time} levels.")


