# The first line indicates the number of cities.
# Each city is a point in the plane, and each subsequent line indicates the x- and y-coordinates
# of a single city.
# The distance between two cities is defined as the Euclidean distance
# Implement the nearest neighbor heuristic:
# Start the tour at the first city.
# Repeatedly visit the closest city that the tour hasn't visited yet.
# In case of a tie, go to the closest city with the lowest index.
# For example, if both the third and fifth cities have the same distance from the first city
# (and are closer than any other city), then the tour should begin by going from the first city to the third city.
# Once every city has been visited exactly once, return to the first city to complete the tour.
import math

cities = {}
with open("nn.txt") as f:
    cities_no = int(next(f))
    for line in f:
        n, x, y = line.split()
        cities[int(n)] = [float(x), float(y)]

not_visited = cities.copy()
last_visited_coordinates = not_visited.pop(1)
path = 0

while not_visited:
    distances = {}
    for key in not_visited:
        distances[key] = math.sqrt(
            (not_visited[key][0] - last_visited_coordinates[0]) ** 2 + (
                    not_visited[key][1] - last_visited_coordinates[1]) ** 2)
    city = min(distances, key=distances.get)
    path += distances[city]
    last_visited_coordinates = not_visited.pop(city)
    print(len(not_visited))

path += math.sqrt(
    (cities[1][0] - last_visited_coordinates[0]) ** 2 + (
            cities[1][1] - last_visited_coordinates[1]) ** 2)

print(path)
