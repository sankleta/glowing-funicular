import math

with open("IntegerArray.txt") as f:
    integer_array = list(map(lambda x: int(x), f))


# integer_array = [1, 3, 5, 2, 4, 6]

def sort_and_count(integer_array):
    n = len(integer_array)
    if n == 1:
        return integer_array, 0
    else:
        a = math.ceil(n / 2)
        left, x = sort_and_count(integer_array[:a])
        right, y = sort_and_count(integer_array[a:])
        merged, z = merge_and_count(left, right, n)
        return merged, x + y + z


def merge_and_count(left, right, n):
    left_index = 0
    left_count = len(left)
    right_index = 0
    right_count = len(right)
    merged = []
    z = 0
    for i in range(0, n):
        if left_index <= left_count - 1 and right_index <= right_count - 1:
            if left[left_index] < right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            elif left[left_index] > right[right_index]:
                merged.append(right[right_index])
                z += left_count - left_index
                right_index += 1
        else:
            if left_index <= left_count - 1:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

    return merged, z


a = sort_and_count(integer_array)
print(a[1])

#2407905288