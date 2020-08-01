# https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python


def valid_parentheses(string):
    # return True if string.count('(') == string.count(')') else False
    string = ''.join([a for a in string if a == '(' or a == ')'])
    while '()' in string:
        string = string.replace('()', '')
    return string == ''


print(valid_parentheses("  ("))  # False)
print(valid_parentheses(")test"))  # False)
print(valid_parentheses(""))  # True)
print(valid_parentheses("hi())("))  # False)
print(valid_parentheses("hi(hi)()"))  # True)
