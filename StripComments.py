# https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python

def solution(string, markers):
    string = string.split('\n')
    for m in markers:
        string = [s.split(m)[0].rstrip() for s in string]
    return '\n'.join(string)


print(solution("apples, pears # and bananas\ngrapes\nbananas !apples",
               ["#", "!"]))  # "apples, pears\ngrapes\nbananas"

print(solution("a #b\nc\nd $e f g", ["#", "$"]))  # "a\nc\nd"

print(solution("' pears , lemons oranges\n^ pears lemons @\napples oranges !"
               + " bananas =\npears apples bananas ^ , strawberries\napples",
               ["'", '=', '@', '#', ',', '!', '-', '^', '.']))


'''
Complete the solution so that it strips all text that follows any of a set of
comment markers passed in. Any whitespace at the end of the line should also
be stripped out.

Example:

Given an input string of:

    apples, pears # and bananas
    grapes
    bananas !apples

The output expected would be:

    apples, pears
    grapes
    bananas

The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples",
                  ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
'''
