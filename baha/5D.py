# Вам задан неориентированный граф с N вершинами и M ребрами (1 ≤ N ≤ 20000, 1 ≤ M ≤ 200000).
# В графе отсутствуют петли и кратные ребра. Определите компоненты связности заданного графа.
from collections import defaultdict, deque


class Graph:
    def __init__(self, nodes_count):
        self._graph = defaultdict(set)
        self._nodes_count = nodes_count

    def add(self, node1, node2):
        self._graph[node1].add(node2)
        self._graph[node2].add(node1)

    def count_connected_components(self):
        components_count = self._nodes_count - len(self._graph)
        if not self._graph:
            return components_count

        not_visited = set(self._graph)

        stack = deque()

        while not_visited:
            stack.append(not_visited.pop())
            components_count += 1
            while stack:
                current_node = stack.pop()
                not_visited.discard(current_node)
                for adjacent_node in self._graph[current_node]:
                    if adjacent_node in not_visited:
                        stack.append(adjacent_node)

        return components_count


nodes_no, edges_no = map(lambda x: int(x), input().split())

graph = Graph(nodes_no)

for _ in range(0, edges_no):
    n1, n2 = map(lambda x: int(x), input().split())
    graph.add(n1, n2)

print(graph.count_connected_components())
