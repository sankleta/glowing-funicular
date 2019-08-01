n, m = map(lambda x: int(x), input().split())
board = []

for i in range(0, n):
    board.append([0] * m)

board[0][0] = 1

for i in range(0,n):
    for j in range(0,m):
        if i - 1 >= 0 and j - 2 >= 0:
            board[i][j] += board[i - 1][j - 2]
        if i - 2 >= 0 and j - 1 >= 0:
            board[i][j] += board[i - 2][j - 1]


print(board[n-1][m-1])
