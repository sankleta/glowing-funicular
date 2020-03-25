# In this programming problem you'll code up the dynamic programming algorithm for computing a maximum-weight
# independent set of a path graph.
# Your task in this problem is to run the dynamic programming algorithm (and the reconstruction procedure)
# from lecture on this data set. The question is: of the vertices 1, 2, 3, 4, 17, 117, 517, and 997,
# which ones belong to the maximum-weight independent set?
# As an answer enter a 8-bit string, where the ith bit should be 1 if the ith of these 8 vertices is in
# the maximum-weight independent set, and 0 otherwise.


def mwis(weights):
    a = [0] * len(weights)
    a[1] = weights[1]
    for i in range(2, len(weights)):
        a[i] = max(a[i - 1], a[i - 2] + weights[i])
    independent = []
    i = len(weights)-1
    while i >= 1:
        if a[i - 1] >= a[i - 2] + weights[i]:
            independent.append(i)
            i -= 1
        else:
            independent.append(i)
            i -= 2

    return independent


with open("mwis.txt") as f:
    nodes_no = int(next(f))
    weights = [0]
    for i in f:
        weights.append(int(i))
    print(mwis(weights))

# 10100110