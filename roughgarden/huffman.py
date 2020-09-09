from heapq import heapify, heappop, heappush

alphabet = []
with open("huffman.txt") as f:
    next(f)
    for line in f:
        alphabet.append((int(line), 0, 0))

heapify(alphabet)
while len(alphabet) > 1:
    a = heappop(alphabet)
    b = heappop(alphabet)

    heappush(alphabet, (a[0] + b[0], max(a[1], b[1]) + 1, min(a[2], b[2]) + 1))

print(alphabet)
