counter = 0


def isPrime(number):
    print(number)
    if number < 2:
        return False
    for d in range(2, int(number**0.5 + 1)):
        if number % d == 0:
            return False

    return True


# def toArray(number):
#     array = []
#     for i in str(number):
#         array.append(int(i))
#     return array


def rec(num1, num2, newNumber):
    global counter
    if len(num1) > 0 and len(num2) > 0:
        if num1 == 1:
            nNum1 = []
        elif num2 == 1:
            nNum2 = []
        else:
            nNum1 = num1[1:]
            nNum2 = num2[1:]
        rec(nNum1, num2, newNumber + num1[0])
        rec(num1, nNum2, newNumber + num2[0])
    elif len(num1) == 0 and len(num2) > 0:
        if num1 == 1:
            nNum2 = []
        else:
            nNum2 = num2[1:]
        rec(num1, nNum2, newNumber + num2[0])
    elif len(num2) == 0 and len(num1) > 0:
        if num1 == 1:
            nNum1 = []
        else:
            nNum1 = num1[1:]
        rec(nNum1, num2, newNumber + num1[0])
    else:
        if isPrime(int(newNumber)):
            counter += 1


def howManyPrimes(x, y):
    global counter
    newNum = ""
    rec(str(x), str(y), newNum)
    return counter


print(howManyPrimes(123, 75))
