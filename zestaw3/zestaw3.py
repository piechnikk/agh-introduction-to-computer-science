import math

# Zadanie 1. Napisać funkcję zamieniającą i wypisującą liczbę naturalną na system o podstawie 2-16.
def changeBase(number, base):
    characters = "0123456789ABCDEF"
    newNumber = ""
    while number > 0:
        newNumber += str(characters[number % base])
        number //= base
    return newNumber[::-1]


print(changeBase(1564378567348657386578365783, 16))


# Zadanie 2. Napisać funkcje sprawdzającą czy dwie liczby naturalne są one zbudowane z takich samych cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001.
def isDigitsTheSame(number1, number2):
    tab1 = [0 for i in range(10)]
    tab2 = [0 for i in range(10)]
    for i in str(number1):
        tab1[int(i)] += 1
    for i in str(number2):
        tab2[int(i)] += 1
    return tab1 == tab2


# print(isDigitsTheSame(101, 101))


# Zadanie 3. Napisać program generujący i wypisujący liczby pierwsze mniejsze od N metodą Sita Eratostenesa.
def eratostenesSieve(number):
    tab = [1 for i in range(number + 1)]
    sqrtNumber = math.isqrt(number)
    for i in range(2, sqrtNumber + 1):
        if tab[i] == 1:
            j = 2
            ij = i * j
            while ij < number:
                tab[ij] = 0
                j += 1
                ij = i * j
    return tab


# print(eratostenesSieve(100))


# Zadanie 4. Napisać program obliczający i wypisujący stałą e z rozwinięcia w szereg e = 1/0! + 1/1! +
# 1/2! + 1/3! + ... z dokładnością N cyfr dziesiętnych (N jest rzędu 1000).


def silnia(n):
    if n > 1:
        return n * silnia(n - 1)
    return 1


def eConst(n):
    wynik = str(2) + ","
    tab = [0 for i in range(n + 1)]
    k = 2
    e_curr = 2
    e_prev = 2
    index = -1
    while e_curr - e_prev > 10**index:
        for i in range(n):
            e_curr, e_prev = e_curr + (1 / silnia(k)), e_curr
            k += 1
            tab[index] = e_curr * 10**index
        index += 1


def ok(n):
    lcz = 10**n
    e = 2 * lcz
    mn = 2
    dl = mn
    ad = lcz // dl
    while ad > 0:
        e += ad
        mn += 1
        dl += mn
        ad = lcz // dl
    print("2.", end="")
    print(e - 2 * lcz)


# ok(1000)
