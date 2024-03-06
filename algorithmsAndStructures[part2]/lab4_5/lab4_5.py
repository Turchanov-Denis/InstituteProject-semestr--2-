import json
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, adj_matrix):
        self.adj_matrix = adj_matrix
        self.num_vertices = len(adj_matrix)

    @classmethod
    def from_json(cls, file_path):
        with open(file_path, 'r') as file:
            adj_matrix = json.load(file)
        return cls(adj_matrix)

    def get_adjacent_vertices(self, v):
        adjacent_vertices = []
        for i in range(self.num_vertices):
            if self.adj_matrix[v][i] == 1:
                adjacent_vertices.append(i)
        return adjacent_vertices
    def get_adjacent_verticesS(self, v, transposed_graph):
        adjacent_vertices = []
        for i in range(self.num_vertices):
            if transposed_graph[v][i] == 1:
                adjacent_vertices.append(i)
        return adjacent_vertices
    def dfs_components(self, start_vertex):
        visited = [False] * self.num_vertices
        components = []
        for vertex in range(self.num_vertices):
            if not visited[vertex]:
                component = []
                queue = [vertex]
                visited[vertex] = True
                while queue:
                    current_vertex = queue.pop(0)
                    component.append(current_vertex)
                    for neighbor in self.get_adjacent_vertices(current_vertex):
                        if not visited[neighbor]:
                            queue.insert(0, neighbor)
                            visited[neighbor] = True
                components.append(component)
        return components

    def dfs_componentsS(self, start_vertex, verticesS, transposed_graph):
        print(verticesS)
        visited = [False] * len(verticesS)
        components = []
        for vertex in verticesS:
            if not visited[vertex]:
                component = []
                queue = [vertex]
                visited[vertex] = True
                while queue:
                    current_vertex = queue.pop(0)
                    component.append(current_vertex)
                    for neighbor in self.get_adjacent_verticesS(current_vertex,transposed_graph):
                        if not visited[neighbor]:
                            queue.insert(0, neighbor)
                            visited[neighbor] = True
                components.append(component)
        return components

    def kosaraju(self):
        finish_times = self.dfs()
        transposed_graph = self.transpose()
        sorted_vertices = sorted(
            range(self.num_vertices), key=lambda x: finish_times[x], reverse=True)
        return self.dfs_componentsS(sorted_vertices[0], sorted_vertices, transposed_graph)

    def dfs(self):
        visited = [False] * self.num_vertices
        finish_times = [0] * self.num_vertices
        time = 0

        for vertex in range(self.num_vertices):
            if not visited[vertex]:
                time = self.dfs_util(self.adj_matrix, vertex,
                                     visited, finish_times, time)

        return finish_times

    def dfs_util(self, graph, vertex, visited, finish_times, time):
        visited[vertex] = True
        for neighbor in range(self.num_vertices):
            if graph[vertex][neighbor] == 1 and not visited[neighbor]:
                time = self.dfs_util(
                    graph, neighbor, visited, finish_times, time)

        time += 1
        finish_times[vertex] = time

        return time

    def draw_graph(self):
        G = nx.Graph()
        for i in range(self.num_vertices):
            G.add_node(i)
            for j in range(self.num_vertices):
                if self.adj_matrix[i][j] == 1:
                    G.add_edge(i, j)

        pos = nx.circular_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='skyblue',
                node_size=1000, font_size=12, font_weight='bold', arrowsize=20)
        plt.show()

    def transpose(self):
        transposed_graph = [
            [0] * self.num_vertices for _ in range(self.num_vertices)]

        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                transposed_graph[i][j] = self.adj_matrix[j][i]

        return transposed_graph


if __name__ == "__main__":
    g4 = Graph.from_json("adjacency_matrix[test1].json")
    g5 = Graph.from_json("adjacency_matrix[test2].json")
    # g5.draw_graph()
    # print("\nDFS components:", g4.dfs_components(0))
    # print("\nDFS components:", g5.draw_graph())
    print("\nDFS5:", g5.kosaraju())
