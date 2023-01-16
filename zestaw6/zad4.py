# problem skoczka szachowego


def czy_mozliwe(x, y):
    return x <= 7 and x >= 0 and y <= 7 and y > 0


t = [[[0] for _ in range(8)] for _ in range(8)]


def rek(t, licz=0, x=0, y=0):
    t[y][x] = licz
    if licz == 64:
        return t
    ruchy = [(2, 1), (2, -1), (1, -2), (-1, -2), (1, -2), (-1, 2), (-2, 1), (-2, -1)]
    for i in range(len(ruchy)):
        if (
            czy_mozliwe(x + ruchy[i[0]], y + ruchy[i[1]])
            and t[y + ruchy[i[1]]][x + ruchy[i[0]]] == 0
        ):
            rek(t, licz + 1, x + ruchy[i[0]], y + ruchy[i[1]])
        if i > 0:
            t[x + ruchy[i][0]][y + ruchy[i][1]] = 0
