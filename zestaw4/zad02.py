tab = [[1, 3, 52], [1, 32, 5], [2, 23, 5]]
n = len(tab)
temp_tab = [0 for _ in range()]
for y in range(n):
    for x in range(n):
        el = tab[y][x]
        isOdd = True
        for i in str(el):
            if int(i) % 2 == 0:
                isOdd = False
                break
