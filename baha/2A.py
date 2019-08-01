l_length, queries_no = map(lambda x: int(x), input().split())
l = input().split()
l_dict = {}

for i in range(0, l_length):
    l_dict[l[i]] = i + 1

for i in range(0, queries_no):
    query = input()
    if query in l_dict:
        print(l_dict[query])
    else:
        print("0")
