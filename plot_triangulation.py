import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np

fname = "superior"

file_node = open(fname+".node", "r")
file_ele = open(fname+".ele", "r")
file_segs = open(fname+".edge", "r")
file_neigh = open(fname+".neigh", "r")
lines_node = file_node.readlines()
lines_ele = file_ele.readlines()
lines_segs = file_segs.readlines()
lines_neigh = file_neigh.readlines()

vertices = []
maps = []
triangles = []
segments = []
neighbours = []

# Read .node file
offset = 0
num_vertices = list(map(int, lines_node[0].rstrip().split(" ")))[0]
offset+=1
for i in range(offset, offset+num_vertices):
    line = lines_node[i]
    vertices.append(list(map(float, line.rstrip().split(" ")))[1:3])
    maps.append(list(map(float, line.rstrip().split(" ")))[3])
    i+=1

# Read .ele file
offset=0
num_triangles = list(map(int, lines_ele[0].rstrip().split(" ")))[0]
offset+=1 
for i in range(offset, offset+num_triangles):
    line = lines_ele[i]
    triangles.append(list(map(int, line.rstrip().split(" ")))[1:4])
    
# Read .edge file
offset=0
num_segments = list(map(int, lines_segs[0].rstrip().split(" ")))[0]
offset+=1 
for i in range(offset, offset+num_segments):
    line = lines_segs[i]
    segments.append(list(map(int, line.rstrip().split(" ")))[1:3])
    
# Read .neigh file
offset=0
num_triangles = list(map(int, lines_neigh[0].rstrip().split(" ")))[0]
offset+=1 
for i in range(offset, offset+num_triangles):
    line = lines_neigh[i]
    neighbours.append(list(map(int, line.rstrip().split(" ")))[1:4])

plt.figure(0, figsize=(8, 8))
plt.axis('off')
ax = plt.gca()

segs = []

for i in range(len(triangles)):
    for k in range(3):
        line = (vertices[triangles[i][k]], vertices[triangles[i][(k+1) % 3]])
        segs.append(line)
    
lc = LineCollection(segs, linewidths=1, linestyle="solid", color='black')
ax.add_collection(lc)

segs = []
for i in range(len(segments)):
    line = (vertices[segments[i][0]], vertices[segments[i][1]])
    segs.append(line)
    
lc = LineCollection(segs, linewidths=2, linestyle="solid", color='black')
ax.add_collection(lc)
    
for i in range(len(vertices)):
    x = vertices[i][0]
    y = vertices[i][1]
    mstyle = "."
    if maps[i] != -1:
        mstyle = "s"
    #plt.plot(x, y, mstyle, color='black')
    
#segs = []
#print(neighbours)
#for i in range(len(neighbours)):
#    x_start = 0.0
#    y_start = 0.0
#    for k in range(3):
#        x_start += vertices[triangles[i][k]][0]
#        y_start += vertices[triangles[i][k]][1]
#    x_start /= 3
#    y_start /= 3
#    for k in range(3):
#        x_end = 0.0
#        y_end = 0.0
#        neighbour = neighbours[i][k]
#        if neighbour < num_triangles:
#            for l in range(3):
#                x_end += vertices[triangles[neighbour][l]][0]
#                y_end += vertices[triangles[neighbour][l]][1]
#            x_end /= 3.0
#            y_end /= 3.0
#            line = ([x_start, y_start], [x_end, y_end])
#            segs.append(line)
#
#lc = LineCollection(segs, linewidths=2, linestyle="solid", color='green')
#ax.add_collection(lc)

ax.set_aspect('equal')
ax.set_xlim(0.1, 0.9)
ax.set_ylim(-0.8, -0.2)
    
plt.savefig("superior.pdf", bbox_inches="tight")
plt.show()