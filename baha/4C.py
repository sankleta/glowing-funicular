n = int(input())
seq = list(map(lambda x: int(x), input().split()))
subseq = [1] * n

max_length = 0

for i in range(0, n):
    for j in range(0, i):
        if seq[i] > seq[j]:
            subseq[i] = max(subseq[i], subseq[j] + 1)
    max_length = max(subseq[i], max_length)

print(max_length)
