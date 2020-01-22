from collections import defaultdict


class Graph:
    def __init__(self, nodes_count):
        self._graph = defaultdict(set)
        self._nodes_count = nodes_count
        self._visited = set()
        self._current_label = nodes_count
        self._order = [0] * (nodes_count + 1)

    def __len__(self):
        return len(self._graph)

    def add(self, node1, node2):
        self._graph[node1].add(node2)

    def topological_sort(self):
        for node in range(1, nodes_no + 1):
            if node not in self._visited:
                self.DFS_DAG(node)
        return self._order[1:]

    def DFS_DAG(self, node):
        self._visited.add(node)
        for adjacent_node in self._graph[node]:
            if adjacent_node not in self._visited:
                self.DFS_DAG(adjacent_node)
        self._order[self._current_label] = node
        self._current_label -= 1


nodes_no, edges_no = map(lambda x: int(x), input().split())

graph = Graph(nodes_no)
for i in range(0, edges_no):
    node1, node2 = map(lambda x: int(x), input().split())
    graph.add(node1, node2)

print(graph.topological_sort())
