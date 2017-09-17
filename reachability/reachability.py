#Uses python3

import sys

visited = []


def reach(adj, x, y):
    return dps(adj, x, y)


def dps(adj, fr, searched):
    for neighbor in adj[fr]:
        if neighbor in visited:
            continue
        else:
            visited.append(neighbor)
        if neighbor == searched:
            return 1
        if 1 == dps(adj, neighbor, searched):
            return 1
    return 0

if __name__ == '__main__':
    inp = sys.stdin.read()
#     inp = """4 2
# 1 2
# 3 2
# 1 4"""
    data = list(map(int, inp.split()))

    vertices, edges_count = data[0:2]

    data = data[2:]
    edges = list(zip(data[0:(2 * edges_count):2], data[1:(2 * edges_count):2]))
    x, y = data[2 * edges_count:]
    adj = [[] for _ in range(vertices)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    print(reach(adj, x, y))
