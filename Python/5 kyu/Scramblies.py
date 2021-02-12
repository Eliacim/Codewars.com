"""

5 kyu
Scramblies

https://www.codewars.com/kata/55c04b4cc56a697bb0000048

Complete the function scramble(str1, str2) that returns true if a portion of
str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be
included.
Performance needs to be considered
Input strings s1 and s2 are null terminated.


Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False

"""

from collections import Counter


# First resolution
def scramble2(s1, s2):
    for s in set(s2):
        if not (s1.count(s) >= s2.count(s)):
            return False
    return True


# Using collections.Counter()
def scramble(s1, s2):
    return False if Counter(s2) - Counter(s1) else True


assert scramble('rkqodlw', 'world')
assert scramble('cedewaraaossoqqyt', 'codewars')
assert not scramble('katas', 'steak')
assert scramble('scriptjava', 'javascript')
assert scramble('scriptingjava', 'javascript')
