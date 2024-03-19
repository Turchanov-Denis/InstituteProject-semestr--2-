import json

class Graph():
    def __init__(self):
        self.graph = {} # {'A': {'B': 5, 'D': 3}, 'B': {'A': 5, 'C': 2}} // example

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


if __name__ == "__main__":
    graph = Graph.from_json("adjacency_matrix_lab_6.json")
    print(graph.graph)
