test_cases_no = int(input())


def compare(begin, end, board, player):
    temp_begin = begin + 1
    temp_end = end - 1
    prev_left = prev_right = player
    while temp_begin < temp_end:
        if board[temp_begin] == prev_left:
            if prev_left == player:
                return True
            else:
                return False
        elif board[temp_end] == prev_right:
            if prev_right == player:
                return False
            else:
                return True

        else:
            prev_left = board[temp_begin]
            prev_right = board[temp_end]
            temp_begin += 1
            temp_end -= 1
    return None


for test in range(test_cases_no):
    board = raw_input().strip()
    begin = 0
    end = len(board) - 1
    i = 1
    while begin <= end:
        if i % 2:
            if board[begin] == 'I' and board[end] != 'I':
                begin += 1
            elif board[begin] != 'I' and board[end] == 'I':
                end -= 1
            elif board[begin] != 'I' and board[end] != 'I':
                print("Case #{}: {} {}".format(test + 1, 'O', end - begin + 2))
                break
            else:
                if begin == end:
                    print("Case #{}: {} {}".format(test + 1, 'I', 1))
                    break

                res = compare(begin, end, board, 'I')
                if res is None:
                    begin += 1
                elif res:
                    begin += 1
                else:
                    end -= 1
        else:
            if board[begin] == 'O' and board[end] != 'O':
                begin += 1
            elif board[begin] != 'O' and board[end] == 'O':
                end -= 1
            elif board[begin] != 'O' and board[end] != 'O':
                print("Case #{}: {} {}".format(test + 1, 'I', end - begin + 2))
                break
            else:
                if begin == end:
                    print("Case #{}: {} {}".format(test + 1, 'O', 1))
                    break
                res = compare(begin, end, board, 'O')
                if res is None:
                    begin += 1
                elif res:
                    begin += 1
                else:
                    end -= 1
        i += 1
