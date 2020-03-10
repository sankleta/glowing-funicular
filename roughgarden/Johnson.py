class Graph:
    def __init__(self, nodes_no):
        self._nodes_no = nodes_no
        self._paths = [[float("Inf")] * self._nodes_no for i in range(self._nodes_no)]
        self._has_negative_cycle = False
        self._shortest_length = 0
        for i in range(self._nodes_no):
            self._paths[i][i] = 0

    def add(self, _from, to, value):
        if _from == to and to < 0:
            self._has_negative_cycle = True

        if self._paths[_from - 1][to - 1] > value:
            self._paths[_from - 1][to - 1] = value

        if value < self._shortest_length:
            self._shortest_length = value

    def johnson(self):
        pass


def calculate_shortest_shortest_path(filename):
    with open(filename, 'r') as f:
        nodes_no, edges_no = map(lambda x: int(x), next(f).split())
        graph = Graph(nodes_no)

        for line in f:
            _from, to, value = map(lambda x: int(x), line.split())
            graph.add(_from, to, value)

        return graph.johnson()


results = [calculate_shortest_shortest_path("g1.txt"), calculate_shortest_shortest_path("g2.txt"),
           calculate_shortest_shortest_path("g3.txt")]

print(results)