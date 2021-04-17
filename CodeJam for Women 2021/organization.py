from collections import deque, defaultdict


class Graph:
    def __init__(self, managers):
        self._graph = defaultdict(set)
        self.managers = managers

    def add(self, node1, node2):
        self._graph[node1].add(node2)
        self._graph[node2].add(node1)

    def find_path(self, a, b):
        if b in self._graph[a]:
            return 0
        used = set()
        queue = deque([(a, 0)])

        while queue:
            current_node, depth = queue.popleft()
            if current_node == b:
                return depth
            used.add(current_node)
            adjacent_nodes = self._graph[current_node]
            for i in adjacent_nodes:
                if i not in used:
                    if i == b:
                        return depth + 1
                    if i <= managers:
                        queue.append((i, depth + 1))
        return None


test_cases_no = int(input())
for test in range(test_cases_no):
    z = raw_input()
    managers, nonmanagers, pairs = map(lambda x: int(x), z.split())
    graph = Graph(managers)
    ans = []
    for i in range(managers + nonmanagers):
        line = raw_input()
        for s in range(len(line)):
            if line[s] == 'Y':
                if i != s:
                    graph.add(i + 1, s + 1)

    for p in range(pairs):
        a, b = map(int, raw_input().split())
        out = graph.find_path(a, b)
        if out is None:
            ans.append(-1)
        elif out == 0:
            ans.append(0)
        else:
            k, l = divmod(out + 1, 3)
            ans.append(2 * k + l - 1)

    print("Case #{}: {}".format(test + 1, ' '.join(map(str, ans))))
