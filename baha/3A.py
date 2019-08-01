n = int(input())
steps = list(map(lambda x: int(x), input().split()))

for i in range(0, n):
    if i > 1:
        if steps[i - 2] >= steps[i - 1]:
            steps[i] = steps[i] + steps[i - 2]
        else:
            steps[i] = steps[i] + steps[i - 1]
    elif i == 1:
        if steps[i] + steps[i - 1] >= steps[i]:
            steps[i] = steps[i] + steps[i - 1]

print(steps[n - 1])
