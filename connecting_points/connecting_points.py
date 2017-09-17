#Uses python3
import sys
from math import hypot
from itertools import combinations

dummy_set = {}
iterator = 0


class SuperSet:
    def __init__(self, size):
        self.data = list(range(size))
        self.rank = [-1]*size

    def make_set(self, value):
        self.data[value] = value
        self.rank[value] = 0

    def find(self, value):
        if self.data[value] == value:
            return value
        self.data[value] = self.find(self.data[value])
        return self.data[value]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.data[x] = y
        else:
            self.data[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


test_input_1 = """4
0 0
0 1
1 0
1 1"""

test_input_2 = """5
0 0
0 2
1 1
3 0
3 2"""


def distance(a, b):
    return hypot(a[0] - b[0], a[1] - b[1])



if __name__ == '__main__':
    input = sys.stdin.read()
    # input = test_input_1
    data = list(map(int, input.split()))
    n = data[0]
    points = list(zip(data[1::2], data[2::2]))
    points_count = len(points)
    edges = list(combinations(range(len(points)), 2))
    distances = [distance(points[edge[0]], points[edge[1]]) for edge in edges]
    sorted_edges = [x[1] for x in sorted(enumerate(edges), key=lambda x: distances[x[0]])]
    sorted_distances = sorted(distances)

    common_distance = 0
    # points_sets = [set([i]) for i in range(len(points))]
    _set = SuperSet(len(points))

    edge_number = 0
    for edge in sorted_edges:
        a, b = edge[0], edge[1]
        # if points_sets[a] != points_sets[b]:
        if _set.find(a) != _set.find(b):
            common_distance += sorted_distances[edge_number]
            _set.union(a, b)
            # for m in points_sets[b]:
            #     points_sets[a].add(m)
            # points_sets[b] = points_sets[a]
        edge_number += 1

    print("{0:.9f}".format(common_distance))
