chessboard = []
for i in range(0, 8):
    line = list(map(lambda x: int(x), input().split()))
    chessboard.append(line)

for i in range(7, -1, -1):
    for j in range(0, 8):
        if i + 1 <= 7 and j - 1 >= 0:
            chessboard[i][j] = chessboard[i][j] + min(chessboard[i + 1][j - 1], chessboard[i][j - 1],
                                                      chessboard[i + 1][j])
        elif i + 1 <= 7 and j - 1 < 0:
            chessboard[i][j] = chessboard[i][j] + chessboard[i + 1][j]
        elif i + 1 > 7 and j - 1 >= 0:
            chessboard[i][j] = chessboard[i][j] + chessboard[i][j - 1]

print(chessboard[0][7])
