# раскраска графа
def greedy_coloring(adj_matrix):
    num_vertices = len(adj_matrix)
    colors = [-1] * num_vertices
    colors[0] = 1
    for vertex in range(1, num_vertices):
        available_colors = set(range(1, num_vertices + 1))
        for neighbor in range(vertex):
            if adj_matrix[vertex][neighbor] == 1 and colors[neighbor] in available_colors:
                available_colors.remove(colors[neighbor])
        colors[vertex] = min(available_colors)
    return colors

adjacency_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0]
]

colors = greedy_coloring(adjacency_matrix)
print("Раскраска вершин графа:")
for vertex, color in enumerate(colors):
    print(f"Вершина {vertex} раскрашена в цвет {color}")
