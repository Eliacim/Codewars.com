'''
https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python

6 kyu Create Phone Number

Write a function that accepts an array of 10 integers (between 0 and 9), that
returns a string of those numbers in the form of a phone number.

Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
# => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!
'''


def create_phone_number2(n):
    return "(%i%i%i) %i%i%i-%i%i%i%i" % (n[0], n[1], n[2], n[3], n[4],
                                         n[5], n[6], n[7], n[8], n[9])


def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}".format(*n)


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))  # "(123) 456-7890")
print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))  # "(111) 111-1111")
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))  # "(123) 456-7890")
print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]))  # "(023) 056-0890")
print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))  # "(000) 000-0000")
