# Zadanie 5. Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
# na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. Długość
# każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu
# 110100 nie jest możliwe.
import math


def isPrime(number: int):
    if number <= 1:
        return False
    if number <= 3:
        return True
    for i in range(3, int(number**1 / 2) + 1, 2):
        if number % i == 0:
            return False
    return True


def isPrimeSequencesExists(sequence: list):
    lenS = len(sequence)
    if lenS <= 30 and isPrime(binListToDec(sequence)):
        return True

    for i in range(2, lenS - 1):
        if isPrimeSequencesExists(sequence[:i]) and isPrimeSequencesExists(
            sequence[i:]
        ):
            return True
    return False


def binListToDec(number: list):
    string = ""
    for i in number:
        string += str(i)
    return int(string, 2)


print(isPrimeSequencesExists([1, 1, 0, 0, 0]))


# def x(x):
#     for i in range(10):
#         print(i)
#         return


# print(x(2))
