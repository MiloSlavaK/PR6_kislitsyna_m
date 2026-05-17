import numpy as np
from task2 import *

def get_outgoing_arcs(graph, rep_type: str, vertex: int) -> list[tuple[int, int]]:

    result = []

    if rep_type in ('матрица смежности', 'adjacency_matrix'):
        for j, val in enumerate(graph[vertex]):
            if val != 0:
                result.append((vertex, j))

    elif rep_type in ('матрица инцидентности', 'incidence_matrix'):
        n_edges = graph.shape[1]
        for j in range(n_edges):
            if graph[vertex, j] == 1:
                for i in range(graph.shape[0]):
                    if graph[i, j] == -1:
                        result.append((vertex, i))
                        break

    elif rep_type in ('список смежности', 'adjacency_list'):
        for v in graph.get(vertex, []):
            result.append((vertex, v))

    elif rep_type in ('список дуг', 'упорядоченный список дуг', 'edge_list'):
        for u, v in graph:
            if u == vertex:
                result.append((u, v))
    else:
        raise ValueError(f"Неизвестный тип: {rep_type}")

    return result

print("\n Исходящие дуги из вершины 1 из списка смежности:")
out_arcs = get_outgoing_arcs(adj_list, 'список смежности', 1)
print(out_arcs)

print("\n Исходящие дуги из вершины 1 из матрицы инцидентности:")
out_arcs_inc = get_outgoing_arcs(inc_matrix, 'матрица инцидентности', 1)
print(out_arcs_inc)


'''
 Исходящие дуги из вершины 1 из списка смежности:
[(1, 2), (1, 3), (1, 4)]

 Исходящие дуги из вершины 1 из матрицы инцидентности:
[(1, 2), (1, 3), (1, 4)]
'''
