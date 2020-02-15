tests_number = int(input())
for j in range(1, tests_number + 1):
    marbles = int(input())
    removal = list(map(lambda x: int(x), input().split()))
    l = [0] * marbles
    is_right = True
    d = dict()
    for i in removal:
        if is_right:
            l[i - 1] = "R"
            is_right = False
        else:
            l[i - 1] = "L"
            is_right = True
    # Rs = 0
    # Ls = 0
    # flips = 0
    #
    # for i in range(0, marbles):
    #     if l[i] == "R":
    #         n = abs((Rs + 1) - Ls)
    #         if n < 2:
    #             Rs += 1
    #         else:
    #             l[i]="L"
    #             flips-=1
    #     else:
    #         if l[i] == "L":
    #             n = abs(Rs - (Ls+1))
    #             if n < 2:
    #                 Ls += 1
    #             else:
    #                 l[i] = "R"
    #                 flips +=1

    print("Case #{}: {}".format(j, "".join(l)))
