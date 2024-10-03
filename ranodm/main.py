## Problem statement

#Given n nodes, 

import random
import math
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class Node():
    count = 1
    def __init__(self, curr_time, depth = 0):
        self.index = Node.count
        Node.count += 1
        self.left = None
        self.right = None
        self.depth = depth
        self.time_to_reproduce = Node.exponential(Node.count)
        self.reproduction_time = curr_time + self.time_to_reproduce
        self.start = curr_time




    def __repr__(self):
        return (f"(Index: {self.index}, Time generated: {self.start}, Time to reproduce: {self.time_to_reproduce} Left child: {self.left}, Right child: {self.right})")

    def reproduce(self):
        self.left = Node(self.reproduction_time, self.depth + 1)
        self.right = Node(self.reproduction_time, self.depth + 1)
        return self.left, self.right


    def exponential(val):
        return random.expovariate(val)
    
n = 5
time = [0] * n
nodes = [] #queue
head = Node(0)
nodes.append(head)
i = 0

while len(nodes) < n:
    current_node = nodes[i]
    left_child, right_child = current_node.reproduce()
    nodes.append(left_child)
    nodes.append(right_child)
    i += 1

print(nodes[0])

#display through networkx

G = nx.DiGraph()

for node in nodes:
    G.add_node(node.index, subset=node.depth)  # Assign the subset_key based on depth
    if node.left:
        G.add_edge(node.index, node.left.index)  # left child
    if node.right:
        G.add_edge(node.index, node.right.index)  # right child

pos = nx.multipartite_layout(G, subset_key="subset")  # Now we are using the node's subset (depth)

# Labels for the nodes
labels = {n: f"Index: {n}" for n in G.nodes()}

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=8)
nx.draw_networkx_labels(G, pos, labels=labels)

plt.title("Node Tree Structure (Multipartite Layout)")
plt.show()