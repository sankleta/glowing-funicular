tests_number = int(input())
socks = map(lambda x: int(x), input().split())

pairs_count = 0
lonely_socks = set()

for sock in socks:
    try:
        lonely_socks.remove(sock)
        pairs_count += 1
    except KeyError:
        lonely_socks.add(sock)

print(pairs_count)


