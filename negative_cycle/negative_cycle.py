#Uses python3

import sys


def negative_cycle(adj, cost):
    distances = [999999] * len(adj)
    distances[0] = 0
    temp = None
    for i in range(len(adj) - 1):
        for vertex_num in range(len(adj)):
            for index, neighbor_num in enumerate(adj[vertex_num]):
                temp = distances[vertex_num] + cost[vertex_num][index]
                if distances[neighbor_num] > temp:
                    distances[neighbor_num] = temp

    for vertex_num in range(len(adj)):
        for index, neighbor_num in enumerate(adj[vertex_num]):
            temp = distances[vertex_num] + cost[vertex_num][index]
            if distances[neighbor_num] > temp:
                return 1
    return 0



test_input_1 = """4 4
1 2 5
4 1 2
2 3 2
3 1 1"""

if __name__ == '__main__':
    input = sys.stdin.read()
    # input = test_input_1
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
