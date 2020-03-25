def allocate(budget, houses):
    houses.sort()
    spent = 0
    bought = 0
    for house in houses:
        spent += house
        if spent > budget:
            return bought
        else:
            bought += 1
    return bought


test_no = int(input())
for i in range(test_no):
    houses_no, budget = map(lambda x: int(x), input().split())
    houses = list(map(lambda x: int(x), input().split()))
    print("Case #{}: {}".format(i+1, allocate(budget, houses)))
