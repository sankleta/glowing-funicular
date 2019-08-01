s, n = map(lambda x: int(x), input().split())
gold_bars = [0]
gold_bars.extend(map(lambda x: int(x), input().split()))

intermediate_results = {}


def knapsack(n, s):
    if "{}_{}".format(n, s) in intermediate_results:
        return intermediate_results["{}_{}".format(n, s)]
    if n == 0 or s == 0:
        result = 0
    elif gold_bars[n] > s:
        result = knapsack(n - 1, s)
    else:
        option_1 = knapsack(n - 1, s)
        option_2 = gold_bars[n] + knapsack(n - 1, s - gold_bars[n])
        result = max(option_1, option_2)
    intermediate_results["{}_{}".format(n, s)] = result
    return result


print(knapsack(n, s))
