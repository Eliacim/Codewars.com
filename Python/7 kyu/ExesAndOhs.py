'''
https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python

7 kyu Exes and Ohs

Check to see if a string has the same amount of 'x's and 'o's. The method must
return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
'''


def xo(s):
    return s.lower().count('x') == s.lower().count('o')


print(xo('xo'))  # 'True
print(xo('xxxoo'))  # 'False
print(xo('xo0'))  # 'True
print(xo('zpzpzpp'))  # 'True