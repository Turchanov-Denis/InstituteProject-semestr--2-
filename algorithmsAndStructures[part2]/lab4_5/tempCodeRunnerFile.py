    while queue:
                    current_vertex = queue.pop(0)
                    component.append(current_vertex)
                    for neighbor in self.get_adjacent_vertices(current_vertex):
                        if not visited[neighbor]:
                            queue.insert(0, neighbor)
                            visited[neighbor] = True
                components.append(component)