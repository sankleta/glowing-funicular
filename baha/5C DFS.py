
# Дан ориентированный невзвешенный граф без кратных рёбер. Необходимо
# определить, есть ли в нём циклы, и если есть, то вывести любой из них.




#####!!!!!!!!!!!!!Doesn't work on large inputs due to stack overflow

from collections import defaultdict


class Graph:
    def __init__(self):
        self._graph = defaultdict(set)

    def add(self, node1, node2):
        self._graph[node1].add(node2)

    def has_cycles(self):
        if len(self._graph) <= 1:
            return False

        visited = set()
        for node in self._graph.keys():
            if node not in visited:
                if self.traverse(node, set(), visited):
                    return True
        return False

    def traverse(self, current_node, cycle, visited):
        if current_node not in self._graph:
            return False
        cycle.add(current_node)
        visited.add(current_node)
        for node in self._graph[current_node]:
            if node in cycle:
                return True
            if node not in visited:
                if self.traverse(node, cycle, visited):
                    return True
        cycle.remove(current_node)
        return False


nodes_no, edges_no = map(lambda x: int(x), input().split())

graph = Graph()

for _ in range(0, edges_no):
    n1, n2 = map(lambda x: int(x), input().split())
    graph.add(n1, n2)

if graph.has_cycles():
    print('YES')
else:
    print('NO')