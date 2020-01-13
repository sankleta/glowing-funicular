# Дан неориентированный граф. Проверьте, является ли он деревом. Граф не содержит петель и кратных рёбер.
from collections import defaultdict
from queue import Queue


class Graph:
    def __init__(self, nodes_count, edges_count, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self._nodes_count = nodes_count
        self._edges_count = edges_count

    def add(self, node1, node2):
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def is_connected(self):
        used = set()
        queue = Queue()
        if self._graph:
            queue.put_nowait(list(self._graph.keys())[0])
        else:
            if self._nodes_count == 1:
                return True
            else:
                return False

        while not queue.empty():
            current_node = queue.get_nowait()
            used.add(current_node)
            adjacent_nodes = self._graph[current_node]
            for i in adjacent_nodes:
                if i not in used:
                    queue.put_nowait(i)

        if len(used) == self._nodes_count:
            return True
        else:
            return False

    def is_tree(self):
        if self._nodes_count - 1 == self._edges_count and self.is_connected():
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
