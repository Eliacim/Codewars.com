'''
https://www.codewars.com/kata/55f2b110f61eb01779000053

7 kyu Beginner Series #3 Sum of Numbers

Given two integers a and b, which can be positive or negative, find the sum of
all the numbers between including them too and return it. If the two numbers
are equal return a or b.

Note: a and b are not ordered!

Examples
get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2
'''


def get_sum(a, b):
    return a if a == b else sum(x for x in range(min(a, b), max(a, b) + 1))


print(get_sum(0, 1))  # ,1)
print(get_sum(0, -1))  # ,-1)
print(get_sum(-1, 2))  # == 2
