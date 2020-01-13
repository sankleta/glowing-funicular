# Дан неориентированный граф. Проверьте, является ли он деревом. Граф не содержит петель и кратных рёбер.
from collections import defaultdict
from queue import Queue


class Graph:
    def __init__(self, nodes_count, directed=False):
        self._graph = defaultdict(set)
        for i in range(1, nodes_count + 1):
            self._graph[i] = set()
        self._directed = directed
        self._edges_count = 0

    def add(self, node1, node2):
        self._graph[node1].add(node2)
        self._edges_count += 1
        if not self._directed:
            self._graph[node2].add(node1)

    def is_connected(self):
        used = set()
        queue = Queue()
        if self._graph:
            queue.put(1)
        else:
            if len(self._graph) == 1:
                return True
            else:
                return False

        while not queue.empty():
            current_node = queue.get()
            used.add(current_node)
            adjacent_nodes = self._graph[current_node]
            for i in adjacent_nodes:
                if i not in used:
                    queue.put(i)

        if len(used) == len(self._graph):
            return True
        else:
            return False

    def is_tree(self):
        if len(self._graph) - 1 == self._edges_count and self.is_connected():
            return True
        else:
            return False


nodes_no, edges_no = map(lambda x: int(x), input().split())

graph = Graph(nodes_no, edges_no)

for _ in range(0, edges_no):
    n1, n2 = map(lambda x: int(x), input().split())
    graph.add(n1, n2)

if graph.is_tree():
    print('YES')
else:
    print('NO')
