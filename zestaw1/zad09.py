def printDividers(number):
    if number == 0:
        print("nie zero")
    divider = 1
    while divider < number ** (1 / 2):
        if number % divider == 0:
            print(divider)
            print(number // divider)
        divider += 1
    if divider**2 == number:
        print(divider)


printDividers(5212356)
