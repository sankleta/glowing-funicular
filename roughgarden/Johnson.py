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
from heapq import heappop, heappush


class Graph:
    def __init__(self, nodes_no, edges_no):
        self._graph = defaultdict(list)
        self._nodes_no = nodes_no
        self._edges_no = edges_no
        self._has_cycles = False

    def add(self, _from, to, value):
        self._graph[_from].append((to, value))

    def bellman_ford(self, start):
        # to_change - path weight changes during the current iteration
        to_change = {start: 0}

        # affected_nodes - nodes that were affected during the previous iteration
        affected_nodes = [start]

        calculated = [float("Inf")] * (self._nodes_no + 1)
        distance = 0

        while True:
            for v in affected_nodes:
                for node, value in self._graph[v]:
                    min_value = min(to_change[node] if node in to_change else calculated[node], calculated[v] + value)
                    if min_value != calculated[node]:
                        if distance > self._nodes_no:
                            return calculated, True
                        else:
                            to_change[node] = min_value
            if to_change:
                affected_nodes = list(to_change.keys())
                for node in affected_nodes:
                    calculated[node] = to_change[node]
                to_change = {}
            else:
                break
            distance += 1

        return calculated, False

    def dijkstra(self, start_node, reweighting_coef):
        visited = dict()
        heap = []
        heappush(heap, (0, start_node))
        while heap:
            value, node = heappop(heap)
            if node in visited:
                continue
            visited[node] = value - reweighting_coef[start_node] + reweighting_coef[node]
            for i, j in self._graph[node]:
                if i not in visited:
                    heappush(heap, (value + j + reweighting_coef[node] - reweighting_coef[i], i))

        return visited

    def johnson(self):
        for v in range(1, self._nodes_no + 1):
            self.add(0, v, 0)

        reweighting_coef, has_cycles = self.bellman_ford(0)

        if not has_cycles:
            shortest_length = float("Inf")
            for v in range(1, self._nodes_no + 1):
                paths = self.dijkstra(v, reweighting_coef)
                for i in paths:
                    if paths[i] < shortest_length:
                        shortest_length = paths[i]
            return shortest_length
        else:
            return "NEGATIVE CYCLE"


def calculate_shortest_shortest_path(filename):
    with open(filename, 'r') as f:
        nodes_no, edges_no = map(lambda x: int(x), next(f).split())
        graph = Graph(nodes_no, edges_no)

        for line in f:
            _from, to, value = map(lambda x: int(x), line.split())
            graph.add(_from, to, value)

        return graph.johnson()


results = [calculate_shortest_shortest_path("g1.txt"), calculate_shortest_shortest_path("g2.txt"),
           calculate_shortest_shortest_path("g3.txt")]

print(results)
