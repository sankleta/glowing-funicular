
books_total_no, libraries_no, days_no = map(lambda x: int(x), input().split())
books_scores = list(map(lambda x: int(x), input().split()))

libraries = {}
scores = set()

for i in range(0, libraries_no):
    books_no, signup, ship = map(lambda x: int(x), input().split())
    books = list(map(lambda x: int(x), input().split()))
    if signup >= days_no:
        continue
    books.sort(key=lambda x: books_scores[x], reverse=True)
    libraries[i] = [ship, books, signup]

all_books = set()
for i in range(0, books_total_no):
    all_books.add(i)

order = []

while days_no > 0:
    scores = []
    for i in libraries:
        if i not in order:
            scores.append([sum(libraries[i][1][:(days_no - libraries[i][2]) * libraries[i][0]]), i])

    m = max(scores, key=lambda x: x[0])
    order.append(m[1])
    all_books.difference_update(libraries[m[1]][1])
    days_no -= libraries[m[1]][2]
    # for i in libraries:
    #     if i not in order:
    #         libraries[i][1] = list(all_books.intersection(libraries[i][1]))

with open('answers.txt', 'w') as f:
    f.write("{}\n".format(len(order)))
    for i in order:
        f.write("{} {}\n".format(i, len(libraries[i][1])))
        f.write("{}\n".format(
            " ".join([str(elem) for elem in sorted(libraries[i][1], key=lambda x: books_scores[x], reverse=True)])))
