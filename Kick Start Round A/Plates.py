def pick_plates(stacks, to_use_no):
    pass


test_no = int(input())
for i in range(test_no):
    stacks_no, plates_no, to_use_no = map(lambda x: int(x), input().split())
    stacks = []
    for j in range(stacks_no):
        stacks.append(list(map(lambda x: int(x), input().split())))
    print("Case #{}: {}".format(i + 1, pick_plates(stacks, to_use_no)))
