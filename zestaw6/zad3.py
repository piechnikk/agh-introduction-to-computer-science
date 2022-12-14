# Zadanie 3. Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi zawierającymi koszt przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i kolumnie
# k. Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy minimalny
# koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt przebywania na
# polu startowym i ostatnim także wliczamy do kosztu przejścia.


import math


def king(T, k, w=0, cost=0):
    if w == len(T) - 1:
        return cost + T[w][k]
    val1 = king(T, k, w + 1, cost + T[w][k])
    val2 = val3 = math.inf
    if k > 0:
        val2 = king(T, k - 1, w + 1, cost + T[w][k])
    if k < len(T) - 1:
        val3 = king(T, k + 1, w + 1, cost + T[w][k])

    return min(val1, val2, val3)


T = [
    [4, 13, 5, 2, 6, 7, 9, 3],
    [1, 4, 6, 8, 2, 1, 3, 5],
    [3, 2, 1, 5, 6, 7, 3, 1],
    [6, 3, 7, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 8, 8, 8, 8, 8, 8, 8],
    [90, 1, 90, 1, 90, 1, 90, 1],
    [23, 1, 2, 1, 1, 1, 1, 1],
]

print(king(T, 3))
