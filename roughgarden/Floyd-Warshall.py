# The first line indicates the number of vertices and edges, respectively.
# Each subsequent line describes an edge (the first two numbers are its tail and head,
# respectively) and its length (the third number).
# NOTE: some of the edge lengths are negative.
# NOTE: These graphs may or may not have negative-cost cycles.
# Your task is to compute the "shortest shortest path".
# Precisely, you must first identify which, if any, of the three graphs have no
# negative cycles. For each such graph, you should compute all-pairs shortest paths
# and remember the smallest one.
# If each of the three graphs has a negative-cost cycle, then enter "NULL" in the box
# below. If one or more of the graphs have no negative-cost cycles, then enter
# the smallest of the lengths of their shortest shortest paths.
from collections import defaultdict


class Graph:
    def __init__(self, nodes_no, edges_no):
        self._graph = defaultdict(list)
        self._nodes_no = nodes_no
        self._edges_no = edges_no
        self._paths = [[float("Inf")] * self._nodes_no for i in range(self._nodes_no)]
        self._has_negative_cycle = False
        for i in range(self._nodes_no):
            self._paths[i][i] = 0

    def add(self, _from, to, value):
        self._graph[_from].append((to, value))
        if _from == to and to < 0:
            self._has_negative_cycle = True

        if self._paths[_from - 1][to - 1] > value:
            self._paths[_from - 1][to - 1] = value

    def floyd_warshall(self):
        if self._has_negative_cycle:
            return "-"
        else:
            for k in range(self._nodes_no):
                for i in range(self._nodes_no):
                    for j in range(self._nodes_no):
                        if self._paths[i][j] > (self._paths[i][k] + self._paths[k][j]):
                            self._paths[i][j] = (self._paths[i][k] + self._paths[k][j])
            return self._paths


with open("g1.txt", 'r') as f:
    nodes_no, edges_no = map(lambda x: int(x), next(f).split())
    graph = Graph(nodes_no, edges_no)

    for line in f:
        _from, to, value = map(lambda x: int(x), line.split())
        graph.add(_from, to, value)

    print(graph.floyd_warshall())
