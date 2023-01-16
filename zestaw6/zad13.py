# Zadanie 13. Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej na sumę składników. Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2.


def fun(n: int, last: int = 1, tab: list = []):
    print(n, tab)
    if n == 0:
        print(tab)
    else:
        for i in range(last, n + 1):
            fun(n - i, i, tab + [i])


print(fun(4))
