import random

clauses = []
with open("2sat4.txt") as f:
    size = int(next(f))
    for line in f:
        a, b = map(lambda x: int(x), line.split())
        clauses.append((a, b))

variables = []
for i in range(size):
    variables.append(bool(random.getrandbits(1)))

to_change = set()

for i in range(2 * (size ^ 2)):
    for c in clauses:
        if c[0] < 0:
            a = not variables[abs(c[0]) - 1]
        else:
            a = variables[c[0] - 1]

        if c[1] < 0:
            b = not variables[abs(c[1]) - 1]
        else:
            b = variables[c[1] - 1]

        if a or b:
            pass
        else:
            to_change.add(abs(random.choice(c)))

    if not to_change:
        print("yes")
        break
    else:
        print(len(to_change))
        # if len(to_change) > 10:
        for j in to_change:
            variables[j - 1] = not variables[j - 1]
        # else:
        #     j = random.choice(list(to_change))
        #     variables[j - 1] = not variables[j - 1]
        to_change = set()

# 10000
