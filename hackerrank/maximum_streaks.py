def getMaxStreaks(toss):
    heads = 0
    max_heads = 0
    is_heads_streak = False
    tails = 0
    max_tails = 0
    is_tails_streak = False
    for i in toss:
        if i == "Heads":
            if is_heads_streak:
                heads += 1
            else:
                is_heads_streak = True
                is_tails_streak = False
                heads = 1
                if tails > max_tails:
                    max_tails = tails
        elif i == "Tails":
            if is_tails_streak:
                tails += 1
            else:
                is_heads_streak = False
                is_tails_streak = True
                tails = 1
                if heads > max_heads:
                    max_heads = heads
    if heads > max_heads:
        max_heads = heads
    if tails > max_tails:
        max_tails = tails
    return max_heads, max_tails


if __name__ == '__main__':

    toss_count = int(input().strip())

    toss = []

    for _ in range(toss_count):
        toss_item = input()
        toss.append(toss_item)

    ans = getMaxStreaks(toss)

    print(' '.join(map(str, ans)))
