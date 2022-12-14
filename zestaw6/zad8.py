# Zadanie 7. Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe odważenie
# określonej masy. Odważniki można umieszczać tylko na jednej szalce.


def scale(list: list, weight: int, counter=0):
    if weight == 0:
        return True
    if counter == len(list):
        return False

    return (
        scale(list, weight - list[counter], counter + 1)
        or scale(list, weight, counter + 1)
        or scale(list, weight + list[counter], counter + 1)
    )


t = [1, 2, 5, 7]
print(scale(t, 4))
