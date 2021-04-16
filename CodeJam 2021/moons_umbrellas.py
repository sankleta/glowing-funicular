cases_no = int(input())
for c in range(cases_no):
    min_cost = 0
    cj_cost, jc_cost, mural = input().split()
    cj_cost = int(cj_cost)
    jc_cost = int(jc_cost)
    before = None
    for i in mural:
        if i == "J":
            if before:
                if "J" != before:
                    min_cost += cj_cost
                    before = i
            else:
                before = i
        elif i == "C":
            if before:
                if "J" != before:
                    min_cost += jc_cost
                    before = i
            else:
                before = i

    print("Case #{}: {}".format(c + 1, min_cost))


