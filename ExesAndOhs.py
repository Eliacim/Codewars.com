# https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python

def xo(s):
    return s.lower().count('x') == s.lower().count('o')


print(xo('xo'))  # 'True
print(xo('xxxoo'))  # 'False
print(xo('xo0'))  # 'True
print(xo('zpzpzpp'))  # 'True
