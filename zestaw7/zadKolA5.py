def is_magic(T):
    my_sum = 0
    for x in T[0]:
        my_sum += x

    for x in range(len(T)):
        subsum = 0
        for y in T[x]:
            subsum += y
        if my_sum != subsum:
            return False

    for x in range(len(T)):
        subsum = 0
        for y in range(len(T)):
            subsum += T[y][x]
        if my_sum != subsum:
            return False
    return True


def rotate_right(row):
    return [row[-1]] + row[
        :-1
    ]  # tablica, w ktorej n-ty wiersz jest obrocony o 1 w prawo


def rotate_down(T, col):
    n = len(T)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if y != col:
                result[x][y] = T[x][y]
            else:
                if x - 1 >= 0:
                    result[x][y] = T[x - 1][y]
                else:
                    result[x][y] = T[-1][y]
    return result  # tablica, w ktorej n-ta kolumna jest obrocona o 1 w dol


def magic(T, depth=0):
    if depth == 2:
        return is_magic(T)
    for x in range(len(T)):
        T1 = T[:]
        T1[x] = rotate_right(T[x])
        T2 = rotate_down(T, x)
        result = magic(T1, depth + 1) or magic(
            T2, depth + 1
        )  # czy z tej permutacji mozna otrzymac magiczny kwadrat?
        if result:
            return result  # zwracam true tylko jesli udalo sie uzyskac kwadrat magiczny, w przeciwnym razie kontynuuje petle
    return False


tablica1 = [[3, 11, 14, 17], [6, 12, 7, 9], [10, 8, 16, 13], [5, 15, 4, 2]]

print(magic(tablica1))
