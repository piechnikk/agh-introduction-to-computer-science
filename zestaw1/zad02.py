suma = 2023
best = [0, 0]

for i in range(2023):
    a = i
    b = 2022
    while a > 0 and b > a:
        a, b = b - a, a
        if a + b < suma:
            suma = a + b
            best = [a, b]
print(suma, best)
