####################
#  Hallo plz halp ##
##    ^~^  , #######
##   ('Y') ) #######
##   /   \/  #######
##  (\|||/) ########
####################



##  to display the edges go to line 101 in functions.py
##  to display node values go to line 90 in functions.py

##  lots of spaghetti so bring a fork

import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from matplotlib.widgets import Slider
import random
from functions import *
# Parameters 

x, y = 15, 10 #sets size of plot

p = 0.2 #removes all edges with value less than p
end = (5,5) #target value to reach
start = manhattan_distance(end, 5) #starting value, can be manually inputted as (x, y)
num = 5 #number of simulations


#Stuff idk don't touch it's used for something probably
arr = [[0] for _ in range(num)]
random_walk_arr = [[0] for _ in range(num)]
curr = 0
grid = [[Node(p) for _ in range(x)] for _ in range(y)]
x_coords = []
y_coords = []
hashmap = {}
marker_size_1 = 15
buffer = 0.5


# Set locations for each node
for i in range(y):
    for j in range(x):
        grid[i][j].set_location(j, i)

#yeah
fig, ax = plt.subplots(figsize=(10, 10))
connect_all_neighbors(grid, p)
# Set up the figure and axis
# plt.subplots_adjust(left=0.1, bottom=0.25)


################### SLIDER SHIT ################### XDDDDDDDDDDDDDDD IT DOESNT FUCKING WORK AND IT CRASHED MY PC NOT GOOD
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



#Random Walk
for i in range(num):
    if (dfs(start, end, grid)):
        random_walk_info = random_walk(start, end, grid)
        if random_walk_info[1][-1] == end:
            random_walk_arr[i] = random_walk_info[1]
            curr += random_walk_info[0]
            arr[i] = random_walk_info[0]


#Prepping Data for Plotting
for sublist in random_walk_arr:
    for coord in sublist:
        hashmap[(coord[0], coord[1])] = hashmap.get((coord[0], coord[1]), 0) + 1
        x_coords.append(coord[0])
        y_coords.append(coord[1])

#Weighting
coords = list(hashmap.keys())
weights = list(hashmap.values())
j = np.sum(weights) #great variable name fred
line_width_scale = (j ** 0.33) 

#x_coords_1, y_coords_1 = zip(*coords)
#print("helo")
#print(x_coords_1, y_coords_1)
plot_nodes_with_values(grid, p, ax)
for i in range(len(x_coords) - 1):
    x_start, y_start = x_coords[i], y_coords[i]
    x_end, y_end = x_coords[i + 1], y_coords[i + 1]
    if abs(x_start - x_end) + abs(y_start - y_end) == 1:  # Check for valid neighbor connections there was a bug where it would map (1,0) to target every time. 
        weight = (hashmap.get((x_start, y_start), 1)) / line_width_scale #Not sure how it got fixed but it somehow disappeared. 
        #print(weight)
        plt.plot([x_start, x_end], [y_start, y_end], color='g', linewidth=weight, marker='o')

#print(x_coords, y_coords)


#plt.plot(x_coords, y_coords, marker='o', linestyle='-', color='r')

#Manually plotting starting, endpoints
plt.plot(start[0], start[1], marker='o', color = 'r', ms = marker_size_1)
plt.plot(end[0], end[1], marker='o', color = 'blue', ms = marker_size_1)

plt.xlim(-buffer, x + buffer)
plt.ylim(-buffer, y + buffer)
#we're done
plt.show()
print(f"Over {num} walks, the average to get from {start} to {end} was {curr/num} steps") #some data gathering info
