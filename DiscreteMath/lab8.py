from collections import deque
import random

def bfs(capacity, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)
    
    while queue:
        u = queue.popleft()
        
        for v in range(len(capacity)):
            if v not in visited and capacity[u][v] > 0:  # Если есть остаточная пропускная способность
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
    return False

# Алгоритм Эдмондса-Карпа для поиска максимального потока
def edmonds_karp(capacity, source, sink):
    n = len(capacity)
    parent = [-1] * n
    max_flow = 0

    # Пока есть увеличивающий путь, увеличиваем поток
    while bfs(capacity, source, sink, parent):
        # Находим минимальную пропускную способность вдоль пути
        path_flow = float('Inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, capacity[u][v])
            v = u

        # Обновляем остаточную сеть
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = u

        max_flow += path_flow

    return max_flow

# Нахождение минимального разреза
def find_min_cut(capacity, source):
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        u = queue.popleft()

        for v in range(len(capacity)):
            if v not in visited and capacity[u][v] > 0:  # Если есть остаточная пропускная способность
                queue.append(v)
                visited.add(v)

    return visited

# Пример графа с рёбрами и их пропускными способностями
edges = [
    ('A', 'B', 5), ('A', 'C', 9), ('A', 'I', 4),
    ('B', 'C', 2), ('B', 'G', 2), ('B', 'I', 2),
    ('I', 'C', 4), ('I', 'G', 2), ('I', 'H', 7),
    ('D', 'C', 2), ('E', 'D', 7), ('F', 'E', 7),
    ('F', 'D', 7), ('G', 'D', 3), ('G', 'C', 7),
    ('G', 'F', 3), ('G', 'E', 3), ('H', 'C', 7),
    ('H', 'G', 7), ('H', 'F', 7), ('F', 'C', 2),
]

# Словарь для преобразования имён узлов в индексы
nodes = list(set([u for u, v, _ in edges] + [v for u, v, _ in edges]))
node_map = {node: i for i, node in enumerate(nodes)}

# Инициализация матрицы пропускных способностей
n = len(nodes)
capacity = [[0] * n for _ in range(n)]

# Заполнение матрицы пропускных способностей
for u, v, c in edges:
    capacity[node_map[u]][node_map[v]] = c

# Исходный исток и сток
source, sink = node_map['A'], node_map['C']

# Вывод истока и стока
print(f"Исток: A, Сток: C")

# Поиск максимального потока
max_flow = edmonds_karp(capacity, source, sink)
print(f"Максимальный поток: {max_flow}")

# Поиск минимального разреза
min_cut_set = find_min_cut(capacity, source)
min_cut_nodes = [nodes[i] for i in min_cut_set]
non_reachable_nodes = [nodes[i] for i in range(n) if i not in min_cut_set]
print(f"Минимальный разрез: {min_cut_nodes} / {non_reachable_nodes}")

# Генерация случайных пропускных способностей от 100 до 1000
random_capacity = [[0] * n for _ in range(n)]
for u, v, _ in edges:
    random_capacity[node_map[u]][node_map[v]] = random.randint(100, 1000)

# Поиск максимального потока с случайными пропускными способностями
max_flow_random = edmonds_karp(random_capacity, source, sink)
print(f"\nМаксимальный поток с случайными пропускными способностями: {max_flow_random}")

# Поиск минимального разреза с случайными пропускными способностями
min_cut_set_random = find_min_cut(random_capacity, source)
min_cut_nodes_random = [nodes[i] for i in min_cut_set_random]
non_reachable_nodes_random = [nodes[i] for i in range(n) if i not in min_cut_set_random]
print(f"Минимальный разрез с случайными пропускными способностями: {min_cut_nodes_random} / {non_reachable_nodes_random}")

