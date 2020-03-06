# The first line indicates the number of vertices and edges, respectively.
# Each subsequent line describes an edge (the first two numbers are its tail and head,
# respectively) and its length (the third number).
# NOTE: some of the edge lengths are negative.
# NOTE: These graphs may or may not have negative-cost cycles.
# Your task is to compute the "shortest shortest path".
# Precisely, you must first identify which, if any, of the three graphs have no
# negative cycles. For each such graph, you should compute all-pairs shortest paths
# and remember the smallest one.
# If each of the three graphs has a negative-cost cycle, then enter "NULL" in the box
# below. If one or more of the graphs have no negative-cost cycles, then enter
# the smallest of the lengths of their shortest shortest paths.
