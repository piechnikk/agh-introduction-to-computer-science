# Zadanie 2. ”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
# waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
# naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
# równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool.


def isPrime(n):
    if n < 1:
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


def waga(number):
    tab = []
    for i in range(2, number + 1):
        boolean = False
        while number > 1 and isPrime(i) and number % i == 0:
            boolean = True
            number //= i
        if boolean:
            tab.append(i)
    print(len(tab))


waga(1)
waga(2)
waga(6)
waga(30)
waga(64)
