'''
https://www.codewars.com/kata/53368a47e38700bd8300030d/train/python

6 kyu Format a string of names like 'Bart, Lisa & Maggie'.

Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for
the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and
'.'.
'''


def namelist(names):
    result = ""
    if names:
        for i, n in enumerate(names):
            i += 1
            if i < len(names):
                result += n['name'] + ", "
            elif len(names) == 1:
                result = n['name']
            else:
                result = result[:-2] + " & " + n['name']
    return result


print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'},
                {'name': 'Homer'}, {'name': 'Marge'}]))
# 'Bart, Lisa, Maggie, Homer & Marge',

print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
# 'Bart, Lisa & Maggie',

print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]))
# 'Bart & Lisa'

print(namelist([{'name': 'Bart'}]))
# 'Bart', "Wrong output for a single name")

print(namelist([]))
# '', "Must work with no names")
