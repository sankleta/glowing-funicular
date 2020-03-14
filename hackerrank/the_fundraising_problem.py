def impossible(groups, students, k, generosities):
    guests = 0
    for _ in generosities:
        if _[0] > students * k:
            return True
        guests += _[0]

    if guests > groups * students * k:
        return True


def solve(groups, students, k, generosities, charm):
    pass


if __name__ == '__main__':
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

        if impossible(groups, students, k, generosities):
            print(-1)
        else:
            res = solve(groups, students, k, generosities, charm)
            print(res)
