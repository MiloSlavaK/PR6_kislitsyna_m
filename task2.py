import numpy as np

vertices = 5
edges_raw = [(0,1), (0,2), (0,4), (1,2), (1,3), (1,4), (3,2), (4,3)]

# а) матрица смежности
adj_matrix = np.zeros((vertices, vertices), dtype=int)
for i, j in edges_raw:
    adj_matrix[i][j] = 1

# б) матрица инцидентности
num_edges = len(edges_raw)
inc_matrix = np.zeros((vertices, num_edges), dtype=int)
for u, (i, j) in enumerate(edges_raw):
    inc_matrix[i][u] = 1
    inc_matrix[j][u] = -1

# в) список смежности
adj_list = {i: [] for i in range(vertices)}
for i, j in edges_raw:
    adj_list[i].append(j)

# г) список дуг
edge_list = list(edges_raw)

print("a)", "\n", adj_matrix, "\n")
print("б)", "\n", inc_matrix, "\n")
print("в)", adj_list, "\n")
print("г)", edge_list, "\n")

'''
a) 
 [[0 1 1 0 1]
 [0 0 1 1 1]
 [0 0 0 0 0]
 [0 0 1 0 0]
 [0 0 0 1 0]] 

б) 
 [[ 1  1  1  0  0  0  0  0]
 [-1  0  0  1  1  1  0  0]
 [ 0 -1  0 -1  0  0 -1  0]
 [ 0  0  0  0 -1  0  1 -1]
 [ 0  0 -1  0  0 -1  0  1]] 

в) {0: [1, 2, 4], 1: [2, 3, 4], 2: [], 3: [2], 4: [3]} 

г) [(0, 1), (0, 2), (0, 4), (1, 2), (1, 3), (1, 4), (3, 2), (4, 3)] 
'''