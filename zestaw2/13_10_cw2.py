from math import isqrt


def isPrime(n):
    divider = 1
    sqrtN = isqrt(n)
    while divider < sqrtN:
        if n % divider == 0:
            return False
        divider += 2
    return True


# print(isPrime(6))


def allDividers(n):
    # for i in range(1, n // 2 + 1):
    #     if n % i == 0:
    #         print(i)
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            print(i, n // i)


# liczby doskonałe mniejsze od 10^6
def isPerfect(n):
    sum = 1
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            sum += i + (n / i)
    if sum == n:
        True
    else:
        False


def allPerfectNumbers(n):
    for i in range(1, n + 1):
        if isPerfect(i):
            print(i)


# zaprzyjaźnione mniejsze od miliona
def sumDividers(n):
    sum = 1
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            sum += i + (n // i)
    return sum


# for i in range(1, 1000000 + 1):
#     s = sumDividers(i)
#     if sumDividers(s) == i and s < i:
#         print(f"{s} {i}")


# dany jest ciąg An+1 = (An % 2) * (3 * An + 1) + (1 - An % 2) * An / 2
# wyraz początkowy 2 do 10000 przy której to trwa największą liczbe kroków


# def n_iter(n):
#     i = 1
#     while n != 1:
#         n = f(n)
#         i += 1
#     return i


# max = n_iter(2)
# a = 2
# for i in range(3, 10001):
#     tmp = n_iter(i)
#     if max < tmp:
#         max = tmp
#         a = i
# print(a)

# znaleźć do których zmierza iloraz 2 kolejnych
