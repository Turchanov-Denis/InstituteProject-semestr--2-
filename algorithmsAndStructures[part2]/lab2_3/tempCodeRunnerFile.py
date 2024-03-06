    distances = [-1] * self.num_vertices
        queue = [(start_vertex, 0)]  # Добавляем начальную вершину и ее расстояние

        while queue:
            current_vertex, distance = queue.pop(0)
            distances[current_vertex] = distance
            visited[current_vertex] = True

            for neighbor in self.get_adjacent_vertices(current_vertex):
                if not visited[neighbor]:
                    # Увеличиваем расстояние на 1 для соседней вершины
                    queue.append((neighbor, distance + 1))

        return distances