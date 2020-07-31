'''
4 kyu Permutations

https://www.codewars.com/kata/5254ca2719453dcc0b00027d

n this kata you have to create all permutations of an input string and remove
duplicates, if present. This means, you have to shuffle all letters from the
input in all possible orders.

Examples:

permutations('a'); # ['a'] permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'] The
order of the permutations doesn't matter.
'''

import itertools


def permutations(string):
    return set(["".join(i) for i in itertools.permutations(string)])


print(sorted(permutations('a')))  # ['a']);
print(sorted(permutations('ab')))  # ['ab', 'ba'])
print(sorted(permutations('aabb')))
# ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
