# metoda bisekcji
# x^x=2020 - najpierw mniejsza i większa np. 2 i 10

a = 2
b = 10
e = 0.00001
x = (a + b) / 2
while abs(x**x - 2020) > e:
    if x**x >= 2020:
        b = x
    else:
        a = x
    x = (a + b) / 2
print(x)
