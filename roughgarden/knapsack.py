with open("knapsack.txt") as f:
    knapsack_size, items_no = map(lambda x: int(x), next(f).split())
    items = []
    for i in f:
        items.append(list(map(lambda x: int(x), next(f).split())))

    a = [[0] * items_no for i in range(knapsack_size)]
    print(a)
    for i in items:
        for j in range(knapsack_size):
            a[j][i] = max(a[j][i - 1], a[j - items[i][0] + items[i][0]])
