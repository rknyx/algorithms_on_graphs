#Uses python3

import sys

visited = []


def number_of_components(adj):
    global visited
    comp_count = 0
    for i in range(len(adj)):
        if i not in visited:
            dps(adj, i)
            comp_count += 1
    return comp_count


def dps(adj, fr):
    global visited
    for neighbor in adj[fr]:
        if neighbor not in visited:
            visited.append(neighbor)
            dps(adj, neighbor)


if __name__ == '__main__':
#     input = """4 2
# 1 2
# 3 2
# """
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    vertices_count, edges_count = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * edges_count):2], data[1:(2 * edges_count):2]))
    adj = [[] for _ in range(vertices_count)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
