# Дан ориентированный невзвешенный граф без кратных рёбер. Необходимо
# определить, есть ли в нём циклы, и если есть, то вывести любой из них.

from collections import defaultdict
from queue import LifoQueue


class Graph:
    def __init__(self, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self._edges_count = 0

    def add(self, node1, node2):
        self._graph[node1].add(node2)
        self._edges_count += 1
        if not self._directed:
            self._graph[node2].add(node1)

    def has_cycles(self):
        if len(self._graph) == 1:
            return False

        not_visited_nodes = set(self._graph.keys())
        queue = LifoQueue()
        used = []

        while not_visited_nodes:
            queue.put(not_visited_nodes.pop())
            while not queue.empty():
                current_node = queue.get()
                used.append(current_node)
                not_visited_nodes.discard(current_node)
                adjacent_nodes = self._graph[current_node]
                for i in adjacent_nodes:
                    if i in used:
                        return True
                    elif i in not_visited_nodes:
                        queue.put(i)
        return False


nodes_no, edges_no = map(lambda x: int(x), input().split())

graph = Graph(True)

for _ in range(0, edges_no):
    n1, n2 = map(lambda x: int(x), input().split())
    graph.add(n1, n2)

if graph.has_cycles():
    print('YES')
else:
    print('NO')
