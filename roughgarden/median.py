# The goal of this problem is to implement the "Median Maintenance" algorithm.
# The text file contains a list of the integers from 1 to 10000 in unsorted order;
# you should treat this as a stream of numbers, arriving one by one.
# Output: the sum of 10000 medians, modulo 10000 (i.e., only the last 4 digits)
# OPTIONAL: Compare the performance achieved by heap-based and search-tree-based implementations of the algorithm.

import heapq

max_heap = []
min_heap = []

median_sum = 0

with open("Median.txt", "r") as f:
    for line in f:
        a = int(line)
        if min_heap and a > min_heap[0]:
            heapq.heappush(min_heap, a)
        else:
            heapq.heappush(max_heap, -a)

        if len(max_heap) - len(min_heap) == 2:
            b = heapq.heappop(max_heap)
            heapq.heappush(min_heap, -b)
        elif len(max_heap) - len(min_heap) == -1:
            b = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -b)

        median_sum -= max_heap[0]

print(median_sum)

#1213