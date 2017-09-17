#Uses python3

import sys
from collections import deque


def bipartite(adj):
    return 1 if breadth_first_search_bipartite(adj, 0) else 0


def breadth_first_search_bipartite(adj, s):
    queue = deque()
    queue.append(s)
    colors = [-1] * len(adj)
    colors[s] = True

    while len(queue) > 0:
        vertex = queue.popleft()
        vertex_color = colors[vertex]
        for neighbor in adj[vertex]:
            if colors[neighbor] == -1:
                colors[neighbor] = not vertex_color
                queue.append(neighbor)
            elif colors[neighbor] == vertex_color:
                return False
    return True

input_test = """5 4
5 2
4 2
3 4
1 4"""

if __name__ == '__main__':
    # input = input_test
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
