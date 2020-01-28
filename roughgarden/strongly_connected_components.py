from collections import defaultdict, deque


class Graph:
    def __init__(self, nodes_count):
        self._graph = defaultdict(set)
        self._graph_reverse = defaultdict(set)
        self._nodes_count = nodes_count
        self._visited = set()
        self._stack = deque()

    def add(self, node1, node2):
        self._graph[node1].add(node2)
        self._graph_reverse[node2].add(node1)

    def SCC(self):
        for node in range(self._nodes_count, 0, -1):
            if node not in self._visited:
                self.DFS(node, True)

        self._visited.clear()

        while self._stack:
            node = self._stack.pop()
            if node not in self._visited:
                print(node)
                self.DFS(node, False)

    def DFS(self, node, reverse):
        self._visited.add(node)

        for adjacent_node in self._graph_reverse[node] if reverse else self._graph[node]:
            if adjacent_node not in self._visited:
                self.DFS(adjacent_node, reverse)

        if reverse:
            self._stack.append(node)


nodes_no, edges_no = map(lambda x: int(x), input().split())

graph = Graph(nodes_no)
for i in range(0, edges_no):
    node1, node2 = map(lambda x: int(x), input().split())
    graph.add(node1, node2)

graph.SCC()

