# Your task is to run Prim's minimum spanning tree algorithm on this graph.
# You should report the overall cost of a minimum spanning tree --- an integer, which may or may not be negative
# IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation
# of Prim's algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge,
# try implementing a heap-based version. The simpler approach, which should already give you a healthy speed-up,
# is to maintain relevant edges in a heap (with keys = edge costs).
# The superior approach stores the unprocessed vertices in the heap.
# Note this requires a heap that supports deletions, and you'll probably need to maintain some
# kind of mapping between vertices and their positions in the heap.
from collections import defaultdict
from heapq import heappush, heappop, heapify


class Graph:
    def __init__(self, nodes_count):
        self._graph = defaultdict(list)
        self._nodes_count = nodes_count
        self.visited = dict()

    def add(self, node1, node2, value):
        self._graph[node1].append((node2, value))
        self._graph[node2].append((node1, value))

    def prim(self, start_node):
        heap = []
        touched = dict()
        heappush(heap, (0, start_node))
        while len(self.visited) < self._nodes_count:
            value, node = heappop(heap)
            if node in self.visited:
                continue
            self.visited[node] = value
            for i, j in self._graph[node]:
                if i not in self.visited:
                    if i not in touched:
                        heappush(heap, (j, i))
                        touched[i] = j
                    else:
                        if touched[i] > j:
                            heap[heap.index((touched[i], i))] = (j, i)
                            touched[i] = j
                            heapify(heap)


with open("prim_edges.txt", "r") as f:
    nodes_no, edges_no = map(lambda x: int(x), next(f).split())
    graph = Graph(nodes_no)
    for line in f:
        _from, to, value = map(lambda x: int(x), line.split())
        graph.add(_from, to, value)

    graph.prim(1)
    cost = 0
    for key in graph.visited:
        cost += graph.visited[key]

    print(cost)
