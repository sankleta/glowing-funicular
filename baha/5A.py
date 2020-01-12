# В этой задаче требуется проверить, что неориентированный граф
# является связным, то есть что из любой вершины можно по рёбрам этого
# графа попасть в любую другую.

# Graph representation - dict of sets
from collections import defaultdict
from queue import Queue


class Graph:
    def __init__(self, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed

    def add(self, node1, node2):
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def is_connected(self):
        nodes = list(self._graph.keys())
        used = set()
        queue = Queue()
        queue.put(nodes[0])

        while not queue.empty():
            current_node = queue.get()
            if current_node not in used:
                used.add(current_node)
                adjacent_nodes = self._graph[current_node]
                for i in adjacent_nodes:
                    queue.put(i)

        if len(used) == len(nodes):
            return True
        else:
            return False


graph = Graph()

nodes_no, edges_no = map(lambda x: int(x), input().split())

for _ in range(0, edges_no):
    n1, n2 = map(lambda x: int(x), input().split())
    graph.add(n1, n2)

if graph.is_connected():
    print("YES")
else:
    print("NO")
