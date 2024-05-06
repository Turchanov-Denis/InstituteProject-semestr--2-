import json
import numpy as np


class Graph:
    def __init__(self):
        self.graph = {}  # Example: {'A': {'B': 5, 'D': 3}, 'B': {'A': 5, 'C': 2}}
        self.nodes = []  # Example: ['A', 'B'...]
        self.source = None

    def add_edge(self, from_node, to_node, weight):
        if from_node in self.graph:
            self.graph[from_node][to_node] = weight
        else:
            self.graph[from_node] = {to_node: weight}
        # Ensure all nodes are tracked
        if from_node not in self.nodes:
            self.nodes.append(from_node)
        if to_node not in self.nodes:
            self.nodes.append(to_node)

    @classmethod
    def from_json(cls, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        graph = cls()
        for i, u in enumerate(data["nodes"]):
            for j, v in enumerate(data["nodes"]):
                if data["adjacency_matrix"][i][j] != 0:
                    graph.add_edge(u, v, data["adjacency_matrix"][i][j])
        graph.source = data
        return graph

    def dijkstra(self, start):
        INF = float('inf')
        n = len(self.nodes)
        dist = {node: INF for node in self.nodes}
        dist[start] = 0
        used = {node: False for node in self.nodes}
        min_dist = 0
        min_vertex = start
        while min_dist < INF:
            i = min_vertex
            used[i] = True
            for j in self.graph.get(i, {}):
                if dist[i] + self.graph[i][j] < dist[j]:
                    dist[j] = dist[i] + self.graph[i][j]
            min_dist = INF
            for j in self.nodes:
                if not used[j] and dist[j] < min_dist:
                    min_dist = dist[j]
                    min_vertex = j
        return dist


    def bellman(self, start):
        INF = float('inf')
        distances = {node: INF for node in self.nodes}
        distances[start] = 0

        for _ in range(len(self.nodes) - 1):
            for from_node, neighbors in self.graph.items():
                for to_node, weight in neighbors.items():
                    if distances[from_node] + weight < distances[to_node]:
                        distances[to_node] = distances[from_node] + weight

        return distances


if __name__ == "__main__":
    graph = Graph.from_json("adjacency_matrix_lab_6.json")
    print(graph.dijkstra('A'))
    print(graph.bellman('A'))
    print("Source", graph.source['nodes'], "\n",
          np.matrix(graph.source['adjacency_matrix']))
