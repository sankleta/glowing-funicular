def get_sort_key(item):
    return item[0]


a = [(1, 2), (3, 3), (2, 4)]
b = [(2, 5), (3, 4), (5, 3)]

a.sort(key=get_sort_key)
b.sort(key=get_sort_key)

visited = {}
result = []
for i in range(0, len(a)):
    ai = a[i]
    bi = b[i]

    if ai[0] == bi[0]:
        result.append((ai[0], ai[1], bi[1]))

    aResult = None
    if ai[0] in visited:
        aResult = (ai[0], ai[1], visited[ai[0]])
    else:
        visited[ai[0]] = ai[1]

    bResult = None
    if bi[0] in visited:
        bResult = (bi[0], bi[1], visited[bi[0]])
    else:
        visited[bi[0]] = bi[1]

    if aResult is not None and bResult is not None:
        if aResult[1] + aResult[2] < bResult[1] + bResult[2]:
            result.append(aResult)
            result.append(bResult)
        else:
            result.append(bResult)
            result.append(aResult)
    elif aResult is not None:
        result.append(aResult)
    elif bResult is not None:
        result.append(bResult)

    if len(result) >= 25:
        break

print(result[:25])
