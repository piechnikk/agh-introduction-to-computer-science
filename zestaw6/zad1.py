# Zadanie 1. Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
# co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej
# cyfry.


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


def recursion(number):
    strNumber = str(number)
    length = len(strNumber)
    if length > 2:
        for i in range(length):
            newNumber = int(strNumber[0:i] + strNumber[i + 1 : length + 1])
            # print(newNumber, strNumber[0:i], strNumber[i + 1 : length + 1])
            if isPrime(newNumber):
                print(newNumber)
            recursion(newNumber)


recursion(1859)
