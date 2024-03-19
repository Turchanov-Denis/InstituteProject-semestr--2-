import json


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
        print(parent)
        for edge in edges:
            u, v, w = edge
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                result.append((u, v, w))

        return result


if __name__ == "__main__":
    graph = Graph.from_json("adjacency_matrix_lab_6.json")
    print(graph.kruskala())
