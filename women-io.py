tests_number = int(input())
for i in range(1, tests_number + 1):
    R, C, K = map(lambda x: int(x), input().split())
    if K == R * C - 1:
        print("Case #{}: IMPOSSIBLE".format(i))
    else:
        print("Case #{}: POSSIBLE".format(i))
        k = 0
        row = []
        for r in range(1, R + 1):
            for c in range(1, C + 1):
                if k < K:
                    row.append('W')
                    k = k + 1
                else:
                    if c < C:
                        row.append('E')
                    else:
                        if r < R:
                            row.append('S')
                        else:
                            row.append('W')

            print(''.join(row))
            row = []
