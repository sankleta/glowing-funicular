import heapq

max_heap = []
min_heap = []

try:
    while True:
        a = input()
        if a == '#':
            if len(max_heap) > len(min_heap):
                print(-heapq.heappop(max_heap))
            else:
                print(heapq.heappop(min_heap))
        else:
            a = int(a)
            heapq.heappush(max_heap, -a)

            if len(max_heap) - len(min_heap) == 2:
                b = heapq.heappop(max_heap)
                heapq.heappush(min_heap, -b)
            if len(min_heap) > 0 and min_heap[0] < - max_heap[0]:
                b = heapq.heappop(max_heap)
                heapq.heappush(min_heap, -b)
            if len(min_heap) - len(max_heap) == 2:
                b = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -b)

except EOFError:
    pass
