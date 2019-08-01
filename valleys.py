##https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

steps_number = int(input())
path = input()

level = 0
valleys = 0
descending = False

for step in path:
    if level < 0:
        descending = True
    else:
        descending = False

    if step == "U":
        level += 1
    elif step == "D":
        level -= 1

    if level == 0 and descending:
        valleys += 1

print(valleys)
