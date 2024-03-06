    visited[vertex] = True
        scc_component.append(vertex)

        for neighbor in range(self.num_vertices):
            if graph[vertex][neighbor] == 1 and not visited[neighbor]:
                self.dfs_util(graph, neighbor, visited, finish_times, time, scc_component)
