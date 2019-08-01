numbers = [3, 5, 7, 6, 8, 2, 1, 10, 11]

pseudo_tree = {}


def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)


def add_to_pseudo_tree(x, y):
    if x in pseudo_tree:
        l = pseudo_tree[x]
        l.append(y)
        pseudo_tree[x] = l
    else:
        pseudo_tree[x] = [y]


def get_winners_in_pairs(numbers):
    winners = []
    for x, y in pairwise(numbers):
        if x > y:
            winners.append(x)
            add_to_pseudo_tree(x, y)
        else:
            winners.append(y)
            add_to_pseudo_tree(y, x)
    return winners


def is_odd(numbers):
    if len(numbers) % 2 != 0:
        return True
    else:
        return False


def get_maximum(numbers, odd_number=None):
    if is_odd(numbers):
        odd_number = numbers[len(numbers) - 1]
    if len(numbers) >= 4:
        numbers = get_winners_in_pairs(numbers)
        get_maximum(numbers, odd_number)
    elif len(numbers) == 2:
        maximum = 0
        second_maximum_candidate = 0
        if numbers[0] > numbers[1]:
            maximum = numbers[0]
            second_maximum_candidate = numbers[1]
        else:
            maximum = numbers[1]
            second_maximum_candidate = numbers[0]
        if odd_number:
            if odd_number > maximum:
                #               add_to_pseudo_tree(odd_number, [maximum, second_maximum_candidate])
                second_maximum_candidate = maximum
                maximum = odd_number
                return second_maximum_candidate
            elif maximum > odd_number > second_maximum_candidate:
                second_maximum_candidate = odd_number

        entry = pseudo_tree[maximum]
        for e in entry:
            if second_maximum_candidate < e:
                second_maximum_candidate = e
        return second_maximum_candidate


########################################################################################
def get_second_maximum(numbers):
    if len(numbers) < 2:
        pass

    winners = {}
    new_numbers = []
    while len(numbers) > 1:
        for i in range(0, len(numbers), 2):
            if i == len(numbers) - 1:
                new_numbers.append(numbers[i])
                continue
            max, min = (numbers[i], numbers[i + 1]) if numbers[i] > numbers[i + 1] else (numbers[i + 1], numbers[i])
            new_numbers.append(max)
            winners[max] = winners[max] + [min] if max in winners else [min]
        numbers.clear()
        numbers.extend(new_numbers)
        new_numbers.clear()

    losers = winners[numbers[0]]
    second_maximum = losers[0]
    for i in range(1, len(losers)):
        if second_maximum < losers[i]:
            second_maximum = losers[i]
    return second_maximum


########################################################################################

second_maximum = get_second_maximum(numbers)
print(second_maximum)
second_maximum = get_maximum(numbers)
print(second_maximum)
