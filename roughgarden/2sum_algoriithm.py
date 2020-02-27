import concurrent.futures
import time

integers = set()
integers_l = []
with open("algo1-programming_prob-2sum.txt", 'r') as f:
    for line in f:
        integers.add(int(line))

integers_l = list(integers)


def find_match(t):
    for i in integers_l:
        if i != (t - i) and (t - i) in integers:
            return 1
    return 0


start = time.time()
t_count = 0
with concurrent.futures.ProcessPoolExecutor() as executor:
    for res in executor.map(find_match, range(-10000, 10000)):
        t_count += res

end = time.time()
print(end - start)
print(t_count)