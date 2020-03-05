from collections import defaultdict


class Graph:
    def __init__(self, nodes_no, edges_no):
        self._graph = defaultdict(list)
        self._nodes_no = nodes_no
        self._edges_no = edges_no

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
                        if distance > (self._nodes_no - 1):
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

        return calculated[1:]


nodes_no, edges_no, start = map(int, input().split())
graph = Graph(nodes_no, edges_no)
for i in range(0, edges_no):
    _from, to, value = map(int, input().split())
    graph.add(_from, to, value)

for i in graph.bellman_ford(start):
    if i == -float('Inf'):
        print("-")
    elif i == float('Inf'):
        print("*")
    else:
        print(i)
