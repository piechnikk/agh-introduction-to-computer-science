import copy

counter = 0


def queen8(lvl, board):
    global counter
    if lvl == 8:
        print(board)
        counter += 1
        return
    for i in range(8):
        if board[lvl][i] == 0:
            bc = copy.deepcopy(board)
            bc[lvl][i] = 2
            k, l = i - 1, lvl + 1
            while k >= 0 and l < 8:
                bc[l][k] = 1
                k -= 1
                l += 1
            l = lvl
            while l < 8:
                bc[l][i] = 1
                l += 1
            k = i + 1
            l = lvl + 1
            while k < 8 and l < 8:
                bc[l][k] = 1
                k += 1
                l += 1
            queen8(lvl + 1, bc)


tab = [[0 for _ in range(8)] for _ in range(8)]
queen8(0, tab)
print(counter)
