#Uses python3
from array import array as arr
from itertools import repeat
import sys
counter = 0


def dps(adj, fr):
    global visited
    global counter
    global post_order
    counter += 1
    for neighbor in adj[fr]:
        if visited[neighbor] == 0:
            visited[neighbor] = 1
            dps(adj, neighbor)
    counter += 1
    post_order[fr] = counter


def toposort(adj):
    for i in range(len(adj)):
        if visited[i] == 0:
            dps(adj, i)
    #write your code here
    return reversed(sorted(range(len(post_order)), key=lambda k: post_order[k]))

input = """5 7
2 1
3 2
3 1
4 3
4 1
5 2
5 3
"""

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    visited = arr('b', repeat(0, n))
    post_order = arr('i', repeat(0, n))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

