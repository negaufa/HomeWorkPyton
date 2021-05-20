from math import factorial


def fact(n):
    i = 1
    while i <= n:
        yield factorial(i)
        i += 1


for el in fact(4):
    print(el)
