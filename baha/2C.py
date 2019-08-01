t = input()
p = input()


def rabin_karp(text, pattern):
    pattern_hash = hash(pattern)
    for i in range(0, len(text) - len(pattern) + 1):
        if hash(text[i:i + len(pattern)]) == pattern_hash:
            if text[i:i + len(pattern)] == pattern:
                return "go"
    return "no"


if len(p) > len(t):
    print("no")
else:
    print(rabin_karp(t, p))