tests_no = int(input())

for i in range(0, tests_no):
    input()
    new_queue = input().split()
    if len(new_queue) == 1:
        print(new_queue[0])
    else:
        new_queue.reverse()
        print(' '.join(new_queue))