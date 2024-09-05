####################
#  Hallo plz halp ##
##    ^~^  , #######
##   ('Y') ) #######
##   /   \/  #######
##  (\|||/) ########
####################


#Backup incase refactoring fails: Uncomment out all of the functions. 
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from matplotlib.widgets import Slider
import random
from functions import *
# Parameters

x, y = 10, 10
p = 0.2
end = (5,5)
start = manhattan_distance(end, 5)
print(start)
num = 5
arr = [[0] for _ in range(num)]
random_walk_arr = [[0] for _ in range(num)]
curr = 0

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


# def connect_all_neighbors(grid):
#     y_dim, x_dim = len(grid), len(grid[0])
    
#     for y in range(y_dim):
#         for x in range(x_dim):
#             node = grid[y][x]

#             if x < x_dim - 1:
#                 right_neighbor = grid[y][x + 1]
#                 average_val = (node.val + right_neighbor.val) / 2
#                 if average_val >= p:
#                     node.add_neighbor("right", right_neighbor)
#                 else:
#                     node.neighbors.pop("right", None)

#             if x > 0:
#                 left_neighbor = grid[y][x - 1]
#                 average_val = (node.val + left_neighbor.val) / 2
#                 if average_val >= p:
#                     node.add_neighbor("left", left_neighbor)
#                 else:
#                     node.neighbors.pop("left", None)

#             if y < y_dim - 1:
#                 down_neighbor = grid[y + 1][x]
#                 average_val = (node.val + down_neighbor.val) / 2
#                 if average_val >= p:
#                     node.add_neighbor("up", down_neighbor)
#                 else:
#                     node.neighbors.pop("up", None)

#             if y > 0:
#                 up_neighbor = grid[y - 1][x]
#                 average_val = (node.val + up_neighbor.val) / 2
#                 if average_val >= p:
#                     node.add_neighbor("down", up_neighbor)
#                 else:
#                     node.neighbors.pop("down", None)

            # if x < x_dim - 1:
            #     right_neighbor = grid[y][x + 1]
            #     node.add_neighbor("right", right_neighbor)

            # if x > 0:
            #     left_neighbor = grid[y][x - 1]
            #     node.add_neighbor("left", left_neighbor)

            # if y < y_dim - 1:
            #     down_neighbor = grid[y + 1][x]
            #     node.add_neighbor("down", down_neighbor)

            # if y > 0:
            #     up_neighbor = grid[y - 1][x]
            #     node.add_neighbor("up", up_neighbor)



# def plot_nodes_with_values(grid, l, ax):
#     ax.clear()  # Clear the axis before redrawing

#     for y in range(len(grid)):
#         for x in range(len(grid[0])):
#             node = grid[y][x]
#             node_x, node_y = node.location
#             val = node.val
            
#             ax.plot(node_x, node_y, 'ko', ms=10)
#             #ax.text(node_x, node_y, f'{val:.2f}', color='blue', fontsize=12, ha='center', va='center')

#             neighbors = node.get_neighbors()
#             for direction, neighbor in neighbors.items():
#                 if neighbor is not None:
#                     nx, ny = neighbor.location
#                     ax.plot([node_x, nx], [node_y, ny], 'k-', lw=2)
                    
#                     average_val = (val + neighbor.get_val()) / 2
#                     midpoint_x = (node_x + nx) / 2
#                     midpoint_y = (node_y + ny) / 2
#                     ax.text(midpoint_x, midpoint_y, f'{average_val:.2f}', color='red', fontsize=10, ha='center', va='center')

#     ax.set_xlim(-0.5, len(grid[0]) - 0.5)
#     ax.set_ylim(-0.5, len(grid) - 0.5)
#     ax.set_aspect('equal')
#     ax.grid(True)

# def random_walk(start, end):
#     current = grid[start[0]][start[1]]
#     counter = 0
#     end_node = grid[end[0]][end[1]]
#     temp = []

#     #print(f"Initial node at {current.location} has neighbors: {current.get_neighbors().keys()}")
#     #print("HI")
#     #print(current)
#     #print(grid[start[0]][start[1]])
#     while current.location != end_node.location:

#         test = list(current.get_neighbors())
#         #print(test)
#         neighbors = list(current.get_neighbors().values())


#         if not neighbors:
#             # No more neighbors to move to
#             print("No path found")
#             return None
        
#         current = random.choice(neighbors)
#         #print(current.location)
#         temp.append(current.location)
#         counter += 1
#     return (counter, temp)
        

# def dfs(start, end):
#     #print(start)
#     #print(start[0] + 1, start[1])
#     current = grid[start[0]][start[1]]
#     end_node = grid[end[0]][end[1]]
#     if start == end:
#         return True
    
#     neighbors = list(current.get_neighbors())
#     if 'up' in neighbors:
#         start = (start[0] + 1, start[1])
#         dfs(start, end)
#     if 'right' in neighbors:
#         start = (start[0], start[1] + 1)
#         dfs(start, end)
#     if 'down' in neighbors:
#         start = (start[0] - 1, start[1])
#         dfs(start, end)
#     if 'left' in neighbors:
#         start = (start[0], start[1] - 1)
#         dfs(start, end)

#     return False

def dfs(start, end, visited=None):
    if visited is None:
        visited = set()
    
    current = grid[start[0]][start[1]]
    end_node = grid[end[0]][end[1]]
    
    if start == end:
        return True
    
    if start in visited:
        return False
    
    visited.add(start)

    neighbors = current.get_neighbors()
    directions = {'up': (0, -1), 'right': (1, 0), 'down': (0, 1), 'left': (-1, 0)}
    
    for direction, neighbor in neighbors.items():
        if neighbor is not None:
            neighbor_location = neighbor.location
            new_start = (neighbor_location[1], neighbor_location[0])  # Convert to (y, x)
            if dfs(new_start, end, visited):
                return True
    
    return False
    


    



# Create grid
grid = [[Node(p) for _ in range(x)] for _ in range(y)]

# Set locations for each node
for i in range(y):
    for j in range(x):
        grid[i][j].set_location(j, i)

connect_all_neighbors(grid, p)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 10))
# plt.subplots_adjust(left=0.1, bottom=0.25)

# Initial plot

#print(grid)
################### SLIDER SHIT ################### XDDDDDDDDDDDDDDD IT DOESNT FUCKING WORK AND IT BREAKS MY COMPUTER LOLOLOL
# Create a slider axis and slider
# ax_slider = plt.axes([0.1, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
# slider = Slider(ax_slider, 'Scale', 0.1, 10.0, valinit=p)

# # Update function for the slider
# def update(val):
#     l = slider.val
#     plot_nodes_with_values(grid, l, ax)
#     fig.canvas.draw_idle()  # Redraw the current figure

# slider.on_changed(update)
#print(dfs(start, end))
for i in range(num):
    if (dfs(start, end)):
        random_walk_info = random_walk(start, end, grid)
        if random_walk_info[1][-1] == end:
            random_walk_arr[i] = random_walk_info[1]
            curr += random_walk_info[0]
            arr[i] = random_walk_info[0]

#print(random_walk_arr)
x_coords = []
y_coords = []
hashmap = {}
for sublist in random_walk_arr:
    for coord in sublist:
        hashmap[(coord[0], coord[1])] = hashmap.get((coord[0], coord[1]), 0) + 1
        x_coords.append(coord[0])
        y_coords.append(coord[1])


coords = list(hashmap.keys())
weights = list(hashmap.values())


#print(weights)
j = np.sum(weights)


#x_coords_1, y_coords_1 = zip(*coords)
#print("helo")
#print(x_coords_1, y_coords_1)
plot_nodes_with_values(grid, p, ax)
for i in range(len(x_coords) - 1):
    x_start, y_start = x_coords[i], y_coords[i]
    x_end, y_end = x_coords[i + 1], y_coords[i + 1]
    if abs(x_start - x_end) + abs(y_start - y_end) == 1:  # Check for valid neighbor connections
        weight = (hashmap.get((x_start, y_start), 1)) / (j**.33)
        #print(weight)
        plt.plot([x_start, x_end], [y_start, y_end], color='g', linewidth=weight, marker='o')
       # print('hihihii')

#print(x_coords, y_coords)


#plt.plot(x_coords, y_coords, marker='o', linestyle='-', color='r')
plt.plot(start[0], start[1], marker='o', color = 'r', ms = 10)
plt.plot(end[0], end[1], marker='o', color = 'blue', ms = 10)
plt.show()
print(f"Over {num} walks, the average to get from {start} to {end} was {curr/num} steps")
#print(random_walk_arr)
