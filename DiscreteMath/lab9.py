import networkx as nx
import matplotlib.pyplot as plt

# Задаем граф по списку ребер
edges = [
    (5, 12), (12, 1), (12, 2), (3, 10), (10, 1), (6, 15),
    (11, 9), (4, 1), (8, 1), (10, 14), (13, 9), (2, 9),
    (7, 6), (7, 8), (10, 7), (9, 7), (10, 2), (5, 9),
    (3, 8), (3, 4), (4, 7), (3, 12), (6, 13), (11, 8),
    (14, 6), (10, 5), (2, 6), (4, 11), (3, 9), (8, 14)
]

# Создаем граф
G = nx.Graph()
G.add_edges_from(edges)

# Функция проверки двудольности
def is_bipartite(graph):
    return nx.is_bipartite(graph)

# Если граф не двудольный, находим минимальные ребра для удаления
def make_bipartite(graph):
    if is_bipartite(graph):
        return graph, []
    
    # Находим компоненты и их цвет
    colors = {}
    for node in graph.nodes():
        if node not in colors:
            stack = [node]
            colors[node] = 0
            
            while stack:
                current = stack.pop()
                for neighbor in graph.neighbors(current):
                    if neighbor not in colors:
                        colors[neighbor] = 1 - colors[current]
                        stack.append(neighbor)
                    elif colors[neighbor] == colors[current]:
                        graph.remove_edge(current, neighbor)
    
    return graph, []

# Алгоритм Форда-Фалкерсона для поиска наибольшего паросочетания
def ford_fulkerson(graph):
    def bfs(s, t, parent):
        visited = {node: False for node in graph.nodes()}
        queue = [s]
        visited[s] = True
        
        while queue:
            u = queue.pop(0)
            for v in graph.neighbors(u):
                if not visited[v] and (u, v) in graph.edges():
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
                    if v == t:
                        return True
        return False
    
    # Создаем ориентированный граф для алгоритма
    flow_graph = nx.DiGraph()
    flow_graph.add_edges_from(graph.edges())
    
    # Начальные параметры
    source = list(graph.nodes())[0]
    sink = list(graph.nodes())[-1]
    parent = {}
    max_flow = 0
    
    while bfs(source, sink, parent):
        # Находим минимальную пропускную способность
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, 1)  # В двудольном графе пропускная способность всегда 1
            s = parent[s]
        
        # Обновляем граф
        v = sink
        while v != source:
            u = parent[v]
            flow_graph[u][v]['capacity'] = flow_graph[u][v].get('capacity', 0) + path_flow
            flow_graph[v][u]['capacity'] = flow_graph[v][u].get('capacity', 0) - path_flow
            v = parent[v]
        
        max_flow += path_flow

    return max_flow, flow_graph

# Создаем двудольный граф
bipartite_graph, removed_edges = make_bipartite(G)

# Находим наибольшее паросочетание
matching = nx.bipartite.maximum_matching(bipartite_graph)

# Функция для визуализации графа
def visualize_graph(graph, matching):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500)
    
    # Отображаем паросочетание
    matching_edges = [(u, v) for u, v in matching.items() if v is not None]
    nx.draw_networkx_edges(graph, pos, edgelist=matching_edges, edge_color='red', width=2)
    
    plt.title("Bipartite Graph with Maximum Matching")
    plt.show()

# Визуализируем граф и результаты
visualize_graph(bipartite_graph, matching)

# Печатаем результаты
if removed_edges:
    print(f"Removed edges to make the graph bipartite: {removed_edges}")
else:
    print("The graph is already bipartite.")

print("Maximum matching:", matching)
