def sqrt(n):
    sum = 0
    counter = 0
    for i in range(1, n, 2):
        sum += i
        counter += 1
        if sum == n:
            return counter
    return False


print(sqrt(625))
