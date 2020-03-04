from collections import defaultdict
from math import inf


class Graph:
    def __init__(self, nodes_no, edges_no):
        self._graph = defaultdict(list)
        self.nodes_no = nodes_no
        self.edges_no = edges_no

    def add(self, node1, node2, value):
        self._graph[node1].append((node2, value))

    def bellman_ford(self, start):
        changed = {}
        calculated = [inf] * (self.nodes_no + 1)
        calculated[start] = 0

        for i in range(1, 2 * nodes_no):
            for v in range(1, nodes_no + 1):
                for node, value in self._graph[v]:
                    min_value = min(changed[node] if node in changed else calculated[node], calculated[v] + value)
                    if min_value != calculated[node]:
                        if i > (nodes_no - 1):
                            changed[node] = -inf
                        else:
                            changed[node] = min_value
            if changed:
                for node in changed:
                    calculated[node] = changed[node]
                changed = {}
            else:
                break

        return calculated[1:]


nodes_no, edges_no, start = map(int, input().split())
graph = Graph(nodes_no, edges_no)
for i in range(0, edges_no):
    node1, node2, value = map(int, input().split())
    graph.add(node1, node2, value)

for i in graph.bellman_ford(start):
    if i == -inf:
        print("-")
    elif i == inf:
        print("*")
    else:
        print(i)
