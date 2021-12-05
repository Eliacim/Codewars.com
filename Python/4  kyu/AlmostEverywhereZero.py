"""

4 kyu
Almost Everywhere Zero

https://www.codewars.com/kata/5e64cc85f45989000f61526c


You are given 2 numbers is n and k. You need to find the number of integers
between 1 and n (inclusive) that contains exactly k non-zero digit.

Example1

almost_everywhere_zero(100, 1) return 19

by following condition we have 19 numbers that have k = 1 digits( not count
zero ) [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100]



Example2

almost_everywhere_zero(11, 2) return 1

we have only 11 that has 2 digits(ten not count because zero is not count) 11


constrains

1≤n<pow(10,100)

1≤k≤100

"""


def almost_everywhere_zero(n, k):
    if k < 1:
        return 1

    if n < 10 and k < 2:
        return n

    div = n // 10
    mod = n % 10

    return \
        almost_everywhere_zero(div, k - 1) * mod \
        + almost_everywhere_zero(div - 1, k - 1) * (9 - mod) \
        + almost_everywhere_zero(div, k)


assert almost_everywhere_zero(100, 1) == 19
assert almost_everywhere_zero(11, 2) == 1
assert almost_everywhere_zero(20, 2) == 9
assert almost_everywhere_zero(101, 2) == 82
assert almost_everywhere_zero(10001, 2) == 487
assert almost_everywhere_zero(10001000, 2) == 1729
assert almost_everywhere_zero(500309160, 2) == 2604
assert almost_everywhere_zero(10000000000000000000000, 3) == 1122660
assert almost_everywhere_zero(10000000000000000000000, 21)\
    == 2407217760893271902598
assert almost_everywhere_zero(1203, 4) == 81
