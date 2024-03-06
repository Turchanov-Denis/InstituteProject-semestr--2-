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

    def dfs_components(self):
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
                            queue.append(neighbor)
                            visited[neighbor] = True

                components.append(component)

        return components

    def draw_graph(self):
        G = nx.Graph()
        for i in range(self.num_vertices):
            G.add_node(i)
            for j in range(i+1, self.num_vertices):
                if self.adj_matrix[i][j] == 1:
                    G.add_edge(i, j)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='skyblue',
                node_size=1000, font_size=12, font_weight='bold', arrowsize=20)
        plt.show()


if __name__ == "__main__":
    g = Graph.from_json("adjacency_matrix.json")
    # g.draw_graph()
    print("\nBFS components:", g.dfs_components(), "amount: ",len(g.dfs_components()) )
    
