from collections import defaultdict

inf = 10000 * 2001


class Graph:
    def __init__(self, nodes_no, edges_no, start, stop):
        self._graph = defaultdict(list)
        self._nodes_no = nodes_no
        self._edges_no = edges_no
        self._start = start
        self._stop = stop

    def add(self, _from, to, value):
        self._graph[_from].append((to, value))

    def bellman_ford(self):

        # to_change - path weight changes during the current iteration
        to_change = {self._start: 0}

        # affected_nodes - nodes that were affected during the previous iteration
        affected_nodes = [self._start]

        calculated = [-inf] * (self._nodes_no + 1)
        distance = 0

        while True:
            for v in affected_nodes:
                for node, value in self._graph[v]:
                    max_value = max(to_change[node] if node in to_change else calculated[node], calculated[v] + value)
                    if max_value != calculated[node]:
                        if distance > (self._nodes_no - 1):
                            if node == self._stop:
                                return inf
                            to_change[node] = inf
                        else:
                            to_change[node] = max_value
            if to_change:
                affected_nodes = list(to_change.keys())
                for node in affected_nodes:
                    calculated[node] = to_change[node]
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

if res == -inf:
    print(":(")
elif res >= inf:
    print(":)")
else:
    print(res)
