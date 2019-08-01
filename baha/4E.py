n = int(input())
trottoir = [input(), input()]

def find_a_way(trottoir, n):
    for i in range(0, n):
        if trottoir[0][i] == "W" and trottoir[1][i] == "W":
            return "NO"
    return "YES"

print(find_a_way(trottoir, n))
