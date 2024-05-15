import json
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import copy


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

    def draw_graph(self):
        G = nx.Graph()
        for node in self.graph:
            G.add_node(node)
        for node, edges in self.graph.items():
            for neighbor, weight in edges.items():
                G.add_edge(node, neighbor, weight=weight)
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()

    def fleury(self, inNode):
        eulerian_cycle = []
        graph = copy.deepcopy(self.graph)
        num_nodes = len(self.nodes)
        start_node = inNode
        while len(eulerian_cycle) < num_nodes:
            for node in eulerian_cycle:
                if not graph[node]:
                    start_node = node
                    return 'not found'
            temp_cycle = [start_node]
            while graph[start_node]:
                next_node = list(graph[start_node].keys())[0]
                edge_weight = graph[start_node].pop(next_node)
                if not graph[start_node]:
                    del graph[start_node]
                del graph[next_node][start_node]

                if temp_cycle[0] != temp_cycle[-1] or (len(temp_cycle)==1):

                    temp_cycle.append(next_node)

                start_node = next_node
            # Combine  temporary cycle in main
            if temp_cycle[0] != temp_cycle[-1]:
                return 'not found'
            eulerian_cycle += temp_cycle

        return eulerian_cycle


if __name__ == "__main__":
    graph = Graph.from_json("adjacency_matrix_lab_6.json")
    print("Source", graph.source['nodes'], "\n",
          np.matrix(graph.source['adjacency_matrix']))
    print("Eulerian Cycle:", graph.fleury('D'))
    print([graph.fleury(item) for item in graph.nodes])
    graph.draw_graph()
