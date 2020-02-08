# Дан ориентированный взвешенный граф. Найдите кратчайшее расстояние
# одной заданной вершины до другой.

# 3 1 2
# 0 -1 2
# 3 0 -1
# -1 4 0
# Answer 6

from collections import defaultdict
from heapq import heappush, heappop


class Graph:
    def __init__(self):
        self._graph = defaultdict(list)

    def add(self, node1, node2, value):
        self._graph[node1].append((node2, value))

    def dijkstra(self, start_node, end_node):
        heap = []
        visited = dict()
        heappush(heap, (0, start_node))
        while heap:
            value, node = heappop(heap)
            if node == end_node:
                return value
            if node in visited:
                continue
            visited[node] = value
            for i, j in self._graph[node]:
                if i not in visited:
                    heappush(heap, (value + j, i))
        return -1


nodes_no, start_node, end_node = map(lambda x: int(x), input().split())
graph = Graph()
for node1 in range(1, nodes_no + 1):
    row = list(map(lambda x: int(x), input().split()))
    for i in range(0, len(row)):
        if (node1 - 1) != i and row[i] != -1:
            graph.add(node1, i + 1, row[i])

print(graph.dijkstra(start_node, end_node))

