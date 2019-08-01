n = int(input())
memoise = [[1, 1, 1]]
if n == 0:
    print('1')
else:
    for i in range(1, n):
        a = memoise[i - 1][0] + memoise[i - 1][1] + memoise[i - 1][2]
        b = memoise[i - 1][1] + memoise[i - 1][2]
        memoise.append([a, b, a])

    print(memoise[n - 1][0] + memoise[n - 1][1] + memoise[n - 1][2])