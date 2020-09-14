# For example, the third line of the file "0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1"
# denotes the 24 bits associated with node #2.
# The distance between two nodes u and v in this problem is defined as the Hamming distance---
# the number of differing bits --- between the two nodes' labels. For example, the Hamming distance
# between the 24-bit label of node #2 above and the label
# "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1" is 3 (since they differ in the 3rd, 7th, and 21st bits).
# The question is: what is the largest value of kk such that there is a k-clustering with spacing
# at least 3? That is, how many clusters are needed to ensure that no pair of nodes with all but 2 bits
# in common get split into different clusters?
# NOTE: The graph implicitly defined by the data file is so big that you probably can't write it
# out explicitly, let alone sort the edges by cost. So you will have to be a little creative
# to complete this part of the question. For example, is there some way you can identify
# the smallest distances without explicitly looking at every pair of nodes?

# 0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1
from collections import defaultdict
from itertools import combinations

from union_find import UnionFind



with open("clustering_big.txt", "r") as f:
    size, bitsize = map(lambda x: int(x), next(f).split())
    unionFind = UnionFind(size)
    elements = []
    for line in f:
        number = int("".join(line.split()), 2)
        elements.append(number)

    element_dict = defaultdict(list)
    for i in range(size):
        element_dict[elements[i]].append(i)

    hamming_one = []
    for i in range(bitsize):
        number = ["0"] * bitsize
        number[i] = "1"
        hamming_one.append(int("".join(number), 2))

    hamming_two = []
    r = combinations(hamming_one, 2)
    for i, j in r:
        hamming_two.append(i ^ j)

    for i in element_dict:
        l = element_dict[i]
        if len(l) > 1:
            for j in l:
                unionFind.union(j, l[0])

    for i in hamming_one:
        for j in element_dict:
            if j ^ i in element_dict:
                unionFind.union(element_dict[j ^ i][0], element_dict[j][0])

    for i in hamming_two:
        for j in element_dict:
            if j ^ i in element_dict:
                unionFind.union(element_dict[j ^ i][0], element_dict[j][0])

    print(unionFind.size)
