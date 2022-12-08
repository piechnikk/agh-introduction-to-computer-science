# !!!! poprawić
import math


# def isPrime(n):
#     divider = 2
#     sqrtN = math.isqrt(n)
#     while divider <= sqrtN:
#         if n % divider == 0:
#             return False
#         divider += 1
#     return True


def isPrime(n):
    if n < 1 or n % 2 == 0:
        return False
    elif n == 2:
        return True
    else:
        divider = 3
        n_sqrt = n ** (1 / 2) + 1
        while divider < n_sqrt:
            if n % divider == 0:
                return False
            divider += 2
        return True


print(isPrime(7))
