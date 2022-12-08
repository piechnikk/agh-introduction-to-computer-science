# ciąg fibbonaciego

# print(0)
# print(1)
# a = 1
# b = 1
# while b < 100:
#     print(b)
#     # tmp = a + b
#     # a = b
#     # b = tmp
#     a, b = b, a + b


def metodaBisekcji(n, e):
    a = n
    b = 1
    while a - b > e:
        a = (a + b) / 2
        b = n / a
    print(b)


# metoda bisekcji
# x^x=2020 - najpierw mniejsza i większa np. 2 i 10

# a = 2
# b = 10
# e = 0.00001
# x = (a + b) / 2
# while abs(x**x - 2020) > e:
#     if x**x >= 2020:
#         b = x
#     else:
#         a = x
#     x = (a + b) / 2
# print(x)


def NWD(m, w):
    if m == w:
        return m
    while w % m != 0:
        w, m = m, w % m
    return m


print(NWD(25, 125))


def NWDT(a, b, c):  # zakładam że a>b>c
    # return NWD(NWD(a, b), c)
    if a == b == c:
        return a
    else:
        mod1 = a % c
        mod2 = b % c
        while mod1 != 0 or mod2 != 0:
            if mod1 > mod2:
                a, b, c = c, mod1, mod2
            else:
                a, b, c = c, mod2, mod1
            mod1 = a % c
            mod2 = b % c
        return c


# print(NWDT(16, 12, 8))


def NWD3(a, b, c):
    if a > b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b

    if a > c:
        a, c = c, a
    while c != 0:
        a, c = c, a % c
    return a
