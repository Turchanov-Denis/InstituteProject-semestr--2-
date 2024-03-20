import json
import matplotlib.pyplot as plt
import networkx as nx
import copy
import sys

class Graph():
    def __init__(self):
        self.graph = {}  # {'A': {'B': 5, 'D': 3}, 'B': {'A': 5, 'C': 2}} // example

    @classmethod
    def from_json(cls, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        graph = cls()
        for i, u in enumerate(data["nodes"]):
            for j, v in enumerate(data["nodes"]):
                if data["adjacency_matrix"][i][j] != 0:
                    graph.add_edge(u, v, data["adjacency_matrix"][i][j])
        return graph

    @staticmethod
    def draw_graph(graph_data, graph_data_ext=None):
        # не нравица что тупо дублируется ветка if - elif, но зато работает
        G1 = nx.DiGraph()
        G2 = nx.DiGraph()
        if isinstance(graph_data, dict):
            for node in graph_data:
                G1.add_node(node)

            for node, edges in graph_data.items():
                for edge, weight in edges.items():
                    G1.add_edge(node, edge, weight=weight)

        elif isinstance(graph_data, list):
            for edge in graph_data:
                source, target, weight = edge
                G1.add_edge(source, target, weight=weight)
        #  2 arg tree begin -> compose -> view
        if graph_data_ext:
            if isinstance(graph_data_ext, dict):
                for node in graph_data_ext:
                    G2.add_node(node)

                for node, edges in graph_data_ext.items():
                    for edge, weight in edges.items():
                        G2.add_edge(node, edge, weight=weight)

            elif isinstance(graph_data_ext, list):
                for edge in graph_data_ext:
                    source, target, weight = edge
                    G2.add_edge(source, target, weight=weight)
            G = nx.compose(G1, G2)
            pos_G1 = nx.spring_layout(G1)
            pos_G2 = nx.spring_layout(G2)

            pos_G2_shifted = {node: (x + 1, y + 1)
                              for node, (x, y) in pos_G2.items()}

            pos = {**pos_G1, **pos_G2_shifted}

            plt.subplot(121)
            nx.draw(G1, pos=pos, with_labels=True,
                    node_color='lightblue', node_size=1000, font_size=12)
            plt.title('Граф G1')

            plt.subplot(122)
            nx.draw(G2, pos=pos, with_labels=True,
                    node_color='lightgreen', node_size=1000, font_size=12)
            plt.title('Граф G2')

            plt.tight_layout()
            plt.show()
         #  1 arg tree continue
        else:
            pos = nx.spring_layout(G1)
            nx.draw(G1, pos, with_labels=True, node_size=2000, node_color="skyblue",
                    font_size=12, font_weight="bold")  # Рисуем узлы
            nx.draw_networkx_edge_labels(G1, pos, edge_labels={(
                u, v): d['weight'] for u, v, d in G1.edges(data=True)}, font_color='red')

            plt.title("Граф")
            plt.axis("off")
            plt.show()

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = {}
        self.graph[u][v] = w

        if v not in self.graph:
            self.graph[v] = {}
        self.graph[v][u] = w

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)
        parent[x_root] = y_root

    def kruskala(self):
        result = []
        edges = []
        parent = {}
        for u in self.graph.keys():
            for v, w in self.graph[u].items():
                edges.append((u, v, w))
        edges.sort(key=lambda x: x[2])

        for u, v, _ in edges:
            parent[u] = u
            parent[v] = v
        print(self.graph)
        for edge in edges:
            u, v, w = edge
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                result.append((u, v, w))
                self.union(parent, x, y)
        return result

    def prime(self):
        result = []
        visited = set()

        start_vertex = list(self.graph.keys())[0]

        visited.add(start_vertex)

        while len(visited) < len(self.graph):
            min_weight = sys.maxsize
            min_edge = None

            for u in visited:
                for v, weight in self.graph[u].items():
                    if v not in visited and weight < min_weight:
                        min_weight = weight
                        min_edge = (u, v, weight)

            if min_edge:
                u, v, weight = min_edge
                result.append((u, v, weight))
                visited.add(v)

        return result
        

    def edges(self):
        edges = []
        for u in self.graph.keys():
            for v, w in self.graph[u].items():
                edges.append((u, v, w))
        edges.sort(key=lambda x: x[2])
        return edges


if __name__ == "__main__":
    graph = Graph.from_json("adjacency_matrix_lab_6.json")

    # graph.draw_graph(graph.graph, graph.kruskala())
    # print(graph.kruskala())
    print(graph.edges())
    graph.draw_graph(graph.graph, graph.prime())
