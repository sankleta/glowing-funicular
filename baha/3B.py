n = int(input())
m = input()
steps = []
for i in m:
    if i == "w":
        steps.append(-2000)
    elif i == ".":
        steps.append(0)
    else:
        steps.append(1)

for i in range(0, n):
    if i - 1 >= 0:
        if i - 3 >= 0:
            if i - 5 >= 0:
                steps[i] = steps[i] + max(steps[i - 1], steps[i - 3], steps[i - 5])
            else:
                steps[i] = steps[i] + max(steps[i - 1], steps[i - 3])
        else:
            steps[i] = steps[i] + steps[i - 1]

if steps[n - 1] < 0:
    print("-1")
else:
    print(steps[n - 1])
