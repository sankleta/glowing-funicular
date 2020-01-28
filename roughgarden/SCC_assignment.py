# Vertices are labeled as positive integers from 1 to 875714
# Return the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes.

from collections import defaultdict, deque
import sys

x = 875714
sys.setrecursionlimit(x)


class Graph:
    def __init__(self, nodes_count):
        self._graph = defaultdict(set)
        self._graph_reverse = defaultdict(set)
        self._nodes_count = nodes_count
        self._visited = set()
        self._stack = deque()
        self._top = []

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
                size = len(self._visited)
                self.DFS(node, False)
                self._top.append(len(self._visited) - size)

        return self._top

    def DFS(self, node, reverse):
        self._visited.add(node)

        for adjacent_node in self._graph_reverse[node] if reverse else self._graph[node]:
            if adjacent_node not in self._visited:
                self.DFS(adjacent_node, reverse)

        if reverse:
            self._stack.append(node)


nodes_no = 875714

graph = Graph(nodes_no)

try:
    while True:
        node1, node2 = map(lambda x: int(x), input().split())
        graph.add(node1, node2)
except EOFError:
    pass

top = graph.SCC()

