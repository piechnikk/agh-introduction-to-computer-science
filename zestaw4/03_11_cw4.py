# Zadanie 1. Dana jest tablica T[N][N]. Proszę napisać funkcję wypełniającą tablicę kolejnymi liczbami naturalnymi po spirali.
import math


def spirala(n, tab, count):
    x, y = 0, 0
    max = n**2
    while count <= max:
        while x < n - 1 and tab[y][x + 1] == 0:
            tab[y][x] = count
            x += 1
            count += 1
        while y < n - 1 and tab[y + 1][x] == 0:
            tab[y][x] = count
            y += 1
            count += 1
        while x > 0 and tab[y][x - 1] == 0:
            tab[y][x] = count
            y -= 1
            count += 1
        while tab[y - 1][x] == 0:
            tab[y][x] = count
            y -= 1
            count += 1
    return tab


# n = 5
# print(spirala(n, [[0] * n for _ in range(n)], 1))


# Zadanie 6. Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], gdzie
# M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane rosnąco (w obrębie wiersza) liczby
# naturalne. Proszę napisać funkcję przepisującą wszystkie singletony (liczby występujące dokładnie raz) z
# tablicy T1 do T2, tak aby liczby w tablicy T2 były uporządkowane rosnąco. Pozostałe elementy tablicy T2
# powinny zawierać zera.


def singletons(tab1):
    n = len(tab1)
    tab2 = [0] * (n**2)
    tab3 = []
    counter = 0
    for i in range(n):
        tab3 += tab1[i]
    tab3.sort()
    if tab3[0] != tab3[1]:
        tab2[counter] = tab3[0]
        counter += 1
    for i in range(1, len(tab3) - 1):
        if tab3[i] != tab3[i + 1] and tab3[i] != tab3[i - 1]:
            tab2[counter] = tab3[i]
            counter += 1
    if tab3[len(tab3) - 1] != tab3[len(tab3) - 2]:
        tab2[counter] = tab3[len(tab3) - 1]
        counter += 1
    print(tab2)


# singletons([[2, 3, 4], [1, 2, 3], [7, 8, 9]])


def singletonsNoSort(tab1):
    n = len(tab1)
    tab2 = [0] * (n**2)
    while True:
        k = 0
        wsk = [0] * n
        min = math.inf
        min_i = -1
        for i in range(1, n):
            if wsk[i] < n and tab1[i][wsk[i]] < min:
                min_i = i
                min = tab1[i][wsk[i]]
        tab2[k] = min
        wsk[k] += 1
        k += 1
        if min_i == -1:
            break


singletonsNoSort([[2, 3, 4], [1, 2, 3], [7, 8, 9]])
