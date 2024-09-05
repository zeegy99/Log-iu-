import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from matplotlib.widgets import Slider
import random

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

class Node:
    def __init__(self, p=-1):
        self.neighbors = defaultdict(lambda: None)
        self.val = np.random.uniform(0, 1)
        self.location = (0, 0)  # Initialize with a default location

    def get_val(self):
        return self.val

    def add_neighbor(self, direction, node):
        self.neighbors[direction] = node

    def __repr__(self):
        return f"Node(val={self.val}, Location={self.location}, neighbors={list(self.neighbors.keys())})"

    def set_location(self, x, y):
        self.location = (x, y)

    def get_neighbors(self):
        return self.neighbors


def connect_all_neighbors(grid, p):
    y_dim, x_dim = len(grid), len(grid[0])
    
    for y in range(y_dim):
        for x in range(x_dim):
            node = grid[y][x]

            if x < x_dim - 1:
                right_neighbor = grid[y][x + 1]
                average_val = (node.val + right_neighbor.val) / 2
                if average_val >= p:
                    node.add_neighbor("right", right_neighbor)
                else:
                    node.neighbors.pop("right", None)

            if x > 0:
                left_neighbor = grid[y][x - 1]
                average_val = (node.val + left_neighbor.val) / 2
                if average_val >= p:
                    node.add_neighbor("left", left_neighbor)
                else:
                    node.neighbors.pop("left", None)

            if y < y_dim - 1:
                down_neighbor = grid[y + 1][x]
                average_val = (node.val + down_neighbor.val) / 2
                if average_val >= p:
                    node.add_neighbor("up", down_neighbor)
                else:
                    node.neighbors.pop("up", None)

            if y > 0:
                up_neighbor = grid[y - 1][x]
                average_val = (node.val + up_neighbor.val) / 2
                if average_val >= p:
                    node.add_neighbor("down", up_neighbor)
                else:
                    node.neighbors.pop("down", None)

def plot_nodes_with_values(grid, l, ax):
    ax.clear()  # Clear the axis before redrawing

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            node = grid[y][x]
            node_x, node_y = node.location
            val = node.val
            
            ax.plot(node_x, node_y, 'ko', ms=10)
            #ax.text(node_x, node_y, f'{val:.2f}', color='blue', fontsize=12, ha='center', va='center')

            neighbors = node.get_neighbors()
            for direction, neighbor in neighbors.items():
                if neighbor is not None:
                    nx, ny = neighbor.location
                    ax.plot([node_x, nx], [node_y, ny], 'k-', lw=2)
                    
                    average_val = (val + neighbor.get_val()) / 2
                    midpoint_x = (node_x + nx) / 2
                    midpoint_y = (node_y + ny) / 2
                    #ax.text(midpoint_x, midpoint_y, f'{average_val:.2f}', color='red', fontsize=10, ha='center', va='center')

    ax.set_xlim(-0.5, len(grid[0]) - 0.5)
    ax.set_ylim(-0.5, len(grid) - 0.5)
    ax.set_aspect('equal')
    ax.grid(True)

def random_walk(start, end, grid):
    current = grid[start[0]][start[1]]
    counter = 0
    end_node = grid[end[0]][end[1]]
    temp = []

    #print(f"Initial node at {current.location} has neighbors: {current.get_neighbors().keys()}")
    #print("HI")
    #print(current)
    #print(grid[start[0]][start[1]])
    while current.location != end_node.location:

        test = list(current.get_neighbors())
        #print(test)
        neighbors = list(current.get_neighbors().values())


        if not neighbors:
            # No more neighbors to move to
            print("No path found")
            return None
        
        current = random.choice(neighbors)
        #print(current.location)
        temp.append(current.location)
        counter += 1
    return (counter, temp)

def dfs(start, end, grid, visited=None):
    print(start)
    print(end)
    if visited is None:
        visited = set()
    
    current = grid[start[0]][start[1]]
    end_node = grid[end[0]][end[1]]
    
    if start == end:
        return True
    
    if start in visited:
        return False
    
    #visited.add(start)

    y, x = start
    if not (0 <= y < len(grid) and 0 <= x < len(grid[0])):
        return False  # Out of bounds
    
    current = grid[y][x]
    visited.add(start)

    neighbors = current.get_neighbors()
    directions = {'up': (0, -1), 'right': (1, 0), 'down': (0, 1), 'left': (-1, 0)}
    
    for direction, neighbor in neighbors.items():
        if neighbor is not None:
            neighbor_location = neighbor.location
            new_start = (neighbor_location[1], neighbor_location[0])  # Convert to (y, x)
            if dfs(new_start, end, grid, visited):
                return True
    
    return False
