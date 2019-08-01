with open("QuickSortArray.txt") as f:
    integer_array = list(map(lambda x: int(x), f))


def quick_sort(start_index, stop_index):
    if stop_index - start_index > 0:
        pivot_index = choose_pivot(start_index, stop_index)
        left, right = partition(pivot_index, start_index, stop_index)
        quick_sort(left[0], left[1])
        quick_sort(right[0], right[1])


def choose_pivot(start, stop):
    middle = start + ((stop - start) // 2)

    if integer_array[start] > integer_array[stop]:
        if integer_array[stop] > integer_array[middle]:
            return stop
        else:
            if integer_array[middle] > integer_array[start]:
                return start
            else:
                return middle
    else:
        if integer_array[start] > integer_array[middle]:
            return start
        else:
            if integer_array[middle] > integer_array[stop]:
                return stop
            else:
                return middle


def partition(pivot_index, start, stop):
    looked_at = 0
    split_index = start

    integer_array[len(integer_array) - 1] += stop - start

    if pivot_index != start:
        integer_array[pivot_index], integer_array[start] = integer_array[start], integer_array[pivot_index]
        pivot_index = start

    for i in range(start + 1, stop + 1):
        if integer_array[i] > integer_array[pivot_index]:
            looked_at += 1
        else:
            if looked_at > 0:
                integer_array[i], integer_array[split_index + 1] = integer_array[split_index + 1], integer_array[i]
                split_index += 1
            else:
                split_index += 1

    integer_array[pivot_index], integer_array[split_index] = integer_array[split_index], integer_array[pivot_index]

    left = [start, split_index - 1]
    right = [split_index + 1, stop]
    return left, right


integer_array.append(0)
quick_sort(0, len(integer_array) - 2)

print(integer_array[len(integer_array) - 1])
