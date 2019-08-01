tables = []
input()

try:
    while True:
        tables.extend(list(map(lambda x: int(x), input().split())))
except EOFError:
    print(sum(tables))
