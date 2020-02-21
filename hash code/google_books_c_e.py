import os


def diff(first, second):
    return [item for item in first if item not in second]


def solve(filename):
    with open(filename, 'r') as f:
        books_total_no, libraries_no, days_no = map(lambda x: int(x), next(f).split())
        books_scores = list(map(lambda x: int(x), next(f).split()))

        libraries = {}

        for i in range(0, libraries_no):
            books_no, signup, ship = map(lambda x: int(x), next(f).split())
            books = list(map(lambda x: int(x), next(f).split()))
            if signup >= days_no:
                continue
            books.sort(key=lambda x: books_scores[x], reverse=True)
            libraries[i] = [ship, books, signup]

    libraries_order = []
    libraries_signed = set()
    books_sent = set()

    days_left = days_no

    while days_left > 0:
        scores = []
        if len(libraries_order) == len(libraries):
            break
        for i in libraries:
            if i not in libraries_signed:
                scores.append([((days_left - libraries[i][2]) * libraries[i][0]), i])

        m = max(scores, key=lambda x: x[0])
        libraries_order.append(m[1])
        libraries_signed.add(m[1])

        books_sent.update(libraries[m[1]][1][:(days_left - libraries[m[1]][2]) * libraries[m[1]][0]])
        to_delete = []
        for i in libraries:
            if i not in libraries_signed:
                if libraries[i][1]:
                    libraries[i][1] = diff(libraries[i][1], books_sent)
                if not libraries[i][1]:
                    to_delete.append(i)

        for i in to_delete:
            del libraries[i]

        days_left -= libraries[m[1]][2]

    with open('answers/{}-answers.txt'.format(os.path.basename(filename)), 'w') as f:
        f.write("{}\n".format(len(libraries_order)))
        for i in libraries_order:
            f.write("{} {}\n".format(i, len(libraries[i][1])))
            f.write("{}\n".format(
                " ".join([str(elem) for elem in sorted(libraries[i][1], key=lambda x: books_scores[x], reverse=True)])))


# solve("a_example.txt")
solve("b_read_on.txt")
solve("c_incunabula.txt")
solve("e_so_many_books.txt")
solve("f_libraries_of_the_world.txt")
# #solve("d_tough_choices.txt")

# B
# books 100000 libraries 100 days 1000
# all books have the same score
