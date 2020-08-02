'''
https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

6 kyu Split Strings

Complete the solution so that it splits the string into pairs of two
characters. If the string contains an odd number of characters then it should
replace the missing second character of the final pair with an underscore
('_').

Examples:

solution('abc') # should return ['ab', 'c_']

solution('abcdef') # should return ['ab', 'cd', 'ef']
'''


def solution(s):
    s = s + "_" if len(s) % 2 == 1 else s
    return [s[i:i+2] for i in range(0, len(s), 2)]


tests = (
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
)

for inp, exp in tests:
    print(solution(inp), exp)
