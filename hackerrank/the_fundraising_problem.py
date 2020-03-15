import os


def solve(groups, students, k, generosities, charm):
    guests = 0
    table_rank = []
    for _ in generosities:
        if _[0] > students * k:
            return -1
        table_rank.append(
            [sum(_[1:]), _[0]])
        guests += _[0]

    if guests > groups * students * k:
        return -1
    else:
        return None


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    tc = int(input())
    for tc_itr in range(tc):
        groups, students, tables = map(int, input().rstrip().split())

        charm = []

        for _ in range(groups):
            charm.append(list(map(int, input().rstrip().split())))

        generosities = []

        for _ in range(tables):
            guests = list(map(int, input().rstrip().split()))
            generosities.append(guests)

        k = int(input())

        res = solve(groups, students, k, generosities, charm)
        fptr.write(str(res) + '\n')

    fptr.close()
