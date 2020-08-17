with open("jobs.txt", "r") as f:
    a = []
    job_no = int(next(f))
    for line in f:
        w, l = map(lambda x: int(x), line.split())
        a.append([w/l, w, l])
        # a.append([w-l, w, l])

    b = sorted(sorted(a, key=lambda x: x[1], reverse=True), key=lambda x: x[0], reverse=True)
    sum = 0
    completion_time = 0
    for i in b:
        completion_time += i[2]
        sum += completion_time * i[1]

    print(sum)
    print(b)
