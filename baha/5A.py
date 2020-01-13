# В этой задаче требуется проверить, что неориентированный граф
# является связным, то есть что из любой вершины можно по рёбрам этого
# графа попасть в любую другую.

# Graph representation - dict of sets
from collections import defaultdict
from queue import Queue


class Graph:
    def __init__(self, nodes_no, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self._nodes_no = nodes_no

    def add(self, node1, node2):
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def is_connected(self):
        used = set()
        queue = Queue()
        queue.put(list(self._graph.keys())[0])

        while not queue.empty():
            current_node = queue.get()
            used.add(current_node)
            adjacent_nodes = self._graph[current_node]
            for i in adjacent_nodes:
                if i not in used:
                    queue.put(i)

        if len(used) == self._nodes_no:
            return True
        else:
            return False


nodes_no, edges_no = map(lambda x: int(x), input().split())

graph = Graph(nodes_no)

for _ in range(0, edges_no):
    n1, n2 = map(lambda x: int(x), input().split())
    graph.add(n1, n2)

if graph.is_connected():
    print("YES")
else:
    print("NO")
