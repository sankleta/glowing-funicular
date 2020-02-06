# Дан ориентированный взвешенный граф. Найдите кратчайшее расстояние
# одной заданной вершины до другой.

from collections import defaultdict
from heapq import heappush, heappop


class Graph:
    def __init__(self, nodes_count):
        self._graph = defaultdict(list)
        self._nodes_count = nodes_count
        self._visited = dict()

    def add(self, node1, node2, value):
        self._graph[node1].append((node2, value))

    def dijkstra(self, start_node, end_node):
        heap = []
        heappush(heap, (0, start_node))
        while heap:
            value, node = heappop(heap)
            if node == end_node:
                return value
            if node in self._visited:
                continue
            self._visited[node] = value
            for i, j in self._graph[node]:
                if i not in self._visited:
                    heappush(heap, (value + j, i))
        return -1


nodes_no, start_node, end_node = map(lambda x: int(x), input().split())
graph = Graph(nodes_no)
for node1 in range(1, nodes_no + 1):
    row = list(map(lambda x: int(x), input().split()))
    for i in range(0, len(row)):
        if (node1 - 1) != i and row[i] != -1:
            graph.add(node1, i + 1, row[i])

print (graph.dijkstra(start_node, end_node))

