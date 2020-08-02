'''
https://www.codewars.com/kata/55d1d6d5955ec6365400006d/train/python

7 kyu Round up to the next multiple of 5

Given an integer as input, can you round it to the next (meaning, "higher") 5?

Examples:

input:    output:
0    ->   0
2    ->   5
3    ->   5
12   ->   15
21   ->   25
30   ->   30
-2   ->   0
-5   ->   -5
etc.
Input may be any positive or negative integer (including 0).

You can assume that all inputs are valid integers.
'''


def round_to_next5_2(n):
    if n % 5 == 0:
        n = n
    else:
        n = (n // 5) * 5 + 5
    return n


def round_to_next5(n):
    return n if n % 5 == 0 else (n // 5) * 5 + 5


print(round_to_next5(0))
print(round_to_next5(2))
print(round_to_next5(5))
print(round_to_next5(12))
print(round_to_next5(30))
print(round_to_next5(-2))
