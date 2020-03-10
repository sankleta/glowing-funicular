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


class Graph:
    def __init__(self, nodes_no):
        self._nodes_no = nodes_no
        self._paths = [[float("Inf")] * self._nodes_no for i in range(self._nodes_no)]
        self._has_negative_cycle = False
        self._shortest_length = 0
        for i in range(self._nodes_no):
            self._paths[i][i] = 0

    def add(self, _from, to, value):
        if _from == to and to < 0:
            self._has_negative_cycle = True

        if self._paths[_from - 1][to - 1] > value:
            self._paths[_from - 1][to - 1] = value

        if value < self._shortest_length:
            self._shortest_length = value

    def floyd_warshall(self):
        if self._has_negative_cycle:
            return "NEGATIVE CYCLE"
        else:
            for k in range(self._nodes_no):
                for i in range(self._nodes_no):
                    for j in range(self._nodes_no):
                        if self._paths[i][j] > (self._paths[i][k] + self._paths[k][j]):
                            if i == j and self._paths[i][k] + self._paths[k][j] < 0:
                                self._has_negative_cycle = True
                                return "NEGATIVE CYCLE"
                            self._paths[i][j] = (self._paths[i][k] + self._paths[k][j])
                            if self._paths[i][k] + self._paths[k][j] < self._shortest_length:
                                self._shortest_length = self._paths[i][k] + self._paths[k][j]
            return self._shortest_length


def calculate_shortest_shortest_path(filename):
    with open(filename, 'r') as f:
        nodes_no, edges_no = map(lambda x: int(x), next(f).split())
        graph = Graph(nodes_no)

        for line in f:
            _from, to, value = map(lambda x: int(x), line.split())
            graph.add(_from, to, value)

        return graph.floyd_warshall()


results = [calculate_shortest_shortest_path("g1.txt"), calculate_shortest_shortest_path("g2.txt"),
           calculate_shortest_shortest_path("g3.txt")]

print(results)
