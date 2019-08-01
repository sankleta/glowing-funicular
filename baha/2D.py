import sys

input = sys.stdin.readlines()

for i in range(len(input)-1,-1,-1):
    line = input[i]
    for j in range(len(line)-1,-1,-1):
        sys.stdout.write(line[j])
sys.stdout.flush()
