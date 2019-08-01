clouds_number = int(input())
clouds = list(map(lambda x: int(x), input().split()))

end = clouds_number - 1
jumps = 0
n = 0
while n < end:
    try:
        if clouds[n + 2] == 0:
            n += 2
            jumps += 1
        else:
            n += 1
            jumps += 1
    except IndexError:
        n += 1
        jumps += 1

print(jumps)
