import numpy as np
from task2 import *

def _infer_n(graph, rep_type: str) -> int:
    if rep_type in ('матрица смежности', 'adjacency_matrix'):
        return graph.shape[0]
    elif rep_type in ('матрица инцидентности', 'incidence_matrix'):
        return graph.shape[0]
    elif rep_type in ('список смежности', 'adjacency_list'):
        return max(graph.keys()) + 1 if graph else 0
    elif rep_type in ('список дуг', 'упорядоченный список дуг', 'edge_list'):
        return max(max(u, v) for u, v in graph) + 1 if graph else 0
    return 0

def _to_edge_list(graph, rep_type: str) -> list[tuple[int, int]]:
    n = _infer_n(graph, rep_type)
    edges = []

    if rep_type in ('матрица смежности', 'adjacency_matrix'):
        for i in range(n):
            for j in range(n):
                if graph[i, j] != 0:
                    edges.append((i, j))
    elif rep_type in ('матрица инцидентности', 'incidence_matrix'):
        n_edges = graph.shape[1]
        for j in range(n_edges):
            start = end = None
            for i in range(n):
                if graph[i, j] == 1:
                    start = i
                elif graph[i, j] == -1:
                    end = i
            if start is not None and end is not None:
                edges.append((start, end))
    elif rep_type in ('список смежности', 'adjacency_list'):
        for u, neighbors in graph.items():
            for v in neighbors:
                edges.append((u, v))
    elif rep_type in ('список дуг', 'упорядоченный список дуг', 'edge_list'):
        edges = list(graph)
    return edges


def _from_edge_list(edges: list[tuple[int, int]], to_type: str, n: int):
    if to_type in ('матрица смежности', 'adjacency_matrix'):
        mat = np.zeros((n, n), dtype=int)
        for u, v in edges:
            mat[u, v] = 1
        return mat
    elif to_type in ('матрица инцидентности', 'incidence_matrix'):
        m = len(edges)
        mat = np.zeros((n, m), dtype=int)
        for j, (u, v) in enumerate(edges):
            mat[u, j] = 1
            mat[v, j] = -1
        return mat
    elif to_type in ('список смежности', 'adjacency_list'):
        d = {i: [] for i in range(n)}
        for u, v in edges:
            d[u].append(v)
        return d
    elif to_type in ('список дуг', 'edge_list'):
        return list(edges)
    else:
        raise ValueError(f"Неизвестный целевой тип: {to_type}")


def convert_graph(graph, from_type: str, to_type: str):

    if from_type == to_type:
        return graph
    edges = _to_edge_list(graph, from_type)
    n = _infer_n(graph, from_type)
    return _from_edge_list(edges, to_type, n)




print("\nМатрица смежности → Матрица инцидентности:")
inc_from_adj = convert_graph(adj_matrix, 'матрица смежности', 'матрица инцидентности')
print(inc_from_adj)

print("\nСписок дуг → Список смежности:")
adj_from_edges = convert_graph(edge_list, 'список дуг', 'список смежности')
print(adj_from_edges)

'''
Матрица смежности → Матрица инцидентности:
[[ 1  1  1  0  0  0  0  0]
 [-1  0  0  1  1  1  0  0]
 [ 0 -1  0 -1  0  0 -1  0]
 [ 0  0  0  0 -1  0  1 -1]
 [ 0  0 -1  0  0 -1  0  1]]

Список дуг → Список смежности:
{0: [1, 2, 4], 1: [2, 3, 4], 2: [], 3: [2], 4: [3]}
'''