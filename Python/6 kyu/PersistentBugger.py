'''
https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

6 kyu Persistent Bugger.

Write a function, persistence, that takes in a positive parameter num and
returns its multiplicative persistence, which is the number of times you must
multiply the digits in num until you reach a single digit.

For example:

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

 persistence(4) => 0   # Because 4 is already a one-digit number.
 persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit

 persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                  # 1*2*6=12, and finally 1*2=2

 persistence(4) # returns 0, because 4 is already a one-digit number

'''


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
