def reversort(numbers):
    count = 0
    for i in range(len(numbers)-1):
        j = numbers.index(min(numbers[i:]))
        count += j - i + 1
        z = i
        while z != j and j > z:
            numbers[z], numbers[j] = numbers[j], numbers[z]
            z += 1
            j -= 1
    return count


cases_no = int(input())
for i in range(cases_no):
    count = int(input())
    n = input()
    numbers = list(map(int, n.rstrip().split()))
    out = reversort(numbers)

    print("Case #{}: {}".format(i + 1, out))
