def serial(x, y):
    return x + y


def parallel(x, y):
    return (x * y) / (x + y)


def fun(tab, ohm):
    n = len(tab)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for z in range(j + 1, n):
                x = tab[i] + tab[j] + tab[z]
                if x < ohm:
                    continue
                if x == ohm:
                    return True
                x = parallel(parallel(tab[i], tab[j]), tab[z])
                if x > ohm:
                    continue
                if x == ohm:
                    return True
