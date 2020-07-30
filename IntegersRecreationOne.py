'''
https://www.codewars.com/kata/55aa075506463dac6600010d

Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1,
4, 9, 36, 49, 196, 441, 1764. The sum of the squared divisors is 2500 which is
50 * 50, a square!

Given two integers m, n (1 <= m <= n) we want to find all integers between m
and n whose sum of squared divisors is itself a square. 42 is such a number.

The result will be an array of arrays or of tuples (in C an array of Pair) or a
string, each subarray having two elements, first the number whose squared
divisors is a square and then the sum of the squared divisors.

#Examples:

list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]] list_squared(42,
250) --> [[42, 2500], [246, 84100]]
'''


from math import sqrt, ceil


# Works, but is too slow to codewars
def list_squared1(m, n):
    if m >= 1 and m <= n:
        divisors = []
        for mn in range(m, n + 1):
            tmp = sum([num ** 2 for num in range(1, mn + 1) if mn % num == 0])
            if float.is_integer(sqrt(tmp)) or tmp == 1:
                divisors.append([mn, tmp])
        return(divisors)


# Works + execution time acceptable by codewars
def list_squared2(m, n):
    if m >= 1 and m <= n:
        divisors = []
        for mn in range(m, n):
            sumsqrt = 0
            for num in range(1, ceil(sqrt(mn))):  # listing till sqrt!
                if mn % num == 0:
                    sumsqrt += num ** 2
                    if not mn == 1:
                        sumsqrt += (mn // num) ** 2
            if mn == 1:
                sumsqrt = 1
            if float.is_integer(sqrt(sumsqrt)):
                divisors.append([mn, sumsqrt])
        return divisors


# This is the tempative to sumarized the code above
def list_squared(m, n):
    if m >= 1 and m <= n:
        divisors = []

        for mn in range(m, n):

            tmp = sum([num ** 2 + ((mn // num) ** 2 if not mn == 1 else 0)
                      for num in range(1, ceil(sqrt(mn))) if mn % num == 0])

            tmp = 1 if mn == 1 else tmp

            if float.is_integer(sqrt(tmp)):
                divisors.append([mn, tmp])

        return divisors


print(list_squared(1, 250))  # [[1, 1], [42, 2500], [246, 84100]])
print(list_squared(42, 250))  # [[42, 2500], [246, 84100]])
print(list_squared(250, 500))  # [[287, 84100]])
