'''
https://www.codewars.com/kata/5518a860a73e708c0a000027

3 kyu
Last digit of a huge number

For a given list [x1, x2, x3, ..., xn] compute the last (decimal) digit of x1 ^
(x2 ^ (x3 ^ (... ^ xn))).

E. g.,

last_digit([3, 4, 2]) == 1
because 3 ^ (4 ^ 2) = 3 ^ 16 = 43046721.

Beware: powers grow incredibly fast. For example, 9 ^ (9 ^ 9) has more than 369
millions of digits. lastDigit has to deal with such numbers efficiently.


Corner cases: we assume that 0 ^ 0 = 1 and that lastDigit of an empty list
equals to 1.


This kata generalizes Last digit of a large number; you may find useful to
solve it beforehand.
'''


def last_digit(lst):
    i = 1
    for ls in reversed(lst):
        i = ls ** (i if i < 4 else i % 4 + 4)
    return i % 10

# if exponent is divisible by 4 that means last
# digit will be pow(a, 4) % 10.
# if exponent is not divisible by 4 that means last
# digit will be pow(a, b % 4) % 10


test_data = [
    ([], 1),
    ([0, 0], 1),
    ([0, 0, 0], 0),
    ([1, 2], 1),
    ([3, 4, 5], 1),
    ([4, 3, 6], 4),
    ([7, 6, 21], 1),
    ([12, 30, 21], 6),
    ([2, 2, 2, 0], 4),
    ([937640, 767456, 981242], 0),
    ([123232, 694022, 140249], 6),
    ([499942, 898102, 846073], 6)
]

for test_input, test_output in test_data:
    print(last_digit(test_input) == test_output)
