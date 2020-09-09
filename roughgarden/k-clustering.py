# In this programming problem and the next you'll code up the clustering algorithm
# from lecture for computing a max-spacing k-clustering.
# This file describes a distance function (equivalently, a complete graph with edge costs).
# It has the following format:
# [number_of_nodes]
# [edge 1 node 1] [edge 1 node 2] [edge 1 cost]
# [edge 2 node 1] [edge 2 node 2] [edge 2 cost]
# There is one edge (i,j)(i,j) for each choice of 1≤i<j≤n, where n is the number of nodes.
# For example, the third line of the file is "1 3 5250", indicating that the distance between
# nodes 1 and 3 (equivalently, the cost of the edge (1,3)) is 5250. You can assume that distances
# are positive, but you should NOT assume that they are distinct.
# Your task in this problem is to run the clustering algorithm from lecture on this data set,
# where the target number k of clusters is set to 4. What is the maximum spacing of a 4-clustering?
from union_find import UnionFind

with open("clustering1.txt", "r") as f:
    size = int(next(f))
    unionFind = UnionFind(size)
    elements = []
    for line in f:
        first, second, distance = map(lambda x: int(x), line.split())
        elements.append([first, second, distance])

    elements.sort(key=lambda x: x[2])
    max_spacing = 0
    for e in elements:
        if unionFind.size >= 4:
            max_spacing = e[2]
            unionFind.union(e[0], e[1])
        else:
            break

    print(max_spacing)
