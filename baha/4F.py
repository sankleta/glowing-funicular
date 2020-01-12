n = int(input())
bugs = list(map(lambda x: int(x), input().split()))

bugs.sort()
temp_no = 1
total_max = 1
for i in range(1, len(bugs)):
    if bugs[i] // bugs[i - 1] < 2:
        temp_no += 1
    else:
        if temp_no > total_max:
            total_max = temp_no
        temp_no = 1

if temp_no > total_max:
    total_max = temp_no

print(total_max)