import random
import matplotlib.pyplot as plt
import networkx as nx

class Node():
    def __init__(self, curr_time, index, depth=0):
        self.index = index  # Set the index directly
        self.left = None
        self.right = None
        self.depth = depth  # Track depth in the tree (generation level)
        self.time_to_reproduce = self.exponential(index)
        self.reproduction_time = round(curr_time + self.time_to_reproduce, 2)  # Final time of reproduction
        self.start = curr_time

    def __repr__(self):
        return (f"(Index: {self.index}, Time generated: {self.start}, Time to reproduce: {self.time_to_reproduce}, Left child: {self.left}, Right child: {self.right})")

    def reproduce(self, current_index):
        # Pass the current index for left and right child
        self.left = Node(self.reproduction_time, current_index, self.depth + 1)  # Increment depth for child nodes
        self.right = Node(self.reproduction_time, current_index + 1, self.depth + 1)  # Update index for right child
        return self.left, self.right

    @staticmethod
    def exponential(val):
        return random.expovariate(val)

def draw_graph(G, pos, labels):
    """Draw the directed graph with given positions and labels."""
    plt.figure(figsize=(12, 10))  # Increase figure size to accommodate more nodes
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=8, font_color='black')
    nx.draw_networkx_labels(G, pos, labels=labels)

    plt.title("Node Reproduction Tree with Dynamic Spacing")
    plt.show()

def assign_positions(node, pos, level_width, x=0, level=0):
    """Recursively assign positions to each node based on time and hierarchy, with depth-based horizontal spacing."""
    if level not in level_width:
        level_width[level] = 0

    # Increase horizontal spacing as we go deeper into the tree
    current_spacing = 1.0 * (level + 1)  # Increase horizontal spacing with depth

    # Horizontal position based on the number of nodes at the current level
    pos[node.index] = (x + level_width[level] * current_spacing, -node.start * 10)

    # Increment the count for this level (spread nodes horizontally)
    level_width[level] += 1

    # Recursive calls to position the children with more space between siblings
    if node.left:
        assign_positions(node.left, pos, level_width, x - current_spacing / 2, level + 1)  # Left child closer to the parent
    if node.right:
        assign_positions(node.right, pos, level_width, x + current_spacing / 2, level + 1)  # Right child closer to the parent

def main(n):
    nodes = []  # queue
    longest_times = []  # Store longest reproduction times for each node
    head = Node(0, 1)  # Create the root node with index 1
    nodes.append(head)
    longest_times.append(head.reproduction_time)  # Store the longest time for the root node
    i = 0
    current_index = 2  # Start indexing child nodes from 2

    while len(nodes) < n:
        current_node = nodes[i]
        left_child, right_child = current_node.reproduce(current_index)
        nodes.append(left_child)
        nodes.append(right_child)

        # Append the longest reproduction times for each node created
        longest_times.append(max(current_node.reproduction_time, left_child.reproduction_time, right_child.reproduction_time))

        # Increment the current index for the next child nodes
        current_index += 2  # Increment by 2 as we create two children

        i += 1

    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes and edges to the graph, with each node's depth and reproduction time
    for node in nodes:
        G.add_node(node.index, reproduction_time=node.reproduction_time, start=node.start)
        if node.left:
            G.add_edge(node.index, node.left.index)  # left child
        if node.right:
            G.add_edge(node.index, node.right.index)  # right child

    # Create a layout with dynamic horizontal spacing
    pos = {}
    level_width = {}

    # Assign positions to nodes
    assign_positions(head, pos, level_width)

    # Labels for the nodes
    labels = {n: f"Index: {n}\nT_gen: {G.nodes[n]['start']}\nT_reprod: {G.nodes[n]['reproduction_time']:.2f}" for n in G.nodes()}

    return G, pos, labels, longest_times  # Return the graph, positions, labels, and longest times

def plot_graph(n):
    G, pos, labels, longest_times = main(n)  # Call main to get the graph details
    draw_graph(G, pos, labels)  # Call the drawing function with returned values

if __name__ == "__main__":
    n = 15  # Number of nodes to create
    plot_graph(n)  # Call the new function to plot the graph
