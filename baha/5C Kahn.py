# Дан ориентированный невзвешенный граф без кратных рёбер. Необходимо
# определить, есть ли в нём циклы, и если есть, то вывести любой из них.

from collections import defaultdict, deque


class Graph:
    def __init__(self, nodes_count):
        self._graph = defaultdict(set)
        self._nodes_count = nodes_count

    def add(self, node1, node2):
        self._graph[node1].add(node2)

    def has_cycles(self):
        in_degree = [0] * (self._nodes_count + 1)
        for i in self._graph:
            for j in self._graph[i]:
                in_degree[j] += 1

        queue = deque()
        for i in range(1, self._nodes_count + 1):
            if in_degree[i] == 0:
                queue.append(i)

        nodes_count = 0

        while queue:
            node = queue.pop()

            for i in self._graph[node]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)

            nodes_count += 1

        if nodes_count == self._nodes_count:
            return False
        else:
            return True


nodes_no, edges_no = map(lambda x: int(x), input().split())

graph = Graph(nodes_no)

for _ in range(0, edges_no):
    n1, n2 = map(lambda x: int(x), input().split())
    graph.add(n1, n2)

if graph.has_cycles():
    print('YES')
else:
    print('NO')
