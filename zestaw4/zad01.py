def spiral(tab):
    n = len(tab)
    x = 0
    y = 0
    counter = 1
    for i in range(n):
        for j in range(n):
            tab[x][y] = counter
            counter += 1
            if (
                y + 1 < n and tab[x][y + 1] == 0 and (x == 0 or tab[x - 1][y] != 0)
            ):  # prawo
                y += 1
            elif x + 1 < n and tab[x + 1][y] == 0:  # dół
                x += 1
            elif y > 0 and tab[x][y - 1] == 0:  # lewo
                y -= 1
            elif x > 0 and tab[x - 1][y] == 0:  # góra
                x -= 1


n = 6
tab = [[0 for _ in range(n)] for _ in range(n)]

spiral(tab)
for i in tab:
    print(i)
