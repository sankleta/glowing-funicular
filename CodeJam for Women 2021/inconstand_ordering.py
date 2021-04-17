import collections


def next_alpha(s, distance=1):
    return chr((ord(s) + distance - 65) % 26 + 65)


def prev_alpha(s, distance=1):
    return chr((ord(s) - distance - 65) % 26 + 65)


test_cases_no = int(input())
for test in range(test_cases_no):
    string = ['A']
    blocks_no = int(input())
    blocks = list(map(int, raw_input().split()))
    for i in range(1, len(blocks) + 1):
        if i % 2:
            for letter in range(blocks[i - 1]):
                string.append(next_alpha(string[-1]))
        else:
            if ord(string[-1]) - ord('A') >= blocks[i - 1]:
                string.append(prev_alpha(string[-1], (ord(string[-1]) - ord('A') - blocks[i - 1]+1)))
                for letter in range(blocks[i - 1] - 1):
                    string.append(prev_alpha(string[-1]))
            else:
                string[-1] = next_alpha(string[-1], blocks[i - 1] - ord(string[-1]) - ord('A'))
                for letter in range(blocks[i - 1]):
                    string.append(prev_alpha(string[-1]))

    print("Case #{}: {}".format(test + 1, ''.join(string)))
