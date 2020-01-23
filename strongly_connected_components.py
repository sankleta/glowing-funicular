from collections import defaultdict, deque


class Graph:
    def __init__(self, nodes_count):
        self._graph = defaultdict(set)
        self._nodes_count = nodes_count
        self._visited = set()
        self._queue = deque()

    def add(self, node1, node2):
        self._graph[node1].add(node2)

    def topological_sort(self):
        for node in range(nodes_no, 0):
            if node not in self._visited:
                self.DFS(node)

    def DFS(self, node):
        self._visited.add(node)
        for adjacent_node in self._graph[node]:
            if adjacent_node not in self._visited:
                self.DFS(adjacent_node)
        self._queue.append(node)


nodes_no, edges_no = map(lambda x: int(x), input().split())

graph = Graph(nodes_no)
for i in range(0, edges_no):
    node1, node2 = map(lambda x: int(x), input().split())
    graph.add(node1, node2)

print(graph.topological_sort())