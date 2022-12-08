def newton(n, e=0.0000001):
    a = n
    b = 1
    while a - b > e:
        a = (a + b) / 2
        b = n / a
    print(b)


newton(5)
