# Implement one or more algorithms for the traveling salesman problem.
# The first line indicates the number of cities. Each city is a point in the plane,
# and each subsequent line indicates the x- and y-coordinates of a single city.
# The distance between two cities is defined as the Euclidean distance.

import math

points = {}
graph = {}
with open("tsp.txt") as f:
    size = int(next(f))
    for i in range(1, size+1):
        x, y = list(map(lambda x: float(x), next(f).split()))
        for point in points:
            graph[f"{point}_{i}"] = math.sqrt((x-points[point][0])**2 + (y-points[point][1])**2)
        points[i] = (x, y)

print(graph)

print(points)






