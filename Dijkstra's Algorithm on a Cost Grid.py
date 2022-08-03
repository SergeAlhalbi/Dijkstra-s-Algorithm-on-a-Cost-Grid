# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 09:12:11 2022
Reference: https://levelup.gitconnected.com/dijkstras-shortest-path-algorithm-in-a-grid-eb505eb3a290
@author: Serge Alhalbi
"""

#==============================================================================
# Dijkstra's Algorithm on a Cost Grid
#==============================================================================

# Import Libraries
import numpy as np
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------
# Map
#------------------------------------------------------------------------------

# Define Variables
max_val = 25;   # you can change the size of the map
max_cost = 50;  # you can change the maximum cost of cells, if max_cost = 2 then the cost grid reduces to a normal grid

# Define the Map
np.random.seed(2022)
map = np.random.randint(1, max_cost, size=(max_val, max_val))

# Define Both Start and End Coordinates
start = [4,2];
end = [21,20];
# No Costs are Applied to Start and End Points
map[start[0],start[1]] = 0
map[end[0],end[1]] = 0

# Generate Random Obstacles
obstacles_matrix = np.matrix(np.zeros((max_val, max_val)))
obstacles_number = 40;
obstacles_index_list = [None]*obstacles_number;
for i in range(obstacles_number):
        obstacles_index_list[i] = np.random.randint(0, max_val, size=2)
        temp_obstacles_index_list = obstacles_index_list.copy();
        temp_obstacles_index_list.pop(i)
        while np.array_equal(obstacles_index_list[i], start) or np.array_equal(obstacles_index_list[i], end) or any(np.array_equal(obstacles_index_list[i], element) for element in temp_obstacles_index_list):
            obstacles_index_list[i] = np.random.randint(0, max_val, size=2)
            if not np.array_equal(obstacles_index_list[i], start) and not np.array_equal(obstacles_index_list[i], end) and not any(np.array_equal(obstacles_index_list[i], element) for element in temp_obstacles_index_list):
                break
        obstacles_matrix[obstacles_index_list[i][0],obstacles_index_list[i][1]] = np.inf
        map = map + obstacles_matrix;

# Plot the Heatmap
fig, ax = plt.subplots(figsize=(12,12))
cmap=plt.cm.Blues
cmap.set_bad(color='brown')
ax.matshow(map, cmap=plt.cm.Blues, vmin=0, vmax=max_cost)
ax.set_xlabel('y')
ax.set_ylabel('x')
ax.set_title('Cost Grid')
for i in range(max_val):
    for j in range(max_val):
      c = map[j,i]
      ax.text(i, j, str(c), va='center', ha='center', fontsize=8)
      if c == np.inf:
          ax.text(i, j, str(c), va='center', ha='center', color='w', fontsize=8)

#------------------------------------------------------------------------------
# Dijkstra's Algorithm
#------------------------------------------------------------------------------

# Initialize Auxiliary Arrays
distmap=np.ones((max_val,max_val),dtype=int)*np.Infinity
distmap[start[0],start[1]]=0
originmap=np.ones((max_val,max_val),dtype=int)*np.nan
visited=np.zeros((max_val,max_val),dtype=bool)
finished = False
x,y=np.int(start[0]),np.int(start[1])
count=0

# Loop Dijkstra Until Reaching the Target Cell
while not finished:
  # move down to x+1,y
  if x < max_val-1:
    if distmap[x+1,y]>map[x+1,y]+distmap[x,y] and not visited[x+1,y]:
      distmap[x+1,y]=map[x+1,y]+distmap[x,y]
      originmap[x+1,y]=np.ravel_multi_index([x,y], (max_val,max_val))
  # move up to x-1,y
  if x > 0:
    if distmap[x-1,y]>map[x-1,y]+distmap[x,y] and not visited[x-1,y]:
      distmap[x-1,y]=map[x-1,y]+distmap[x,y]
      originmap[x-1,y]=np.ravel_multi_index([x,y], (max_val,max_val))
  # move right to x,y+1
  if y < max_val-1:
    if distmap[x,y+1]>map[x,y+1]+distmap[x,y] and not visited[x,y+1]:
      distmap[x,y+1]=map[x,y+1]+distmap[x,y]
      originmap[x,y+1]=np.ravel_multi_index([x,y], (max_val,max_val))
  # move left to x,y-1
  if y > 0:
    if distmap[x,y-1]>map[x,y-1]+distmap[x,y] and not visited[x,y-1]:
      distmap[x,y-1]=map[x,y-1]+distmap[x,y]
      originmap[x,y-1]=np.ravel_multi_index([x,y], (max_val,max_val))
# =============================================================================
# # Uncomment the Following Block if the Robot Can Move in All Directions
#   # move upper left to x-1,y-1
#   if x > 0 and y > 0:
#     if distmap[x-1,y-1]>map[x-1,y-1]+distmap[x,y] and not visited[x-1,y-1]:
#       distmap[x-1,y-1]=map[x-1,y-1]+distmap[x,y]
#       originmap[x-1,y-1]=np.ravel_multi_index([x,y], (max_val,max_val))
#   # move upper right to x-1,y+1
#   if x > 0 and y < max_val-1:
#     if distmap[x-1,y+1]>map[x-1,y+1]+distmap[x,y] and not visited[x-1,y+1]:
#       distmap[x-1,y+1]=map[x-1,y+1]+distmap[x,y]
#       originmap[x-1,y+1]=np.ravel_multi_index([x,y], (max_val,max_val))      
#   # move lower left to x+1,y-1
#   if x < max_val-1 and y > 0:
#     if distmap[x+1,y-1]>map[x+1,y-1]+distmap[x,y] and not visited[x+1,y-1]:
#       distmap[x+1,y-1]=map[x+1,y-1]+distmap[x,y]
#       originmap[x+1,y-1]=np.ravel_multi_index([x,y], (max_val,max_val))
#   # move lower right to x+1,y+1
#   if x < max_val-1 and y < max_val-1:
#     if distmap[x+1,y+1]>map[x+1,y+1]+distmap[x,y] and not visited[x+1,y+1]:
#       distmap[x+1,y+1]=map[x+1,y+1]+distmap[x,y]
#       originmap[x+1,y+1]=np.ravel_multi_index([x,y], (max_val,max_val))         
# =============================================================================

# Update the Visited Cell and Shorter Measured Distances
  visited[x,y]=True
  dismaptemp=distmap
  dismaptemp[np.where(visited)]=np.Infinity
  # now we find the shortest path so far
  minpost=np.unravel_index(np.argmin(dismaptemp),np.shape(dismaptemp))
  x,y=minpost[0],minpost[1]
  if x==end[0] and y==end[1]:
    finished=True
  count=count+1

# Start Backtracking to Plot the Path
mattemp=map.astype(float)
path=[]
mattemp[np.int(x),np.int(y)]=-1
while x>start[0] or y>start[1]:
  path.append([np.int(x),np.int(y)])
  index=np.unravel_index(np.int(originmap[np.int(x),np.int(y)]), (max_val,max_val))
  x,y=index[0],index[1]
  mattemp[np.int(x),np.int(y)]=-1
path.append([np.int(x),np.int(y)])

# Save the Coordinates of the Path
X, Y = np.where(mattemp == -1)

# Save the Coordinates of the Obstacles
Xobs, Yobs = np.where(mattemp == np.inf)

#------------------------------------------------------------------------------
# Path Visualization
#------------------------------------------------------------------------------

# Output and Visualization of the Path
current_cmap = plt.cm.Blues
current_cmap.set_bad(color='brown')
cmap.set_under('green')
fig, ax = plt.subplots(figsize=(12,12))
ax.matshow(mattemp,cmap=plt.cm.Blues, vmin=0, vmax=max_cost)
ax.set_xlabel('y')
ax.set_ylabel('x')
ax.set_title('Path Planning')
for i in range(max_val):
    for j in range(max_val):
      c = map[j,i]
      ax.text(i, j, str(c), va='center', ha='center', fontsize=8)
      if c == np.inf:
          ax.text(i, j, str(c), va='center', ha='center', color='w', fontsize=8)
# Results
print('The path length is: '+np.str(distmap[end[0],end[1]]))

#==============================================================================