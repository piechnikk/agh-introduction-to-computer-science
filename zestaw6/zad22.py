# Zadanie 25. Tablica t[N] jest wypełniona liczbami naturalnymi. Skok z pola i-tego można wykonać na pola
# o indeksach i+k, gdzie k jest czynnikiem pierwszym liczby t[i] (mniejszym od niej samej). Napisz funkcję,
# która sprawdza, czy da się przejść z pola 0 do N-1 – jeśli się da, zwraca ilość skoków, jeśli się nie da, zwraca
# -1.


import math


def isPrime(n):
    if n < 1 or n % 2 == 0:
        return False
    elif n == 2:
        return True
    else:
        divider = 3
        n_sqrt = n ** (1 / 2) + 1
        while divider < n_sqrt:
            if n % divider == 0:
                return False
            divider += 2
        return True


def czynniki(number):
    t = []
    i = 2
    while i <= math.isqrt(n) + 1:
        if n % i == 0:
            if i not in t:
                t.append(i)
                n //= i

        else:
            i += 1
    return t


def jump(t, counter=0, index=0):
    if index == len(t) - 1:
        return counter
    if index > len(t) - 1:
        return -1
    x = czynniki(t[index])
    for i in range(len(x)):
        jump(t, index + czynniki[i], counter + 1)
