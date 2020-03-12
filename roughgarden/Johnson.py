from collections import defaultdict
from heapq import heappop, heappush


class Graph:
    def __init__(self, nodes_no, edges_no):
        self._graph = defaultdict(list)
        self._nodes_no = nodes_no
        self._edges_no = edges_no
        self._visited = dict()

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
                            to_change[node] = -float("Inf")
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

        return calculated

    def dijkstra(self, start_node):
        heap = []
        heappush(heap, (0, start_node))
        while heap:
            value, node = heappop(heap)
            if node in self._visited:
                continue
            self._visited[node] = value
            for i, j in self._graph[node]:
                if i not in self._visited:
                    heappush(heap, (value + j, i))

        return self._visited

    def johnson(self):
        for v in range(1, self._nodes_no + 1):
            self.add(0, v, 0)

        reweighting_coef = self.bellman_ford(0)


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
