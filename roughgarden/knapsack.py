with open("knapsack.py") as f:
    knapsack_size, items_no = map(lambda x: int(x), next(f).split())
    items = []
    for i in f:
        items.append(list(map(lambda x: int(x), next(f).split())))
