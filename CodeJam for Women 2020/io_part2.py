tests_number = int(input())
for j in range(1, tests_number + 1):
    line = input()
    IOs = 0
    I = []
    i = []

    comb = {"IO": [], "Io": [], "iO": [], "io": []}

    for u in range(0, len(line)):
        if line[u] == "I":
            I.append(u)
        elif line[u] == "i":
            i.append(u)
        elif line[u] == "O":
            if len(I):
                I -= 1
                comb["IO"].append((I.pop(), u))
            else:
                i -= 1
        elif line[u] == "o":
            if i > 0:
                i -= 1
            else:
                I -= 1

    print("Case #{}: {}".format(j, IOs))
