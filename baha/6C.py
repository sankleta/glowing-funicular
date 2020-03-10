# Дан неориентированный взвешенный граф. Найти вес минимального пути между двумя вершинами

from collections import defaultdict
from heapq import heappush, heappop


class Graph:
    def __init__(self):
        self._graph = defaultdict(list)

    def add(self, node1, node2, value):
        self._graph[node1].append((node2, value))
        self._graph[node2].append((node1, value))

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


nodes_no, edges_no = map(lambda x: int(x), input().split())
start_node, end_node = map(lambda x: int(x), input().split())

graph = Graph()
for edges in range(edges_no):
    node1, node2, value = map(lambda x: int(x), input().split())
    graph.add(node1, node2, value)

print(graph.dijkstra(start_node, end_node))
