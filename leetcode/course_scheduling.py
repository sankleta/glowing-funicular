# L - Empty list that will contain the sorted elements
# S - Set of all nodes with no incoming edge
#
# while S is not empty do
#     remove a node n from S
#     add n to L
#     for each node m with an edge e from n to m do
#         remove edge e from the graph
#         if m has no other incoming edges then
#             insert m into S
#
# if graph has edges then
#     return error   (graph has at least one cycle)
# else
#     return L   (a topologically sorted order)
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses, prerequisites):
        ans = []
        graph = defaultdict(set)
        reversed_graph = defaultdict(set)
        s = []

        for i, j in prerequisites:
            graph[i].add(j)
            reversed_graph[j].add(i)

        for i in range(numCourses):
            if i not in graph:
                s.append(i)

        while s:
            a = s.pop()
            ans.append(a)
            for i in reversed_graph[a]:
                graph[i].discard(a)
                if len(graph[i]) == 0:
                    s.append(i)
                    del graph[i]
            if a in reversed_graph:
                del reversed_graph[a]

        if graph:
            return []
        return ans


a = Solution()
print(a.findOrder(1, []))
