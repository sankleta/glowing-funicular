import collections

test_cases_no = int(input())
for test in range(test_cases_no):
    animals_no = int(input())
    animals = list(map(int, input().split()))

    counter = collections.Counter(animals)
    animal_types = list(counter.keys())
    animal_types.sort()
    i = 1
    treats = 0
    for t in animal_types:
        treats += i * counter[t]
        i += 1

    print("Case #{}: {}".format(test + 1, treats))
