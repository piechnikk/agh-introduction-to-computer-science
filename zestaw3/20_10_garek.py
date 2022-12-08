from math import sqrt


def fib(a):
    n1 = n2 = 1
    while n1 <= sqrt(a):
        n3 = n4 = 1
        while a % n1 == 0 and n1 * n3 <= a:
            n3, n4 = n4, n3 + n4
            if a // n1 == n3:
                return True

        n1, n2 = n2, n1 + n2

    return False


# print(fib(123))


def is_in_fib(a):
    f1 = f2 = k1 = k2 = 1
    sum = 0
    while sum < a:
        sum += f1
        f1, f2 = f2, f1 + f2
    while sum > a:
        sum -= k1
        k1, k2 = k2, k1 + k2
    return sum == a


# print(is_in_fib(7))


def r235(n):
    counter = 0
    i2 = 1
    while i2 <= n:
        i3 = i2
        while i3 <= n:
            i5 = i3
            while i5 <= n:
                counter += 1
                i5 *= 5
            i3 *= 3
        i2 *= 2
    return counter


# print(r235(25))
