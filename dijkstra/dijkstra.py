#Uses python3

import sys
import heapq
from array import array


def distance(adj, cost, s, t):
    visited = [False] * len(adj)
    _distance = [9999999] * len(adj)
    heap = [(9999999, i) for i in range(len(adj))]
    _distance[s], heap[s] = 0, (0, s)
    heapq.heapify(heap)
    while len(heap) > 0:
        vertex = heapq.heappop(heap)
        vertex_num = vertex[1]
        if visited[vertex_num]:
            continue
        visited[vertex_num] = True
        for index, neighbor_num in enumerate(adj[vertex_num]):
            if _distance[neighbor_num] > _distance[vertex_num] + cost[vertex_num][index]:
                _distance[neighbor_num] = _distance[vertex_num] + cost[vertex_num][index]
                heapq.heappush(heap, (_distance[neighbor_num], neighbor_num))
    return -1 if _distance[t] == 9999999 else _distance[t]


test_input_1 = """3 3
1 2 7
1 3 5
2 3 2
3 2"""

if __name__ == '__main__':
    input = sys.stdin.read()
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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
