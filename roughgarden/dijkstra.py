from collections import defaultdict
from heapq import heappush, heappop


class Graph:
    def __init__(self, nodes_count):
        self._graph = defaultdict(list)
        self._nodes_count = nodes_count
        self._visited = dict()

    def add(self, node1, node2, value):
        self._graph[node1].append((node2, value))

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


nodes_no = 200
graph = Graph(nodes_no)
for node1 in range(1, nodes_no + 1):
    row = input().split()
    for i in range(0, len(row)):
        if i != 0:
            node2, value = map(lambda x: int(x), row[i].split(','))
            graph.add(node1, node2, value)

d = graph.dijkstra(1)

for i in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]:
    print(i, d[i])

#7 2599
#37 2610
#59 2947
#82 2052
#99 2367
#115 2399
#133 2029
#165 2442
#188 2505
#197 3068