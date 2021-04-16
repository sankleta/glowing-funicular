def reversort(numbers):
    count = 0
    for i in range(len(numbers) - 1):
        j = numbers.index(min(numbers[i:]))
        count += j - i + 1
        z = i
        while z != j and j > z:
            numbers[z], numbers[j] = numbers[j], numbers[z]
            z += 1
            j -= 1
    return count


def count_max(n):
    out = 0
    while n > 2:
        out += n
        n -= 1
    return out


cases_no = int(input())
for i in range(cases_no):
    n, cost = map(int, input().split())
    n_min = n - 1
    n_max = count_max(n)
    if n_min > cost or n_max < cost:
        print("Case #{}: IMPOSSIBLE".format(i + 1))
    else:
        numbers = [0] * n
        count = n_min
        is_right = None
        left = 0
        right = n - 1
        for i in range(1, n + 1):
            if (count - 1) + (n - (i - 1)) < cost:
                count = (count - 1) + (n - (i - 1))
                if is_right is None or is_right:
                    numbers[right] = i
                    right -= 1
                    is_right = False
                else:
                    numbers[left] = i
                    left += 1
                    is_right = True
            elif (count - 1) + (n - (i - 1)) > cost:
                if is_right is None or is_right:
                    numbers[left] = i
                    left += 1
                else:
                    numbers[right] = i
                    right -= 1
            else:
                if is_right is None or is_right:
                    for j in range(i, n+1):
                        numbers[right] = j
                        right -= 1
                    break
                else:
                    for j in range(i, n+1):
                        numbers[left] = j
                        left += 1
                    break

        print("Case #{}: {}".format(i + 1, numbers))
