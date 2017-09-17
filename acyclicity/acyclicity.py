#Uses python3

import sys
from array import array as arr
from itertools import repeat
from collections import deque
visited = None


def acyclic(adj):
    global visited
    for vertex in range(len(adj)):
        if visited[vertex] == 0:
            if dps(adj, vertex, arr('b', repeat(0, len(visited)))):
                return 1
    return 0


def dps(adj, fr, on_stack):
    global visited
    on_stack[fr] = 1
    for neighbor in adj[fr]:
        if on_stack[neighbor] == 1:
            return True
        if visited[neighbor] == 0:
            visited[neighbor] = 1
            if dps(adj, neighbor, on_stack):
                return True
    on_stack[fr] = 0
    return False


# def dps_non_recursive2(adj, fr):
#     global visited
#     local_visited = arr('b', repeat(0, len(visited)))
#     stack = deque()
#     stack.append(fr)
#     visited[fr] = 1
#     while len(stack) > 0:
#         v = stack.pop()
#         if local_visited[v] == 1:
#             return True
#         local_visited[v] = 1
#         visited[v] = 1
#         stack.extend(reversed(adj[v]))
#


# def dps_non_recursive(adj, fr):
#     stack = deque()
#     stack.append(fr)
#     while len(stack) > 0:
#         vertex = stack[0]
#         if visited[vertex] == 1:
#             if vertex in stack:
#                 return True
#             stack.pop()
#         else:
#             visited[vertex] = 1
#
#
#         if visited[vertex] == 1:
#             stack.pop()
#         elif vertex in stack:
#             return True
#         else:
#             visited[vertex] = 1
#             stack.pop()
#             stack.extend(adj[vertex])

inp_0 = """5 7
1 2
2 3
1 3
3 4
1 4
2 5
3 5"""

inp_1 = """4 4
1 2
4 1
2 3
3 1"""

if __name__ == '__main__':
    # input = inp_0
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    visited = arr('b', repeat(0, n))
    print(acyclic(adj))
