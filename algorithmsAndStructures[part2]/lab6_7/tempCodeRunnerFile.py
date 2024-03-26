@staticmethod
    def draw_graph_from_dict(graph):
        plt.figure(figsize=(len(graph) * 0.5, len(graph) * 0.4))
        for i, u in enumerate(graph):
            for v, w in graph[u].items():
                x = i
                y = list(graph.keys()).index(v)
                plt.plot([x, y], [y, x], linewidth=2, color='b')
                plt.text((x + y) / 2, (x + y) / 2, str(w), fontsize=12, color='r')
        plt.scatter(range(len(graph)), [list(graph.keys()).index(v) for v in graph.keys()], color='g', zorder=5)
        plt.grid(True)
        plt.xlabel('Vertex')
        plt.ylabel('Vertex')
        plt.title('Graph Visualization')
        plt.show()