# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

import operator
from functools import reduce


def persistence2(n):
    i = 0
    while len(str(n)) > 1:
        x = 1
        for nn in str(n):
            x *= int(nn)
        i += 1
        n = x
    return i


def persistence(n):
    i = 0
    while n >= 10:
        n = reduce(operator.mul, [int(x) for x in str(n)], 1)
        i += 1
    return i


print(persistence(39))  # 3)
print(persistence(4))  # 0)
print(persistence(25))  # 2)
print(persistence(999))  # 4)
