def matrix_adjacency(graph, count_top):
    result = [[0] * count_top for _ in range(count_top)]
    for edge in graph:
        result[edge[0]][edge[1]] = 1
    return result

def matrix_incidence(matrix_adjacency, count_edge, count_top):
    result = [[0] * count_edge for _ in range(count_top)]
    count = 0
    for i in range(len(matrix_adjacency)):
        for j in range(len(matrix_adjacency[i])):
            if matrix_adjacency[i][j] != 0:
                result[i][count] = 1
                result[j][count] = -1
                count += 1
    return result

def algorithm_floyd(graph, count_top):
    INF = float('inf')
    dist_int = [[INF] * count_top for _ in range(count_top)]
    for i in range(count_top):
        dist_int[i][i] = 0

    for i in graph:
        dist_int[i[0]][i[1]] = min(dist_int[i[0]][i[1]], i[2])
        dist_int[i[1]][i[0]] = min(dist_int[i[1]][i[0]], i[2])

    for v in range(count_top):
        for a in range(count_top):
            for b in range(count_top):
                if dist_int[a][v] != INF and dist_int[v][b] != INF and dist_int[a][b] > dist_int[a][v] + dist_int[v][b]:
                    dist_int[a][b] = dist_int[a][v] + dist_int[v][b]
    return dist_int

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            if element >= 0:
                print(" ", element, " ", end="")
            else:
                print(element, " ", end="")
        print()

def main():
    graph = []
    count = 0
    count_top, count_edge = map(int, input().split())
    while count < count_edge:
        edge = list(map(int, input().split()))
        graph.append(edge)
        count += 1

    print("\nМатрица смежности:\n")
    print_matrix(matrix_adjacency(graph, count_top))

    print("\nМатрица инцидентности:\n")
    adj_matrix = matrix_adjacency(graph, count_top)
    print_matrix(matrix_incidence(adj_matrix, count_edge, count_top))

    print("\nКратчайшие пути между вершинами:\n")
    print_matrix(algorithm_floyd(graph, count_top))

if __name__ == "__main__":
    main()