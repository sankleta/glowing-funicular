# [value_1] [weight_1]
# OUT: the value of the optimal solution


import sys

sys.setrecursionlimit(10 ** 4)

knapsack_size = 0
number_of_items = 0
items = []
memoize = {}


def fill(n, knapsack_size):
    if n == 0 or knapsack_size == 0:
        return 0
    elif items[n][1] > knapsack_size:
        return fill(n - 1, knapsack_size)
    else:
        if (n, knapsack_size) in memoize:
            return memoize[(n, knapsack_size)]
        else:
            result = max(fill(n - 1, knapsack_size), items[n][0] + fill(n - 1, knapsack_size - items[n][1]))
            memoize[(n, knapsack_size)] = result
            return result


with open("knapsack.txt") as f:
    knapsack_size, number_of_items = map(lambda x: int(x), next(f).split())
    for line in f:
        items.append(list(map(lambda x: int(x), line.split())))

print(fill(len(items) - 1, knapsack_size))

#4243395
#2493893