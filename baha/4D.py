n = int(input())
stars = list(map(lambda x: int(x), input().split()))
energy = 0
energy_calculations = []

for i in range(1, n - 1):
    energy_calculations.append(stars[i - 1] * stars[i + 1])


def update_calculations(x):
    stars.pop(x + 1)
    energy_calculations.pop(x)
    if x == 0:
        energy_calculations[x] = stars[x] * stars[x + 2]
    elif x == len(stars) - 2:
        energy_calculations[x - 1] = stars[x - 1] * stars[x + 1]
    else:
        energy_calculations[x] = stars[x] * stars[x + 2]
        energy_calculations[x - 1] = stars[x - 1] * stars[x + 1]


for i in range(0, n - 2):
    if i == n - 3:
        energy += energy_calculations[0]
    else:
        energy_max = max(energy_calculations)
        indexes = [i for i, x in enumerate(energy_calculations) if x == energy_max]
        energy += energy_max
        if len(indexes) == 1:
            update_calculations(indexes[0])
        else:
            sublist = [stars[i + 1] for i in indexes]
            update_calculations(indexes[sublist.index(min(sublist))])

print(energy)
