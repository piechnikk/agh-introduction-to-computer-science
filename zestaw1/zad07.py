n = 87841
a = b = 1
while a * a <= n:
    if a * b == n:
        print(True)
        break
    a, b = b, a + b
if a * b != n:
    print(False)
