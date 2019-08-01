level = [1]
total = [1]
i = 1
while total[i - 1] < 30000:
    level.append(level[i - 1] + i + 1)
    total.append(level[i] + total[i - 1])
    i += 1
total.pop()

answers = [None] * 30001
answers[0] = 0
for i in total:
    answers[i] = 1

def optimal_solution(i):




for i in range(1, 30001):
    if answers[i] is not None:
        answers[i] = optimal_solution(i)
