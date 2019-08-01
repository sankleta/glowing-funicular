n = int(input())
mountain = []

for i in range(0, n):
    mountain.append(list(map(lambda x: int(x), input().split())))

for i in range(0, n):
    for j in range(0, i + 1):
        if i - 1 >= 0:
            if j == 0:
                mountain[i][j] = mountain[i][j] + mountain[i - 1][j]
            elif j <= i - 1:
                mountain[i][j] = mountain[i][j] + max(mountain[i - 1][j - 1], mountain[i - 1][j])
            elif j > i - 1:
                mountain[i][j] = mountain[i][j] + mountain[i - 1][j - 1]

print(max(mountain[n - 1]))
