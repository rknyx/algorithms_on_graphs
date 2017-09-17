#Uses python3

import sys
from collections import deque


def distance(adj, s, t):
    return breadth_first_search(adj, s, t)


def breadth_first_search(adj, s, t):
    queue = deque()
    queue.append(s)
    distances = [-1] * len(adj)
    distances[s] = 0

    while len(queue) > 0:
        vertex = queue.popleft()
        for neighbor in adj[vertex]:
            if distances[neighbor] != -1:
                continue
            distances[neighbor] = distances[vertex] + 1
            if neighbor == t:
                return distances[neighbor]
            queue.append(neighbor)
    return -1

test_input1 = """5 4
5 2
1 3
3 4
1 4
3 5"""


if __name__ == '__main__':
    # input = test_input1
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
