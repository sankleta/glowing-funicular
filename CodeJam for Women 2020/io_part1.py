tests_number = int(input())
for j in range(1, tests_number+1):
    line = input()
    IOs = 0
    I = 0
    i = 0
    for _ in line:
        if _ == "I":
            I += 1
        elif _ == "i":
            i += 1
        elif _ == "O":
            if I > 0:
                IOs += 1
                I -= 1
            else:
                i -= 1
        elif _ == "o":
            if i > 0:
                i -= 1
            else:
                I -= 1

    print("Case #{}: {}".format(j, IOs))
