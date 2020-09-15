# The file contains the adjacency list representation of a simple undirected graph.
# There are 200 vertices labeled 1 to 200. The first column in the file represents the vertex label,
# and the particular row (other entries except the first column) tells all the vertices
# that the vertex is adjacent to. So for example, the 6 row looks like : "6 155 56 52 120 ......".
# This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with)
# the vertices with labels 155,56,52,120,......,etc
# Your task is to code up and run the randomized contraction algorithm for the min cut problem
# and use it on the above graph to compute the min cut. (HINT: Note that you'll have to figure
# out an implementation of edge contractions. Initially, you might want to do this naively,
# creating a new graph from the old every time there's an edge contraction.
# But you should also think about more efficient implementations.)
# (WARNING: please make sure to run the algorithm many times with
# different random seeds, and remember the smallest cut that you ever find.) Write your numeric
# answer in the space provided. So e.g., if your answer is 5, just type 5 in the space provided.
import random


def min_cut(edges):
    removed = []
    while len(removed) < 198:
        edges_copy = []
        edge = random.choice(edges)
        removed.append(edge[1])
        for i in edges:
            if i[0] == edge[1]:
                if i[1] != edge[0]:
                    edges_copy.append((edge[0], i[1]))
            elif i[1] == edge[1]:
                if i[0] != edge[0]:
                    edges_copy.append((i[0], edge[0]))
            else:
                edges_copy.append(i)
        edges = edges_copy

    return len(edges)


edges = []
removed = []

with open("karger-min-cut.txt") as f:
    for line in f:
        values = list(map(lambda x: int(x), line.split()))
        for i in values[1:]:
            edges.append((values[0], i))

min_cuts = []
for i in range(100):
    min_cuts.append(min_cut(edges.copy()))
    print(i)
    print(min(min_cuts) / 2)
