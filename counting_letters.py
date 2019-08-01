from math import floor

snippet = input()
string_length = int(input())


def count_as(snippet):
    a_in_snippet = 0

    for letter in snippet:
        if letter == "a":
            a_in_snippet += 1

    return a_in_snippet


a_in_snippet = count_as(snippet)

snippet_len = len(snippet)

answer = floor(string_length / snippet_len) * a_in_snippet + count_as(snippet[:(string_length % snippet_len)])
print(answer)
