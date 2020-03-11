from collections import defaultdict


class Graph:
    def __init__(self, nodes_no, edges_no, start, stop):
        self._graph = defaultdict(dict)
        self._nodes_no = nodes_no
        self._edges_no = edges_no
        self._start = start
        self._stop = stop
        self._stop_in_degree = 0

    def add(self, _from, to, value):
        if to == self._stop:
            self._stop_in_degree += 1

        if _from in self._graph and to in self._graph[_from]:
            if value > self._graph[_from][to]:
                self._graph[_from][to] = value
        else:
            self._graph[_from][to] = value

    def bellman_ford(self):
        if self._start not in self._graph:
            return -float("Inf")
        if self._stop_in_degree == 0:
            return -float("Inf")

        # to_change - path weight changes during the current iteration
        to_change = {self._start: 0}

        # affected_nodes - nodes that were affected during the previous iteration
        affected_nodes = [self._start]

        calculated = [-float("Inf")] * (self._nodes_no + 1)
        distance = 0

        while True:
            for v in affected_nodes:
                for node, value in self._graph[v].items():
                    max_value = max(to_change[node] if node in to_change else calculated[node], calculated[v] + value)
                    if max_value != calculated[node]:
                        if distance > (self._nodes_no - 1):
                            to_change[node] = float("Inf")
                        else:
                            to_change[node] = max_value
            if to_change:
                affected_nodes = list(to_change.keys())
                for node in affected_nodes:
                    calculated[node] = to_change[node]
                    if node == self._stop and calculated[node] == float("Inf"):
                        return calculated[-1]
                to_change = {}
            else:
                break
            distance += 1

        return calculated[-1]


nodes_no, edges_no = map(int, input().split())
graph = Graph(nodes_no, edges_no, 1, nodes_no)
for i in range(0, edges_no):
    _from, to, value = map(int, input().split())
    graph.add(_from, to, value)

res = graph.bellman_ford()

if res == -float("Inf"):
    print(":(")
elif res == float("Inf"):
    print(":)")
else:
    print(res)
