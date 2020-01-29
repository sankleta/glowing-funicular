# Vertices are labeled as positive integers from 1 to 875714
# Return the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes.

from collections import defaultdict, deque


class Graph:
    def __init__(self, nodes_count):
        self._graph = defaultdict(set)
        self._graph_reverse = defaultdict(set)
        self._nodes_count = nodes_count
        self._visited = set()
        self._second_traverse_stack = deque()
        self._dfs_stack = deque()
        self._component_sizes = []

    def add(self, node1, node2):
        self._graph[node1].add(node2)
        self._graph_reverse[node2].add(node1)

    def SCC(self):
        for node in range(self._nodes_count, 0, -1):
            if node not in self._visited:
                sequence_stack = self.DFS(node, True)
                sequence_stack.reverse()
                self._second_traverse_stack.extend(sequence_stack)

        self._visited.clear()

        while self._second_traverse_stack:
            node = self._second_traverse_stack.pop()
            if node not in self._visited:
                visited_before = len(self._visited)
                self.DFS(node, False)
                self._component_sizes.append(len(self._visited) - visited_before)

        return self._component_sizes

    def DFS(self, node, reverse):

        sequence_stack = deque()
        self._dfs_stack.append(node)

        while self._dfs_stack:
            node = self._dfs_stack.pop()
            if reverse:
                sequence_stack.appendleft(node)
            self._visited.add(node)
            for adjacent_node in self._graph_reverse[node] if reverse else self._graph[node]:
                if adjacent_node not in self._visited:
                    self._dfs_stack.append(adjacent_node)
        return sequence_stack


nodes_no = 875714

graph = Graph(nodes_no)

try:
    while True:
        node1, node2 = map(lambda x: int(x), input().split())
        graph.add(node1, node2)
except EOFError:
    pass

component_sizes = graph.SCC()

print(sorted(component_sizes, reverse=True)[:5])
