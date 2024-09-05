
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import random

##################
##    ^~^  , ######
##   ('Y') ) ######
##   /   \/  ######
##  (\|||/) ######
###################

class Node:
    def __init__(self, p=-1):
        self.neighbors = defaultdict(lambda: None)
        temp = np.random.uniform(0, 1)
        self.val = 1 if temp > p else 0

    def add_neighbor(self, direction, node):
        self.neighbors[direction] = node

    def __repr__(self):
        return f"Node(val={self.val}, Location = {self.location}, neighbors={list(self.neighbors.keys())})"
    
    def location(self, x, y):
        self.location = (x, y)

    def get_neighbor(self):
        return (self.neighbors)

def manhattan_distance(target_1, dist):
    x1, y1 = target_1
    possible_points = []
    for dx in range(dist + 1):
        dy = dist - dx
        possible_points.extend([
            (x1 + dx, y1 + dy), (x1 + dx, y1 - dy),
            (x1 - dx, y1 + dy), (x1 - dx, y1 - dy)
        ])
    possible_points = list(set(possible_points))
    return random.choice(possible_points)

def random_walk(start, end, grid):
    x, y = start
    path = [(x, y)]
    while (x, y) != end:
        node = grid[y][x]
        neighbors = node.neighbors.values()
        if not neighbors:
            break  # No more moves possible
        next_node = random.choice(list(neighbors))
        x, y = next_node.location
        path.append((x, y))
    return path

# Parameters
n, m = 3, 3  # n = x (columns), m = y (rows)
p = 0.5
ms_size = 3

# Define your target here
target_1 = (1, 1)
dist = 1
target_2 = manhattan_distance(target_1, dist)
target_3 = (0, 1)

# Create grid
grid = [[Node(p) for _ in range(n)] for _ in range(m)]
for i in range(m):
    for j in range(n):
        grid[i][j].location(j, i)
        if j < n - 1:
            right_prob = np.random.uniform(0, 1)
            if right_prob > p:
                grid[i][j].add_neighbor("right", grid[i][j + 1])
        if i < m - 1:
            down_prob = np.random.uniform(0, 1)
            if down_prob > p:
                grid[i][j].add_neighbor("down", grid[i + 1][j])
        if j > 0:
            if grid[i][j-1].get_neighbor() == 'down':
                grid[i][j].add_neighbor("up", grid[i][j-1])

print(grid)
# Plotting
def plot_grid(grid, path=[]):
    fig, ax = plt.subplots(figsize=(10, 10))
    for i in range(m):
        for j in range(n):
            node = grid[i][j]
            x, y = j, i  # Coordinate system: x-axis is j, y-axis is i
            ax.plot(x, y, 'ko', ms=ms_size)  # Plot nodes as black dots
            
            # Plot right connection
            if "right" in node.neighbors and node.neighbors["right"]:
                ax.arrow(x, y, 1, 0, fc='k', ec='r')
            
            # Plot down connection
            if "down" in node.neighbors and node.neighbors["down"]:
                ax.arrow(x, y, 0, -1, fc='k', ec='g')

    # Plot targets
    ax.plot(target_1[0], target_1[1], 'bo', ms=5)
    ax.plot(target_2[0], target_2[1], 'ro', ms=5)
    ax.plot(target_3[0], target_3[1], 'go', ms=5)

    # Plot the path with a different color
    if path:
        path_x, path_y = zip(*path)
        ax.plot(path_x, path_y, 'b-', lw=2)  # Path in blue with line width 2

    ax.set_xlim(-0.5, n-0.5)
    ax.set_ylim(-0.5, m-0.5)
    ax.set_aspect('equal')
    ax.grid(True)
    plt.show()

# Run the simulation
path = random_walk(target_2, target_1, grid)
plot_grid(grid, path)
# class Node:
#     def __init__(self, p=0.5):
#         self.neighbors = defaultdict(lambda: None)
#         temp = np.random.uniform(0, 1)
#         self.val = 1 if temp > p else 0

#     def add_neighbor(self, direction, node):
#         self.neighbors[direction] = node

#     def __repr__(self):
#         return f"Node(val={self.val}, Location = {self.location}, neighbors={list(self.neighbors.keys())})"
    
#     def location(self, x, y):
#         self.location = (x, -y)

# def manhattan_distance(target_1, dist):
#     x1 = target_1[0]
#     y1 = target_1[1]
#     possible_points = []
#     for dx in range(dist + 1):
#         dy = dist - dx
#         possible_points.extend([
#             (x1 + dx, y1 + dy), (x1 + dx, y1 - dy),
#             (x1 - dx, y1 + dy), (x1 - dx, y1 - dy)
#         ])

#     possible_points = list(set(possible_points))
#     return random.choice(possible_points)

# def random_walk(start, end, grid):
#     x, y = start
#     path = [(x, y)]
#     while (x, y) != end:
#         node = grid[y][x]
#         neighbors = node.neighbors.values()
#         print(f"neighbors: {neighbors}")
#         if not neighbors:
#             break  # No more moves possible
#         x, y = random.choice(list(neighbors)).location
#         path.append((x, y))
#         print(f"path: {path}")
#     return path


# # Manually setting stuff for now
# n, m = 3, 3  # n = x (rows), m = y (columns)
# p = 0.5
# ms_size = 3 #for plotting purposes, should be a function but TBD

# #####################       Define your target here ##############
# target_1 = (1, -1) #y needs to be inverted
# dist = 1
# target_2 = manhattan_distance(target_1, dist) #TO DO, if there is no way to escape target_2, idk choose a different target_2

# #we could manually assign target_2 i guess
# #print(target_2)

# target_3 = (0, -1)


# # Grid creation: Create a grid of nodes
# grid = [[Node(p) for _ in range(n)] for _ in range(m)]


# # Linking Nodes
# for i in range(m):
#     for j in range(n):
#         grid[i][j].location(i, j)
#         if j < n - 1:  
#             right_prob = np.random.uniform(0, 1)
#             if right_prob > p:
#                 grid[i][j].add_neighbor("right", grid[i][j + 1])

#         if i < m - 1:  
#             down_prob = np.random.uniform(0, 1)
#             if down_prob > p:
#                 grid[i][j].add_neighbor("down", grid[i + 1][j])
        

# print(grid)

# # Plotting
# def plot_grid(grid, path = []):
#     fig, ax = plt.subplots(figsize = (10, 10))
#     for i in range(m):
#         for j in range(n):
#             node = grid[i][j]
#             x, y = j, -i  # Coordinate system: x-axis is j, y-axis is -i
#             ax.plot(x, y, 'ko', ms = ms_size)  # Plot nodes as black dots
            
#             # Plot right connection
#             if "right" in node.neighbors and node.neighbors["right"]:
#                 ax.arrow(x, y, 1, 0, fc='k', ec='r')
            
#             # Plot down connection
#             if "down" in node.neighbors and node.neighbors["down"]:
#                 ax.arrow(x, y, 0, -1, fc='k', ec='g')
    

#     #plotting green shit
#     ax.plot(target_1[0], target_1[1], 'bo', ms = 5)
#     ax.plot(target_2[0], target_2[1], 'ro', ms = 5)
#     ax.plot(target_3[0], target_3[1], 'go', ms = 5)

#     if path:
#         path_x, path_y = zip(*path)
#         ax.plot(path_x, path_y, 'b-', lw= 6)


#     ax.set_xlim(-0.5, n-0.5)
#     ax.set_ylim(-m+0.5, 0.5)
#     ax.set_aspect('equal')
#     ax.grid(True)
#     plt.gca().invert_yaxis()  
#     plt.show()


# #random walk
# path = random_walk(target_2, target_1, grid)


# #simulation time won't my computer break
# plot_grid(grid, path)

