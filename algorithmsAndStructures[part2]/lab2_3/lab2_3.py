import json


def read_adjacency_matrix(filename):
    with open(filename, 'r') as file:
        adjacency_matrix = json.load(file)
    return adjacency_matrix


def shortest_paths(graph, start):
    n = len(graph)
    
    sdl = [None] * n  # shortest distances list
    sdl[start] = 0
    bypass = [start]     # queue to bypass
    while bypass:
        u = bypass.pop(0)
        for v in range(n):
            if graph[u][v] == 1 and sdl[v] is None:
                sdl[v] = sdl[u] + 1
                bypass.append(v)

    return sdl

filename = 'adjacency_matrix.json'
graph = read_adjacency_matrix(filename)

start_node = 0
distances = shortest_paths(graph, start_node)
print("Shortest distances from a vertex", start_node,
      "to all other vertices:", distances)

